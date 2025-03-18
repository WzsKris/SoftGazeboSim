# SoftGazeboSim
## Major requirements
Ubuntu 20.04.3 LTS (Desktop Version), ROS Noetic, Gazebo (Version 11)


**Instructions**

1) Download or clone the repo
2) Open a terminal inside the repo directory
3) source the setup.bash file. You will need to do this every time before you launch and .launch files mentioned below

4) If controller packages are not installed, please follow the following commands and install ros controller packages

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

curl -sSL 'http://keyserver.ubuntu.com/pks/lookupop=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -

sudo apt update

sudo apt-get install ros-noetic-ros-control ros-noetic-ros-controllers

## Launch Gazebo Model and Applications

Step #1: Open a terminal and launch the Gazebo model 

```bash
  catkin_make
  source devel/setup.bash
  cd ~/src
  roslaunch fullurdf3 gazebo.launch
```
  Step #2: Open a 2nd new terminal and launch position publication and effort controllers

```bash
  cd ~/src
  source devel/setup.bash
  roslaunch fullurdf3 control.launch
```
  Step #3: Open a 3rd new terminal and launch the necessary scripts either for joint-control of stiffness/damping-control
  
```bash  
  cd ~/src/fullurdf3/scripts
  python3 stiffness_value.py
  python3 damping_value.py
  python3 increment.py
```
```bash
stiffness_client.cpp
```
**ROS controller tutorial link**

https://classic.gazebosim.org/tutorials?tut=ros_control
