#!/usr/bin/env python3

import rospy
from fullurdf3.srv import SetStiffness, SetStiffnessRequest
import time

def change_stiffness():
    rospy.init_node('change_stiffness_node')
    rospy.loginfo("Node initialized")
    
    # Wait for stiffness service
    rospy.wait_for_service('/gazebo/set_joint_stiffness_fullurdf3')
    rospy.loginfo("Service /gazebo/set_joint_stiffness_fullurdf3 found")
    set_stiffness = rospy.ServiceProxy('/gazebo/set_joint_stiffness_fullurdf3', SetStiffness)
    rospy.loginfo("ServiceProxy for stiffness created")
    
    # Define the stiffness value to set for all joints
    stiffness_value = 1.11  

    # Iterate over joint indices
    for joint_index in range(2, 51):
        joint_name = f'joint{joint_index:02d}'
        
        # Prepare the stiffness service request
        stiffness_req = SetStiffnessRequest()
        stiffness_req.joint_name = joint_name
        stiffness_req.stiffness = stiffness_value

        rospy.loginfo(f"Calling /gazebo/set_joint_stiffness_fullurdf3 service for {joint_name} with stiffness {stiffness_value}")

        # Call the stiffness service
        try:
            stiffness_resp = set_stiffness(stiffness_req)
            if stiffness_resp.success:
                rospy.loginfo(f"Successfully set stiffness of {joint_name} to {stiffness_value}")
            else:
                rospy.logerr(f"Failed to set stiffness of {joint_name} to {stiffness_value}: {stiffness_resp.message}")
        except rospy.ServiceException as e:
            rospy.logerr(f"Service call failed for stiffness: {e}")

        # Sleep briefly between service calls (adjust as needed)
        time.sleep(0.1)

if __name__ == '__main__':
    change_stiffness()
