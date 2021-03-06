#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = (message.data*2)-1


rospy.init_node('odd')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('odd', Int32, queue_size=1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub.publish(n)
    rate.sleep()
