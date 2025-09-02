# Networking

## Network layer

1. Packet forwarding, from one network segment to another by nodes in a computer network
2. Each data unit is separately addressed and routed based on the information carried by it
3. Splitting data packets that are too large to be transmitted by the network is called fragmentation

### OSI model

1. Physical layer: bits
2. Data link: frames
3. Network: packets, IP 
4. Transport: TCP/UDP
5. Session: connections
6. Presentation : encryption/translation
7. Application: HTTP

### Forwarding

Router local action of transferring a packet from an input link interface to the appropriate output link interface.

### Routing

Process that determines the end to end paths that packets take from source to destination

## TCP 

1. Transmission Control Protocol
2. Connection oriented byte stream
3. Guaranteed Delivery
4. Sliding Window Protocol with timeouts and retransmissions
5. Acks from data are piggybanked on the new data 


## Ethernet

Ethernet frame consists of a destination address, source address, type field and data.

Ethernet address is 6 bytes. 

