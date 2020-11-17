cmake_minimum_required(VERSION 2.8.3)
project(reconfigure)

find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure
  roscpp
  rospy
)

generate_dynamic_reconfigure_options(
  cfg/position_reconfigure.cfg
  cfg/current_reconfigure.cfg
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
