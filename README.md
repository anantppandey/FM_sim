Introduction – The Project features a drivable model of the formula manipal’s race car in the         simulated real world enviroment of Gazebo. The project required creation of a gazebo model using the provided CAD model, adding the necessary sensors to it that can publish their outputs to appropriate ROS topics.



How to Use – Copy all the packages from the src folder into a new Workspace and run catkin_make then follow the steps given below.
There are two ways of accessing the simulation -
    • Run the following commands in seprate terminals and then finally move back to the turtlebot_teleop terminal to control the vehicle.
        	
                • roslaunch catvehicle FM_car.launch 
                • roslaunch turtlebot_teleop keyboard_teleop.launch
                • rosrun topic_tools relay /cmd_vel_mux/input/teleop /catvehicle/cmd_vel
    
    • Alternatively – Run the following commands in seprate terminals and then finally move back to the turtlebot_teleop terminal to control the vehicle.
        	
                • roslaunch catvehicle catvehicle_empty.launch

                • gzclient

                • roslaunch catvehicle catvehicle_spawn.launch robot:=catvehicle X:=0 Y:=0 yaw:=1.5707963267

                • roslaunch turtlebot_teleop keyboard_teleop.launch

                • rosrun topic_tools relay /cmd_vel_mux/input/teleop /catvehicle/cmd_vel		

P.s. - 	The launch file does not seem to work in lower end laptops so the alternative methord is  	recommended.
-	You need to increase the velocity in the turtlebot_teleop terminal with the “W” key first to a 	sufficient velocity for the vehicle to move
-	The vehicle moves with the < U, I, O, J, K, L, M, ‘,’, ‘.’ > keys as explained the 	turtlebot_teleop_keyboard terminal.
