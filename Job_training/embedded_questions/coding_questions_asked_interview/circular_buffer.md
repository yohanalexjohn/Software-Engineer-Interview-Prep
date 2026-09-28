# Circular Buffer in C

## What is a Circular Buffer

- Fixed Sized queues
- Useful for embedded systems as it is useful for static storage
- Useful when data protection and access happens at the same rates

## Implementation in C

1. Uses two pointers. **Head** and **Tail**
2. Data written into the buffer the header pointer is incremented.
3. Data being removed or read from the buffer the tail pointer is incremented.

## Active recall

- Fixed-size circular buffer uses static storage and wraparound indexes.
- Reserved-slot design: `head` is the next write, `tail` is the next read.
- Empty means `head == tail`: there is no unread slot between them.
- Full means `(head + 1) % maxlen == tail`: advancing the writer would collide
  with the reader, so that one reserved slot distinguishes full from empty.
- Usable capacity is `maxlen - 1`.
- Push and pop are O(1).
- `pop` returns false when empty and writes the output byte by reference/pointer.
- Alternative design: track `count`; empty is `count == 0`, full is `count == maxlen`.
- Common mistake: full and empty can look the same unless the rule is explicit.

Recall prompt:

- What does `head` own: next write or last written byte?
- What byte does `tail` point to?

```c

// Create the data structure first
typedef struct {
    uint8_t * const buffer;
    int head;
    int tail;
    const int maxlen;
}circular_buffer_t;

// Method to push data into the buffer
bool push_data_buffer(circular_buffer_t *buffer, uint8_t data)
{
    int next;

    // Move the current head pointer to the next position
    // If the next is max length the mod value sets it back 
    // to the start of the buffer
    next = (buffer->head + 1) % buffer->maxlen;

    // If the next points to the Tail, circular buffer is full
    // Or if want a condition to overwrite the buffer can continue 
    // to do so. Have the tail only return the latest byte
    // if the trigger pattern is needed to return a note that the 
    // buffer is full to be read can use this 
    if( next == buffer->tail )
    {
        return false;
    }

    // Load the data and then move
    buffer->buffer[buffer->head] = data;
    // Head to the next data offset
    buffer->head = next;

    return true;

}

// Method to delete / read the data from the circular buffer
bool pop_data_buffer(circular_buffer_t *buffer, uint8_t *data)
{
    int next;

    // If the head is the tail buffer is empty so there is no data to read
    if( buffer->head == buffer->tail )
    {
        return false;
    }
    
    // Next is where the tail will point to after the read
    next = (buffer->tail + 1) % buffer->maxlen;
    
    // Read the data then move the tail
    *data = buffer->buffer[buffer->tail];
    // Tail to the next offset
    buffer->tail = next;

    return true;
}
```


```cpp 
class CircularBuffer {
private:
    static constexpr size_t CAPACITY = 8;

    int buffer[CAPACITY];
    size_t head;
    size_t tail;

public:
    CircularBuffer() : head(0), tail(0){
    }

    bool push(int value) {
        if(full())
        {
            return false;
        }

        buffer[head] =  value;
        head = (head+1) % CAPACITY;

        return true;
    }

    bool pop(int& value) {
        if(empty())
        {
            return false;
        }

        value = buffer[tail];
        tail = (tail + 1) % CAPACITY;

        return true;
    }

    int front() const {
        return buffer[tail];
    }

    bool empty() const {
        return (head == tail);
    }

    bool full() const {
        return (((head+1) % CAPACITY) == tail);
    }
};

```

## ISR/main-loop ownership

For a bare-metal single-producer/single-consumer buffer:

- Give `head` to the producer only and `tail` to the consumer only.
- A common design is ISR producer + main-loop consumer. Publish the element
  before advancing `head`; consume the element before advancing `tail`.
- The reserved-slot rules remain: empty is `head == tail`; full is
  `(head + 1) % CAPACITY == tail`; usable storage is `CAPACITY - 1`.
- Define overflow policy explicitly: reject/drop newest, overwrite oldest, or
  record an overrun. Overwriting oldest makes both contexts touch `tail` and
  breaks the clean ownership model unless synchronised.
- `volatile` can force memory accesses, but it does not make a multi-byte index
  atomic and does not provide inter-core/thread ordering or synchronization.
- Check whether index reads/writes are naturally atomic on the MCU and use a
  short critical section or platform atomic operations when needed.
- Under an RTOS, prefer an ISR-safe queue/stream-buffer API or proper atomics.
  Do not describe `volatile` as "volatile atomic."
