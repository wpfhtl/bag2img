Instructions
-----------------------------

copy the code to the src folder of a catkin workspace, and build, for example:

    cd ~/catkin_ws/src

    git clone https://github.com/wpfhtl/bag2img.git

    cd ..

catkin_make

chmod +x src/bag2img/src/bag2img.py

Test an example with python:
-----------------------------
open a terminal, type as follows:

    roscore

open another terminal, type as follows:

    cd ~/catkin_ws/src/bag2img/src

    python bag2img.py ~/data/fisheye/2020-04-08-18-06-53 ~/data/fisheye/2020-04-08-18-06-53.bag mono16 image_rect_raw 06d 0 2

the parameters of the python command above are: (1) folder to save exported image; (2) path of the bag file; (3) image format; (4) topic name of image; (5) index format of saved image; (6) whether to view the image; (7) skip number of images while save, must be a multiple of 2;

Test an example with launch file:
-----------------------------

type in the value the parameter of the file export_images_from_bag.launch
e.g.:
<arg name="save_dir" default="/home/tl/data/fisheye/2020-04-08-18-06-53" /> <arg name="filename" default="/home/tl/data/fisheye/2020-04-08-18-06-53.bag"/>

and use the roslaunch command as follows

    roslaunch bag2img export_images_from_bag.launch

