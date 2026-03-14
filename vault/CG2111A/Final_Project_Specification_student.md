---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Phase 3: Final Robot Project - Moonbase SG Rescue Mission

## Overview
The CG2111A Phase 3 project involves designing a remotely-operated robot for a rescue mission on Moonbase SG, following a catastrophic explosion. The robot must navigate the lunar environment, locate injured astronauts, and deliver critical supplies. This project serves as an educational opportunity for students to apply engineering principles in a practical scenario, integrating various subsystems and adhering to specific constraints.

## Key Concepts & Definitions
- **Remotely-operated robot**: A robot controlled from a distance, often used in hazardous environments.
- **LIDAR sensor**: A sensor that uses laser light to measure distances and create a 3D map of the environment.
- **Arduino Mega**: A microcontroller board used for building digital devices and interactive objects.
- **Raspberry Pi**: A small, affordable computer used for programming and controlling hardware.
- **Emergency stop button**: A safety feature that allows immediate cessation of robot operations.

## Detailed Technical Breakdown

### 1. Mission Scenario: Moonbase SG Rescue
#### 1.1 Background: An Alternate History
- The Moonbase SG project is a significant milestone in Singapore's space exploration.
- It relies on advanced oxygen generation systems, posing risks in harsh lunar conditions.

#### 1.2 The Crisis
- An explosion at 0340H Lunar Time on mission day 65 has injured all astronauts and damaged supplies.
- The urgent task is to build a robot to deliver medical supplies.

#### 1.3 Rescue Mission
- A launch vehicle will deliver the robot and supplies to the Moon.
- The robot must find and retrieve supplies from designated areas.

#### 1.4 Mission Objectives
- Navigate the environment without collisions.
- Detect and retrieve medpak supplies.
- Deliver supplies to astronauts and map the base.

### 2. Mission Environment
- **Arena**: Rectangular, approximately 3m x 3m, with walls and obstacles.
- **Environmental Constraints**:
  - Minimum wall height of 21cm.
  - Specific start location for the robot.
  - Multiple astronaut figures and medpak dimensions specified.

### 3. Robot System Overview
#### 3.1 Chassis and Control Platform
- Two-layer chassis with independent motor control.
- Powered by Arduino Mega and Raspberry Pi.

#### 3.2 Core Components
- **Actuation**:
  - 4-DoF robotic arm.
  - DC motors for movement.
- **Sensing & Navigation**:
  - LIDAR sensor for environment scanning.
  - Color sensor for detecting floor markers.
  - Camera for limited use.

#### 3.3 Chassis Kit
- Provided for assembly during studio sessions.

#### 3.4 Component Examples
- Images of robot components, including sensors and actuators.

### 4. Constraints and Rules
> [!important] **Spirit of the Rules**: Creativity is encouraged within the framework of the rules. Discuss any potential rule contraventions with the teaching team early to avoid penalties.

#### 4.1 Hardware / Sensor / Actuator Constraints
- Must use provided components, including Arduino Mega and Raspberry Pi.
- The robot arm is essential for medpak handling.

#### 4.2 Software Constraints
- Bare-metal programming required for Arduino.
- Remote control must involve two operators without line-of-sight.

#### 4.3 Mission Constraints
- Unknown arena layout at mission start.
- Specific conditions for mission completion and penalties for rule violations.

### 5. Timeline
- **Weeks 1-4**: Introduction to bare-metal programming and electronics.
- **Week 5**: Mini-Project 1 - Building the robot arm.
- **Weeks 6-7**: Raspberry Pi setup and sensor fundamentals.
- **Week 8**: Mini-Project 2 - Sensor integration.
- **Weeks 9-11**: Robot assembly and communication system integration.
- **Weeks 12-13**: Trial runs and final evaluations.

### 6. Grading
- Assessment breakdown to be provided, focusing on project execution and adherence to constraints.

## Implementation/Examples
```python
# Example code snippet for controlling the robot arm
#include <Servo.h>

Servo armServo;

void setup() {
  armServo.attach(9); // Attach servo to pin 9
}

void loop() {
  armServo.write(90); // Move arm to pick up position
  delay(1000); // Wait for a second
  armServo.write(0); // Move arm to drop position
  delay(1000); // Wait for a second
}
```

## Related
- See [[AY2122+Sem1+Homework+3]] for foundational concepts.
- Refer to [[Logic - Propositional Logic]] for logical reasoning in programming.
- Explore [[Chapter+4+How+Designers+Think]] for design principles relevant to robotics.