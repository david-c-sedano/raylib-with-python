#include <pybind11/pybind11.h>
#include <raylib.h>
namespace py = pybind11;

int add (int foo, int pippo) 
{
    return foo + pippo;
}

PYBIND11_MODULE(_rl_w_py, m) {
    m.doc() = "Make programming fun again!!";
    m.def("add_from_cpp", &add, "A test. This should add two numbers from REAL MACHINE CODE!!");
}
