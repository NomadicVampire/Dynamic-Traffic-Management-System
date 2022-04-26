# Dynamic-Traffic-Management-System
Dynamic Traffic system overcomes the issue of static traffic light system according to real time environment.
Abstract:
Traffic congestion is becoming a serious problem with a large number of cars on the roads.It not only add time and stress to drivers' lives, but they also increase fuel consumption and pollution. Congestion in traffic can be caused by a variety of factors such as a lack of capacity, unregulated demand, long red light delays, and so on.Traffic lights being one of the critical factors affecting traffic flow.Conventional traffic system like Automating control system is creating  a serious problem with large number of vehicles on the road. With a lot of vehicles waiting in queue to be proceded is increasing. And traditional system cannot manage it.

Our suggested system attempts to create a computer vision-based traffic signal controller that can adapt to the present traffic situation. It calculates real-time traffic density using live video feed from traffic junction CCTV cameras by recognising vehicles at the signal and adjusting the green signal time accordingly. To get a more exact estimation of the green signal time, the vehicles are classed as automobile, bike, bus/truck, or rickshaw. To determine the number of vehicles in each direction, we employed object detection techniques such as YOLO. The timers of these traffic signals are then set based on the vehicle density in each direction, and the system becomes adaptable. This aids in the optimization of green signal timings and traffic flow.

Problem Statement:

To develop a self-adaptive traffic light control system based on yolo. Due to disproportionate and diverse traffic in various lanes, inefficient usage of the same time slot for each of them results in slower speeds, longer trip durations, and more vehicle waiting.Design a system that allows the traffic management system to make time allocation decisions for a given lane based on the traffic density on other lanes using cameras and image processing modules.This method can override the earlier system of hardcoded lights, which causes unnecessary delays, lowering traffic and waiting time, reducing the frequency of accidents and fuel usage, and so helping to control air pollution.


Conventional Systems:

Manual Controlling : As the name suggests ,we require manpower to manage traffic.The traffic police sees road status and decides the allowed duration of each direction.  
Automatic Controlling :Timers and electrical sensors operate the automatic traffic light. In the case of a traffic signal, the timer is set to a constant numerical number. Based on the timer value, the lights automatically turn on and off.
Electronic Sensors : Placing loop detectors or proximity sensors on the road is another advanced option. This sensor provides information about road traffic. Traffic signals are controlled based on this information.


Introduction:

Many cites facing a major problem of traffic congestion.Megacities(Mumbai,Hyderabad,Bengaluru,Delhi,etc) are the ones who are most afflicted by it, despite the fact that it appears to be present everywhere. Its ever-increasing nature necessitates real-time knowledge of road traffic density for improved signal control and traffic management. One of the most important variables affecting traffic flow is the traffic controller. The present traffic management systems are mostly static, meaning they don't respond to the needs of the traffic flow.

Exeution:

Technology:

You only look once (YOLO) is a state-of-the-art, real-time object detection system YOLO, a new approach to object detection. Prior work on object detection repurposes classifiers to perform detection. Instead, we frame object detection as a regression problem to spatially separated bounding boxes and associated class probabilities. A single neural network predicts bounding boxes and class probabilities directly from full images in one evaluation. Since the whole detection pipeline is a single network, it can be optimized end-to-end directly on detection performance.The object detection task consists in determining the location on the image where certain objects are present, as well as classifying those objects. Previous methods for this, like R-CNN and its variations, used a pipeline to perform this task in multiple steps. This can be slow to run and also hard to optimize, because each individual component must be trained separately. YOLO, does it all with a single neural network



