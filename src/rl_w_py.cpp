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
	py::class_<Vector2>(m, "Vector2")
		.def(py::init([](float x, float y) {
			return Vector2{x, y};
		}))
		.def_readwrite("x", &Vector2::x)
		.def_readwrite("y", &Vector2::y);

	py::class_<Rectangle>(m, "Rectangle")
		.def(py::init([](float x, float y, float width, float height) {
			return Rectangle{x, y, width, height};
		}))
		.def_readwrite("x", &Rectangle::x)
		.def_readwrite("y", &Rectangle::y)
		.def_readwrite("width", &Rectangle::width)
		.def_readwrite("height", &Rectangle::height);

	py::class_<Color>(m, "Color")
		.def(py::init([](unsigned char r, unsigned char g, unsigned char b, unsigned char a) {
			return Color{r, g, b, a};
		}))
		.def_readwrite("r", &Color::r)
		.def_readwrite("g", &Color::g)
		.def_readwrite("b", &Color::b)
		.def_readwrite("a", &Color::a);

	py::class_<Camera2D>(m, "Camera2D")
		.def(py::init([](Vector2 offset, Vector2 target, float rotation, float zoom) {
			return Camera2D{offset, target, rotation, zoom};
		}))
		.def_readwrite("offset", &Camera2D::offset)
		.def_readwrite("target", &Camera2D::target)
		.def_readwrite("rotation", &Camera2D::rotation)
		.def_readwrite("zoom", &Camera2D::zoom);

    /* RCORE FUNCTIONS */
    // Windowing Related Functions
    m.def("InitWindow", &InitWindow);
    m.def("WindowShouldClose", &WindowShouldClose);
    m.def("CloseWindow", &CloseWindow);
    // Timing Related Functions
    m.def("SetTargetFPS", &SetTargetFPS);
    // Drawing Related Functions
    m.def("BeginDrawing", &BeginDrawing);
    m.def("EndDrawing", &EndDrawing);
    m.def("ClearBackground", &ClearBackground);
    m.def("BeginMode2D", &BeginMode2D);
    m.def("EndMode2D", &EndMode2D);
    // Input Related Functions
    m.def("IsKeyDown", &IsKeyDown);
    m.def("IsKeyPressed", &IsKeyPressed);
    // Input Related Functions (MOUSE)
    m.def("GetMouseWheelMove", &GetMouseWheelMove);
    // Random Value Related Functions
    m.def("GetRandomValue", &GetRandomValue);

    /* RSHAPES FUNCTIONS */
    // Basic Shapes Drawing Functions
    m.def("DrawLine", &DrawLine);
    m.def("DrawRectangle", &DrawRectangle);
    m.def("DrawRectangleRec", &DrawRectangleRec);
    m.def("DrawRectangleLines", &DrawRectangleLines);

    /* RTEXTURES FUNCTIONS */
    m.def("Fade", &Fade);

    /* RTEXT FUNCTIONS */
    m.def("DrawText", &DrawText);
}
