# Parse a 16 bit Little Endian Value 


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

