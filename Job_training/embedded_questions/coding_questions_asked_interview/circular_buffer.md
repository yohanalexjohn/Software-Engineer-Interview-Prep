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

- With the one-empty-slot design, `head == tail` means empty.
- Full means `(head + 1) % maxlen == tail`.
- Alternative design: track `count`; empty is `count == 0`, full is `count == maxlen`.
- Common mistake: full and empty can look the same unless the rule is explicit.

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
    uint8_t next;

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

    return True;

}

// Method to delete / read the data from the circular buffer
bool pop_data_buffer(circular_buffer_t *buffer, unit8_t data)
{
    uint8_t next;

    // If the head is the tail buffer is empty so there is no data to read
    if( buffer->head == buffer->tail )
    {
        return False;
    }
    
    // Next is where the tail will point to after the read
    next = (buffer->tail + 1) % buffer->maxlen;
    
    // Read the data then move the tail
    *data = buffer->buffer[buffer->tail];
    // Tail to the next offset
    buffer->tail = next;

    return True;
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
            return false
        }

        buffer[head] =  value;
        head = (head+1) % CAPACITY;

        return true;
    }

    bool pop() {
        if(empty())
        {
            return false;
        }

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
