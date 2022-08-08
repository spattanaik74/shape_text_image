from PIL import Image
import cv2
import matplotlib.pyplot as plt

from utilities import text_to_image

path = "./image/515958.jpg"
path_save = "./image/demo.png"
fonts = './fonts/roboto-Black.ttf'
image_path = "./image/5c7c71feb51b6.png"

template_1 = {"header": [(5, 5), (694, 73)],
              "image": [(5, 79), (322, 760)],
              "description": [(327, 79), (694, 760)],
              "footer": [(5, 766), (694, 894)]}

template_2 = {"image": [(5, 5), (694, 296)],
              "header": [(5, 300), (693, 429)],
              "description": [(5, 429), (694, 761)],
              "footer": [(5, 766), (694, 894)]}

template_3 = {'image': [(5, 5), (360, 894)],
              "header": [(364, 5), (990, 140)],
              "description": [(365, 150), (990, 720)],
              "footer": [(365, 730), (995, 890)]}

img = Image.open(path)
img = img.resize((1000, 900))
img.save(path_save)

# bg = Image.open('./save/image.png')
# img2 = Image.open(image_path).convert('RGBA')
# img2 = img2.resize((300, 680))
# bg.paste(img2, (5, 85))
# bg.save('result.png')

img2 = cv2.imread(path_save)
# cv2.rectangle(img2, template_3['header'][0], template_3['header'][1], (0, 0, 255), 2)
# cv2.rectangle(img2, template_3['image'][0], template_3['image'][1], (0, 0, 255), 2)
# cv2.rectangle(img2, template_3['description'][0], template_3['description'][1], (0, 0, 255), 2)
# cv2.rectangle(img2, template_3['footer'][0], template_3['footer'][1], (0, 0, 255), 2)
#
# plt.imshow(img2)
# plt.show()

text_to_image.add_text_to_image(image_path, template_3, fonts, font_size=65, path=path_save)
