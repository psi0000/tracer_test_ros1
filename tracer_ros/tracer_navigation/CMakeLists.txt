cmake_minimum_required(VERSION 3.0.2)
project(tracer_navigation)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED)


catkin_package()



install(DIRECTORY launch rviz maps param
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
