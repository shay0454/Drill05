import os
import random
from pico2d import*
os.chdir(os.path.dirname(os.path.abspath(__file__)))

TUK_WIDTH,TUK_HEIGHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
hand=load_image("hand_arrow.png")
ch=load_image("animation_sheet.png")
TUK_GOUND=load_image("TUK_GOUND.png")
def handle_events():
    events=get_events()
x,y
while(1):
    clear_canvas()
    TUK_GOUND.draw(TUK_WIDTH//2,TUK_HEIGHT//2)

    update_canvas()
close_canvas()