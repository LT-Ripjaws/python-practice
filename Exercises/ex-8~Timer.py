# A countdown timer program.
import os
import time
os.system('cls' if os.name == 'nt' else 'clear')


my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(1, my_time+1)):
    seconds = x % 60
    print(f"00:00:{seconds:02}")
    time.sleep(1)
print('TIMES UP!!!')