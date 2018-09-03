# -*- coding: UTF-8 -*-
# 第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image, ImageDraw, ImageFont, ImageColor


def add_num(image, num):
    # image.show()
    box = (200, 140, 800, 880)  #(left,upper,right,lower)
    image = image.crop(box) #cut the picture
    draw = ImageDraw.Draw(image)
    width, height = image.size
    font = ImageFont.truetype("C:/windows/fonts/arial.ttf", 150) #(font,size)
    draw.text((width - 100, 0), num, font=font, fill='red') #((location),text,font,color)
    image.save('F:/learnpython/add_num_result.jpg', 'jpeg')

    return 0

if __name__ == '__main__':
    image = Image.open("F:/learnpython/add_num.jpg")
    add_num(image, '4')
