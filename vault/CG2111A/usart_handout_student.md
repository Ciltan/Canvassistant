---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Studio 10: USART Serial Communications

## Overview
In this studio, students will explore the capabilities of the ATmega328P's Universal Synchronous Asynchronous Receiver Transmitter (USART) for serial communication. The focus will be on setting up USART in both polling and interrupt modes, enabling two-way communication between Arduino boards. This hands-on experience will enhance understanding of USART functionality beyond the basic Serial library.

## Key Concepts & Definitions
- **USART**: [[USART]] is a hardware communication protocol that allows for asynchronous and synchronous data transmission.
- **Polling Mode**: A method where the CPU actively checks the status of a device to see if it needs attention.
- **Interrupt Mode**: A method where the CPU is alerted by the hardware when an event occurs, allowing for more efficient processing.
- **Frame Format**: The configuration of data bits, stop bits, and parity bits in serial communication, such as 8N1 or 7E1.

## Detailed Technical Breakdown

### Learning Objectives
1. Set up USART communications in polling mode.
2. Set up USART communications in interrupt mode.
3. Configure USART registers for different frame formats.
4. Implement serial communication between two Arduino boards.

### Equipment Needed
| Item                | Quantity |
|---------------------|----------|
| Arduino UNO         | ×1       |
| Push button          | ×2       |
| LEDs (Red, Green)   | ×1 of each color |
| Resistors (330Ω)    | ×2       |
| Resistors (10kΩ)    | ×2       |
| Jumper wires        | As required |

### Activities
- **Activity 1**: USART in Polling Mode
- **Activity 2**: USART in Interrupt Mode

## Implementation/Examples

### Activity 1: USART in Polling Mode
1. **Construct the Circuit**: Build the circuit as per the provided diagram.
2. **Set up External Interrupts**: Modify the `p1.ino` sketch to trigger interrupts on button presses.
3. **Configure USART for 9600 bps 8N1**: Set up USART in asynchronous mode.
4. **Implement sendData and recvData**: Write functions to send and receive data using polling.
5. **Main Program Logic**: Implement the main loop to handle LED flashing based on received data.

```c
void setupSerial() {
    // Set UCSR0C for 9600 bps 8N1
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00); // 8 data bits, no parity, 1 stop bit
    // Set baud rate
    UBRR0H = (F_CPU / (16 * BAUD)) >> 8;
    UBRR0L = (F_CPU / (16 * BAUD));
}

void sendData(char data) {
    while (!(UCSR0A & (1 << UDRE0))); // Wait for empty transmit buffer
    UDR0 = data; // Put data into buffer, sends the data
}

char recvData() {
    while (!(UCSR0A & (1 << RXC0))); // Wait for data to be received
    return UDR0; // Get and return received data from the buffer
}
```

> [!warning] **Important Note**: Ensure to disconnect Arduinos when uploading code to avoid communication issues.

### Activity 2: USART in Interrupt Mode
1. **Implement setupSerial**: Ensure it matches the polling setup.
2. **Configure startSerial for Interrupt Mode**: Set up USART to use interrupts for data transmission.
3. **Implement ISRs**: Create interrupt service routines for handling data reception and transmission.

```c
ISR(USART_RX_vect) {
    dataRecv = UDR0; // Read received data
}

ISR(USART_UDRE_vect) {
    UDR0 = dataSend; // Send data
}
```

> [!note] **Note**: Using interrupts allows for more efficient communication compared to polling.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Studio+GPIO_Programming_E+Lecture]]
- [[Interrupts]]