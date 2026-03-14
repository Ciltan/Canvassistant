---
tags: [CG2111A, timers, CTC, registers]
---

# Timers and Counters

## Overview
Timers are hardware counters that increment automatically based on the system clock. They are essential for:
- Reading sensors / writing actuators at **precise intervals**
- Running time-sensitive algorithms (e.g., PID control)
- Generating **PWM** signals (see [[03_PWM]])
- Task switching in multi-tasking OS (CG2271)

## ATmega328P Timer Hardware

| Timer | Size | Counter Range | Notes |
|---|---|---|---|
| Timer 0 | 8-bit | 0 to 255 | Used by Arduino `millis()` / `delay()` |
| Timer 1 | 16-bit | 0 to 65535 | Best for longer periods / higher precision |
| Timer 2 | 8-bit | 0 to 255 | Similar to Timer 0 |

## CTC Mode (Clear Timer on Compare)

The simplest and most common mode. Counter counts from 0 to a preset value V, triggers an interrupt, then resets to 0.

### Key Formulas

$$res = \frac{P}{F_{clk}}$$

$$V = \frac{T_{cycle}}{res}$$

Where:
- $res$ = timer resolution (time per tick)
- $P$ = prescaler value
- $F_{clk}$ = clock frequency (16 MHz for Arduino Uno)
- $T_{cycle}$ = desired interrupt period
- $V$ = compare value to load into OCRnA

### Prescaler Options (Timer 0)

| CS02:CS00 | Prescaler P | Resolution (16 MHz) |
|---|---|---|
| 000 | Stopped | - |
| 001 | 1 | 0.0625 us |
| 010 | 8 | 0.5 us |
| 011 | 64 | 4 us |
| 100 | 256 | 16 us |
| 101 | 1024 | 64 us |

### Example: 1ms Interrupt

Want $T_{cycle} = 1000 \mu s$:

| Prescaler | Resolution | V = T/res | Fits 8-bit? |
|---|---|---|---|
| 1 | 0.0625 us | 16000 | No |
| 8 | 0.5 us | 2000 | No |
| **64** | **4 us** | **250** | **Yes** |
| 256 | 16 us | 62.5 | Fractional |
| 1024 | 64 us | 15.63 | Fractional |

Best choice: **P = 64, V = 250** (set OCR0A = 249 since counting starts at 0)

## Timer 0 Registers

### TCCR0A - Timer/Counter Control Register A
```
Bit:    7      6      5      4    3  2    1      0
     COM0A1 COM0A0 COM0B1 COM0B0 -  - WGM01  WGM00
```

**COM0A1:0** - Compare Output Mode for OC0A:
| COM0A1 | COM0A0 | Action |
|---|---|---|
| 0 | 0 | OC0A disconnected |
| 0 | 1 | Toggle OC0A on match |
| 1 | 0 | Clear OC0A on match |
| 1 | 1 | Set OC0A on match |

**WGM bits** - Waveform Generation Mode:
| WGM02 | WGM01 | WGM00 | Mode |
|---|---|---|---|
| 0 | 0 | 0 | Normal |
| 0 | 1 | 0 | **CTC** (TOP = OCR0A) |
| 0 | 1 | 1 | Fast PWM (TOP = 0xFF) |
| 1 | 1 | 1 | Fast PWM (TOP = OCR0A) |

### TCCR0B - Timer/Counter Control Register B
```
Bit:   7     6    5  4    3     2    1    0
     FOC0A FOC0B  -  -  WGM02 CS02 CS01 CS00
```
CS02:CS00 selects prescaler (see table above). Setting any non-zero value **starts the timer**.

### TIMSK0 - Timer Interrupt Mask Register
- Bit 1 (OCIE0A): Enable Output Compare Match A interrupt
- Bit 0 (TOIE0): Enable Timer Overflow interrupt

## Complete CTC Example: LED Blink Every 100ms

```c
#include <avr/io.h>
#include <avr/interrupt.h>

volatile int count;

void InitTimer0(void) {
    TCNT0 = 0;           // Initial counter value
    OCR0A = 249;          // TOP value (250 counts = 1ms)
    TCCR0A = 0b01000010;  // Toggle OC0A, CTC mode
    TIMSK0 |= 0b10;       // Enable OCIE0A interrupt
}

void StartTimer0(void) {
    TCCR0B = 0b00000011;  // Prescaler 64, start timer
    sei();                 // Enable global interrupts
}

ISR(TIMER0_COMPA_vect) {
    count++;
    if ((count % 100) == 0)  // Every 100ms
        PORTB ^= (1 << 5);  // Toggle LED on pin 13
}

int main(void) {
    DDRB |= (1 << 5);  // Pin 13 as output
    count = 0;
    InitTimer0();
    StartTimer0();
    while (1) { }  // Main loop does nothing
}
```

> [!warning] Common Mistakes
> - Forgetting `sei()` — interrupts won't fire without global interrupt enable
> - Using V instead of V-1 in OCR0A (off-by-one, usually acceptable)
> - Not declaring ISR variables as `volatile`
> - Modifying timer registers while timer is running

## Related Notes
- [[01_GPIO]] - GPIO fundamentals used with timers
- [[03_PWM]] - Timer-based PWM generation
- [[05_Interrupts]] - Interrupt system (timers use ISRs)
