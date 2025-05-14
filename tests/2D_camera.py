from raylib import *
import math

MAX_BUILDINGS = 100
WIDTH, HEIGHT = 800, 450

player = Rectangle(400, 280, 40, 40)
buildings = [Rectangle(0, 0, 0, 0)] * MAX_BUILDINGS
buildColors = [Color(0, 0, 0, 0)] * MAX_BUILDINGS

spacing = 0

for i in range(MAX_BUILDINGS):
    x = -6000.0 + spacing
    width = GetRandomValue(50, 200)
    height = GetRandomValue(100, 800)
    y = HEIGHT - 130.0 - height

    buildings[i] = Rectangle(x, y, width, height)
    spacing += int(buildings[i].width)

    buildColors[i] = Color(
        GetRandomValue(200, 240),
        GetRandomValue(200, 240),
        GetRandomValue(200, 240),
        255
    )

camera = Camera2D(
    Vector2(player.x + 20.0, player.y + 20.0),
    Vector2( WIDTH/2.0, HEIGHT/2.0),
    0.0, 1.0
)

InitWindow(WIDTH, HEIGHT, "raylib [core] example - 2d camera - PYTHON EDITION")
SetTargetFPS(60)

while not WindowShouldClose():
    if IsKeyDown(KEY_RIGHT): 
        player.x += 2
    elif IsKeyDown(KEY_LEFT):
        player.x -= 2

    camera.target = Vector2(player.x + 20, player.y + 20)

    if IsKeyDown(KEY_A):
        camera.rotation -= 1
    elif IsKeyDown(KEY_S): 
        camera.rotation += 1

    if camera.rotation > 40: 
        camera.rotation = 40
    elif camera.rotation < -40: 
        camera.rotation = -40

    camera.zoom = math.exp(math.log(camera.zoom) + GetMouseWheelMove() * 0.1)

    if camera.zoom > 3.0: 
        camera.zoom = 3.0
    elif camera.zoom < 0.1:
        camera.zoom = 0.1

    if IsKeyPressed(KEY_R):
        camera.zoom = 1.0
        camera.rotation = 0.0

    BeginDrawing()
    ClearBackground(RAYWHITE)

    BeginMode2D(camera)

    DrawRectangle(-6000, 320, 13000, 8000, DARKGRAY)
    for building, buildColor in zip(buildings, buildColors):
        DrawRectangleRec(building, buildColor)

    DrawRectangleRec(player, RED)

    # I kid you not, if you don't cast the floats - camera.target.x or camera.target.y - IT WILL SEGFAULT!!!
    DrawLine(int(camera.target.x), -HEIGHT * 10, int(camera.target.x), HEIGHT * 10, GREEN)
    DrawLine(-WIDTH * 10, int(camera.target.y), WIDTH * 10, int(camera.target.y), GREEN)

    EndMode2D()

    DrawText("SCREEN AREA", 640, 10, 20, RED)

    DrawRectangle(0, 0, WIDTH, 5, RED)
    DrawRectangle(0, 5, 5, HEIGHT - 10, RED)
    DrawRectangle(WIDTH - 5, 5, 5, HEIGHT - 10, RED)
    DrawRectangle(0, HEIGHT - 5, WIDTH, 5, RED)

    DrawRectangle(10, 10, 250, 113, Fade(SKYBLUE, 0.5))
    DrawRectangleLines( 10, 10, 250, 113, BLUE)

    DrawText("Free 2d camera controls:", 20, 20, 10, BLACK)
    DrawText("- Right/Left to move Offset", 40, 40, 10, DARKGRAY)
    DrawText("- Mouse Wheel to Zoom in-out", 40, 60, 10, DARKGRAY)
    DrawText("- A / S to Rotate", 40, 80, 10, DARKGRAY)
    DrawText("- R to reset Zoom and Rotation", 40, 100, 10, DARKGRAY)

    EndDrawing()

CloseWindow()

print(dir(rl))