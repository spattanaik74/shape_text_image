from random import random
from unittest import TestCase

from PIL import Image

from shape_text_image import text_to_image
from shape_text_image.config import TemplateConfig

path = "../tests/resources/image/515958.jpg"
base_path = "../shape_text_image/base_template/base.png"
fonts = '../shape_text_image/fonts/roboto-Black.ttf'
image_path = "../tests/resources/image/cheerful-asian-plumber-sitting-floor-repairing-kitchen-sink (2).jpg"
save_image = "../tests/resources/save/save_image/"
temp = '../tests/resources/save/temp folder/temp.png'
header = 'WHERE TO FIND EXPERT URGENT TO REPAIR DRIPPING FAUCET'
desc = "if the water continously comes out from the faucet and it doesn't shut off smoothly, there may be a problem, which may lead to significant problems over time.If you neglect thisissue, the repair cost a great deal or even require a complete replacement.At 1manhelper.com/contactus you can loacte a qualified plumbing technician to repair any faucet issue quickly."
footer = "Get here the answers for all ayour questions 1manhelper.com/contactus"

class TestTextToImage(TestCase):
    def test_convert(self):
        text_image = text_to_image.TextToImage(base_template=base_path,
                                               template=TemplateConfig().get_template("TEMPLATE_LANDSCAPE"), font=fonts,
                                               image_path=image_path, output_path=temp,
                                               header=header, desc=desc, footer=footer, font_size=65)
        text_image.convert()
        save_1 = Image.open(temp)
        save_1.save(save_image + str(random.randint(0, 99999999)) + '.png')
