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
x0,y0=x,y
hand_x,hand_y=TUK_WIDTH//2,TUK_HEIGHT//2
running=True
frame,move_count,t=0,10,0
direction=0
def handle_events():
    global running
    events=get_events()
    for event in events:
        if event.type==SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
                running=False
            
def rand_hand():
    global hand_x,hand_y,direction,x,y,x0,y0
    x0,y0=hand_x,hand_y
    hand_x,hand_y=random.randint(0,TUK_WIDTH),random.randint(0,TUK_HEIGHT)
    direction=int(hand_x>x)
while(running):
    clear_canvas()
    TUK_GROUND.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    ch.clip_draw(frame*100,direction*100,100,100,x,y)
    hand.draw(hand_x,hand_y)
    if x==hand_x and y==hand_y:
        rand_hand()
    else:
        per=1/move_count
        x,y=(1-per*t)*x0+per*t*hand_x,(1-per*t)*y0+per*t*hand_y
        t=(t+1)%(move_count+1)
        frame=(frame+1)%8
    print(x,y)
    handle_events()
    update_canvas()
    delay(0.03)
close_canvas()