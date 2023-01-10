cmake_minimum_required(VERSION 3.5)
project(social_network_microservices)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O0 -Wall --coverage")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} --coverage")
set(CMAKE_CXX_OUTPUT_EXTENSION_REPLACE ON)
set(CMAKE_INSTALL_PREFIX /usr/local/bin)

add_subdirectory(src)
#add_subdirectory(test)
#enable_testing()


