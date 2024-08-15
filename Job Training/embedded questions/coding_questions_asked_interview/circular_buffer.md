# Circular Buffer in C

## What is a Circular Buffer

- Fixed Sized queues
- Useful for embedded systems as it is useful for static storage
- Useful when data protection and access happens at the same rates

## Implementation in C

1. Uses two pointers. **Head** and **Tail**
2. Data written into the buffer the header pointer is incremented.
3. Data being removed or read from the buffer the tail pointer is incremented.

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
    next = buffer->head + 1;
    
    // If the head points to the end of the buffer set it to
    // the initial position or start of the buffer again.
    if( next >= buffer->maxlen )
    {
        next = 0;
    }

    // If the next points to the Tail, circular buffer is full
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

    // If the head is the tail buffer is full cannot read or delete
    // as there is no data to read from
    if( buffer->head == buffer->tail )
    {
        return False;
    }
    
    // Next is where the tail will point to after the read
    next = buffer->tail + 1;
    
    // Reached length of the buffer
    if(next >= buffer->maxlen)
    {
        next = 0;
    }
    
    // Read the data then move the tail
    *data = buffer->buffer[buffer->tail];
    // Tail to the next offset
    buffer->tail = next;

    return True;
}
```
