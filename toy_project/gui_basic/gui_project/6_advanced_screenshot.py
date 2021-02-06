import time
import keyboard
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime('_%Y%m%d_%H%M%S')
    img = ImageGrab.grab()
    img.save('image{}.png'.format(curr_time))


keyboard.add_hotkey('F12', screenshot) # 사용자가 F12 누르면 스크린 샷 저장

keyboard.wait('esc') # 사용자가 esc 누를 때까지 프로그램 수행