#!/usr/bin/python

from std_msgs.msg import Float64
import rospy


def main():

    rospy.init_node('limb')
    pubList = []
    pubList.append(rospy.Publisher('/joint02_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint03_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint04_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint05_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint06_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint07_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint08_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint09_effort_controller/command', Float64, queue_size=9))
    pubList.append(rospy.Publisher('/joint10_effort_controller/command', Float64, queue_size=9))

    rate = rospy.Rate(50)  

    
    slope = 3.58#3.3
    max_torque = 0.391 #0.33
    num_joints = len(pubList)

    start_time = rospy.get_time()

    # while not rospy.is_shutdown():
        
    #     current_time = (rospy.get_time() - start_time) % 1.0
    #     jointValList = []

    #     if 0.0 <= current_time < 0.1:
            
    #         torque_value = slope * current_time
    #     elif 0.1 <= current_time < 0.4:
            
    #         torque_value = max_torque
    #     elif 0.4 <= current_time < 0.6:
            
    #         torque_value = -slope * (current_time - 0.4)
    #     elif 0.6 <= current_time < 0.9:
            
    #         torque_value = -max_torque
    #     elif 0.9 <= current_time < 1.0:
            
    #         torque_value = slope * (current_time - 0.9)

    while not rospy.is_shutdown():

        tpc = 0.833   #time per cycle
        
        current_time = (rospy.get_time() - start_time) % tpc
        jointValList = []

        if 0.0 <= current_time < tpc*0.1:
            
            torque_value = slope * current_time
        elif tpc*0.1 <= current_time < tpc*0.4:
            
            torque_value = max_torque
        elif tpc*0.4 <= current_time < tpc*0.6:
            
            torque_value = -slope * (current_time - tpc*0.4)
        elif tpc*0.6 <= current_time < tpc*0.9:
            
            torque_value = -max_torque
        elif tpc*0.9 <= current_time < tpc:
            
            torque_value = slope * (current_time - tpc*0.9)

        for i in range(num_joints):
            pubList[i].publish(Float64(torque_value))
            print(f"Publishing torque for joint {i + 2}: {torque_value:.3f}")

        # Print the current torque value and time for debugging
        print(f"Time: {current_time:.2f}s, Torque: {torque_value:.3f}")

        rate.sleep()  # Sleep for the defined rate (10 Hz)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print("Program interrupted before completion")
