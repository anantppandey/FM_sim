#Formula Manipal Car Gazebo Simulation 

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
