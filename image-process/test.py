print("中国人11444")

# import requests
#
# res = requests.get('https://www.baidu.com')
# save_file = open("itcast.html", "w")
# save_file.write(res.content)
# save_file.close()
#


# #载入必要的模块
# import pygame
# #pygame初始化
# pygame.init()
# # 待转换文字
# text = u"文字转图片"
# #设置字体和字号
# font = pygame.font.SysFont('Microsoft YaHei', 64)
# #渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
# ftext = font.render(text, True, (65, 83, 130),(255, 255, 255))
# #保存图片
# pygame.image.save(ftext, "image.jpg")#图片保存地址


# -*- coding: utf-8 -*-
import os

from PIL import Image, ImageFont, ImageDraw

text = u"这是一段测试文本，test 123。"
im = Image.new("RGB", (300, 50), (255, 255, 255))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype(os.path.join("fonts", "msyh.ttf"), 14)
dr.text((10, 5), text, font=font, fill="#000000")
im.show()
im.save('output.png')
