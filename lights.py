import board
import neopixel
import collections


def draw_colors(interval_start, interval_end, beginning_color,
                ending_color, pixels):
    interval = interval_end - interval_start
    interval_one = 1/interval
    # The distance needed to go from one rgb value to another
    red_delta = ending_color[0] - beginning_color[0]
    green_delta = ending_color[1] - beginning_color[1]
    blue_delta = ending_color[2] - beginning_color[2]

    # These factors just get us from one end of the gradient to the other
    #  in the given amount of time
    red_level_one_factor = red_delta*interval_one
    green_level_one_factor = green_delta*interval_one
    blue_level_one_factor = blue_delta*interval_one

    red = beginning_color[0]
    green = beginning_color[1]
    blue = beginning_color[2]

    for x in range(interval):
        if int(red) != ending_color[0]:
            red += red_level_one_factor
            pixels[x + interval_start] = ((int(red), int(green), int(blue)))
        if int(green) != ending_color[1]:
            green += green_level_one_factor
            pixels[x + interval_start] = ((int(red), int(green), int(blue)))
        if int(blue) != ending_color[2]:
            blue += blue_level_one_factor
            pixels[x + interval_start] = ((int(red), int(green), int(blue)))
        if (int(red) == ending_color[0] and int(green) == ending_color[1]
                and int(blue) == ending_color[2]):
            break
        else:
            continue


def main():
    # rgb(70, 0, 120) - starting
    # rgb(178, 31, 31) - intermediate
    # rgb(200, 60, 5) - final
    starting = (70, 0, 120)
    intermediate = (178, 31, 31)
    final = (200, 60, 5)
    pixels = neopixel.NeoPixel(board.D18, 144)
    print("Initialized lights")

    draw_colors(0, 36, starting, intermediate, pixels)
    draw_colors(36, 72, intermediate, final, pixels)
    draw_colors(72, 108, final, intermediate, pixels)
    draw_colors(108, 144, intermediate, starting, pixels)
    deq = collections.deque(pixels)
    while True:
        print('rotating deque')
        deq.rotate()
        for x in range(len(pixels)-1):
            pixels[x] = deq[x]


if __name__ == '__main__':
    main()
