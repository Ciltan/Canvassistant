---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A: Engineering Principles and Practice II

## Overview
This course aims to provide students with hands-on experience in building complex computer engineering solutions. It emphasizes foundational knowledge, practical applications, and real-world problem-solving skills. The curriculum is designed to bridge the gap between theoretical concepts and practical implementation, preparing students for future challenges in engineering.

## Key Concepts & Definitions
- **Hands-on Experience**: Practical engagement in engineering tasks to reinforce learning.
- **Rigorous Depth**: In-depth study of materials not covered in other courses, focusing on bare-metal programming.
- **Workable Depth**: Sufficient understanding of materials that will be revisited in future courses, such as [[TCP/IP]] and [[Network Security]].
- **Studios**: Practical sessions that constitute 10% of the course grade, designed to enhance understanding through hands-on activities.
- **Real-world Problem Solving**: Application of engineering principles to tackle practical challenges.

## Detailed Technical Breakdown

### Course Structure
- **Teaching Team**: 
  - Sriram Sami
  - Henry Tan
  - Colin Tan
  - Boyd Anderson
  - Nguyen Tien Khoa

### Course Philosophy
- **Goals**:
  - Provide hands-on experience.
  - Build problem-solving skills.
  - Encourage self-driven learning.

### The Two Depth Approach
- **Rigorous Depth**: Focus on unique materials.
- **Workable Depth**: Focus on materials relevant to future courses.

### Studios
- **Weightage**: 10% of total grade.
- **Format**: 15 studios, with 5 graded (best 4 counted).
- **Objective**: Help students complete course projects.

### Course Projects
1. **Robotic Arm Mini-Project** (Week 5)
   - Build a 4-DoF robot arm.
   - Implement control via Arduino.
   
2. **Sensor Array Mini-Project** (Week 8)
   - Integrate sensors using Raspberry Pi.

3. **Teleoperated Robot Project** (Weeks 10-13)
   - Assemble chassis and power systems.
   - Focus on communication and system integration.

### Important Dates
- **Quizzes**: 
  - Quiz 1: February 7, 10 am - 12 pm
  - Quiz 2: March 28, 10 am - 12 pm
- **Checkpoints**: 
  - Robot Arm: Week 5
  - Sensor Array: Week 8
  - Trial Run: Week 12
  - Final Run: Week 13

### Weightage Breakdown
| Component                     | Percentage |
|-------------------------------|------------|
| Quiz 1                        | 15%        |
| Quiz 2                        | 15%        |
| Attendance                    | 5%         |
| Robot Arm Checkpoint          | 5%         |
| Sensor Array Checkpoint       | 10%        |
| Design Report                 | 5%         |
| Trial Run                     | 10%        |
| Final Demo                    | 20%        |
| Final Report                  | 5%         |
| Studios                       | 10%        |
| **Total**                     | **100%**   |

> [!important] **Feedback Summary**: 
> - Positive: Fun projects, significant learning, sense of achievement.
> - Negative: Stressful, rushed content, overwhelming material.

### Machine Communications
- **Challenges**:
  - Different processing speeds and transfer sizes.
  - Security concerns regarding unauthorized access.

### Arduino Programming
- **Bare Metal Programming**: Understanding low-level operations beyond library functions.

## Implementation/Examples
```c
void setup() {
    pinMode(12, OUTPUT);
    pinMode(13, OUTPUT);
}
```

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Logic - Propositional Logic]]
- [[CS1231+TUTORIAL+3]]