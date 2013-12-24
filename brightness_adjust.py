#!/usr/bin/env python
import sys
MAX_BRIGHTNESS=2800
BRIGHTNESS_FILE='/sys/class/backlight/pwm-backlight.0/brightness'
BRIGHTNESS_INTERVAL = 200

def valid_usage():
    if len(sys.argv) == 2 and (sys.argv[1] == "up" or sys.argv[1] == "down"):
        return True

def print_usage():
    print "Usage: "+sys.argv[0]+" [up|down]"

def get_current_brightness():
    with open(BRIGHTNESS_FILE, 'r') as f:
        return int(f.read().strip())

def set_current_brightness(brightness):
    if brightness > MAX_BRIGHTNESS or brightness < 0:
        return false
    with open(BRIGHTNESS_FILE, 'w') as f:
        f.write(str(brightness))

if __name__ == "__main__":
    if not valid_usage():
        print_usage()
        exit()
    current_brightness = get_current_brightness()
    if sys.argv[1] == "up":
        set_current_brightness(current_brightness + BRIGHTNESS_INTERVAL)
    elif sys.argv[1] == "down":
        set_current_brightness(current_brightness - BRIGHTNESS_INTERVAL)
