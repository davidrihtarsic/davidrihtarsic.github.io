# [EARLY LEARNING OF ROBOTICS](../index) ↪ <++>
[🏡HOME](./index){: .btn}
[📝COURSE](./Skripta/index.md){: .btn}
[👨‍🎓INFO](./info.html){: .btn}
[💾DOWNLOAD](./Presnemi/index){: .btn}

---

- [Students Informations](./Obvestila/index)

---

## Basic Course

Hoverer learning process will not be divided into three separate parts but it will consist of lectures and work exercises simultaneously. During the first part of course (cca. 45h) we will be discussing:

> 1. What is robotics, branches of robotics, the role if robotics in education.
> 2. Open electronic platforms suitable for learning robotics (eg Arduino, raspberry, etc.).
> 3. Operation of the basic input and output functions of the robot controller with examples of use.
> 4. An overview of the various programming environments for school projects on robotics.
> 5. Using analogue to digital in digital to analogue conversion.
> 6. Controlling various motors and other power systems.
> 7. A review of basic electronic sensors important for robotics.
> 8. S-R-A loop (sensing - reasoning - acting loop).
> 9. Communication protocols between robotic systems.
> 10. Assembly of programming devices (for example, mobile robot, lockable ...) in conjunction with the controller, programming of operation.
> 11. Planning, implementation and documentation of the project from robotics.
> 12. The importance of robotics in motivating young people for science in technology, robotics competitions.
> 13. Robotics as the starting point for an integrated approach to teaching science, technology, engineering and math (STEM).

## Project time

The last part of the course (cca 15h) will be dedicated to your's project. You will have to make and program a mobile robot which will have to solve different tasks e.g.:
- follow the line and avoiding the obstacles
- push the trash over the table edge
- find the nearest obstacle and drive to it
- find the way out from the maze
- ...
- solve your own problem

## Assesment

1. 50% - Exam/Oral interview
2. 50% - Project

## Robotics Project Evaluation Criteria

| Code | Group | Criterion | What is assessed | Repeated use rule | 0 pts | 1–2 pts | 3 pts | 4 pts | 5 pts | Examples |
|------|-------|----------|------------------|-------------------|--------|----------|--------|--------|--------|----------|
| S1 | Sensing | Digital inputs | Use of at least one digital input. | Repeated use of the same type does not add extra points inside this criterion. | No digital input. | Connected but unreliable or only partly demonstrated. | Basic working digital input. | Working and meaningfully integrated. | Reliable, well-chosen, and clearly demonstrated. | Button, switch, digital detector |
| S2 | Sensing | Analog inputs | Use of at least one analog sensor or analog reading. | Repeated use of the same analog principle does not add extra points inside this criterion. | No analog input. | Reading exists but weakly used or unstable. | Basic working analog input. | Good use with meaningful threshold or interpretation. | Reliable analog use with clear purpose. | LDR, potentiometer, analog distance sensor |
| S3 | Sensing | Advanced sensors | Use of a more advanced sensing principle. | Second advanced sensor may support the same criterion but should improve quality, not quantity. | No advanced sensor. | Attempted but not functioning well. | Basic use of one advanced sensor. | Good advanced sensing with correct interpretation. | Reliable advanced sensing with strong integration. | Ultrasonic timing, PWM input, multi-signal sensing |
| S4 | Sensing | Sensor design (circuit) | Student designs or tunes the sensing circuit. | Repeated resistor changes alone do not justify full points. | No independent sensor circuit work. | Minimal adjustment without clear understanding. | Basic circuit design or tuning. | Good adjustment with correct component choice. | Well-designed and justified sensor circuit. | Voltage divider, pull-up/down, light shielding |
| R1 | Reasoning | Basic logic (if) | Use of simple conditions. | More if statements alone do not increase the score unless quality improves. | No meaningful logic. | Logic partly works. | Basic if-based behavior works. | Good logical response to inputs. | Robust and consistently correct logic. | if / else |
| R2 | Reasoning | Multi-condition logic | Use of combined or multi-step decisions. | Repeated simple conditions do not replace real multi-condition logic. | No multi-condition logic. | Very limited combined logic. | At least one meaningful multi-condition solution. | Several good combined decisions. | Clear and robust higher-level decision logic. | if-else chain, logical AND/OR, state choice |
| R3 | Reasoning | Loops | Use of loop-based control suitable for robotics. | Repeated delay-based repetition does not by itself earn full points. | No proper loop use. | Loop exists but is weak or misused. | Basic working loop. | Good loop structure for sensing and acting. | Strong continuous control loop with clear behavior. | loop(), iterative checking |
| R4 | Reasoning | Program structure (functions) | Program is divided into functions or modules. | Repeated code should be reduced, not copied. | No structure. | Some structure but much repetition. | Basic use of functions. | Well-structured code. | Very clear modular organization. | moveForward(), readSensor(), stopRobot() |
| R5 | Reasoning | Code readability | Readable names and clean arrangement. | More comments do not improve score if code stays unclear. | Code is hard to read. | Some readable parts. | Generally readable. | Clear names and good organization. | Very readable and easy to understand. | Meaningful variable names, short functions |
| A1 | Acting | Digital outputs | Use of simple on/off outputs. | Repeated outputs of the same kind do not add extra points. | No digital output. | Output weakly demonstrated. | Basic working digital output. | Good use in the project. | Reliable and purposeful output behavior. | LED, buzzer, relay, lamp |
| A2 | Acting | Motor control | Use of motor direction/start/stop control. | More motors do not automatically mean more points. | No motor control. | Motor use limited or unstable. | Basic working motor control. | Good movement control. | Reliable motor control clearly tied to project goal. | DC motor direction, stop/start |
| A3 | Acting | PWM control | Use of PWM to control speed, power, or brightness. | Extra PWM channels do not increase score without added quality. | No PWM use. | PWM attempted but limited. | Basic PWM works. | Good PWM control. | Smooth and well-tuned PWM behavior. | Motor speed, LED brightness |
| A4 | Acting | Actuator diversity | Use of more than one output principle. | The emphasis is on diversity, not repetition. | Only one simple output type. | Mostly one output type. | At least two different output types. | Several output types with purpose. | Well-combined and meaningful output diversity. | Motor + LED, motor + servo |
| E1 | Engineering | Construction quality | Mechanical stability and neat build. | Extra parts do not matter if build quality is weak. | Weak or unsafe construction. | Acceptable but fragile. | Basic stable construction. | Good construction quality. | Very robust and neat build. | Stable chassis, secure wiring |
| E2 | Engineering | System complexity | Meaningful integration of multiple subsystems. | Purely adding parts without purpose does not improve the score. | Very simple system. | Limited integration. | Moderate integrated system. | Good integration of several parts. | Complex but still understandable and functional. | Sensor + logic + motor + output |
| E3 | Engineering | Idea and design | Quality and clarity of the project idea. | More decorative features do not replace a good concept. | No clear idea. | Basic idea only. | Clear basic concept. | Good and meaningful concept. | Very strong, creative, and purposeful concept. | Useful, original, or well-targeted project |
