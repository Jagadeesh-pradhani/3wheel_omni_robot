#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_rectangular():
    rospy.init_node('move_forward_node', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    twist_msg = Twist()
    movements = [
        (1.0, 0.5, 8.0),  # Move forward
        (0.0, 0.0, 2.0),  # Stop
        (1.0, 0.5, 8.0),  # Move forwar
        (0.0, 0.0, 2.0),  # Stop
    ] 
      
    for linear_x, angular_z, duration in movements:
        twist_msg.linear.x = linear_x
        twist_msg.angular.z = angular_z
        pub.publish(twist_msg)
        rospy.sleep(duration)

    rospy.signal_shutdown("Finished movement sequence")

if __name__ == '__main__':
    try:
        move_rectangular()
    except rospy.ROSInterruptException:
        pass

   
