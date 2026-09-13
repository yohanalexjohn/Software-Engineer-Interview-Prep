# Bit Manipulation

```cpp
class Solution {
public:
    uint8_t extractBits(uint8_t value) {

        uint8_t temp = value >> 2;
        return (uint8_t)(temp & 0x07);

    }
};
```


