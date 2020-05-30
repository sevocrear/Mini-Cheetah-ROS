#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import random
import time

import numpy as np
import time 
def move_joint(pub, speed, upper_limit, lower_limit):
    i = rospy.get_time()
    diff = (upper_limit - lower_limit)/2
    offset = upper_limit - diff
    position = np.sin(i/rate_value*speed)*diff + offset
    # rospy.loginfo(position)
    pub.publish(position)


def joint_name(joint):
    joint_name = '/mini_chee/'+joint+'/command'
    return joint_name


if __name__ == '__main__':
    time.sleep(3)

    speed = 100
    upper_limit = np.pi
    lower_limit = -np.pi

    joints = {1:'FL_hip_position_controller',2:'FL_thigh_position_controller',3:'FL_calf_position_controller',

    4:'FR_hip_position_controller',5:'FR_thigh_position_controller',6:'FR_calf_position_controller',

    7:'RL_hip_position_controller',8:'RL_thigh_position_controller',9:'RL_calf_position_controller',

    10:'RR_hip_position_controller',11:'RR_thigh_position_controller',12:'RR_calf_position_controller'}

    pub = {}
    joints_number = len(joints)
    for i in range(1,joints_number+1):
        pub[i]=rospy.Publisher(joint_name(joints[i]), Float64, queue_size=10)

    rospy.init_node('joints_talker', anonymous=True)
    rate_value = 50  # 50hz
    rate = rospy.Rate(rate_value)

    while not rospy.is_shutdown():
        # for i in range(joints_number):
        #     try:
        #         move_joint(pub[i], speed, upper_limit, lower_limit)
        #     except rospy.ROSInterruptException:
        #         pass
        try:
            move_joint(pub[1], speed, upper_limit, lower_limit)
            move_joint(pub[4], speed, upper_limit, lower_limit)

        except rospy.ROSInterruptException:
            pass
        rate.sleep()