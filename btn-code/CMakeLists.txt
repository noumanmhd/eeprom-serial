cmake_minimum_required(VERSION 3.20)
project(btn_code)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(btn_code
        btn-code.ino)
