---
tags: [CG2111A, lecture-notes, academic]
---

# Communication Protocols in Engineering

## Overview
This lecture focuses on the concept of communication protocols, specifically application layer protocols, which dictate how data is represented and exchanged between devices. Building on previous knowledge of physical and link layer protocols, we explore the design and implementation of serial communication protocols, including packet creation, data transmission, and error checking mechanisms. Understanding these protocols is crucial for effective communication between devices such as Arduino and Raspberry Pi.

## Key Concepts & Definitions
- **[[Protocol]]**: An agreement between machines on how to represent data.
- **[[Application Layer Protocols]]**: Protocols that define how instructions and data are structured for controlling remote systems.
- **[[Serial Communication]]**: A method of transmitting data one bit at a time over a communication channel.
- **[[Packet]]**: A formatted unit of data carried by a packet-switched network.
- **[[Checksum]]**: A value used to verify the integrity of a data packet.
- **[[Serialization]]**: The process of converting a data structure into a format suitable for transmission.
- **[[Deserialization]]**: The reverse process of converting a serialized format back into a data structure.

## Detailed Technical Breakdown

### 1. Establishing Communication
- **Physical Connection**: Connect Arduino to Raspberry Pi using USB.
- **Bit-Level Protocol**:
  - Baud rate: 9600
  - Data length: 8 bits
  - Parity bits: None
  - Stop bits: 1

### 2. Building a Protocol
- **Device Identification**: Assign unique IDs to each device (sensors/actuators).
- **Packet Types**: Define types of packets for communication and expected responses.

### 3. Data Transmission Methods
- **Periodic Push by Arduino**:
  - Arduino sends data in "heartbeat packets" at regular intervals.
  - Raspberry Pi buffers incoming data.
  
- **Periodic Poll by Raspberry Pi**:
  - Raspberry Pi requests data from Arduino.
  - Risk of data loss if polling is infrequent.

### 4. Commanding the Arduino
- Commands can be sent using a variation of poll packets.
- Arduino acknowledges commands with an ACK packet.

### 5. Error Checking with Checksums
- **Sender Side**:
  - Compute checksum using XOR operation on data bytes.
  - Attach checksum to the end of the packet.
  
- **Receiver Side**:
  - Compute checksum from received data and compare with the attached checksum.
  - Respond with ACK if they match, otherwise send NAK.

### 6. Serialization and Deserialization
- **Serialization**:
  - Convert structures into byte streams for transmission.
  - Example structure for command packet:
    ```c
    typedef struct {
        int command;
        int speed;
        int distanceInMeters;
    } TCommand;
    ```

- **Deserialization**:
  - Convert byte streams back into structures.
  - Ensure to handle packet length and checksum.

### 7. Complications in Serialization
- **Endianness**: Ensure consistent byte order across different architectures.
- **Different Data Sizes**: Use standardized integer types to avoid discrepancies between platforms.

### 8. Handling Packet Fragments
- Implement logic to manage incomplete packets due to transmission errors.

## Implementation/Examples
```c
// Example of serialization function
unsigned int serialize(char *buf, void *p, size_t size) {
    char checksum = 0;
    buf[0] = size;
    memcpy(buf + 1, p, size);
    for (int i = 1; i <= size; i++) {
        checksum ^= buf[i];
    }
    buf[size + 1] = checksum;
    return size + 2;
}

// Example of deserialization function
unsigned int deserialize(void *p, char *buf) {
    size_t size = buf[0];
    char checksum = 0;
    for (int i = 1; i <= size; i++) {
        checksum ^= buf[i];
    }
    if (checksum == buf[size + 1]) {
        memcpy(p, buf + 1, size);
        return PACKET_OK;
    } else {
        printf("CHECKSUM ERROR\n");
        return PACKET_BAD_CHECKSUM;
    }
}
```

> [!important] Ensure to handle endianness and data size discrepancies when designing communication protocols between different hardware platforms.

> [!note] Regularly test your communication setup to identify potential issues with data integrity and transmission reliability.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Logic - Propositional Logic]]
- [[Chapter+2]]