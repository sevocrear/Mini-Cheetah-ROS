#!/usr/bin/env python3
# license removed for brevity
import rospy
import time
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
class cheetah_control():
    def __init__(self, type_of_control = 'position', time_pause_before_control = 0, rate_value = 50):
        rospy.init_node('cheetah_control', anonymous=True)
        self.type_of_control = type_of_control
        self.time_pause_before_control = time_pause_before_control
        time.sleep(self.time_pause_before_control)

        if type_of_control == 'position':
            self.joints = {1: 'FL_hip_position_controller', 2: 'FL_thigh_position_controller', 3: 'FL_calf_position_controller',

        4: 'FR_hip_position_controller', 5: 'FR_thigh_position_controller', 6: 'FR_calf_position_controller',

        7: 'RL_hip_position_controller', 8: 'RL_thigh_position_controller', 9: 'RL_calf_position_controller',

        10: 'RR_hip_position_controller', 11: 'RR_thigh_position_controller', 12: 'RR_calf_position_controller'}

        elif type_of_control == 'torque':
            self.joints = {1: 'FL_hip_Effort_controller', 2: 'FL_thigh_Effort_controller', 3: 'FL_calf_Effort_controller',

        4: 'FR_hip_Effort_controller', 5: 'FR_thigh_Effort_controller', 6: 'FR_calf_Effort_controller',

        7: 'RL_hip_Effort_controller', 8: 'RL_thigh_Effort_controller', 9: 'RL_calf_Effort_controller',

        10: 'RR_hip_Effort_controller', 11: 'RR_thigh_Effort_controller', 12: 'RR_calf_Effort_controller'}

        self.pub = {}
        self.joints_number = len(self.joints)

        self.cheetah_joints_sub = rospy.Subscriber("/mini_chee/joint_states", JointState, self.joints_pos_callback)
        for i in range(1,self.joints_number+1):
            self.pub[i]=rospy.Publisher(self.joint_name(self.joints[i]), Float64, queue_size=10)

        self.rate = rospy.Rate(rate_value)

        self.joints_positions = {}

    def move_joint(self,i, pos):
        """

        i - number of joint: 
        1: 'FL_hip_controller', 
        2: 'FL_thigh_controller', 
        3: 'FL_calf_controller',
        4: 'FR_hip_controller', 
        5: 'FR_thigh_controller', 
        6: 'FR_calf_controller',
        7: 'RL_hip_controller', 
        8: 'RL_thigh_controller', 
        9: 'RL_calf_controller',
        10: 'RR_hip_controller', 
        11: 'RR_thigh_controller', 
        12: 'RR_calf_controller'


        pos - angle in rad
        """	
        self.pub[i].publish(pos)	

    def joint_name(self, joint):
        joint_name = '/mini_chee/'+joint+'/command'
        return joint_name

    #callback function for robot pos
    def joints_pos_callback(self, cheetah_joints_pos):
        '''
        joints:
        ['FL_calf_joint', 'FL_hip_joint', 'FL_thigh_joint', 
        'FR_calf_joint', 'FR_hip_joint', 'FR_thigh_joint', 
        'RL_calf_joint', 'RL_hip_joint', 'RL_thigh_joint', 
        'RR_calf_joint', 'RR_hip_joint', 'RR_thigh_joint']
        '''
        self.joints_positions = dict(zip(cheetah_joints_pos.name, cheetah_joints_pos.position))