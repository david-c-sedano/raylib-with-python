cmake_minimum_required(VERSION 3.15)
project(raylib_with_python LANGUAGES CXX)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

#  -fPIC flag REQUIRED on LOONIX
if(NOT MSVC)
    set(CMAKE_POSITION_INDEPENDENT_CODE ON)
endif()

add_subdirectory(vendor/raylib)

pybind11_add_module(_rl_w_py 
    src/rl_w_py.cpp
)

target_link_libraries(_rl_w_py PRIVATE raylib)

install(TARGETS _rl_w_py DESTINATION .)
