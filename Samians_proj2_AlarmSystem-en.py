# Samians Team from Greece
# Secondary mission: a Visual Alarm Detection System

# Takes Temperature, Humidity, Pressure and Gyroscope pitch-roll-yaw readings,
# then visualises Temperature/Humidity/Pressure with pixel bars that take
# red colours for abnormal values. It logs all readings to a timestamped file.

# Code Tested in Python 3.4.2

from sense_hat import SenseHat

# Imports library needed for the sleep time module
import time
# Library used to measure the cpu temperature
import os

# Instantiate object Sense Hat
sense = SenseHat()
# Low light levels for better camera viewing
sense.low_light = True

# This LED matrix rotation is due to AstroPi's vertical orientation aboard ISS
sense.set_rotation(270)

# Define our colours
white = (255,255,255)
blue = (0,0,255)
orange = (255,165,0)
green = (0,255,0)
red = (255,0,0) 
blank = (0,0,0)
yellow = (255,255,0)
red2 = (255,99,71)  # tomato
red3 = (128,0,0)  # maroon
indigo = (75,0,130)

# Our country's flag to be used as intro graphics
def greek_flag():
    W = white
    B = blue
    logo = [
    B, W, B, B, B, B, B, B,
    B, W, B, W, W, W, W, W,
    W, W, W, B, B, B, B, B, 
    B, W, B, W, W, W, W, W,
    B, B, B, B, B, B, B, B,
    W, W, W, W, W, W, W, W,
    B, B, B, B, B, B, B, B,
    W, W, W, W, W, W, W, W,
    ]
    return logo

def getCPUtemperature():
 res = os.popen('vcgencmd measure_temp').readline()
 return(res.replace("temp=","").replace("'C\n",""))

# Clear SenseHat LEDs
sense.clear()

# Output our Logo, the Greek Flag followed by our School's name
sense.set_pixels(greek_flag())
time.sleep(3)
sense.show_message("2o Gymnasio Samou", scroll_speed=0.07, text_colour=blue)

# Open a file for writing (creates file if not exists), to collect program's data
# In Excel Spreadsheet use Menu Data > Get External From Text , use comma delimiter
file = open("SamiansLogMission2.csv", "a")

# Add in the file, the columns labels (\n for new line)
file.write("Date, Time, Temperature, Humidity, Pressure, Gyro_x, Gyro_y, Gyro_z \n")
print("Data Log File to be used: SamiansLogMission2.csv for Date, Time, Temperature, Humidity, Gyro_x, Gyro_y, Gyro_z")

# Variable "seconds" measures the total execution time of this program
# It is used to stop the program after 1,5 hrs of running time, as suggested by the Contest Instructions
seconds = 0  # initialise

# The IMU (inertial measurement unit) sensor is a combination of three sensors, each with an x, y and z axis
# Since accelerometer not working in space free fall (zero readings) it will be disabled. Magnetometer disabled too. 
sense.set_imu_config(False, True, False)  # gyroscope only

