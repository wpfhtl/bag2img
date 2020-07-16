Instructions
-----------------------------

copy the code to the src folder of a catkin workspace, and build

catkin_make

chmod +x bag2img/src/bag2img.py

Test an example with python:
-----------------------------

cd ~/catkin_ws/src/bag2img/src
python bag2img.py /home/tl/data/fisheye/2020-04-08-18-06-53 /home/tl/data/fisheye/2020-04-08-18-06-53.bag mono16 image_rect_raw 06d 0

Test an example with launch file:
-----------------------------

type in the value the parameter of the file export_images_from_bag.launch
e.g.:
<arg name="save_dir" default="/home/tl/data/fisheye/2020-04-08-18-06-53" /> <arg name="filename" default="/home/tl/data/fisheye/2020-04-08-18-06-53.bag"/>

and use the roslaunch command as follows

    roslaunch bag2img export_images_from_bag.launch

