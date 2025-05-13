# this test should add two numbers USING REAL MACHINE CODE
# compiled from C++ of course. Im not writing Assembly today.

from _rl_w_py import add_from_cpp
print(add_from_cpp(1, 2)) # should print THREE - 3 (neither two nor four. five is right out)