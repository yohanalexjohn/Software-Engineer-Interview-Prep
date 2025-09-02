# CAN bus 

- Controller Area Network

- Two message formats
    1. Base Frame Format - 11 identifier bits
    2. Extended Frame Format - 29 identifier bits
- Message Prioritisation features 

- Retransmission of corrupt messages automatically when the bus is idle

- 120 Ohms at each end to minimise the reflection and reduce noise

- To avoid multiple transmissions (Can Arbitration) when more than one node transmits 
    - Talk sends a bit 
    - Listens for the bit transferred 
    - If the bit transferred is not seen back it knows that a higher priority message is being 
      transmitted

- Dominant bit is 0 

- CSMA/CA: Carrier Sense Multiple Access/collision **avoidance**.
    - Checks the state of the medium before transmitting
    - If bus is idle start transmission if not wait

- CSMA/CD: Carrier Sense Multiple Access/ collision **detection**
    - Applicable when data transmission has started 
    - Detects collision and stops the data transmission
    - Enable Data Retransmission
    - Enabled through bit monitoring feature of transmission node

- 4 Types of CAN frame
  1. Data Frame - node data 
  2. Remote Frame - requesting transmission of a specific identifier
  3. Error Frame - frame transmitted by any node detecting an error 
  4. Overload Frame - frame to inject a delay between data or remote frame

- Terminator resistor - absorb the signal at the end of transmission to avoid reflection
- Terminator resistor impedance must be equal to the impedance generated 



