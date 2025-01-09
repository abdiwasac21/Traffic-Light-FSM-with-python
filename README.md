**Traffic Light Finite State Machine**

This repository contains a simple implementation of a Finite State Machine (FSM) for a traffic light system. The FSM simulates the behavior of a traffic light at an intersection, cycling through different states to regulate the flow of traffic. The code is written with python and we also used GUI (tkinter) to make the code more understandable. There is also a state diagram included.

**Overview**

The traffic light FSM consists of several states representing different phases of the traffic light cycle, along with transitions between these states triggered by predefined conditions or events. All that you can see it in the state diagram.
The main states include:

_**GreenMain:**_ Green signal for the main road, allowing traffic to proceed.
**_YellowMain:_** Yellow signal for the main road, indicating the transition to a stop.
_**GreenSide:**_ Red signal for the main road and green signal for the side road, allowing traffic from the side road to proceed.
_**YellowSide:**_ Yellow signal for the side road, indicating the transition to a stop.
_**RedBoth:**_ Red signal for both roads, indicating a complete stop for all traffic.

**Features**

Simple Representation: The FSM is represented using a state diagram, providing a clear visualization of the traffic light states and transitions.
Modular Design: The implementation allows for easy extension or modification to accommodate additional features or requirements.
Event-Driven: State transitions are triggered by predefined events such as timer expiration or external triggers, mimicking real-world behavior.
Usage


**To use the traffic light FSM:**

Clone the repository to your local machine.
Review the state diagram and code to understand the FSM implementation.
Modify the code as needed to suit specific requirements or scenarios.
Execute the program to observe the traffic light behavior.
Contributions

Contributions to enhance the functionality or improve the implementation of the traffic light FSM are welcome! To contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them with descriptive messages.
Push your changes to your fork.
Submit a pull request to the main repository.


Acknowledgments

Inspiration: The implementation of this traffic light FSM was inspired by real-world traffic light systems and the principles of Finite State Machines.
Resources: Thanks to the resources and tutorials available on FSMs and traffic light systems for providing valuable insights.
