import cv2
import random
import matplotlib.pyplot as plt
from PIL import Image

from utilities import text_to_image
from template import Template

path = "./image/515958.jpg"
path_save = "./image/demo.png"
fonts = './fonts/roboto-Black.ttf'
image_path = "./image/plumber-with-his-arms-crossed.jpg"
save_image = "./save/save_image/"
temp = './save/temp folder/temp.png'


img = Image.open(path)
img = img.resize((1000, 900))
img.save(path_save)

# bg = Image.open('./save/image.png')
# img2 = Image.open(image_path).convert('RGBA')
# img2 = img2.resize((300, 680))
# bg.paste(img2, (5, 85))
# bg.save('result.png')

# img2 = cv2.imread(path_save)
# cv2.rectangle(img2, Template.template_portrait_2['header'][0], Template.template_portrait_2['header'][1], (0, 0, 255), 2)
# cv2.rectangle(img2, Template.template_portrait_2['image'][0], Template.template_portrait_2['image'][1], (0, 0, 255), 2)
# cv2.rectangle(img2, Template.template_portrait_2['description'][0], Template.template_portrait_2['description'][1], (0, 0, 255), 2)
# cv2.rectangle(img2, Template.template_portrait_2['footer'][0], Template.template_portrait_2['footer'][1], (0, 0, 255), 2)
#
# plt.imshow(img2)
# plt.show()

if __name__ == '__main__':
    text_to_image.add_text_to_image(image_path, Template.template_portrait_2, fonts, font_size=65, path=path_save, temp=temp)
    save_1 = Image.open(temp)
    save_1.save(save_image + str(random.randint(0, 99999999))+'.png')


