#!/usr/bin/python

from std_msgs.msg import Float64
import rospy

def main():
    rospy.init_node('base_combined')
    pubList = []

    # Publishers for all four joints
    pubList.append(rospy.Publisher('/joint11_effort_controller/command', Float64, queue_size=36))
    pubList.append(rospy.Publisher('/joint21_effort_controller/command', Float64, queue_size=36))
    pubList.append(rospy.Publisher('/joint31_effort_controller/command', Float64, queue_size=36))
    pubList.append(rospy.Publisher('/joint41_effort_controller/command', Float64, queue_size=36))

    num_joints = len(pubList)

    # Torque values for each pair of joints
    torque_values = [-0.8, -0.8, 1.3, 1.3]  

    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        jointValList = []

        # Assign the torque values to respective joints
        for i in range(num_joints):
            jointValList.append(Float64(torque_values[i]))
            print(f"Setting torque {torque_values[i]} for joint {i+1}")

        # Publish torque values
        for j in range(num_joints):
            pubList[j].publish(jointValList[j])
            print('Publishing torque to joint', j+1)

        rate.sleep()  # Maintain loop frequency

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print("Program interrupted before completion")
