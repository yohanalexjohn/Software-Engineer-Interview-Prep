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
- For absolute `bitPosition`: `byteIndex = bitPosition / 8` chooses the byte
  and `bitIndex = bitPosition % 8` chooses the position inside it.
- Big-endian/MSB-first extraction is
  `(data[byteIndex] >> (7u - bitIndex)) & 1u`: logical position `0` is the
  byte's MSB, which is physical shift position `7`.
- Reconstruct each candidate in reading order:
  `candidate <<= 1; candidate |= bit;`. Shift first to make room at bit 0,
  then OR in the newly read bit.
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

## Binary gap

Find the longest run of zero bits bounded by `1` bits. Leading and trailing
zeros do not count because they are not enclosed.

LSB-to-MSB scan:

```cpp
int binaryGap(uint32_t value)
{
    int best = 0;
    int zeros = 0;
    bool seenOpeningOne = false;

    while (value != 0)
    {
        if ((value & 1u) != 0u)
        {
            if (seenOpeningOne) best = std::max(best, zeros);
            seenOpeningOne = true; // this 1 closes the old gap and opens the next
            zeros = 0;
        }
        else if (seenOpeningOne)
        {
            ++zeros;
        }
        value >>= 1;
    }
    return best;
}
```

An MSB-to-LSB scan uses the same state; only update `best` when another `1`
closes the current gap. Common mistake: counting zeros after the final `1`.

## Reverse bits

For a fixed 32-bit value, repeat exactly 32 times so leading input zeros become
trailing output zeros:

```cpp
uint32_t reverseBits(uint32_t value)
{
    uint32_t result = 0;
    for (int i = 0; i < 32; ++i)
    {
        result <<= 1;       // make room for the next output bit
        result |= value & 1u;
        value >>= 1;
    }
    return result;
}
```

Invariant: after `i` iterations, `result` contains the reverse of the `i`
least-significant input bits. Time O(32), extra space O(1).
