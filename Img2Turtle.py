# Developed by @MnesicDev
# https://github.io/Flangry

import turtle
from PIL import Image

# Resize the image to a given scale
def resize_image(image, scale):
    width, height = image.size
    new_width = int(width * scale)
    new_height = int(height * scale)
    return image.resize((new_width, new_height))

# Load the image
filename = input("Enter the location of the image: ")
res = input("Enter the scale of the image as a decimal (0.1 = 10%, 1 = 100%): ")
original_image = Image.open(filename)
resized_image = resize_image(original_image, res)  # Resize to 70% of the original size

# Create a turtle screen and turtle object
screen = turtle.Screen()
screen.setup(float(1), float(1))

turtle_obj = turtle.Turtle()
turtle.tracer(0, 0)
turtle_obj.speed(0)
turtle_obj.penup()


# Convert the image to RGB mode if it's not already
if resized_image.mode != 'RGB':
    resized_image = resized_image.convert('RGB')

# Draw the image using turtle graphics
for y in range(resized_image.height):
    for x in range(resized_image.width):
        r, g, b = resized_image.getpixel((x, y))
        turtle_x = x - (resized_image.width // 2)
        turtle_y = (resized_image.height // 2) - y
        # print(f"goto({turtle_x}, {turtle_y})")
        # print(f"dot(2, {r/255}, {g/255}, {b/255})")
        turtle_obj.goto(turtle_x, turtle_y)
        turtle_obj.dot(2, r/255, g/255, b/255)
        turtle_obj.hideturtle()

# Update the screen and run the main loop
turtle.update()
turtle.mainloop()
