#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import json
import random

def gen_rnd_obstacles():
    res = []
    for i in range(random.randint(10,100)):
        for j in range(random.randint(10,100)):
            res.append([i,j])
    return res

def talker():
    pub = rospy.Publisher('plan2rviz_notifier', String, queue_size=10)
    rospy.init_node('player_gen', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    obstacles = gen_rnd_obstacles()
    test_players = { 'obstacles': obstacles }
    # one line list element composed of two lists: one for xs and one for ys
    # a line is drawn for each couple of subsequent points
    test_players['edges'] = [ [[20, 25, 30, 33],[20, 25, 30, 33]] ]
    pub.publish(json.dumps(test_players))
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
