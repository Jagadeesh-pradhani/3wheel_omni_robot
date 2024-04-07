#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Wrench
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
import time


rospy.init_node("movement")

pub = rospy.Publisher("/force",Wrench, queue_size=10)
pub2 = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

pu = rospy.Publisher('/omni_robot/back_joint_velocity_controller/command', Float64, queue_size=10)
pu1 = rospy.Publisher('/omni_robot/left_joint_velocity_controller/command', Float64, queue_size=10)
pu2 = rospy.Publisher('/omni_robot/right_joint_velocity_controller/command', Float64, queue_size=10)

rate=rospy.Rate(2)

vel = Float64()
vel1 = Float64()
vel2 = Float64()

lin = Wrench()
ang = Twist()

vel.data = 20
vel1.data = 20
vel2.data = 20

print("Starting movement")
print("Rotation: CCW")

ang.angular.z = 0
lin.force.x = 0
lin.force.y = 0

pub.publish(lin)
pub2.publish(ang)

time.sleep(1)

ang.angular.z = 1
lin.force.y = 100

pub.publish(lin)
pub2.publish(ang)



time.sleep(10)

ang.angular.z = 0
lin.force.x = 0
lin.force.y = 0

pub.publish(lin)
pub2.publish(ang)


print("end")

