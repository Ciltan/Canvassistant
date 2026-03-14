---
tags: [CG2111A, lecture-notes, academic]
---

# Arduino GPIO Programming

## Overview
This lecture focuses on the fundamentals of [[GPIO]] programming using the Arduino platform, emphasizing binary representation and the manipulation of digital signals. It covers essential concepts such as bitwise operations, number systems, and the architecture of the Arduino Uno board. Understanding these principles is crucial for effective hardware control and programming in digital systems.

## Key Concepts & Definitions
- **Binary Representation**: All digital systems utilize binary (1s and 0s) to represent logical states, where 0 corresponds to LOW/FALSE and 1 to HIGH/TRUE.
- **Bit**: A single binary digit (0 or 1).
- **Byte**: A collection of 8 bits.
- **Nibble**: A group of 4 bits (less common).
- **Word**: A set of multiple bytes, dependent on architecture.
- **Bitwise Operators**: Operators used in programming to manipulate bits directly, including AND (&), OR (|), and NOT (~).
- **Registers**: Small storage locations within a microcontroller used to control hardware.

## Detailed Technical Breakdown

### Binary Representation
- **Logical States**:
  - Logic 0 → 0V
  - Logic 1 → Supply voltage (5V or 3.3V)

### Number Systems
- **Positional Number Systems**: The value of a digit is determined by its position and the base of the number system.
  - **Decimal Example**: \( (7594)_{10} = 7 \times 10^3 + 5 \times 10^2 + 9 \times 10^1 + 4 \times 10^0 \)
  - **Binary Example**: \( (1101)_{2} = 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 \)

### Binary to Decimal Conversion
- Formula: 
  \[
  \text{decimal} = d \times 2^0 + d \times 2^1 + d \times 2^2 + ... + d \times 2^{n-1}
  \]
- Example: 
  - \( 111001_{2} = 1 \times 2^5 + 1 \times 2^4 + 1 \times 2^3 + 0 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 = 57_{10} \)

### Binary to Hexadecimal Conversion
- **Hexadecimal**: A base-16 number system.
- Conversion: Split hex into groups of 4 bits.
- Examples:
  - \( (1E3)_{16} = (0001 \, 1110 \, 0011)_{2} \)

### Bitwise Operators in C
| Operator | Meaning |
|----------|---------|
| &        | AND     |
| \|      | OR      |
| ~        | NOT     |

### Bit Masking
- **Clearing a Bit**: Use a mask where the target bit is 0.
- **Setting a Bit**: Use a mask where the target bit is 1.

### Example Code
```c
int value = 0b11011110;
// Clear bit 3
value &= 0b11110111;
// Set bit 5
value |= 0b00100000;
```

### Arduino Uno Board
- **Specifications**:
  - 8-bit microcontroller
  - 32 single-byte registers
  - 23 GPIO lines
  - 6 ADC channels
  - 3 PWM channels

### GPIO Programming
- **Setting Pin Direction**: Use DDRx registers.
- **Changing Pin State**: Use PORTx registers.
- **Reading Pin State**: Use PINx registers.

### Example: Blinking an LED
```c
#include "Arduino.h"

void setup() {
    DDRB = B00100000; // Set PB5 as output
}

void loop() {
    PORTB = B00100000; // LED ON
    delay(1000);
    PORTB = B00000000; // LED OFF
    delay(1000);
}
```

> [!note] **Key Takeaways**:
> - GPIO pins are controlled using registers.
> - Each pin corresponds to one bit.
> - Use bit masking to prevent unintended changes.

> [!important] **Important Concepts**:
> - Understanding binary representation is crucial for effective programming in digital systems.
> - Mastery of bitwise operations enhances control over hardware functionalities.

## Related
- [[Studio+GPIO_Programming_E+Lecture]]
- [[adc_handout_student]]
- [[Logic - Propositional Logic]]
- [[Midterm+Briefing]]