#!/usr/bin/env python

import rospy
from ez_utils.msg import TargetJoints
from ez_utils.ez_joints import JointsServer

if __name__ == '__main__':
    rospy.init_node('pr2_joints')
    head = JointsServer('/head_traj_controller')
    left_arm = JointsServer('/l_arm_controller')
    right_arm = JointsServer('/r_arm_controller')
    rospy.spin()

