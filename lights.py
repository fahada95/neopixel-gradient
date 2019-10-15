import board
import neopixel
from time import sleep
import collections

def display(red, green, blue):
    print("Initializing lights")
    pixels = neopixel.NeoPixel(board.D18, 3)
    pixels.fill((0, 0, 0))
    pixels[0] = (255, 0, 0)
    pixels[1] = (0, 255, 0)
    pixels[2] = (0, 0, 255)
    sleep(2)
    deq = collections.deque(pixels)
    while True:
        sleep(.05)
        deq.rotate()
        print(str(deq))
        for x in range(len(pixels)):
            pixels[x] = deq[x]
    sleep(5)
    pixels.deinit()
    
def main():
    # time interval to travel across gradient
    interval = 72
    interval_one = 1/interval

    # Starting values for stage one
    # rgb(70, 0, 120)
    red_starting = 70
    green_starting = 0
    blue_starting = 120

    # Ideally we shouldn't have to set these since these are the intermediary values,
    #  but it helps keeps the colors going in the direction we want them to go
    # rgb(178, 31, 31)
    red_intermediate = 178
    green_intermediate = 31
    blue_intermediate = 31

    # Final values for where the gradient should be. By the end of it we proabably
    #  want to cycle back around to the beginning values.
    # rgb(200, 60, 5)
    red_final = 200
    green_final = 60
    blue_final = 5

    # The distance needed to go from one rgb value to another
    red_delta = red_intermediate - red_starting
    green_delta = green_intermediate - green_starting
    blue_delta = blue_intermediate - blue_starting

    # These factors just get us from one end of the gradient to the other
    #  in the given amount of time
    red_level_one_factor = red_delta*interval_one
    green_level_one_factor = green_delta*interval_one
    blue_level_one_factor = blue_delta*interval_one

    print("Initializing lights")
    pixels = neopixel.NeoPixel(board.D18, 144)

    red = red_starting
    green = green_starting
    blue = blue_starting
    print(int(red))
    print(int(green))
    print(int(blue))
    for x in range(interval):
        red += red_level_one_factor
        green += green_level_one_factor
        blue += blue_level_one_factor
        pixels[x] = ((int(red), int(green), int(blue)))

    red_delta = red_final - red_intermediate
    green_delta = green_final - green_intermediate
    blue_delta = blue_final - blue_intermediate

    red_level_one_factor = red_delta*interval_one
    green_level_one_factor = green_delta*interval_one
    blue_level_one_factor = blue_delta*interval_one

    red = red_intermediate
    green = green_intermediate
    blue = blue_intermediate
    print('red: ' + str(int(red)))
    print('green: ' + str(int(green)))
    print('blue: ' + str(int(blue)))
    #~ sleep(10)
    for x in range(interval):
        print('interval + x = ' + str(interval+x))
        if int(red) != red_final:
            red += red_level_one_factor
            pixels[interval + x] = ((int(red), int(green), int(blue)))
        if int(green) != green_final:
            green += green_level_one_factor
            pixels[interval + x] = ((int(red), int(green), int(blue)))
        if int(blue) != blue_final:
            blue += blue_level_one_factor
            pixels[interval + x] = ((int(red), int(green), int(blue)))
        
        print('red: ' + str(int(red)))
        print('green: ' + str(int(green)))
        print('blue: ' + str(int(blue)))
        if (int(red) == red_final and int(green) == green_final and int(blue) == blue_final):
            print('set!')
            break
        else:
            continue
    deq = collections.deque(pixels)
    while True:
        print('rotating deque')        
        deq.rotate()
        for x in range(len(pixels)-1):
            pixels[x] = deq[x]
        
if __name__ == '__main__':
    #~ display(0, 0, 0)
    main()
