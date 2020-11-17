#!/usr/bin/env python3

import rospy

from dynamic_reconfigure.server import Server
from reconfigure.cfg import current_reconfigureConfig

def callback(config, level):
    rospy.loginfo("""Configure : {FR_hip_cur}, {FR_thigh_cur}, {FR_calf_cur}, 
                                {FL_hip_cur}, {FL_thigh_cur}, {FL_calf_cur},
                                {BR_hip_cur}, {BR_thigh_cur}, {BR_calf_cur},
                                {BL_hip_cur}, {BL_thigh_cur}, {BL_calf_cur}""".format(**config))
    return config

if __name__ == "__main__":
    rospy.init_node("Cheetah joint currents SET", anonymous = False)
    srv = Server(current_reconfigureConfig, callback)
    rospy.spin()