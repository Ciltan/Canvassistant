---
tags: [CG2111A, lecture-notes, academic]
---

# USART Communications in CG2111A

## Overview
This note provides a comprehensive overview of the Universal Synchronous/Asynchronous Receiver/Transmitter (USART) communications protocol as utilized in the CG2111A module. It covers the fundamental principles of asynchronous data transmission, the specifications for USART communication, and the setup procedures for both polling and interrupt modes. Understanding these concepts is crucial for coordinating the Atmega328P microcontroller with various smart devices in engineering applications.

## Key Concepts & Definitions
- **USART**: [[Universal Synchronous/Asynchronous Receiver/Transmitter]], a critical component for serial communication.
- **Asynchronous Data Transmission**: A method of data transmission where data is sent without a clock signal.
- **Data Frame**: A unit of data transmission in USART.
- **Baud Rate**: The rate at which information is transferred in a communication channel, often measured in bits per second.
- **Parity Bit**: An extra bit added to data for error checking.
- **Polling**: A method of checking the status of a device at regular intervals.
- **Interrupts**: Signals that temporarily halt the CPU's current operations to allow a higher-priority task to be processed.

## Detailed Technical Breakdown

### Physical Connection
- **Wires**:
  - **Receive (RX)**: Incoming data.
  - **Transmit (TX)**: Outgoing data.
  - **Ground (GND)**: Common ground for RX and TX.
- **Voltage Levels**:
  - 5V for standard devices (e.g., Arduino UNO).
  - 3.3V for low-power devices (e.g., Raspberry Pi).
  - Use a level converter when connecting different voltage devices.

### USART Transmission Specification
- **Data Link Configuration**:
  - Number of data bits: 5, 6, 7, 8 (standard is 8).
  - Parity bit: None (N), Even (E), Odd (O).
  - Stop bits: 1 or 2.
  - Bit rate: Common rates include 1200, 2400, 4800, 9600, 38400, 57600, 115200 bps.

### Setting Up the USART
- **USART Mode**: Set bits 7 and 6 of UCSR0C to 00 for asynchronous mode.
- **Parity Mode**: Configure bits 5 and 4 for parity settings.
- **Stop Bits**: Set bit 3 for the number of stop bits.
- **Data Size**: Choose between 5 and 9 bits, typically 8 bits.
- **Clock Polarity**: Set bit 0 of UCSR0C to 0 for asynchronous mode.
- **Baud Rate Calculation**:
  - Formula: \( B = \frac{f_{osc}}{16 \times baud} - 1 \)
  - Example for 115200 bps: \( B = round(\frac{16000000}{16 \times 115200}) - 1 = 8 \)

### Complete Setup Code
```c
void setBaud(unsigned long baudRate) {
    unsigned int b;
    b = (unsigned int) round(F_CPU / (16.0 * baudRate)) - 1;
    UBRR0H = (unsigned char) (b >> 8);
    UBRR0L = (unsigned char) b;
}
```

### Sending and Receiving Data
- **Polling Mode**:
  - To send data, poll the UDRE0 bit in UCSR0A until it is set.
  - To receive data, poll the RXC0 bit in UCSR0A until it is set.

### Interrupt Mode
- **Setup**:
  - Enable RXCIE0 for receive interrupts.
  - Use either UDRIE0 or TXCIE0 for transmit interrupts.
- **Receive Operation**:
  - Triggered by incoming data, read from UDR0 and insert into buffer.
- **Transmit Operation**:
  - Move the first byte into UDR0 and enable UDRIE0 for subsequent bytes.

> [!important]  
> Ensure that both communicating devices agree on the USART configuration parameters (data bits, parity, stop bits, and baud rate) to avoid communication errors.

> [!note]  
> When using different voltage levels, always implement a level converter to protect your devices from damage.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Studio+GPIO_Programming_E+Lecture]]
- [[Interrupts]]