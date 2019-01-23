from PIL import Image, ImageDraw
from colormap import rgb2hex
from collections import defaultdict

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
            hexColor = rgb2hex(r, g, b)
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
        if colours_dict[r] > 2 and current_count < 9:
            # print(r, my_dict[r])
            common_colours.append(r)
            current_count += 1

    outputPalette(im, common_colours)


def outputPalette(im, colours):
    width, height = im.size

    # Add 210 Pixels to Height for 200px high rects and a 10px gap
    img = Image.new('RGBA', (width, height + 210), color='white')

    # Get Width of Rects
    rect_width = width / 10

    # Setup Draw
    draw = ImageDraw.Draw(img)

    # Current X
    current_x = 0

    img.paste(im, (0, 0))

    print(colours)

    for colour in colours:
        print(colour)
        draw.rectangle([(current_x, 586), (rect_width + current_x, 786)], fill=colour)
        current_x += 200

    img.save('pil_red.png')

def main():
    im = Image.open("wallpaper.jpg")

    width, height = im.size
    getColours(width, height, im)


if __name__ == '__main__':
    main()
