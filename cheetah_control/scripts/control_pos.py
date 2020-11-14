#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import random
import time
import numpy as np

class cheetah_control():
	def __init__(self, type_of_control = 'position', time_pause_before_control = 5, rate_value = 50):
		rospy.init_node('rotate', anonymous=True)

		self.type_of_control = type_of_control
		self.time_pause_before_control = time_pause_before_control

		time.sleep(self.time_pause_before_control)

		self.joints = {1: 'FL_hip_position_controller', 2: 'FL_thigh_position_controller', 3: 'FL_calf_position_controller',

		4: 'FR_hip_position_controller', 5: 'FR_thigh_position_controller', 6: 'FR_calf_position_controller',

		7: 'RL_hip_position_controller', 8: 'RL_thigh_position_controller', 9: 'RL_calf_position_controller',

		10: 'RR_hip_position_controller', 11: 'RR_thigh_position_controller', 12: 'RR_calf_position_controller'}
		self.pub = {}
		self.joints_number = len(self.joints)

		for i in range(1,self.joints_number+1):
			self.pub[i]=rospy.Publisher(self.joint_name(self.joints[i]), Float64, queue_size=10)

		self.rate = rospy.Rate(rate_value)




	def move_joint_to_pos(self,i, pos):
		"""

		i - number of joint: 
		1: 'FL_hip_position_controller', 
		2: 'FL_thigh_position_controller', 
		3: 'FL_calf_position_controller',
		4: 'FR_hip_position_controller', 
		5: 'FR_thigh_position_controller', 
		6: 'FR_calf_position_controller',
		7: 'RL_hip_position_controller', 
		8: 'RL_thigh_position_controller', 
		9: 'RL_calf_position_controller',
		10: 'RR_hip_position_controller', 
		11: 'RR_thigh_position_controller', 
		12: 'RR_calf_position_controller'


		pos - angle in rad
		"""	
		self.pub[i].publish(pos)	

	def joint_name(self, joint):
		joint_name = '/mini_chee/'+joint+'/command'
		return joint_name


if __name__ == '__main__':
	cheetah_control_pos = cheetah_control()

	LF_hip = (0.0,)
	LF_upper = (-0.45,)
	LF_lower = (0.9,)

	RF_hip = (0.0,)
	RF_upper = (-0.45,)
	RF_lower = (0.9,)

	LH_hip = (0.0,)
	LH_upper = (-0.45,)
	LH_lower = (0.9,)

	RH_hip = (0.0,)
	RH_upper = (-0.45,)
	RH_lower = (0.9,)
	len_configurations = len(LF_hip)

	while not rospy.is_shutdown():
		try:
			for i in range(len_configurations):
				cheetah_control_pos.move_joint_to_pos(1,LF_hip[i])
				cheetah_control_pos.move_joint_to_pos(2,LF_upper[i])
				cheetah_control_pos.move_joint_to_pos(3,LF_lower[i])

				cheetah_control_pos.move_joint_to_pos(4,RF_hip[i])
				cheetah_control_pos.move_joint_to_pos(5,RF_upper[i])
				cheetah_control_pos.move_joint_to_pos(6,RF_lower[i])

				cheetah_control_pos.move_joint_to_pos(7,LH_hip[i])
				cheetah_control_pos.move_joint_to_pos(8,LH_upper[i])
				cheetah_control_pos.move_joint_to_pos(9,LH_lower[i])

				cheetah_control_pos.move_joint_to_pos(10,RH_hip[i])
				cheetah_control_pos.move_joint_to_pos(11,RH_upper[i])
				cheetah_control_pos.move_joint_to_pos(12,RH_lower[i])
				cheetah_control_pos.rate.sleep()
		except rospy.ROSInterruptException:
			pass