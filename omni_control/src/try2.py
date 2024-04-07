#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

rospy.init_node('vel_Publisher')
pub = rospy.Publisher('/omni_robot/back_joint_velocity_controller/command', Float64, queue_size=10)
pub1 = rospy.Publisher('/omni_robot/left_joint_velocity_controller/command', Float64, queue_size=10)
pub2 = rospy.Publisher('/omni_robot/right_joint_velocity_controller/command', Float64, queue_size=10)

rate=rospy.Rate(2)

vel = Float64()
vel1 = Float64()
vel2 = Float64()
vx= 1
vy = 0
wz = 1

L = 0.04
vel.data = 20
vel1.data = 20
vel2.data = 20

while not rospy.is_shutdown():
	pub.publish(vel)
	pub1.publish(vel1)
	pub2.publish(vel2)
	
	rate.sleep()


