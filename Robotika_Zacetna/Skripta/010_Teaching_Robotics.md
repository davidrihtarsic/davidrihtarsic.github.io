# TEACHING ROBOTICS

## What is robotics

- Science of robots. :)

+ What is a robot?
+ How does the robot works?
+ How are robots constructed?
+ What is intended task of the robot?
+ How do we control a robot?

## What is a robot?

- automated (coffee) machine
- ...
- Printer
- 3D printer
- CNC machine
- ...
- "Robot" Vacuum cleaner (a.k.a. Roomba)
- Industrial robot arm ([YASKAWA](https://www.motoman.com/en-us/products/robots/industrial))
- [Humanoid robot](https://www.youtube.com/watch?v=_sBBaNYex3E)

> It is not defined by the definition... but we have to describe it.

## International Organization for Standardization - ISO

- Standards are not excluding each other...
- `ISO 2806` - defining the CNC machines
    - describing the processing technology
- `ISO 8373` - defining the robots
    - describing machine autonomy

### ISO 8373 - General Terms in Robotics

#### ROBOTICS
science and practice of designing, manufacturing, and applying robots (2.6)

#### ROBOT
actuated mechanism programmable in two or more axes (4.3) with a degree of autonomy (2.2), moving within its environment, to perform intended tasks

- Note 1 to entry: A robot includes the control system (2.7) and interface of the control system.
- Note 2 to entry: The classification of robot into industrial robot (2.9) or service robot (2.10) is done according to its intended application.

#### REPROGRAMMABLE
designed so that the programmed motions or auxiliary functions can be changed without physical alteration (2.3)

#### AUTONOMY
ability to perform intended tasks based on current state and sensing, without human intervention

<!--
### Autonomous vs Automated

Avtonomen brezpilotni zrakoplov zmore varno leteti brez pilotovih posegov. Pri tem se poslužuje umetne inteligence, ki mu omogoča soočanje z nepredvidenimi in nepredvidljivimi izrednimi dogodki vseh vrst. To je drugo kot avtomatske operacije, pri katerih brezpilotni zrakoplov leti po vnaprej določeni ruti, ki jo je operator UAS vnesel pred začetkom leta.

Za tovrstne brezpilotne zrakoplove je ključno, da pilot na daljavo prevzame nadzor nad brezpilotnim zrakoplovom in ukrepa ob nepredvidenih dogodkih, za katere brezpilotni zrakoplov ni bil programiran.
-->

#### MANIPULATOR
machine in which the mechanism usually consists of a series of segments, jointed or sliding relative to one another, for the purpose of grasping and/or moving objects (pieces or tools) usually in several degrees of freedom (4.4)

- Note 1 to entry: A manipulator can be controlled by an operator (2.17), a programmable electronic controller, or any logic system (for example cam device, wired).
- Note 2 to entry: A manipulator does not include an end effector (3.11).

#### CONTROL SYSTEM
set of logic control and power functions which allows monitoring and control of the mechanical structure of the robot (2.6) and communication with the environment (equipment and users)

#### ROBOTIC DEVICE
actuated mechanism fulfilling the characteristics of an industrial robot (2.9) or a service robot (2.10), but lacking either the number of programmable axes (4.3) or the degree of autonomy (2.2)
EXAMPLE:Power assist device; teleoperated device; two-axis industrial manipulator (2.1)

#### INDUSTRIAL ROBOT
automatically controlled, reprogrammable (2.4), multipurpose (2.5)manipulator (2.1), programmable in three or more axes (4.3), which can be either fixed in place or mobile for use in industrial automation applications
Note 1 to entry: The industrial robot includes:
— the manipulator, including actuators (3.1);
— the controller, including teach pendant (5.8) and any communication interface (hardware and software).
Note 2 to entry: This includes any integrated additional axes.

#### SERVICE ROBOT
robot (2.6) that performs useful tasks for humans or equipment excluding industrial automation applications
Note 1 to entry: Industrial automation applications include, but are not limited to, manufacturing, inspection, packaging, and assembly.
Note 2 to entry: While articulated robots (3.15.5) used in production lines are industrial robots (2.9), similar articulated robots used for serving food are service robots (2.10).

#### MOBILE ROBOT
robot (2.6) able to travel under its own control
Note 1 to entry: A mobile robot can be a mobile platform (3.18) with or without manipulators (2.1).

#### ROBOT COOPERATION
information and action exchanges between multiple robots (2.6) to ensure that their motions work effectively together to accomplish the task

#### INTELLIGENT ROBOT
robot (2.6) capable of performing tasks by sensing its environment and/or interacting with external sources and adapting its behaviour
EXAMPLE:Industrial robot (2.9) with vision sensor to pick and place an object; mobile robot (2.13) with collision avoidance; legged robot (3.16.2) walking over uneven terrain.

## Robotics and Education

### Definition of the robots in education

Slangen:  
> Definition of the robot must be based
> on the main operation that robot performs:
>
> - zaznavanje (angl. Sensing),
> - sklepanje (angl. Reasoning) &
> - delovanje (angl. Acting).
>
> This operation is constantly executing in a.k.a. S-R-A loop.

Slo. nat. curriculum:`Robotics in Engineering`  
- almost exact interpretation of S-R-A loop
> Krmiljenje s povratnim delovanje (angl. feedback control regulation)

- including learning objective:
> ...kjer učenci ugotovijo potrebe po
> **krmiljenju s povratnim delovanjem**
> in izpostavijo pomanjkljivosti, če takega krmiljenja ni.
>
> (angl. where students identify the need for
> **feedback control** and point out shortcomings
> in the absence of such control)

- misconception:
> Playing with robots or using a robot is robotics.

- Robots are meant to be user friendly.

### Robotics in Schools

- very popular in last decade

We can find robots in learning process as:

1. Robotics curses:
  - Electronics
  - Computer Science
  - Engineering
2. motivation for learning other disciplines:
  - Science
  - Technology
  - Engineering
  - Math

### Important educational impacts

#### LEARNING by DOING

> ... learning as “BUILDING KNOWLEDGE STRUCTURES” through progressive internalization of actions... this HAPPENS especially felicitously in a context where the LEARNER is consciously engaged in CONSTRUCTING A PUBLIC ENTITY, whether it’s a sand castle on the beach or a theory of the universe. (Papert, S. (1980). Mindstorms. Children, Computers and Powerful Ideas. New York: Basic books.)

#### PRACTICAL APPLICATIONS

Applying knowledge and skills learned into a `public entity` make us proud of ourself. We have something to show to people that matters to us (friends, parents, classmates).

#### CREATIVITY

There is not an only one solution to the problem. Kids can explore their ideas and put it to the test.

#### LEARNING from MISTAKES

Kids are ALLOWED to LEARN from MISTAKES!?! In general, MISTAKES has very bad reputation in school sistem. To degree, that kids are often afraid to give an answer so as not to make a mistake (-> they stop trying). However, Robotics is so complicated field that mistakes can not be avoided. Thus, MISTAKES are very common thing in this learning proces of robotics.

#### CRITICAL THINKING

Critical thinking is ability to do analysis of facts and form objective judgments based on reasonable arguments.

#### SELF-ASSESSMENT

Kids are able to see if they fulfill the intended task or not. They can asses their own performance based on results of intended tasks.
<!--
It is quite difficult to asses ourself if we are well qualified in some topic. Remember: Dunning-Kruger effect: Confidence(Competence)
-->

#### ICT LITERACY

European commission is warning for several years now that EU has large lack in computer science and ICT professionals. Only 55% of computer science and ICT jobs in EU are filled with relevant experts.

### How to teach robotics?

- Is learning robotics difficult?
    + No and Yes

#### HOW DO WE THINK?

- [Kolb's Learning Cycle](https://www.researchgate.net/publication/325475416/figure/fig1/AS:643699918766080@1530481428256/Kolbs-learning-cycle-and-experiential-learning-styles.png)

- [Thinking, Fast and Slow, by Daniel Kahneman](./slike/ThinkingFastSlow.png)

#### HOW DO WE CONSTRUCT OUR KNOWLEDGE?

Piaget (ConstructiVisem):  
> Children must be actively engaged to encounter
> the experiences necessary to build and adapt their schema.
>
> We need to set up these experiences for our learners.

Papert (ConstructioNism):  
> Constructionism—the N word as opposed to the V word — shares
> contructivism’s view of learning as “building knowledge structures”
> through progressive internalization of actions… It then adds the
> idea that this happens especially felicitously in a context where
> the learner is consciously engaged in constructing a public entity,
> whether it’s a sand castle on the beach or a theory of the universe
> ( Papert, 1991, p.1)

### Učne prakse

#### KIRSCHNER
>Active learning, Project lerning, Research based learning ... so le učne situacije s pomanjkljivimi navodili.

#### DEREK MULER
[Effects of science vidos](https://youtu.be/RQaW2bFieo8?t=156 )

### Tehnologije v učnih procesih

- Tomas Edison:

        New Your Times (1922)
>I believe that the motion picture is destined to revolutionize our educational system and that in a few years it will supplant largely, if not entirely, the use of textbooks.

- dr. Michel Resnick:

        Beyond the balck boxes.

        Rethinking Learning in the Digital Age
> Because education is associated with information and computers are associated with information, the two seem to make a perfect marriage.

- dr. Derek Muller
[This will revolutionize education](https://www.youtube.com/watch?v=GEmuEWjHr5c)


!!! question:
    Kako uporabljamo pametne table?

!!! note:
    Kot grafoskop.

### Learning equipment

### Katero učno opremo naj uporabim?

- [Lego We-Do](https://le-www-live-s.legocdn.com/sc/media/files/user-guides/wedo-2/introduction/introduction-en-us-v1-9a5c0557dd5e2d052e77cbc7c39e6a5f.pdf)
- [Lego Mindstiorms](https://education.lego.com/en-au/support/mindstorms-ev3/quick-start-guide)
- [Fischertehnik](https://www.fischertechnik.de/en/service/elearning/teaching)
- [Vex](http://www.vexrobotics.fi/wp-content/uploads/sites/5/2016/03/228-3319-VEX-IQ-Robotics-Education-Guide-201511051.pdf)


!!! question: Ali smo si zastavili pravo vprašanje?

### Kaj moramo učence naučiti?

- what are our learning objectives?
  + electronics (sensors)
  + computer science (IO units, programming)
  + mechanical engineering (gears, construction)

- Then we can choose a proper equipment...

#### ELECTRONICS

- sensors
    - voltage dividers
    - Ohm's Law, Kirshhoff Rules
    -

#### COMPUTER SCIENCE

- basic programming
- Should we learn `hard` or `easy` programming language
    - `easy` programming language -> closer to human understanding of code
        - `skratch`
        - `javascript`
        - `python`
    - `hard` programming language -> closer to the hardware
        - `c++`
        - `assembler`

> More easy the language is - less you will learn about the language.  
> ...
> Migration form python to other languages is far less common then
> migration from c to other languages.  
> ...
> If your gola is to be quick in "getting job done" use `easy` language,
> if your goal are to learn and uderstand how the computer works always begin
> to learn `hard` programming language first.
> (by Rob Muhlestein)

#### MECHANICAL ENGINEERING

- translation of the movements
    - rotation to linear motion
- gear reduction
- torque, forces

<!--
Literature

- [Programming books](https://github.com/EbookFoundation/free-programming-books)
- [Programming Arduino](https://github.com/EbookFoundation/free-programming-books/blob/master/books/free-programming-books.md#arduino)

-->
