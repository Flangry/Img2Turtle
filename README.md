# Img2Turtle
Convert Images to Python Turtle Graphics


Img2Turtle is a Python script that utilizes the Turtle graphics library and the Python Imaging Library (PIL) to render an image using turtle graphics. This script allows you to visualize images by converting them into pointillist-style representations using dots of various colors.

## Features

- Load an image from the filesystem.
- Resize the image to a desired scale.
- Render the image using turtle graphics, representing pixels as dots on the screen.
- Control the scale of the rendered image.
- Output a graphical representation of the image using Turtle.
- Animations file which takes a lot longer but you can visualise the render process.

## Installation

1. Install the required dependencies:

    ```bash
    pip install Pillow
    ```

2. Run the script:

    ```bash
    python flangry.py
    ```

## Usage

1. Run the script using Python.
2. Enter the location of the image file when prompted.
3. Enter the scale of the image as a decimal (e.g., 0.1 for 10%, 1 for 100%).
4. It will take some time to render your image depending on the size of the image. Windows will tell you that the program has stopped responding, please be patient
5. View the rendered image using Turtle graphics.

## Examples

Check out the [examples](examples/) folder for sample images and their corresponding rendered outputs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



