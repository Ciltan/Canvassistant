---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Studio 12: Remote Control

## Overview
In this studio, students will connect an Arduino and a Raspberry Pi to facilitate communication between the two processors. The focus will be on overcoming challenges related to data transmission, including differences in data type sizes and struct padding. By the end of the session, students will implement a simple packet format for two-way communication and create a hardware emergency-stop (E-Stop) button.

## Key Concepts & Definitions
- **Arduino**: A microcontroller platform ideal for low-level tasks such as reading sensors and generating PWM signals.
- **Raspberry Pi**: A full Linux-based computer suitable for compute-heavy tasks like processing LIDAR data.
- **USB Serial Communication**: A method of connecting the Arduino to the Raspberry Pi via USB, allowing for data exchange.
- **Data Serialization**: The process of converting data structures into a format suitable for transmission.
- **Struct Padding**: The addition of unused bytes in data structures to align data in memory, which can lead to discrepancies across platforms.
- **Endianness**: The order of bytes in multi-byte data types, which can affect data interpretation.

## Detailed Technical Breakdown

### Learning Objectives
1. Send a C struct from the Arduino to the Raspberry Pi, observing issues with data type sizes and struct padding.
2. Resolve these issues using fixed-width integer types and explicit struct padding.
3. Receive the struct in Python and compare it with the C approach.
4. Develop a simple extensible packet format for two-way communication.
5. Implement an E-Stop button triggered by both hardware and software commands.

### Equipment Needed
| Item                          | Quantity |
|-------------------------------|----------|
| Arduino Uno + USB cable       | ×1       |
| Raspberry Pi                  | ×1       |
| Laptops with Tailscale        | ×1       |
| Push button                   | ×1       |
| Resistor 10 kΩ                | ×1       |
| Breadboard + jumper wires     | as required |

### Background Knowledge
- **Why connect the Arduino and Raspberry Pi?**  
  The Arduino excels at low-level tasks, while the Raspberry Pi handles compute-heavy operations. Together, they form a flexible system that requires reliable communication.

### USB Serial Communication
1. The Raspberry Pi detects the Arduino's USB-to-serial chip and creates a device node (e.g., `/dev/ttyACM0`).
2. The Arduino's Serial library connects to this link, allowing for communication at specified baud rates.
3. The connection uses UART hardware, appearing as a virtual serial port to Linux.

### Data Serialization
- **Data Type Sizes**: Different platforms may have varying sizes for data types (e.g., `int` on ATmega328P vs. Raspberry Pi).
- **Byte Order (Endianness)**: The order of bytes in memory can affect data interpretation.
- **Struct Padding**: Compilers may insert padding bytes, leading to discrepancies in struct sizes across platforms.

## Implementation/Examples

### Activity 1: Cross-Platform Struct Communication
```c
typedef struct {
    int x;
    int y;
} TData;

void setup() {
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        char ch = (char)Serial.read();
        if (ch == 's') {
            TData d;
            d.x = 100;
            d.y = 200;
            Serial.write((uint8_t)sizeof(d)); // first byte: size
            Serial.write((uint8_t*)&d, sizeof(d)); // the struct itself
        }
    }
}
```

> [!important] Ensure your Raspberry Pi is running a 64-bit OS. Use `getconf LONG_BIT` to verify.

> [!warning] Avoid using VNC for this project as it adds computational overhead and is not suitable for real-time control systems.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Logic - Propositional Logic]]
- [[Tutorial+1+Solution]]
- [[Midterm+Briefing]]