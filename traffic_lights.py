from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

g = (0, 255, 0) # Πράσινο
r = (255, 0, 0) # Red colour
o = (255,165, 0) # Orange colour

n = (0, 0, 0) # Μαύρο - σβηστά pixels

s.set_rotation(180)

green_sign = [
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, g, g, g, g, n, n,
  n, n, g, g, g, g, n, n,
  ]

orange_sign = [


  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, o, o, o, o, n, n,
  n, n, o, o, o, o, n, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  ]

red_sign = [
  n, n, r, r, r, r, n, n,
  n, n, r, r, r, r, n, n,
  n, n, n, n, n,


  n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  n, n, n, n, n, n, n, n,
  ]

s.clear()

#s.stick.wait_for_event()

while True:

    for event in s.stick.get_events():

        # Events when key is pressed (Enter)
        if event.direction == "middle":
            s.set_pixels(green_sign)
            time.sleep(2)
            s.set_pixels(orange_sign)
            time.sleep(2)
            s.set_pixels(red_sign)
            time.sleep(2)
            s.clear()

        # Events when LEFT key is pressed
        if event.direction == "left":
            s.set_pixels(red_sign)
            time.sleep(2)
            
            s.clear()

       # Events when RIGHT key is pressed
        if event.direction == "right":
            s.set_pixels(green_sign)
            time.sleep(2)
            s.clear()

       # Events when UP or DOWN key is pressed
        if (event.direction == "up") | (event.direction == "down"):
            s.set_pixels(orange_sign)
            time.sleep(2)
            s.clear()

            


#s.set_pixels(green_sign)
#time.sleep(2)
#s.set_pixels(orange_sign)
#time.sleep(2)
#s.set_pixels(red_sign)
