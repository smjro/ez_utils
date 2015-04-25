# ez_utils

ros utility for follow_joint_trajectory

## How to use

This is client for follow_joint_trajectory action. You can use it very easily from Python.

```python
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
```

This program starts subscriber like below.

- /head_traj_controller/follow_position (uz_utils/TargetJoints)

`uz_utils/TargetJoints` is just an array of float64. You can move joints very easily.
You can use the server object directory if you want to omit publisher.

```
head.set_positions([0.5, 0.1])
```
