---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Mid-Term Assessment Overview

The CG2111A Mid-Term Assessment evaluates students' understanding of engineering principles and practices, focusing on topics such as data transfer rates, polling, interrupts, and timers. This assessment consists of twenty questions, covering various aspects of microcontroller operations and programming. It is crucial for students to adhere to the guidelines provided to ensure proper grading and to avoid penalties for academic dishonesty.

## Key Concepts & Definitions

- **Inter-Arrival Time (IAT)**: The time interval between bytes arriving at the processor from the disk drive over the bus. 
- **Polling**: A method where the processor repeatedly checks the status of a device to see if it requires attention.
- **Interrupts**: Signals that temporarily halt the processor's current operations to allow it to respond to an event.
- **Direct Memory Access (DMA)**: A feature that allows peripherals to communicate with the memory without involving the CPU.
- **Timers**: Hardware components that keep track of time and can trigger events at specified intervals.

## Detailed Technical Breakdown

### Assessment Structure
- **Total Questions**: 20
- **Total Marks**: 20 (10% of overall score)
- **Duration**: 60 minutes
- **Format**: Multiple choice questions

### Guidelines for Students
- Ensure the correct number of questions and pages.
- Answer all questions on the provided OCR form using a 2B pencil.
- No electronic devices allowed except for a stand-alone calculator.
- Communication with peers is prohibited during the assessment.

### Technical Questions Breakdown
1. **Inter-Arrival Time Calculation**
   - Maximum throughput: `min(150 MBPS, 120 MBPS) = 120 MBPS`
   - Smallest possible IAT: `1 / (120 × 10^6) = 8.33 ns`

2. **Polling Data Ready Register**
   - Code snippet provided to read data from the disk drive.
   - Total cycles spent polling: `8192 × 12.5 ns = 102400 ns`
   - Total cycles: `102400 ns / 0.3125 ns = 327680 cycles`

3. **Wasted Instructions Calculation**
   - If polling takes 250,000 cycles: `4 × 250,000 = 1,000,000 instructions wasted`.

4. **Interrupt Processing Time**
   - Total cycles to process a single interrupt: `16 cycles`
   - Time in nanoseconds: `16 × 0.3125 = 5 ns`

5. **Polling vs. Interrupts vs. DMA**
   - True statements: ii., iv., and v. ONLY.

6. **Interrupts on ATMega328P**
   - True statements: iii. and v. ONLY.

### Timer Configuration and PWM
- **Timer Settings**: 
  - TCCR1A, TCCR1B, TIMSK1, TCNT1, OCR1A settings provided.
  - Timer period and frequency calculations based on prescaler and clock rate.

### Example Code Snippets
```c
unsigned char MASK(unsigned char bit_position) {
    return (0x80 >> bit_position);
}
```

### Callouts
> [!important] Ensure to shade and write your Student Number on the OCR form to avoid receiving 0 marks.
> [!warning] Cheating will result in disciplinary action, potentially leading to a score of 0 for the assessment.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[CS1231+TUTORIAL+3]]
- [[Studio+GPIO_Programming_E+Lecture]]