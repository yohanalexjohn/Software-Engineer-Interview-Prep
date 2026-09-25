# Packet Validation

Format:

```text
HEADER | LENGTH | PAYLOAD | CHECKSUM
```

Assume:

- Header byte is `0xAA`.
- Payload length is `0..8`.
- Checksum is over the payload bytes.

## Active recall

- Validate minimum size before reading fields.
- Check header before trusting the rest of the packet.
- Check payload length range.
- Check exact packet size: no missing checksum, no truncated payload, no extra
  bytes in a full-vector validator.
- Zero-length payload is valid if length is `0` and checksum matches the empty
  payload rule.
- Only compute checksum after bounds are known safe.

Recall prompt:

- Have I proved every byte I read exists?
- Is this a full packet already, or bytes arriving over time?

## Full-vector validation

Use direct checks when the whole packet is already in memory.

```cpp
bool isValidPacket(const vector<uint8_t>& packet) {
    constexpr uint8_t HEADER = 0xAA;
    constexpr size_t HEADER_SIZE = 1;
    constexpr size_t LENGTH_SIZE = 1;
    constexpr size_t CHECKSUM_SIZE = 1;
    constexpr size_t MAX_PAYLOAD = 8;

    if (packet.size() < HEADER_SIZE + LENGTH_SIZE + CHECKSUM_SIZE) {
        return false;
    }

    if (packet[0] != HEADER) {
        return false;
    }

    const uint8_t length = packet[1];
    if (length > MAX_PAYLOAD) {
        return false;
    }

    const size_t expectedSize = HEADER_SIZE + LENGTH_SIZE + length + CHECKSUM_SIZE;
    if (packet.size() != expectedSize) {
        return false;
    }

    uint8_t checksum = 0;
    for (size_t i = 0; i < length; ++i) {
        checksum += packet[2 + i];
    }

    return checksum == packet.back();
}
```

## Streaming UART parser

- A UART parser usually receives bytes gradually.
- Persistent state machine is clearer than repeatedly treating partial bytes as
  a full vector.
- States: `HEADER -> LENGTH -> PAYLOAD -> CHECKSUM`.
- On bad header/length/checksum, reset to `HEADER`.
- Full parsing, checksum validation, and command dispatch belong in task
  context, not in a long ISR.
