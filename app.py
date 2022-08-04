from PIL import Image
import cv2
import matplotlib.pyplot as plt

from utilities import text_to_image

path = "./image/515958.jpg"
path_save = "./image/demo.png"
fonts = './fonts/roboto-Black.ttf'
image_path = "./image/5c7c71feb51b6.png"


dict1 = {"header": [(5, 5), (694, 73)],
         "image": [(5, 79), (322, 760)],
         "description": [(327, 79), (694, 760)],
         "footer": [(5, 766), (694, 894)]}

img = Image.open(path)
img = img.resize((700, 900))
img.save(path_save)

bg = Image.open('./save/image.png')
img2 = Image.open(image_path).convert('RGBA')
img2 = img2.resize((300, 680))
bg.paste(img2, (5, 85))
bg.save('result.png')


# img2 = cv2.imread(path_save)
# cv2.rectangle(img2, dict1['header'][0], dict1['header'][1], (0, 0, 255), 2)
# cv2.rectangle(img2, dict1['image'][0], dict1['image'][1], (0, 0, 255), 2)
# cv2.rectangle(img2, dict1['description'][0], dict1['description'][1], (0, 0, 255), 2)
# cv2.rectangle(img2, dict1['footer'][0], dict1['footer'][1], (0, 0, 255), 2)
#
# plt.imshow(img2)
# plt.show()

# for i in range(3):
#     text_1 = input("text: ")
#     type1 = input("type: ")
#     w = int(input("w "))
#     h = int(input("h: "))
#     text_to_image.add_text_to_image(text_1, fonts, font_size=70, path='./save/image.png', x=dict1[type1][0][0], y=dict1[type1][0][1], w=w, h=h)