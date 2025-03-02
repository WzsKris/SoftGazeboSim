#!/usr/bin/env python3

import rospy
from fullurdf3.srv import SetDamping, SetDampingRequest
import time

def change_damping():
    rospy.init_node('change_damping_node')
    rospy.loginfo("Node initialized")
    
    # Wait for damping service
    rospy.wait_for_service('/gazebo/set_joint_damping_fullurdf3')
    rospy.loginfo("Service /gazebo/set_joint_damping_fullurdf3 found")
    set_damping = rospy.ServiceProxy('/gazebo/set_joint_damping_fullurdf3', SetDamping)
    rospy.loginfo("ServiceProxy for damping created")
    
    # Define the damping value to set for the specific joints
    damping_value = 1  

    # List of joints to change damping
    joints_to_change = ['joint11', 'joint21', 'joint31', 'joint41']
    
    # Iterate over the specific joints
    for joint_name in joints_to_change:
        # Prepare the damping service request
        damping_req = SetDampingRequest()
        damping_req.joint_name = joint_name
        damping_req.damping = damping_value

        rospy.loginfo(f"Calling /gazebo/set_joint_damping_fullurdf3 service for {joint_name} with damping {damping_value}")

        # Call the damping service
        try:
            damping_resp = set_damping(damping_req)
            if damping_resp.success:
                rospy.loginfo(f"Successfully set damping of {joint_name} to {damping_value}")
            else:
                rospy.logerr(f"Failed to set damping of {joint_name} to {damping_value}: {damping_resp.message}")
        except rospy.ServiceException as e:
            rospy.logerr(f"Service call failed for damping: {e}")

        # Sleep briefly between service calls (adjust as needed)
        time.sleep(0.1)

if __name__ == '__main__':
    change_damping()
