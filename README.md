## Installation

For installing our version of Arena-rosnav, start by running the following command in your terminal. This will make sure you're running on Ubuntu 20.04, install some dependencies, and also check if you have a previously installed version of Arena-rosnav. 

```curl https://raw.githubusercontent.com/andrewwawa/arena-rosnav/patch/install.sh | bash```

Once this has completed, create a new terminal and run the following command. This will create a catkin workspace for arena, install all ROS package dependencies from .repos, and start a build for your workspace.

```curl https://raw.githubusercontent.com/andrewwawa/arena-rosnav/patch/install2.sh | bash```

Finally, if you intend to benchmark against the learned planners Rosnav or AIO, you will need to run the following command. This will install dependencies for the poetry environment that these planners need to be run within.

```curl https://raw.githubusercontent.com/andrewwawa/arena-rosnav/patch/install3_training.sh | bash```
