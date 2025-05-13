from _rl_w_py import *
WIDTH, HEIGHT = 800, 450

InitWindow(WIDTH, HEIGHT, "raylib [core] example - basic window - PYTHON EDITION")
while not WindowShouldClose():
    BeginDrawing()

    ClearBackground(Color(255, 255, 255, 255))
    DrawText("Congrats! You created your first window with Python!", 130, 200, 20, Color(0, 0, 0, 255))

    EndDrawing()

CloseWindow()