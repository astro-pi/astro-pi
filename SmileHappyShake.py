from sense_hat import SenseHat
import time

sense = SenseHat()
sense.low_light = True

o = (0,0,0)  # Λευκό Χρώμα
p = (229, 66, 224)  # Μωβ Χρώμα
y = (255, 255, 0) # Kitrino Xrwma

# Ο πίνακας με τα εικονοστοιχεία για τη Χαρούμενη Φατσούλα
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

# Ο πίνακας με τα εικονοστοιχεία για τη Λυπημένη Φατσούλα
sad = [
    o, o, o, o, o, o, o, o, 
    o, y, y, o, o, y, y, o, 
    o, y, y, o, o, y, y, o, 
    o, o, o, o, o, o, o, o, 
    o, o, o, o, o, o, o, o, 
    o, o, o, o, o, o, o, o, 
    o, o, y, y, y, y, o, o, 
    o, y, o, o, o, o, y, o, 
    ]

# Καθάρισμα της οθόνης
sense.clear()

# Rotate screen to match our sense hat position
sense.set_rotation(180)

# Εμφάνισε τη Χαρούμενη φάτσούλα
sense.set_pixels(smile)

#Επανάλαβε για πάντα
while True:
 x, y,  z = sense.get_accelerometer_raw().values()
  
 # Επανάλαβε όσο δεν υπάρχει τράνταγμα της συσκευής
 while x<2 and y<2 and z<2:
    x, y,  z = sense.get_accelerometer_raw().values()

 # Εμφάνισε τη Λυπημένη φάτσούλα
 sense.set_pixels(sad)
 # Περίμενε 2 δευτερόλεπτα
 time.sleep(2)
 # Επανέφερε τα γραφικά στη Χαρούμενη Φατσούλα
 sense.set_pixels(smile)
