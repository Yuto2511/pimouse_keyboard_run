#!/usr/bin/env python
#encoding: utf8

import rospy, math
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse
from pimouse_keyboard_run.msg import key_val

class ReadRun():
    def __init__(self):
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

        self.key = key_val()
        rospy.Subscriber('key_val', key_val, self.callback)

    def callback(self,message):
        self.key = message

    def run(self):
        r = rospy.Rate(10)
        data = Twist()

        while not rospy.is_shutdown():
            if self.key.key == None:
                data.linear.x = 0.0
            elif self.key.key == 'w':
                data.linear.x = 0.2
            elif self.key.key == 'a':
                data.linear.x = 0.2
                data.angular.z = math.pi / 3
            elif self.key.key == 'd':
                data.linear.x = 0.2
                data.angular.z = - math.pi / 3
            else:
                data.linear.x = 0.0
                data.angular.z = 0.0
            self.cmd_vel.publish(data)
            self.key.key = None
            r.sleep()

if __name__ == '__main__':
    rospy.init_node('read_run', anonymous=True)
    rospy.wait_for_service('/motor_on')
    rospy.wait_for_service('/motor_off')
    rospy.on_shutdown(rospy.ServiceProxy('/motor_off', Trigger).call)
    rospy.ServiceProxy('/motor_on', Trigger).call()
    ReadRun().run()
