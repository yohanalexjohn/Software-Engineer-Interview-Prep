# Parse a 16 bit Little Endian Value

## Active recall

- Pattern: byte parsing / endianness.
- Algorithm: little-endian means low byte first.
- For 16-bit value: `value = low | (high << 8)`.
- Cast before shifting to avoid narrow-byte surprises.
- Time: O(1). Space: O(1).
- Common mistake: reversing byte order; little-endian stores least significant byte first.


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
