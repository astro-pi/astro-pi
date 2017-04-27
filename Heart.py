
from sense_hat import SenseHat

import time

s = SenseHat()

# RGB model
# Red, Green, Blue

n = (0, 0, 0)
p = (241,111,176)

heart = [
    n,n,n,n,n,n,n,n,
    n,p,p,n,n,p,p,n,
    p,p,p,p,p,p,p,p,
    p,p,p,p,p,p,p,p,
    n,p,p,p,p,p,p,n,
    n,n,p,p,p,p,n,n,
    n,n,n,p,p,n,n,n,
    n,n,n,n,n,n,n,n,
    ]

s.set_pixels(heart)
time.sleep(6)

s.show_message("I LOVE SAMOS")





























