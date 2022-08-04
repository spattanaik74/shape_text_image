import cv2
from tkinter import colorchooser
import random

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def text_wrap(text, fonts, font_size, max_width, width):
    font_1 = ImageFont.truetype(font=fonts, size=int(font_size * width * 0.001875))

    lines = []
    if font_1.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        words = text.split(' ')
        i = 0
        while i < len(words):
            line = ''
            while i < len(words) and font_1.getsize(line + words[i])[0] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)

    return lines


def add_text_to_image(text, fonts, font_size, path, x, y, h, w):
    colors = ["#" + "".join([random.choice("ABCDEF0123456789") for i in range(6)])]
    colors = colors[0]
    img = Image.open(path)
    img = img.convert("RGBA")
    draw = ImageDraw.Draw(img)
    width, height = img.size
    font = ImageFont.truetype(font=fonts, size=int(font_size * width * 0.001875))
    font_size1 = font_size
    lines = text_wrap(text, fonts, font_size1, w, width)
    while font.getsize(text)[1] * len(lines) > h:
        font = ImageFont.truetype(font=fonts, size=int(font_size1 * width * 0.001875))
        font_size1 -= 1
        lines = text_wrap(text, fonts, font_size1, w, width)

    width, height = font.getsize(lines[0])

    y_text = int(y + h/2 - height * len(lines)/2)
    for line in lines:
        width, height = font.getsize(line)
        draw.text((x, y_text), line, font=font, fill=colors)
        y_text += height

    img.save('./save/image.png')