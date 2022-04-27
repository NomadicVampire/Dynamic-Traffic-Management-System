# Dynamic-Traffic-Management-System

# Abstract:
Traffic congestion is becoming a serious problem with a large number of cars on the roads.It not only add time and stress to drivers' lives, but they also increase fuel consumption and pollution. Congestion in traffic can be caused by a variety of factors such as a lack of capacity, unregulated demand, long red light delays, and so on.Traffic lights being one of the critical factors affecting traffic flow.Conventional traffic system like Automating control system is creating  a serious problem with large number of vehicles on the road. With a lot of vehicles waiting in queue to be proceded is increasing. And traditional system cannot manage it.

Our suggested system attempts to create a computer vision-based traffic signal controller that can adapt to the present traffic situation. It calculates real-time traffic density using live video feed from traffic junction CCTV cameras by recognising vehicles at the signal and adjusting the green signal time accordingly. To get a more exact estimation of the green signal time, the vehicles are classed as automobile, bike, bus/truck, or rickshaw. To determine the number of vehicles in each direction, we employed object detection techniques such as YOLO. The timers of these traffic signals are then set based on the vehicle density in each direction, and the system becomes adaptable. This aids in the optimization of green signal timings and traffic flow.

# Problem Statement:

To develop a self-adaptive traffic light control system based on yolo. Due to disproportionate and diverse traffic in various lanes, inefficient usage of the same time slot for each of them results in slower speeds, longer trip durations, and more vehicle waiting.Design a system that allows the traffic management system to make time allocation decisions for a given lane based on the traffic density on other lanes using cameras and image processing modules.This method can override the earlier system of hardcoded lights, which causes unnecessary delays, lowering traffic and waiting time, reducing the frequency of accidents and fuel usage, and so helping to control air pollution.


# Conventional Systems:

Manual Controlling : As the name suggests ,we require manpower to manage traffic.The traffic police sees road status and decides the allowed duration of each direction.  
Automatic Controlling :Timers and electrical sensors operate the automatic traffic light. In the case of a traffic signal, the timer is set to a constant numerical number. Based on the timer value, the lights automatically turn on and off.
Electronic Sensors : Placing loop detectors or proximity sensors on the road is another advanced option. This sensor provides information about road traffic. Traffic signals are controlled based on this information.


# Introduction:

Many cites facing a major problem of traffic congestion.Megacities(Mumbai,Hyderabad,Bengaluru,Delhi,etc) are the ones who are most afflicted by it, despite the fact that it appears to be present everywhere. Its ever-increasing nature necessitates real-time knowledge of road traffic density for improved signal control and traffic management. One of the most important variables affecting traffic flow is the traffic controller. The present traffic management systems are mostly static, meaning they don't respond to the needs of the traffic flow.



# Technology:

The term 'You Only Look Once' is abbreviated as YOLO. This is an algorithm for detecting and recognising different items in a photograph (in real-time). Object detection in YOLO is done as a regression problem, and the identified photos' class probabilities are provided.
Convolutional neural networks (CNN) are used in the YOLO method to recognise objects in real time. To detect objects, the approach just takes a single forward propagation through a neural network, as the name suggests.
This indicates that a single algorithm run is used to forecast the entire image. The CNN is used to forecast multiple bounding boxes and class probabilities at the same time.

![WhatsApp Image 2022-04-27 at 12 33 46 AM](https://user-images.githubusercontent.com/72182471/165373716-6cb51d07-94bf-47ad-9087-5d702adb3014.jpeg)


![yolo net](https://user-images.githubusercontent.com/72182471/165361893-fd2fff2d-7f61-4c8c-95f3-7fe828a018ef.png)


# Working:
Get a real time image from the traffic catching camera
Scan and determine the traffic density
Input this data to the Time Allocation module
The output will be the time slots for each lane accordingly.


# Conclusion:
This is a project that counts automobiles in the images using the YoloV3 neural network and it will acts as an input parameter which will help to change the traffic signal timer fixed static value to dynamic value depending upon the situation and Hence our goal of changing the static time period of traffic signals to dynamic time period of signal so that the regulation of traffic signal is better in the city.


![seq](https://user-images.githubusercontent.com/72182471/165362571-06875fea-9fe9-4075-a74e-871503363649.png)


Download the YOLO model from here: https://drive.google.com/drive/folders/1XaxVeDwKMTkE7jk9omMGmKVYea01P9XV?usp=sharing

