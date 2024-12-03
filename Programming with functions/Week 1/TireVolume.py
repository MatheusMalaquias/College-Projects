#I added a delay to appear the results
import math
import time
from datetime import datetime
print('---------------------------------')
def main():
    width = int(input('Enter the width of the tire in mm: '))
    aspect = int(input('Enter the aspect ratio of the tire: '))
    diameter = int(input('Enter the diameter of the wheel in inches: '))
    volume = compute_volume(width, aspect, diameter)
    return volume

def compute_volume(width, aspect, diameter):
   volume = math.pi * width ** 2 * aspect * (width * aspect + 2540 * diameter) / 10000000000
   time.sleep(2)
   print(f'The approximate volume is {volume:.2f} liters')
   time.sleep(2)
   print('---------------------------------')
   current_date_and_time = datetime.now()
   print(f'{current_date_and_time:%Y/%m/%d, {width}, {aspect}, {diameter}, {volume:.2f}}')
main()