import rospy
from follow_joints_utils.msg import TargetJoints
from control_msgs.msg import FollowJointTrajectoryActionGoal
from trajectory_msgs.msg import JointTrajectoryPoint

class EzJoints(object):
    def __init__(self, controller_name):
        self._joint_names = rospy.get_param(controller_name + '/joints')
        self._dof = len(self._joint_names)
        self._sub = rospy.Subscriber(controller_name + '/follow_position',
                                     TargetJoints,
                                     self.position_callback, queue_size=1)
        self._pub = rospy.Publisher(controller_name + '/follow_joint_trajectory/goal', FollowJointTrajectoryActionGoal, queue_size=1)
        self._velocity = rospy.get_param(controller_name + '/follow_velocity', 1.0)
        self._acceleration = rospy.get_param(controller_name + '/follow_acceleration', 1.0)
        rospy.loginfo('initialize %s, dof=%d' % (controller_name, self._dof))

    def position_callback(self, msg):
        action_goal = FollowJointTrajectoryActionGoal()
        action_goal.goal_id.stamp = rospy.get_rostime()
        action_goal.goal.trajectory.joint_names = self._joint_names
        target_point = JointTrajectoryPoint()
        if self._dof == len(msg.positions):
            target_point.positions = msg.positions
        else:
            target_point.positions = []
            for position in msg.positions:
                target_point.positions.append(position)
            for i in range(self._dof - len(msg.positions)):
                target_point.positions.append(0.0)
        target_point.velocities = [self._velocity] * self._dof
        target_point.accelerations = [self._acceleration] * self._dof
        action_goal.goal.trajectory.points.append(target_point)
        self._pub.publish(action_goal)
