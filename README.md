## 2023.8 the last time update 
 for myself and other supporters
 
 -a complete system of detecting shapes and zcodes while controlling the robot arm system
 
 ![e09354b84c711a332494bdc5414aa11](https://github.com/kouge0510/robot_control-with-Opencv/assets/72262866/96492b09-5717-4d66-89f3-c11d2f4cced2)
 
 -Using python to make it with raspberry 4B
 
 -with ZhongLing Tech Company Servo and Uno MCU.
 
 -Six degree of freedom robotic arm
 
 -2 Pwm Servos and 4 Bus servos
 
 -including two kinds of solutions
 
 -1:Deriving an action through the inverse of the final coordinate point and is inverse kinematics
 
 -2.Forward kinematics, which directly adjusts the angle of each servo for control, is relatively rigid and can only rotate a fixed angle

## The file structure

**arm_control.py** shows the inverse kinematics mean to control the robo_arm

**cluster.py** shows the basic way to use opencv to detect things.In this program,I use the python-opencv lib to invoke it.
And it shows the way to detect different colors with RGB

**shapes.py** shows the hough circle algorithm and edge point algorithm to detect triangle and rectangle.

**uart.py** shows the basic usage of uart agreement.And I provide two ways to use it.You can use it with single threading or multiple threadings.

**zcode.py** uses the pyzbar lib to detect zcode.

**word_detect.py** is the final solution to use it.As I use it in the contest that is no longer available to other programs.So I just didn't show it all.

## The progress and features

- [x] finish the program
- [x] can use with uart
- [x] can use with raspberry pi all series
- [x] support python >=3.8
- [x] support cv >=4.0
- [x] can use with other brands of ARM development board as it uses general libs.
