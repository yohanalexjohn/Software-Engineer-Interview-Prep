# Parse a 16 bit Little Endian Value

## Active recall

- Pattern: byte parsing / endianness.
- Algorithm: little-endian means low byte first.
- For 16-bit value: `value = low | (high << 8)`.
- For 32-bit values, place each byte into the correct significance position.
- Cast to `uint32_t` before shifts to avoid narrow-byte surprises.
- Time: O(1). Space: O(1).
- Common mistake: reversing byte order; little-endian stores least significant byte first.

Examples:

- Big-endian bytes `12 34 56 78` reconstruct to `0x12345678`.
- Little-endian storage for that value is byte order `78 56 34 12`.

Recall prompt:

- Which byte is most significant in this protocol?
- Did I cast before shifting by 24?


```cpp 
class Solution {
public:
    uint16_t parseLE16(const uint8_t* data) {
        return static_cast<uint16_t>( 
            (static_cast<uint16_t>(data[1]) << 8) | 
            data[0]
        ); 
    }
};
```

```cpp
uint32_t parseBE32(const uint8_t* data) {
    return (static_cast<uint32_t>(data[0]) << 24) |
           (static_cast<uint32_t>(data[1]) << 16) |
           (static_cast<uint32_t>(data[2]) << 8)  |
            static_cast<uint32_t>(data[3]);
}

uint32_t parseLE32(const uint8_t* data) {
    return (static_cast<uint32_t>(data[3]) << 24) |
           (static_cast<uint32_t>(data[2]) << 16) |
           (static_cast<uint32_t>(data[1]) << 8)  |
            static_cast<uint32_t>(data[0]);
}
```
