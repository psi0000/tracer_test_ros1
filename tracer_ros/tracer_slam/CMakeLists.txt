cmake_minimum_required(VERSION 3.0.2)
project(tracer_slam)


## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  sensor_msgs
)
catkin_package(
  CATKIN_DEPENDS roscpp sensor_msgs  
)
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

install(DIRECTORY bag config launch rviz
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)