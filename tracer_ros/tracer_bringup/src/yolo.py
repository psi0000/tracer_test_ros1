import rospy
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist

cen_x=0
cen_y=0

def callback(data):
    # rospy.loginfo("centerpoint is %d %d ",data.x,data.y)
    global cen_x
    cen_x=data.x
    # print(cen_x)

def listener():
    rospy.init_node('qr_receive',anonymous = True)
    rospy.Subscriber("qr",Point,callback)
    cmd_pub = rospy.Publisher('cmd_vel',Twist,queue_size=10)
    rate =rospy.Rate(10)
    msg=Twist()
    while not rospy.is_shutdown():
        if cen_x>310:    #차가 오른쪽으로 더 가있음  -> 왼쪽으로 회전
            ang = 0.1
        elif cen_x<290 & cen_x>0:
            ang = -0.1
        else:
            ang = 0
        msg.angular.z = ang
        print(msg)
        cmd_pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    
    listener()