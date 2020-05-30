#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import random
import time
import numpy as np


def move_joint(pub, speed, upper_limit, lower_limit, rate_value):
    i = rospy.get_time()
    diff = (upper_limit - lower_limit)/2
    offset = upper_limit - diff
    position = np.sin(i/rate_value*speed)*diff + offset
    # rospy.loginfo(position)
    pub.publish(position)

def move_joint_to_pos(pub, pos):
    pub.publish(pos)	

def joint_name(joint):
    joint_name = '/mini_chee/'+joint+'/command'
    return joint_name


if __name__ == '__main__':
	speed = 100
	upper_limit = np.pi
	lower_limit = -np.pi
	time.sleep(5)
	rospy.init_node('rotate', anonymous=True)

	joints = {1: 'FL_hip_position_controller', 2: 'FL_thigh_position_controller', 3: 'FL_calf_position_controller',

	4: 'FR_hip_position_controller', 5: 'FR_thigh_position_controller', 6: 'FR_calf_position_controller',

	7: 'RL_hip_position_controller', 8: 'RL_thigh_position_controller', 9: 'RL_calf_position_controller',

	10: 'RR_hip_position_controller', 11: 'RR_thigh_position_controller', 12: 'RR_calf_position_controller'}
	pub = {}
	joints_number = len(joints)
	for i in range(1,joints_number+1):
		pub[i]=rospy.Publisher(joint_name(joints[i]), Float64, queue_size=10)


	rate_value = 50  # 50hz
	rate = rospy.Rate(rate_value)

	while not 0:
		try:
			# move_joint(pub[3], speed, upper_limit, lower_limit,rate_value)
			# move_joint(pub[6], speed, upper_limit, lower_limit, rate_value)
			move_joint_to_pos(pub[3],np.pi/4)
			move_joint_to_pos(pub[6], np.pi/4)
		except rospy.ROSInterruptException:
			pass
		rate.sleep()
