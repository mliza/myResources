cmake_minimum_required(VERSION 3.24)

set (CMAKE_CXX_STANDARD 11)
set (CMAKE_CXX_STANDARD_REQUIRED ON)
set (CMAKE_CXX_EXTENSIONS OFF)

project(hello)

set(SOURCE_FILES
    main.cpp
    hello.cpp)

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
