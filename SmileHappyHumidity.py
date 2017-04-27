from sense_hat import SenseHat
import time

sense = SenseHat()

# RGB colour model

b = (0,0,255)
o = (0,0,0)
p = (229, 66, 224)
r = (255, 0 , 0 )

smile = [
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, p, o, o, p, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, p, o, o, o, o, p, o,
    o, o, p, p, p, p, o, o,
    o, o, o, o, o, o, o, o,
    ]

sad = [
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, r, o, o, r, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, r, r, r, r, o, o,
    o, r, o, o, o, o, r, o
    ]

sense.set_rotation(180)
sense.low_light = True
sense.clear()
sense.set_pixels(smile)

while True:

  sense.set_pixels(smile)

  humidity = sense.humidity
  
  print(humidity)


  while humidity<48:
    humidity = round(sense.get_humidity(),1)
    print(humidity)
    time.sleep(0.5)

  sense.set_pixels(sad)
  time.sleep(6)
  


