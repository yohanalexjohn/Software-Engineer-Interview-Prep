# Bit Manipulation

## Active recall: bit extraction

- Shift right so the wanted field starts at bit 0.
- Mask out exactly the required width.
- Formula: `field = (value >> start) & ((1u << width) - 1)`.
- Single bit: direct mask, for example `status & (1u << bit)`.
- Multi-bit field: shift down, then mask.
- Common mistake: bit 0 is the least significant bit.

Status byte example:

- bit 0: `POWER_ON`
- bit 1: `ERROR`
- bits 2-4: `MODE`
- bit 5: `CONNECTED`
- `0b00110101` means power true, error false, mode `5`, connected true.

Recall prompt:

- Is this one bit or a multi-bit field?
- Did I shift before masking the field?

```cpp
class Solution {
public:
    uint8_t extractBits(uint8_t value) {

        uint8_t temp = value >> 2;
        return (uint8_t)(temp & 0x07);

    }
};
```

```cpp
struct Status {
    bool powerOn;
    bool error;
    uint8_t mode;
    bool connected;
};

Status decodeStatus(uint8_t status) {
    return {
        static_cast<bool>(status & (1u << 0)),
        static_cast<bool>(status & (1u << 1)),
        static_cast<uint8_t>((status >> 2) & 0x07u),
        static_cast<bool>(status & (1u << 5)),
    };
}
```
