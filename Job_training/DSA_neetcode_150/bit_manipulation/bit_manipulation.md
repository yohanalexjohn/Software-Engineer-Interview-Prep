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

## Big-endian non-byte-aligned 32-bit pattern search

- Compute the available length without overflowing: `uint64_t totalBits =
  uint64_t(lengthBytes) * 8u`.
- If `totalBits < 32`, there is no complete candidate.
- Try every start bit from `0` through `totalBits - 32`, including starts that
  are not byte-aligned.
- For absolute `bitPosition`: `byteIndex = bitPosition / 8` and
  `bitIndex = bitPosition % 8`.
- Big-endian/MSB-first extraction is
  `(data[byteIndex] >> (7u - bitIndex)) & 1u`.
- Reconstruct each candidate in reading order:
  `candidate = (candidate << 1) | bit`.
- Return the starting bit offset on a match; otherwise return the agreed
  sentinel, such as `-1`. Use a return type capable of representing all valid
  offsets plus the sentinel.

Endian clarification:

- Endianness describes how a multi-byte value is encoded. Here the byte stream
  is read in order and each byte is scanned from bit 7 to bit 0.
- Do not cast an unaligned byte pointer to `uint32_t*`: alignment, host byte
  order, and non-byte-aligned starts make that incorrect.

Complexity: O(B * 32) time for B candidate starts, which is O(B), and O(1)
extra space because 32 is fixed.

Recall prompt:

- Why is the bit shift `7 - bitIndex`, and did I test every possible start?
