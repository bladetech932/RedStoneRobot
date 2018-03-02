# Required dependencies
sudo apt install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev -Y
# Dependencies for Python bindings
# If you use a non-system copy of Python (eg. with pyenv or virtualenv), then you probably don't need to do this part
sudo apt install python3.5-dev libpython3-dev python3-numpy -Y
# Optional, but installing these will ensure you have the latest versions compiled with OpenCV
sudo apt install libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev -Y

# Clone OpenCV somewhere
# I'll put it into $HOME/code/opencv
OPENCV_DIR="$HOME/RedStoneRobot/TestPrograms/vision"
OPENCV_VER="3.1.0"
git clone https://github.com/opencv/opencv "$OPENCV_DIR"
# This'll take a while...

# Now lets checkout the specific version we want
cd "$OPENCV_DIR"
git checkout "$OPENCV_VER"

# First OpenCV will generate the files needed to do the actual build.
# We'll put them in an output directory, in this case "release"
mkdir release
cd release

# Note: This is where you'd add build options, like TBB support or custom Python versions. See above sections.
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local "$OPENCV_DIR"

# At this point, take a look at the console output.
# OpenCV will print a report of modules and features that it can and can't support based on your system and installed libraries.
# The key here is to make sure it's not missing anything you'll need!
# If something's missing, then you'll need to install those dependencies and rerun the cmake command.

# OK, lets actually build this thing!
# Note: You can use the "make -jN" command, which will run N parallel jobs to speed up your build. Set N to whatever your machine can handle (usually <= the number of concurrent threads your CPU can run).
make
# This will also take a while...

# Now install the binaries!
sudo make install
