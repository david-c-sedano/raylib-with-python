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

    /* STRUCTS */
	py::class_<Color>(m, "Color")
		.def(py::init([](unsigned char r, unsigned char g, unsigned char b, unsigned char a) {
			return Color{r, g, b, a};
		}))
		.def_readwrite("r", &Color::r)
		.def_readwrite("g", &Color::g)
		.def_readwrite("b", &Color::b)
		.def_readwrite("a", &Color::a);

    /* RCORE FUNCTIONS */
    m.def("InitWindow", &InitWindow, "InitWindow");
    m.def("WindowShouldClose", &WindowShouldClose, "WindowShouldClose");
    m.def("BeginDrawing", &BeginDrawing, "BeginDrawing");
    m.def("EndDrawing", &EndDrawing, "EndDrawing");
    m.def("ClearBackground", &ClearBackground, "ClearBackground");
    m.def("CloseWindow", &CloseWindow, "CloseWindow");

    /* RTEXT FUNCTIONS */
    m.def("DrawText", &DrawText, "DrawText");
}
