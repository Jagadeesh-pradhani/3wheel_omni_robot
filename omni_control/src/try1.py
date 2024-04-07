#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ModelStates
import math
import time

def model_states_callback(msg):
    # Find the index of the robot in the model_states list
    try:
        index = msg.name.index('omni_robot') # replace 'your_robot_name' with the actual name of your robot
        twist = msg.twist[index]
        # Extract the current yaw (angular velocity around z-axis)
        x = twist.linear.x
        y = twist.linear.y
        z = twist.linear.z
        yaw = twist.angular.z

        nex = Twist()
        nex.linear.x = 1
        nex.linear.y = 0
        nex.angular.z = 0
        pub.publish(nex) 
        time.sleep(2)
        nex.linear.x = 0
        nex.linear.y = 1
        nex.angular.z = 0
        pub.publish(nex) 



    except ValueError:
        rospy.logwarn("Robot not found in model_states")


rospy.init_node('bot_controller')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rospy.Subscriber('/gazebo/model_states', ModelStates, model_states_callback)

rospy.spin()
