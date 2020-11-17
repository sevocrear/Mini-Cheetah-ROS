#!/usr/bin/env python3
# license removed for brevity
import rospy
from chee_control import cheetah_control


if __name__ == '__main__':
	cheetah_control_cur = cheetah_control(type_of_control = 'torque')

	LF_hip = (0.0,0)
	LF_upper = (-5,5)
	LF_lower = (0.9,0.9)

	RF_hip = (0.0,0)
	RF_upper = (-5,5)
	RF_lower = (0.9, 0.9)

	LH_hip = (0.0, 0)
	LH_upper = (-5, 5)
	LH_lower = (0.9, 0.9)

	RH_hip = (0.0, 0.0)
	RH_upper = (-5, 5)
	RH_lower = (0.9, 0.9)
	len_configurations = len(LF_hip)

	while not rospy.is_shutdown():
		try:
			for i in range(len_configurations):
				cheetah_control_cur.move_joint(1,LF_hip[i])
				cheetah_control_cur.move_joint(2,LF_upper[i])
				cheetah_control_cur.move_joint(3,LF_lower[i])

				cheetah_control_cur.move_joint(4,RF_hip[i])
				cheetah_control_cur.move_joint(5,RF_upper[i])
				cheetah_control_cur.move_joint(6,RF_lower[i])

				cheetah_control_cur.move_joint(7,LH_hip[i])
				cheetah_control_cur.move_joint(8,LH_upper[i])
				cheetah_control_cur.move_joint(9,LH_lower[i])

				cheetah_control_cur.move_joint(10,RH_hip[i])
				cheetah_control_cur.move_joint(11,RH_upper[i])
				cheetah_control_cur.move_joint(12,RH_lower[i])
				cheetah_control_cur.rate.sleep()
		except rospy.ROSInterruptException:
			pass