---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Studio 13: Mini-Project 2: Sensor Array

## Overview
This mini-project focuses on integrating essential sensors for a robot designed to operate on the Moonbase. Key components include the TCS3200 Color Sensor, Emergency Stop Button, RPLidar A1M8, and Raspberry Pi Camera. Students will develop a unified command interface on the Raspberry Pi to control these sensors, enhancing their skills in remote control systems and preparing for the graded Sensor Array Checkpoint.

## Key Concepts & Definitions
- [[Arduino Mega 2560]]: A microcontroller board based on the ATmega2560.
- [[Raspberry Pi]]: A small, affordable computer used for various projects.
- [[TCS3200 Color Sensor]]: A sensor that detects color and outputs frequency signals.
- [[RPLidar A1M8]]: A 360-degree laser scanner used for mapping and navigation.
- [[USART]]: Universal Synchronous and Asynchronous serial Receiver and Transmitter.
- [[E-Stop]]: Emergency stop button for immediate halting of operations.

## Detailed Technical Breakdown

### Learning Objectives
1. Port and verify a bare-metal [[USART]] driver on the ATMega2560 for reliable USB serial communication.
2. Implement an [[E-Stop]] state on the Arduino and propagate it to the Raspberry Pi.
3. Integrate the [[TCS3200 Color Sensor]] and implement a command/response path for RGB frequency display.
4. Capture and render greyscale frames from the [[Raspberry Pi Camera]].
5. Perform and render a single [[RPLidar]] scan on demand.

### Equipment Needed
| Item                                   | Quantity |
|----------------------------------------|----------|
| Arduino Mega 2560 + USB cable         | ×1       |
| Raspberry Pi                           | ×1       |
| Raspberry Pi Camera                    | ×1       |
| TCS3200 Color Sensor                   | ×1       |
| RPLidar A1M8 + USB adapter             | ×1       |
| Emergency Stop Button, 10k Resistor   | ×1       |
| Breadboard, Jumper Wires               | -        |

### Provided Functionality
- **Initial Python Sensor Interface**: The `pi_sensor.py` script extends previous functionalities, including framing, user input handling, and debug strings.
- **Reliable Packet Delivery**: Utilizes a magic number and checksum to ensure data integrity during transmission.

### User Input Actions
| Letter | Action                                                                 |
|--------|------------------------------------------------------------------------|
| e      | Send a software E-Stop command to the Arduino (pre-implemented)       |
| c      | Send a color-reading request to the Arduino (if E-Stop inactive)      |
| p      | Capture and display a greyscale camera frame (if E-Stop inactive)     |
| l      | Perform a single LIDAR scan and render it (if E-Stop inactive)        |

## Implementation/Examples
```python
# Example of user input handling in pi_sensor.py
def handleUserInput():
    while True:
        user_input = input("Enter command: ")
        if user_input == 'e':
            sendEStopCommand()
        elif user_input == 'c':
            requestColorReading()
        elif user_input == 'p':
            captureGreyscaleFrame()
        elif user_input == 'l':
            performLidarScan()
```

> [!note] **Important Reminder**: Ensure all team members contribute to the project to adhere to the 'No Sponge' rule.

> [!warning] **Caution**: Be mindful of the pin usage on the Arduino Mega, especially regarding PWM pins that may be needed for motor control in future projects.

## Related
- [[ModuleIndex]]
- [[CG2111A Studio 12: Remote Control]]: Previous studio focusing on remote control systems.
- [[Arduino Programming]]: Essential programming concepts for Arduino development.