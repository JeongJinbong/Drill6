import random
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
cx, cy = random.randint(0,1200), random.randint(0,1100)
hx, hy = cx, cy
frame = 0
moveto = [[cx, cy]]
Start = False
def handle_events():
    global running
    global hx, hy
    global Start
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                hx, hy = event.x, TUK_HEIGHT - 1 - event.y
                moveto.append([hx, hy])

def movetohand():
    global cx, cy
    global hx, hy
    global frame
    x1, y1 = cx, cy
    x2, y2 = moveto[0][0], moveto[0][1]
    for i in range(0, 100, 1):
        handle_events()
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        for j in range(0, len(moveto)):
            hand_arrow.draw(moveto[j][0], moveto[j][1])
        t = i/100
        movex = (1-t) * x1 + t * x2
        movey = (1-t) * y1 + t * y2
        if cx < moveto[0][0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, movex, movey)
        elif cx > moveto[0][0]:
            character.clip_draw(frame * 100, 0 * 1, 100, 100, movex, movey)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.016)
        if i == 100-1:
            cx, cy = moveto[0][0], moveto[0][1]
            moveto.pop(0)

while running:
    movetohand()
close_canvas()