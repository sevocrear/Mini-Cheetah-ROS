#!/usr/bin/env python3

import rospy

from dynamic_reconfigure.server import Server
from reconfigure.cfg import position_reconfigureConfig

def callback(config, level):
    rospy.loginfo("""Configure : {FR_hip_pos}, {FR_thigh_pos}, {FR_calf_pos}, 
                                {FL_hip_pos}, {FL_thigh_pos}, {FL_calf_pos},
                                {BR_hip_pos}, {BR_thigh_pos}, {BR_calf_pos},
                                {BL_hip_pos}, {BL_thigh_pos}, {BL_calf_pos}""".format(**config))
    return config

if __name__ == "__main__":
    rospy.init_node("Cheetah joint positions SET", anonymous = False)
    srv = Server(position_reconfigureConfig, callback)
    rospy.spin()