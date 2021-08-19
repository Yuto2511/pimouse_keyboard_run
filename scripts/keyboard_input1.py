#!/usr/bin/env python
#encoding: utf8
import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse

class KeyInput():
    def __init__(self):
        self.cmd_vel = rospy.Publisher('/cmd_vel',Twist,queue_size=1)

    def run(self):
        rate = rospy.Rate(50)
        date = Twist()

        data.linear.x = 0.0
        data.angular.z = 0.0
        while not rospy.is_shutdown():
            key = input()
            print(key)

            if key =='w':


if __name__ == '__main__':
    rospy.init_node('keyboard_input1')
    #下のサービスが利用可能になるまで待つ
    rospy.wait_for_service('/motor_on')
    rospy.wait_for_service('/motor_off')

    #ROS起動時にノードが立ち下がったら/motor_offを使用する
    rospy.on_shutdown(rospy.ServiceProxy('/motor_off',Trigger).call)
    rospy.ServiceProxy('/motor_on',Trigger).call()
    KeyInput().run()
