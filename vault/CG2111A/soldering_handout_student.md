---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Studio 6: Soldering Practice Lab

## Overview
In this studio session, students will engage in hands-on soldering and printed circuit board (PCB) assembly by constructing an LED Roulette Circuit. This circuit utilizes a 555 Timer IC in astable mode to generate clock pulses, which are then processed by a CD4017 Decade Counter IC to sequentially illuminate LEDs, simulating the behavior of a roulette wheel. This practical experience is crucial for mastering PCB design and soldering techniques.

## Key Concepts & Definitions
- **LED Roulette Circuit**: A circuit designed to mimic the behavior of a roulette wheel using LEDs.
- **555 Timer IC**: A versatile integrated circuit used for generating precise timing and oscillation.
- **CD4017 Decade Counter IC**: An integrated circuit that counts clock pulses and activates outputs sequentially.
- **Soldering**: The process of joining electronic components together using a molten metal alloy.
- **Desoldering**: The technique of removing solder to disconnect components from a circuit.

## Detailed Technical Breakdown

### Learning Objectives
- Understand PCB circuit design and logic.
- Acquire skills in soldering wires and components.

### Equipment Needed
| Item                          | Quantity |
|-------------------------------|----------|
| 555 Timer IC                  | ×1       |
| CD4017 Decade Counter IC      | ×1       |
| PNP Transistor (BC557)       | ×1       |
| LEDs                          | ×10      |
| Resistors: 330Ω, 10kΩ, 2×3.3MΩ, 10MΩ | -        |
| Capacitors: 1µF, 100nF        | -        |
| 9V Battery                    | ×1       |
| PCB, soldering iron, solder    | -        |

### Circuit Design
#### 555 Timer IC
- Operates in three modes: monostable, bistable, and astable.
- In astable mode, it generates continuous clock pulses.

**Pin Connections**:
| Pin No. | Name   | Connection & Function in the Circuit |
|---------|--------|--------------------------------------|
| 1       | GND    | Connected to ground.                 |
| 2       | TRIG   | Connected to Pin 6 (THR).            |
| 3       | OUT    | Provides clock pulse output.         |
| 4       | RESET  | Connected to Vcc to prevent resets.  |
| 5       | CTRL   | Not used.                            |
| 6       | THR    | Connected to Pin 2 and capacitor.    |
| 7       | DIS    | Connected to resistor and capacitor.  |
| 8       | VCC    | Connected to positive supply voltage. |

#### CD4017 Decade Counter
- Activates LEDs in response to clock pulses from the 555 Timer.

**Pin Connections**:
| Pin No. | Name   | Connection & Function in the Circuit |
|---------|--------|--------------------------------------|
| 1-7, 9-11 | Q0 to Q9 | Outputs connected to LEDs.         |
| 8       | GND    | Connected to negative terminal.      |
| 14      | Clock  | Receives clock pulses from 555 Timer. |

#### BC557 PNP Transistor
- Controls the speed of LED rotation by modulating the clock frequency of the 555 Timer.

## Implementation/Examples
```markdown
// Example of a simple LED circuit using the 555 Timer and CD4017
const int ledPin = 9; // Pin connected to the LED
void setup() {
  pinMode(ledPin, OUTPUT);
}
void loop() {
  digitalWrite(ledPin, HIGH); // Turn LED on
  delay(1000);                 // Wait for a second
  digitalWrite(ledPin, LOW);  // Turn LED off
  delay(1000);                 // Wait for a second
}
```

> [!note] **Safety First**: Always wear protective eyewear and ensure the fume extractor is on before soldering.
> [!warning] **Practice Desoldering**: Use empty perfboard to practice desoldering techniques before working on the LED Roulette PCB.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Logic - Propositional Logic]]
- [[Tutorial+1+Solution]]