#! /usr/bin/python
# -*- coding :utf-8 -*-
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('talker',anonymous=True)
    pub = rospy.Publisher('chat',String, queue_size=10)  
    rate  =rospy.Rate(10)

    while not rospy.is_shutdown():
        hello = 'hello world ! %s' % rospy.get_time()
        pub.publish(hello)
        rospy.loginfo(hello)
        rate.sleep()