# Forever loop
while True:

  # Take a Temperature reading
  # ISS maintains temperature to 18.3 - 26.7 Celsius
  # Reading temperature with Sense Hat is a problem due to a design issue. Measured temperatures are too high
  # due to thermal dissipation from the chip. Searching forums and after trying at home we ended to the following code
  # for more accurate temperature readings.
  temp = sense.get_temperature()

  cpuTemp=int(float(getCPUtemperature()))
  calctemp = temp - ((cpuTemp - temp)/1.8)
  temp = round(calctemp,1)
  
  # Normalise to 16 levels, assuming a max temperature of 30 Celcius
  temp_norm = (16 / 30) * temp

  # Visualize the temperature reading in LED matrix
  # Green colour for normal values, red colours for extreme values
  if temp <= 17.8:
    temp_colour = red
  elif temp > 17.8 and temp < 27.3:
    temp_colour = green
  else:
    temp_colour = red
  
  # Light up the appropriate number of LEDs. Temperature uses the first 2 rows (1-2) of the LED Matrix.
  pxl_temp = [temp_colour if i < temp_norm else blank for i in range(16)]
  
  # Take a Humidity reading
  # ISS maintains humidity around 60%
  hum = sense.get_humidity()
  hum = round(hum,1)

  # Normalise to 16 levels, assuming a max humidity of 70%
  hum_norm = (16 / 70) * hum
  
  # Visualize the humidity reading in LED matrix
  # Yellow colour for normal values, red2 colours for extreme values
  if hum <= 50:
    hum_colour = red2  # tomato
  elif hum > 50 and hum < 65:
    hum_colour = yellow
  else:
    hum_colour = red2
  
  # Light up the appropriate number of LEDs. Humidity uses the next 2 rows (3-4) of the LED Matrix.
  pxl_hum = [hum_colour if i < hum_norm else blank for i in range(16)]

  # air pressure inside the ISS is maintained at about 1013 millibars, which is nice and comfortable for the crew
  # ISS maintains pressure to 979 - 1027 millibars
  psi = sense.get_pressure() 
  psi = round(psi,1) 
  #print("psi ", psi)

  # Normalise to 16 levels, assuming a max pressure of 1030 millibars
  psi_norm = (16 / 1030) * psi
  
  # Visualize the pressure reading in LED matrix
  # White colour for normal values, red3 colours for extreme values
  if psi <= 978:
    psi_colour = red3  # maroon
  elif psi > 978 and psi < 1028:
    psi_colour = white
  else:
    psi_colour = red3
  
  # Light up the appropriate number of LEDs. Pressure uses the next 2 rows (5-6) of the LED Matrix.
  pxl_psi = [psi_colour if i < psi_norm else blank for i in range(16)]
  
  # Gyroscope readings. Gets the raw x, y and z axis gyroscope data
  # rotational intensity of the axis in radians per second
  raw = sense.get_gyroscope_raw()

  x = raw['x']
  y = raw['y']
  z = raw['z']

  # Use the absolute values since we only want the size of the values and do not care about the signs
  x = abs(x)
  y = abs(y)
  z = abs(z)

  # Check if an ISS thrusters re-boost acceleration is taking place or anything violent
  # If shake is detected then Light up the next 2 rows (7-8) of the LED matrix with a purple colour
  if x>1 or y>1 or z>1:
    pxl_gyro = [indigo for i in range(16)]
  else:
    pxl_gyro = [blank for i in range(16)]

  # Finally, Concatenate the pixels visualisations for all 4 sensors
  pixels = pxl_temp + pxl_hum + pxl_psi + pxl_gyro
  # Display all 4 sensor values at Sense Hat LED display
  sense.set_pixels(pixels)
  
  # Print timestamp together with all the sensor values
  print(time.strftime('%x %X'), "Temp", temp, "Hum", hum, "Psi", psi, "Gyro", "x: {x}, y: {y}, z: {z}".format(**raw))
  
  # Store data in the log file (Date, Time, Temperature, Humidity, Pressure, Gyroscope x,y,z)
  file.write(time.strftime('%x'))
  file.write(", ")
  file.write(time.strftime('%X'))
  file.write(", ")
  file.write(str(temp))
  file.write(", ")
  file.write(str(hum))
  file.write(", ")
  file.write(str(psi))
  file.write(", ")
  file.write(str(x))
  file.write(", ")
  file.write(str(y))
  file.write(", ")
  file.write(str(z))
  file.write("\n")

  # Time between measurements. Every 3 secs the whole process repeats
  time.sleep(3)
  
  # Update seconds variable
  seconds=seconds+1

  # According to the Contest instructions, this program is to be left running for 1,5 hrs
  # However because the log file is written to the SD card at the very last after the file.close() command and
  # to ensure small filesizes, the program will be left running for only about 40 minutes or 2400 secs.
  if seconds > 2400:
    # Clear SenseHat LEDs
    sense.clear()
    # Close the log file
    file.close()
    # Exit the forever loop
    break
