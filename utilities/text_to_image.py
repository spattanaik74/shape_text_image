import re

import cv2
from tkinter import colorchooser
import random

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

temp = './save/temp.png'


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


def add_text_to_image(picture_path, template, fonts, font_size, path):
    img = Image.open(path)
    img.save(temp)
    for k, v in template.items():
        if k == 'image':
            bg = Image.open(path)
            img2 = Image.open(picture_path).convert('RGBA')
            img2 = img2.resize(template[k][1])
            bg.paste(img2, template[k][0])
            bg.save(temp)
        else:
            text = input(f"{k}: ")
            regex_email = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
            print(re.findall(regex_email, text))
            w = template[k][1][0] - template[k][0][0]
            h = template[k][1][1] - template[ks][0][1]
            x = template[k][0][0]
            y = template[k][0][1]
            colors = ["#" + "".join([random.choice("ABCDEF0123456789") for i in range(6)])]
            colors = colors[0]
            img = Image.open(temp)
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

            y_text = int(y + h / 2 - height * len(lines) / 2)
            for line in lines:
                width, height = font.getsize(line)
                draw.text((x, y_text), line, font=font, fill=colors)
                y_text += height
            img.save(temp)
