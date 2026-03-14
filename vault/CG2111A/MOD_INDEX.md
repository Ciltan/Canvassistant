---
tags: [CG2111A, index, engineering]
---

# CG2111A: Engineering Principles and Practice II

## Module Overview
Hands-on computer engineering module focused on building a **teleoperated robot** using Arduino (bare-metal programming) and Raspberry Pi. Covers embedded systems from low-level register manipulation to sensor integration and communication protocols.

## Assessment Breakdown

| Component | Weight |
|---|---|
| Quiz 1 | 15% |
| Quiz 2 | 15% |
| Attendance | 5% |
| Robot Arm Checkpoint (Week 5) | 5% |
| Sensor Array Checkpoint (Week 8) | 10% |
| Design Report | 5% |
| Trial Run (Week 12) | 10% |
| Final Demo (Week 13) | 20% |
| Final Report | 5% |
| Studios (best 4 of 5, 2.5% each) | 10% |

## Topic Notes

### Bare-Metal Arduino Programming
- [[01_GPIO]] - General Purpose Input/Output
- [[02_ADC]] - Analog-to-Digital Conversion
- [[03_PWM]] - Pulse Width Modulation
- [[04_Timers]] - Timer Programming (CTC, Normal, Fast PWM)
- [[05_Interrupts]] - Interrupt Handling
- [[06_USART]] - Serial Communication

### Communication & Integration
- [[07_Communication_Protocols]] - I2C, SPI, and other protocols
- [[08_RaspberryPi]] - Raspberry Pi Integration
- [[09_LIDAR]] - LIDAR Sensing

### Projects
- [[10_Final_Project]] - Teleoperated Robot Project
- [[11_Past_Papers]] - Quiz Questions and Solutions

## Key Concepts Quick Reference

| Concept | Key Register(s) | Notes |
|---|---|---|
| GPIO Output | DDRx, PORTx | Set DDR bit = 1 for output |
| GPIO Input | DDRx, PINx | Set DDR bit = 0 for input |
| Timer CTC | TCCRnA, TCCRnB, OCRnA | V = T_cycle / res |
| PWM | TCCRnA (WGM bits), OCRnA | Duty cycle = OCRnA / TOP |
| ADC | ADMUX, ADCSRA | 10-bit resolution (0-1023) |
| USART | UBRRn, UCSRnB | Baud = F_clk / (16*(UBRR+1)) |
| Interrupts | SREG (I-bit), specific mask regs | sei() to enable globally |

## Platform
- **Arduino Uno/Mega**: ATmega328P/2560, 8-bit, 16 MHz, 8KB RAM
- **Raspberry Pi**: ARM 32-bit, 1.2 GHz, 1 GB RAM, runs Linux
- **PC/Laptop**: 64-bit Intel, used for remote control via WiFi
