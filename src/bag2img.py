#!/usr/bin/python

# Extract images from a bag file.
#
# Original author: Thomas Denewiler (http://answers.ros.org/users/304/thomas-d/)

# Start up ROS pieces.
PKG = 'bag2img'
import roslib; roslib.load_manifest(PKG)
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# Reading bag filename from command line or roslaunch parameter.
import os
import sys

class ImageCreator():

    image_type = ".png"
    index_in_filename = False
    img_format = "mono16"
    desired_topic = "image_rect_raw"
    index_format = "06d"
    view_image = 0
    image_index = 0

    # Must have __init__(self) function for a class, similar to a C++ class constructor.
    def __init__(self):
        # Get parameters when starting node from a launch file.
        if len(sys.argv) < 6:
            save_dir = rospy.get_param('save_dir')
            filename = rospy.get_param('filename')
            img_format = rospy.get_param('img_format')
            desired_topic = rospy.get_param('desired_topic')
            index_format = rospy.get_param('index_format')
            view_image = rospy.get_param('view_image')
            rospy.loginfo("save to %s, bag filename = %s, image format is %s, desired_topic is %s, index format is %s, view image flag is %d", save_dir, filename, img_format, desired_topic, index_format, view_image)
        # Get parameters as arguments to 'rosrun my_package bag_to_images.py <save_dir> <filename>', where save_dir and filename exist relative to this executable file.
        else:
            save_dir = sys.argv[1]  # os.path.join(sys.path[0], sys.argv[1])
            filename = sys.argv[2]  # os.path.join(sys.path[0], sys.argv[2])
            img_format = sys.argv[3]
            desired_topic = sys.argv[4]
            index_format = sys.argv[5]
            view_image = int(sys.argv[6])
            rospy.loginfo("save to %s, bag filename = %s, image format is %s, desired_topic is %s, index format is %s, view image flag is %d", save_dir, filename, img_format, desired_topic, index_format, view_image)

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        # Use a CvBridge to convert ROS images to OpenCV images so they can be saved.
        self.bridge = CvBridge()

        # Open bag file.
        with rosbag.Bag(filename, 'r') as bag:
            for topic, msg, t in bag.read_messages():
                topic_parts = topic.split('/')
                # rospy.loginfo("topic incudes %d parts", len(topic_parts))
                # for i in range(len(topic_parts)):
                #     rospy.loginfo("topic part %d: %s", i, topic_parts[i])
                # first part is empty string
                # rospy.loginfo("topic incudes %s", topic_parts[-1])
                if topic_parts[-1] == self.desired_topic:
                    try:
                        cv_image = self.bridge.imgmsg_to_cv2(msg, img_format)  # "bgr8")
                        if view_image == 1:
                            cv2.imshow("image", cv_image)
                            cv2.waitKey(1)
                    except CvBridgeError, e:
                        print e
                    timestr = "%.3f" % msg.header.stamp.to_sec()
                    if self.index_in_filename:
                        image_name = str(save_dir) + "/" + topic_parts[-2] + "-" + format(self.image_index, self.index_format) + "-" + timestr + self.image_type
                    else:
                        image_name = str(save_dir) + "/" + topic_parts[-2] + "-" + timestr + self.image_type
                    cv2.imwrite(image_name, cv_image)
                    # rospy.loginfo("save image to %s", image_name)
                    self.image_index = self.image_index + 1

# Main function.    
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node(PKG)
    # Go to class functions that do all the heavy lifting. Do error checking.
    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException: pass