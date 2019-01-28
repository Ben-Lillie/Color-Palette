from PIL import Image, ImageDraw
from colormap import rgb2hex
from collections import defaultdict
import math
import uuid


hexList = []


def getColours(width, height, im):
    # Pixel Count
    pixel_count = width * height
    processed_count = 0
    my_dict = defaultdict(int)
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            # Convert RGB to Hex
            red = int(math.ceil(r / 40.0)) * 40
            green = int(math.ceil(g / 40.0)) * 40
            blue = int(math.ceil(b / 40.0)) * 40

            if red > 255:
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255

            hexColor = rgb2hex(red, green, blue)
            # Append Hex Colour to List
            hexList.append(hexColor)
            if hexColor in my_dict:
                my_dict[hexColor] += 1
            else:
                my_dict[hexColor] = 1

            processed_count += 1

            print("Processed " + str(processed_count) + " Out of " + str(pixel_count))

    findCommonColours(my_dict, im)


def findCommonColours(colours_dict, im):
    common_colours = []
    current_count = 0
    my_dict_sorted_keys = sorted(colours_dict, key=colours_dict.get, reverse=True)
    for r in my_dict_sorted_keys:
        if colours_dict[r] > 2 and current_count < 10:
            # print(r, my_dict[r])
            common_colours.append(r)
            current_count += 1

    outputPalette(im, common_colours)


def outputPalette(im, colours):
    width, height = im.size

    # Add 210 Pixels to Height for 200px high rects and a 10px gap
    img = Image.new('RGBA', (width, height + 215), color='white')

    # Get Width of Rects
    rect_width = width / 10

    # Setup Draw
    draw = ImageDraw.Draw(img)

    # Current X
    current_x = 0

    img.paste(im, (0, 0))

    # work out the gap between each rect
    # image_width / num_boxes + 1
    # This gives us the center point to place each rect

    for colour in colours:
        print(colour)
        # Draw the Coloured Rectangle
        # [(x1,y1),(x2,y2)]
        draw.rectangle([(current_x, height), (current_x + rect_width, height + 215)], fill=colour)
        # print(gap - 50, 586, gap + 50, 786)
        # draw.point((current_x, 586), fill=colour)
        current_x += rect_width

    unique_filename = str(uuid.uuid4())
    img.save(unique_filename + '.png')

def main():
    im = Image.open("wallpaper1.jpg")

    width, height = im.size
    getColours(width, height, im)


if __name__ == '__main__':
    main()
