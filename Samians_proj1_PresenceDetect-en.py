# Samians Team from Greece
# Primary mission: Detect crew presence in the Columbus

# Measures Humidity levels wih baseline. Visualises the readings and logs the data.

# Code Tested in Python 3.4.2

from sense_hat import SenseHat

# Imports library needed for the sleep time module
import time

# Instantiate object Sense Hat
sense = SenseHat()
# Low light levels for better camera viewing
sense.low_light = True

# This LED matrix rotation is due to AstroPi's vertical orientation aboard ISS
sense.set_rotation(180)

# Define our colours
white = (255,255,255)
blue = (0,0,255)
orange = (255,165,0)
green = (0,255,0)
red = (255,0,0)
blank = (0,0,0)
yellow = (255,255,0)

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

# Function used to calculate a baseline value for humidity readings
# Just stores 5 humidity readings to a list
def baseline_list():
  print("Calculating humidity baseline...")
  humid_list = []
  count = 0
  while count < 5:
    h = round(sense.get_humidity(),2)
    humid_list.append(h)
    count = count + 1
  print(humid_list) #the list with the 5 values used
  return(humid_list)

# Clear SenseHat LEDs
sense.clear()

# Output our Logo, the Greek Flag followed by our School's name
sense.set_pixels(greek_flag())
time.sleep(3)
sense.show_message("2o Gymnasio Samou", scroll_speed=0.07, text_colour=blue)

# Open a file for writing (creates file if not exists), to collect program's data
# In Excel Spreadsheet use Menu Data > Get External From Text , use comma delimiter
file = open("SamiansLogMission1.csv", "a")

# Add in the file, the columns labels (\n for new line)
file.write("Date, Time, Humidity, Diff, Percentage \n")
print("Data Log File to be used: SamiansLogMission1.csv for Date, Time, Humidity, Diff, Percentage")

# Scroll text message that indicates start of Humidity Readings
sense.show_message("Humidity..", scroll_speed=0.07, text_colour=green)

# Need to calculate Baseline for the very first time
# Empty the baseline list
humid_list = []
# Flag that sets to true in order to calculate new baseline
new_baseline = True

# Variable "seconds" measures the total execution time of this program
# It is used to force a new baseline calculation, after a fixed period of time
# It is also used to stop the program after 1,5 hrs of running time, as suggested by the Contest Instructions
seconds = 0  # initialise

# Forever loop
while True:

  # Calculate new baseline
  while new_baseline:
    humid_list = baseline_list()
    
    # Check that values are relatively constant to be used as baseline
    if (max(humid_list) - min(humid_list)) < 3:
      new_baseline = False  # Baseline OK, finished!
      
    # Calculate the average baseline humidity
    average_humidity = sum(humid_list) / len(humid_list)
    print("Average humidity ", average_humidity)
  
  # Start checking Humidity for astronaut presence
  humidity = sense.get_humidity()
  humidity = round(humidity,2)
    
  # Print timestamp together with the humidity value
  print(time.strftime('%x %X'), "Humid", humidity)
  
  # Store data in the log file (Date, Time, Humidity)
  file.write(time.strftime('%x'))
  file.write(", ")
  file.write(time.strftime('%X'))
  file.write(", ")
  file.write(str(humidity))
  file.write(", ")

  # Difference of Humidity from the average value of the baseline
  difference = round((abs(humidity - average_humidity)),0)
  file.write(str(difference))
  file.write(", ")

  # Percentage increase in humidity
  increase_percent = round(((100 / average_humidity) * difference),0)
  file.write(str(increase_percent))
  file.write("\n")
  
  # Visualize the humidity reading in LED matrix
  # Green colour for normal values, orange/red colours for extreme values
  if humidity <= 30:
    hum_colour = orange
  elif humidity > 30 and humidity < 60:
    hum_colour = green
  else:
    hum_colour = red

  # Normalise to 64 levels
  humidity = (64 / 100) * humidity

  sense.clear()
  # Light up the appropriate number of LEDs
  pixels = [hum_colour if i < humidity else blank for i in range(64)]
  sense.set_pixels(pixels)
  
  # An Astronaut is said to be detected, if a 4% humidity raise is measured
  if increase_percent > 4:
    file.write('Astronaut present \n')
    sense.show_message("HI", scroll_speed=0.07, text_colour=yellow)
    # Set the flag to force baseline recalculation
    new_baseline = True  
  
  # Every now and then baseline should recalculate
  # This is set every 2 minutes (ie 120 seconds), checked with a modulo operation
  if (seconds % 120 == 0):
    # Set the flag to force baseline recalculation
    new_baseline = True  
  
  # Time between measurements. Every 1 sec the whole process repeats
  time.sleep(1)
  # Update seconds variable
  seconds=seconds+1

  # According to the Contest instructions, this program is to be left running for 1,5 hrs.
  # However because the log file is written to the SD card at the very last after the file.close() command and
  # to ensure small filesizes, the program will be left running for only about 40 minutes or 2400 secs.
  if seconds > 2400:
    # Clear SenseHat LEDs
    sense.clear()
    # Close the log file
    file.close()
    # Exit the forever loop
    break
