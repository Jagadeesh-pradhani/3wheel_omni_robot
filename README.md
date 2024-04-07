# 3wheel_omni_robot


For gmapping and navigation omni robot:


roslaunch omni_gazebo gazebo.launch 

roslaunch omni_gmapping slam_gmapping.launch

move the bot and cover all the area and create a map:

save the map using command: map will be saved in present working directory

rosrun map_server map_saver -f simple_world		//simple_world : name of world

copy paste the map.yaml in the directory:  ~/FC_ws/src/omni_robot/omni_navigation/maps/map.yaml

run navigatin : 
export TURTLEBOT3_MODEL=burger	//see launch file for more info
roslaunch omni_navigation omni_navigation.launch








