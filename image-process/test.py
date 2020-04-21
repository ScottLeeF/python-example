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
from PIL import Image, ImageDraw

im = Image.new('RGB', (1920, 1080), (255, 255, 255))
draw = ImageDraw.Draw(im)
# draw.rectangle((0, 0, 500, 280), 'white', 'black')
# draw.line((0, 40, 500, 40), 'black')
# draw.line((0, 80, 500, 80), 'black')
# draw.line((0, 120, 500, 120), 'black')
# draw.line((0, 160, 500, 160), 'black')
# draw.line((0, 200, 500, 200), 'black')
# draw.line((0, 240, 500, 240), 'black')
# draw.line((125, 0, 125, 280), 'black')
# draw.line((250, 0, 250, 280), 'black')
# draw.line((375, 0, 375, 280), 'black')
# font = ImageFont.truetype(r'/Users/ruiweifang/softwares/images/STZHONGS.TTF', 18, encoding="unic")  # 设置字体  
# draw.text((50, 20), 'bin', 'black', font)
# draw.text((175, 20), 'woe', 'black', font)
# draw.text((280, 20), 'volume', 'black', font)
# draw.text((395, 20), 'bad rate', 'black', font)
# for i in range(6):
#     draw.text((5, 60 + 40 * i), "tuanchejiayou", 'black', font)
#     draw.text((150, 60 + 40 * i), "武汉加油", 'black', font)
#     draw.text((300, 60 + 40 * i), "中国加油", 'black', font)
#     draw.text((425, 60 + 40 * i), "团车加油", 'black', font)
for i in range(0, 20):
    print(i)
    draw.line((i * 200 + 1, 0, i * 200, 1200), 'cyan')

# for i in range(0,20):
#     draw.line((0,i*200 ,2000, i*200), 'cyan')

im.show()

test = "【乌兰察布团购会4.12】购车代金券 一汽红旗 红旗H5 2019款 30TD"
print(bytes(test, encoding="utf8"))
