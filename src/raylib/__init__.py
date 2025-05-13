import _rl_w_py as _rl

FUNCS = {
    "InitWindow",
    "WindowShouldClose",
    "BeginDrawing",
    "EndDrawing",
    "ClearBackground",
    "CloseWindow",
    "SetTargetFPS",
    "BeginMode2D",
    "EndMode2D",
    "IsKeyDown",
    "IsKeyPressed",
    "GetMouseWheelMove",
    "GetRandomValue",
    "DrawLine",
    "DrawRectangle",
    "DrawRectangleRec",
    "DrawRectangleLines"
    "DrawText"
    "Fade"
}

__all__ = [name for name in dir(_rl) if name in FUNCS]
