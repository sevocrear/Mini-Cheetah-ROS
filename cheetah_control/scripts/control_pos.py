#!/usr/bin/env python
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

		self.rate_value = rate_value




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
		12: 'RR_calf_position_controller';


		pos - angle in rad
		"""	
		self.pub[i].publish(pos)	

	def joint_name(self, joint):
		joint_name = '/mini_chee/'+joint+'/command'
		return joint_name


if __name__ == '__main__':
	cheetah_control_pos = cheetah_control()

	while not rospy.is_shutdown():
		try:
			cheetah_control_pos.move_joint_to_pos(3,np.pi/4)
			cheetah_control_pos.move_joint_to_pos(6, np.pi/4)
		except rospy.ROSInterruptException:
			pass
	cheetah_control_pos.rate_value.sleep()
