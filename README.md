# follow_joints_utils

ros utility for follow_joint_trajectory

## How to use

This is client for follow_joint_trajectory action. You can use it very easily from Python.

```python
#!/usr/bin/env python

import rospy
from follow_joints_utils.msg import TargetJoints
from follow_joints_utils.ez_joints import EzJoints

if __name__ == '__main__':
    rospy.init_node('pr2_joints')
    head = EzJoints('/head_traj_controller')
    left_arm = EzJoints('/l_arm_controller')
    right_arm = EzJoints('/r_arm_controller')
    rospy.spin()
```
