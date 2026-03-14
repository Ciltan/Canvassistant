---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Studio 7: Mini-Project 1: Robot Arm

## Overview
In this mini-project, students will assemble a robot arm designed to manipulate objects, ensuring it powers on correctly. The project involves using the Arduino Serial Monitor for control and transitioning to bare-metal programming for servo management. This foundational experience is crucial for the upcoming Robot Arm Checkpoint assessment.

## Key Concepts & Definitions
- **Robot Arm**: A mechanical device that mimics the motion of a human arm, used for various applications in robotics.
- **Arduino**: An open-source electronics platform based on easy-to-use hardware and software.
- **Servo**: A motor that can be controlled for precise angular position, commonly used in robotics.
- **Bare-Metal Programming**: Writing software that directly interacts with hardware without the use of an operating system or libraries.
- **Timer Interrupts**: A mechanism that allows a program to execute a specific function at regular intervals.

## Detailed Technical Breakdown

### Learning Objectives
1. Assemble the robot arm with servos.
2. Utilize the Arduino Serial library for user command input.
3. Implement a control scheme for servo movement.
4. Develop a bare-metal servo controller using Timer interrupts.

### Equipment Needed
| Item                                         | Quantity |
|----------------------------------------------|----------|
| Robot Arm Kit                                | ×1       |
| Robot Arm Kit Fasteners (M3 Screws and Nuts)| ×1       |
| Arduino Uno                                  | ×1       |
| MG90S Servo and Horn                         | ×4       |
| Phillips Head Screwdriver                    | ×1       |
| Benchtop Power Supply                        | ×1       |
| Breadboard, Jumper Wires, Crocodile Clip Wires | -      |

### Supporting Documents
- Servo Midpoint Sketch (`servo_midpoint.ino`)
- Serial Command Template (`serial_arm_template.ino`)

### Activities
1. **Building the Arm**
   - Follow the assembly instructions in the provided Google Slides document.
   
2. **Powering the Arm**
   - Connect servos to a benchtop power supply, ensuring not to use the Arduino's 5V pin.
   - Upload the `servo_midpoint.ino` code to the Arduino.

3. **Controlling the Arm with Serial Commands**
   - Set up the Serial Monitor for command input.
   - Use a defined command format for controlling servos.

4. **Moving to Bare-Metal Control**
   - Transition from using the Servo library to implementing direct control via Timer interrupts.

> [!important] **Safety Note**: Always ensure the power supply is off when making connections to avoid damage to components.

> [!warning] **Servo Limits**: Be cautious with servo angles to prevent mechanical damage. The gripper servo has a limited rotation of 10 degrees.

## Implementation/Examples
```cpp
// Example of a simple command to move the base servo
void moveBaseServo(int angle) {
    // Code to control the base servo
}
```

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[lec04a]]
- [[Logic - Propositional Logic]]
- [[Tutorial+1+Solution]]
- [[Midterm+Briefing]]
- [[Interrupts]]
- [[Chapter+2]]