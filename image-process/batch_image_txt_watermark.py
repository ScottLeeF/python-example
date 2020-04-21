
import glob
import os

from PIL import Image, ImageDraw, ImageFont

# 字体位置
BASE_PATH = "/Users/ruiweifang/softwares/images/"


def add_num(pattern):
    set_font = ImageFont.truetype(r'/Users/ruiweifang/softwares/images/STZHONGS.TTF', 40)
    fill_color = "red"

    for img in glob.glob(pattern):
        image = Image.open(img)
        draw = ImageDraw.Draw(image)
        width, height = image.size
        draw.text((40, height - 100), u'团车网', font=set_font, fill=fill_color)
        image.save(BASE_PATH + "watermark/" + os.path.basename(img), 'jpeg')

    return 0


if __name__ == '__main__':
    pattern = BASE_PATH + '*.jpg'

    add_num(pattern)
    print("批量完成添加图片水印")
