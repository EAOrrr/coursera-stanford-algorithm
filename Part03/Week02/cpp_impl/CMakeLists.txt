cmake_minimum_required(VERSION 3.22)
project(cluster)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++23 -Wall -Werror -pedantic")

include_directories(include/)

add_executable(main
    src/main.cpp
    src/cluster.cpp
)