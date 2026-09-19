# Bit Manipulation

## Active recall: bit extraction

- Shift right so the wanted field starts at bit 0.
- Mask out exactly the required width.
- Formula: `field = (value >> start) & ((1u << width) - 1)`.
- Common mistake: bit 0 is the least significant bit.

```cpp
class Solution {
public:
    uint8_t extractBits(uint8_t value) {

        uint8_t temp = value >> 2;
        return (uint8_t)(temp & 0x07);

    }
};
```

