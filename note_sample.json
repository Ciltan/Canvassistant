---
tags: [CG2111A, GPIO, bare-metal, registers]
---

# GPIO - General Purpose Input/Output

## Overview
GPIO is the most fundamental way to interact with hardware on the ATmega328P. Bare-metal GPIO programming bypasses the Arduino library (e.g., `digitalWrite`) and directly manipulates hardware registers for faster, more efficient code.

## Key Registers (Per Port)

The ATmega328P has 3 GPIO ports: **Port B**, **Port C**, **Port D**.

| Register | Purpose | Read/Write |
|---|---|---|
| **DDRx** | Data Direction Register - sets pin as input (0) or output (1) | R/W |
| **PORTx** | Output Data Register - sets output HIGH (1) or LOW (0) | R/W |
| **PINx** | Input Pins Register - reads current pin state | R only |

> [!note] Pin Direction
> - `DDRx bit = 1` → Output mode
> - `DDRx bit = 0` → Input mode
> - When input: setting `PORTx bit = 1` enables internal pull-up resistor

## Arduino Pin to ATmega328P Port Mapping

| Arduino Pin | ATmega328P Port.Pin |
|---|---|
| 0-7 | Port D, pins 0-7 |
| 8-13 | Port B, pins 0-5 |
| A0-A5 | Port C, pins 0-5 |

> [!warning] Reserved Pins
> - Pins 0 (RXD) and 1 (TXD) are used for USART serial — avoid for GPIO if using Serial
> - Pin 13 has a built-in LED on the Arduino Uno

## Bit Manipulation Techniques

### Setting a bit (turn ON)
```c
PORTB |= (1 << 5);  // Set bit 5 of PORTB (pin 13 HIGH)
```

### Clearing a bit (turn OFF)
```c
PORTB &= ~(1 << 5);  // Clear bit 5 of PORTB (pin 13 LOW)
```

### Toggling a bit
```c
PORTB ^= (1 << 5);  // Toggle bit 5 of PORTB
```

### Checking a bit (read input)
```c
if (PIND & (1 << 4)) {
    // Pin D4 is HIGH
}
```

### Using defines for readability
```c
#define PIN5 (1 << 5)
#define PIN4 (1 << 4)
DDRB = (PIN5 | PIN4);  // Set pins 4 and 5 as output
```

## Example: LED Blink (Bare-Metal)

```c
#include "Arduino.h"

void setup() {
    DDRB = B00110000;  // PB4 and PB5 as outputs
}

void loop() {
    PORTB = B00100000;  // Green LED (pin 13) ON
    delay(1000);
    PORTB = B00010000;  // Red LED (pin 12) ON
    delay(1000);
}
```

## Example: Reading DIP Switch → Controlling LEDs

Map switches on D7-D4 (PORTD upper nibble) to LEDs on D13-D10 (PORTB upper nibble):

```c
void setup() {
    DDRB |= 0b00111100;   // PB2-PB5 (pins 10-13) as output
    DDRD &= ~0b11110000;  // PD4-PD7 (pins 4-7) as input
}

void loop() {
    uint8_t switches = (PIND >> 4) & 0x0F;  // Read upper nibble of PORTD
    PORTB = (PORTB & 0b11000011) | (switches << 2);  // Map to PORTB
}
```

## 7-Segment Display with 7447 Decoder

- Arduino sends 4-bit BCD (Binary-Coded Decimal) to 7447 IC
- 7447 drives 7-segment display segments (a-g)
- Block diagram: `Arduino → 7447 decoder → 7-segment display`
- Only 4 GPIO pins needed to display digits 0-9

> [!important] Project Relevance
> GPIO is the foundation for all hardware interaction in the final robot project. Create reusable functions for bare-metal pin control early on.

## Related Notes
- [[04_Timers]] - Timer-based GPIO toggling
- [[05_Interrupts]] - Pin change interrupts
- [[02_ADC]] - Analog input (extends GPIO concept)
