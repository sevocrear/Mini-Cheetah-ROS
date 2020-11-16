#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import random
import time
import numpy as np
from dynamic_reconfigure.msg import Config # dynamics reconfigure

config = Config() # dynamics reconfigure

def reconfigure_cb(data): # dynamics reconfigure callback
    global config
    config = data

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

    reconfigure_sub = rospy.Subscriber('/cheetah_pos_reconfigure/parameter_updates', Config, reconfigure_cb) # dynamics reconfigure subscriber

    cheetah_control_pos = cheetah_control()

    while not rospy.is_shutdown():

        for i in range(len(config.doubles)):
            if config.doubles[i].name == 'FR_hip_pos':
                FR_hip_pos = config.doubles[i].value
            if config.doubles[i].name == 'FR_thigh_pos':
                FR_thigh_pos = config.doubles[i].value
            if config.doubles[i].name == 'FR_calf_pos':
                FR_calf_pos = config.doubles[i].value

            if config.doubles[i].name == 'FL_hip_pos':
                FL_hip_pos = config.doubles[i].value
            if config.doubles[i].name == 'FL_thigh_pos':
                FL_thigh_pos = config.doubles[i].value
            if config.doubles[i].name == 'FL_calf_pos':
                FL_calf_pos = config.doubles[i].value
            
            if config.doubles[i].name == 'BR_hip_pos':
                BR_hip_pos = config.doubles[i].value
            if config.doubles[i].name == 'BR_thigh_pos':
                BR_thigh_pos = config.doubles[i].value
            if config.doubles[i].name == 'BR_calf_pos':
                BR_calf_pos = config.doubles[i].value

            if config.doubles[i].name == 'BL_hip_pos':
                BL_hip_pos = config.doubles[i].value
            if config.doubles[i].name == 'BL_thigh_pos':
                BL_thigh_pos = config.doubles[i].value
            if config.doubles[i].name == 'BL_calf_pos':
                BL_calf_pos = config.doubles[i].value

        cheetah_control_pos.move_joint_to_pos(1,FL_hip_pos)
        cheetah_control_pos.move_joint_to_pos(2,FL_thigh_pos)
        cheetah_control_pos.move_joint_to_pos(3,FL_calf_pos)

        cheetah_control_pos.move_joint_to_pos(4,FR_hip_pos)
        cheetah_control_pos.move_joint_to_pos(5,FR_thigh_pos)
        cheetah_control_pos.move_joint_to_pos(6,FR_calf_pos)

        cheetah_control_pos.move_joint_to_pos(7,BL_hip_pos)
        cheetah_control_pos.move_joint_to_pos(8,BL_thigh_pos)
        cheetah_control_pos.move_joint_to_pos(9,BL_calf_pos)

        cheetah_control_pos.move_joint_to_pos(10,BR_hip_pos)
        cheetah_control_pos.move_joint_to_pos(11,BR_thigh_pos)
        cheetah_control_pos.move_joint_to_pos(12,BR_calf_pos)
        cheetah_control_pos.rate.sleep()