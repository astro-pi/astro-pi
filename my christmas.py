from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

r = [255, 0, 0]
w = [255, 255, 255]
e = [0, 0, 0]  # e stands for empty/black

image = [
e,e,e,e,e,e,w,w,
e,e,e,e,r,r,w,w,
e,e,e,r,r,e,e,e,
e,r,r,r,r,r,e,e,
e,r,r,r,r,r,e,e,
r,r,r,r,r,r,r,e,
r,r,r,r,r,r,r,e,
w,w,w,w,w,w,w,e]

sense.set_pixels(image)
sleep(2)
sense.flip_h()
sleep(2)

sense.show_message("Kalh Xronia 2017 !!!", scroll_speed=0.07, text_colour=[0,0,255], back_colour=[0,0,0])

sense.show_letter("O",text_colour=[255, 255, 0])
sleep(1)
sense.show_letter("M",text_colour=[255, 0, 255])
sleep(1)
sense.show_letter("G",text_colour=[0, 255, 0])
sleep(1)
sense.show_letter("!",text_colour=[0, 0, 0], back_colour=[255, 255, 0])
sleep(1)
sense.clear()
sense.set_rotation(90)
sense.set_pixel(0, 3, [0, 255, 0])
sense.set_pixel(1, 2, [0, 255, 0])
sense.set_pixel(1, 3, [0, 255, 0])
sense.set_pixel(1, 4, [0, 255, 0])
sense.set_pixel(2, 3, [0, 255, 0])
sense.set_pixel(3, 2, [0, 255, 0])
sense.set_pixel(3, 3, [0, 255, 0])
sense.set_pixel(3, 4, [0, 255, 0])
sense.set_pixel(4, 1, [0, 255, 0])
sense.set_pixel(4, 2, [0, 255, 0])
sense.set_pixel(4, 3, [0, 255, 0])
sense.set_pixel(4, 4, [0, 255, 0])
sense.set_pixel(4, 5, [0, 255, 0])
sense.set_pixel(5, 2, [0, 255, 0])
sense.set_pixel(5, 3, [0, 255, 0])
sense.set_pixel(5, 4, [0, 255, 0])
sense.set_pixel(6, 1, [0, 255, 0])
sense.set_pixel(6, 2, [0, 255, 0])
sense.set_pixel(6, 3, [0, 255, 0])
sense.set_pixel(6, 4, [0, 255, 0])
sense.set_pixel(6, 5, [0, 255, 0])
sense.set_pixel(7, 0, [0, 255, 0])
sense.set_pixel(7, 1, [0, 255, 0])
sense.set_pixel(7, 2, [0, 255, 0])
sense.set_pixel(7, 3, [0, 255, 0])
sense.set_pixel(7, 4, [0, 255, 0])
sense.set_pixel(7, 5, [0, 255, 0])
sense.set_pixel(7, 6, [0, 255, 0])
sleep(6)
sense.clear()


