# Formula Manipal Car Gazebo Simulation 

**Introduction** - The Project features a drivable model of the formula manipal’s race car in the         simulated real world enviroment of Gazebo. The project required creation of a gazebo model using the provided CAD model, adding the necessary sensors to it that can publish their outputs to appropriate ROS topics.


**How to Use** -

*Empty World* - To run the simulation in an empty world :
```
roslaunch catvehicle FM_car.launch
```
*Alternatively* - 
```
roslaunch catvehicle catvehicle_empty.launch
roslaunch catvehicle catvehicle_spawn.launch robot:=catvehicle yaw:=1.5707963267
```
Here the first command launces the empty world and the second one launches the vehicle.


**Acceleration Track** - To run the simulation in an acceleration track :
```
roslaunch catvehicle fm_acceleration.launch
```
*Alternatively* -
```
roslaunch eufs_gazebo acceleration.launch
roslaunch catvehicle catvehicle_spawn.launch robot:=catvehicle X:=-53
```

**Skidpad Track** - To run the simulation in an acceleration track:
```
roslaunch catvehicle fm_skidpad.launch
```
*Alternatively* -
```
roslaunch eufs_gazebo skidpad.launch 
roslaunch catvehicle catvehicle_spawn.launch robot:=catvehicle Y:=-14.4 yaw:=1.5707963267
```

**Controling the Vehicle** - In order the steer the vehicle run the following commands :
```
roslaunch  turtlebot_teleop keyboard_teleop.launch
rosrun topic_tools relay /cmd_vel_mux/input/teleop /catvehicle/cmd_vel
```
After executing the second command you need to return to the terminal with the first 	command i.e. keyboard_teleop.launch in order to control the vehicle



**P.S.** -The launch file does not seem to work in lower end laptops so the alternative methord is  	recommended.
-You need to increase the velocity in the turtlebot_teleop terminal with the “W” key first to a 	sufficient velocity for the vehicle to move.
-The vehicle moves with the < U, I, O, J, K, L, M, ‘,’, ‘.’ > keys as explained the 	turtlebot_teleop_keyboard terminal.
