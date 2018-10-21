#!/usr/bin/env python
   3 import rospy
   4 from geometry_msgs.msg import Twist
   5 
   6 def publisher():
   7     pub = rospy.Publisher('commands', Twist, queue_size=10)
   8     rospy.init_node('publisher', anonymous=True)
   9     rate = rospy.Rate(10) # 10hz
         cmd_vel = Twist()
  10     while not rospy.is_shutdown():
  13         if (abs(angle) < 30 and abs(angle) > 2):
                 cmd_vel.linear.x = 1.0
                 cmd_vel.linear.y = 0.0
                 cmd_vel.linear.z = 0.0
                 cmd_vel.angular.x = 1.0
                 cmd_vel.angular.y = 0.0
                 cmd_vel.angular.z = 0.0
             else:
                 cmd_vel.linear.x = 0.0
                 cmd_vel.linear.y = 0.0
                 cmd_vel.linear.z = 0.0
                 cmd_vel.angular.x = 0.0
                 cmd_vel.angular.y = 0.0
                 cmd_vel.angular.z = 0.0
             pub.publish(cmd_vel)
  14         rate.sleep()
  15 
  16 if __name__ == '__main__':
  17     try:
  18         publisher()
  19     except rospy.ROSInterruptException:
  20         pass
