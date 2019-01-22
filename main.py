from PIL import Image
from colormap import rgb2hex
from collections import defaultdict

hexList = []

im = Image.open("wallpaper.jpg")
out = Image.new('I', im.size, 0xffffff)


width, height = im.size

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

# Find 10 top most used Hex Colours
common_colours = []
current_count = 0
my_dict_sorted_keys = sorted(my_dict, key=my_dict.get, reverse=True)
for r in my_dict_sorted_keys:
    if my_dict[r] > 2 and current_count < 9:
        # print(r, my_dict[r])
        common_colours.append(r)
        current_count += 1


out.save('bar.png')