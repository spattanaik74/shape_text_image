import re
import random

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class TextToImage:
    def __init__(self, base_template,  template, font, image_path, output_path, header, desc, footer, font_size):
        self.base_template = base_template
        self.template = template
        self.font = font
        self.image_path = image_path
        self.output_path = output_path
        self.header = header
        self.desc = desc
        self.footer = footer
        self.font_size = font_size

    def _text_wrap(self, text, fonts, font_size, max_width, width):
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

    def convert(self):
        temp = "../tests/resources/save/temp folder/temp.png"
        img = Image.open(self.base_template)
        img.save(temp)
        for k, v in self.template.items():
            if k == 'image':
                bg = Image.open(self.base_template)
                img2 = Image.open(self.image_path).convert('RGBA')
                img2 = img2.resize(self.template[k][1])
                bg.paste(img2, self.template[k][0])
                bg.save(temp)
            else:
                text = None
                if k == "header":
                    text = self.header
                elif k == "footer":
                    text = self.footer
                else:
                    text = self.desc
                print(f"{k}: {text}")
                regex_email = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
                word_tuple = re.findall(regex_email, text)
                # print(f"word_typle: {word_tuple}")
                if len(word_tuple) == 0:
                    word_set = ''
                else:
                    word_set = max(word_tuple[0])
                # word_set = max(word_tuple[0])
                print(f"word: {word_set}")
                w = self.template[k][1][0] - self.template[k][0][0]
                h = self.template[k][1][1] - self.template[k][0][1]
                x = self.template[k][0][0]
                y = self.template[k][0][1]
                colors = ["#" + "".join([random.choice("ABCDEF0123456789") for i in range(6)])]
                colors = colors[0]
                img = Image.open(temp)
                img = img.convert("RGBA")
                draw = ImageDraw.Draw(img)
                width, height = img.size
                _font = ImageFont.truetype(font=self.font, size=int(self.font_size * width * 0.001875))
                # _font = ImageFont.truetype(font=self.font, size=int(self.font_size))
                _font_size = self.font_size
                lines = self._text_wrap(text, self.font, _font_size, w, width)
                while _font.getsize(text)[1] * len(lines) > h:
                    _font = ImageFont.truetype(font=self.font, size=int(_font_size * width * 0.001875))
                    # _font = ImageFont.truetype(font=self.font, size=int(_font_size))
                    _font_size -= 1
                    lines = self._text_wrap(text, self.font, _font_size, w, width)
                # print(lines)
                width, height = _font.getsize(lines[0])
                count = 0
                y_text = int(y + h / 2 - height * len(lines) / 2)
                if len(word_set) != 0:
                    for line in lines:
                        if word_set in line:
                            list_1 = line.split()
                            count = 0
                            for i in list_1:
                                width_font, height_font = _font.getsize(i)
                                # print(f'width_font: {width_font}')
                                # print(i)
                                if i == word_set:
                                    draw.text((x + count, y_text), i, font=_font, fill='#FF0000')
                                    count += width_font + 10
                                else:
                                    draw.text((x + count, y_text), i, font=_font, fill=colors)
                                    count += width_font + 10

                        else:
                            draw.text((x, y_text), line, font=_font, fill=colors)
                        y_text += height
                else:
                    for line in lines:
                        width, height = _font.getsize(line)
                        draw.text((x, y_text), line, font=_font, fill=colors)
                        y_text += height

                img.save(temp)

