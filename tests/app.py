import cv2
import random
from PIL import Image

from shape_text_image import text_to_image
from shape_text_image import config

path = "../tests/resources/image/515958.jpg"
base_path = "../shape_text_image/base_template/base.png"
fonts = '../shape_text_image/fonts/roboto-Black.ttf'
image_path = "../tests/resources/image/cheerful-asian-plumber-sitting-floor-repairing-kitchen-sink (2).jpg"
save_image = "../tests/resources/save/save_image/"
temp = '../tests/resources/save/temp folder/temp.png'
header = 'WHERE TO FIND EXPERT URGENT TO REPAIR DRIPPING FAUCET'
desc = "if the water continously comes out from the faucet and it doesn't shut off smoothly, there may be a problem, which may lead to significant problems over time.If you neglect thisissue, the repair cost a great deal or even require a complete replacement.At 1manhelper.com/contactus you can loacte a qualified plumbing technician to repair any faucet issue quickly."
footer = "Get here the answers for all ayour questions 1manhelper.com/contactus"

img = Image.open(path)
img = img.resize((1000, 900))
img.save(base_path)

# bg = Image.open('./save/image.png')
# img2 = Image.open(image_path).convert('RGBA')
# img2 = img2.resize((300, 680))
# bg.paste(img2, (5, 85))
# bg.save('result.png')

img2 = cv2.imread(base_path)
# cv2.rectangle(img2, Template.template_portrait_3['header'][0], Template.template_portrait_3['header'][1], (0, 0, 255), 2)
# cv2.rectangle(img2, Template.template_portrait_3['image'][0], Template.template_portrait_3['image'][1], (0, 0, 255), 2)
# cv2.rectangle(img2, Template.template_portrait_3['description'][0], Template.template_portrait_3['description'][1], (0, 0, 255), 2)
# cv2.rectangle(img2, Template.template_portrait_3['footer'][0], Template.template_portrait_3['footer'][1], (0, 0, 255), 2)
#
# plt.imshow(img2)
# plt.show()

if __name__ == '__main__':
    text_image = text_to_image.TextToImage(base_template=base_path, template=config.TemplateConfig.template_landscape, font=fonts, image_path=image_path, output_path=temp,
                                           header=header, desc=desc, footer=footer, font_size=65)
    text_image.convert()
    save_1 = Image.open(temp)
    save_1.save(save_image + str(random.randint(0, 99999999))+'.png')


