#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math

publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

# Initialize a variable to store the last calculated distance along the x-axis
a = 0
b = 0

def callback(msg):
    global a  # global variable 'a' 
    global b 
    # angles positions to process
    i = [0, 15, 30, 45, 60]
    left = [700, 730, 760]

    #  list to store distances at each angle place
    right_distances = []
    left_distances = []

    for angle in i:
        #  angle to radians
        rad_angle = math.radians(angle)

        #  distance along the x-axis
        x_distance = msg.ranges[angle % len(msg.ranges)] * math.cos(rad_angle)

        a = x_distance

        # Store distance at each angle
        right_distances.append(a)

        print("Distance along x-axis at %d degrees: %f meters" % (angle, a))
        
    for angle in left:
        #  angle to radians
        rad_angle = math.radians(angle)

        #  distance along the x-axis
        y_distance = msg.ranges[angle % len(msg.ranges)] * math.cos(rad_angle)

        b = y_distance

        # Store distance at each angle
        left_distances.append(b)

        print("Distance along left-axis at %d degrees: %f meters" % (angle, b))

    # Check the condition
    if min(right_distances) >1 and min(left_distances) > 1:
        # Command to move straight when both conditions are met
        twist_msg = Twist()
        twist_msg.linear.x = 2.0  
        twist_msg.linear.y = 2.0  
        twist_msg.angular.z = 1.0
        publisher.publish(twist_msg)
    else:
        # command to move straight
        twist_msg = Twist()
        twist_msg.linear.x = 0.0  
        twist_msg.linear.y = 0.0  
        twist_msg.angular.z = 0.9
        publisher.publish(twist_msg)

if __name__ == '__main__':
    rospy.init_node('scan_values')

    sub = rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

