import os
import random
from pico2d import*
os.chdir(os.path.dirname(os.path.abspath(__file__)))

TUK_WIDTH,TUK_HEIGHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
hand=load_image("hand_arrow.png")
ch=load_image("animation_sheet.png")
TUK_GROUND=load_image("TUK_GROUND.png")
x,y=TUK_WIDTH//2,TUK_HEIGHT//2
hand_x,hand_y=TUK_WIDTH//2,TUK_HEIGHT//2
running=True
frame=0
direction=0
def handle_events():
    global running
    events=get_events()
    for event in events:
        if event.type==SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
                running=False
            
def rand_hand():
    global hand_x,hand_y
    hand_x,hand_y=random.randint(0,TUK_WIDTH),random.randint(0,TUK_HEIGHT)
while(running):
    clear_canvas()
    TUK_GROUND.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    ch.clip_draw(frame*100,direction*100,100,100,x,y)
    hand.draw(hand_x,hand_y)
    if x==hand_x and y==hand_y:
        rand_hand()
        print(hand_x,hand_y)
    
    frame=(frame+1)%8
    handle_events()
    update_canvas()
close_canvas()