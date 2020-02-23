import os

from PIL import Image
from PIL import ImageDraw, ImageFont

BASE_PATH = "/Users/ruiweifang/softwares/images/"

hwxw_path = os.path.join(BASE_PATH, "STKAITI.TTF")
hwxk_path = os.path.join(BASE_PATH, "STLITI.TTF")
hwls_path = os.path.join(BASE_PATH, "STXINWEI.TTF")
# 新建画板
im_board = Image.new("RGB", (500, 500), (255, 255, 255))
# 画笔对象
drawObject = ImageDraw.Draw(im_board)
# 定义字体  ImageFont.truetype(file,size)
# 创建一个字体对象.这个函数从指定的文件加载了一个字体对象，并且为指定字体大小
hwxw_font = ImageFont.truetype(hwxw_path, 18)
hwxk_font = ImageFont.truetype(hwxk_path, 24)
hwls_font = ImageFont.truetype(hwls_path, 36)
"""
注意事项：笔的默认颜色为白色，画笔的颜色可以通过draw的ink属性来改变
draw.ink = 0(R) + 0(G) * 256 + 0(B) * 256 * 256
也可以通过fill参数更改字体颜色
"""

drawObject.rectangle([100, 100, 400, 400], outline=128)

text = u"人生苦短"
text_ = u"我用"
text__ = u"Python"
# 利用text函数添加文字
# drawObject.ink = 0 + 0 * 256 + 0 * 256 * 256
drawObject.text([180, 170], text, font=hwxw_font, fill="yellow")
# drawObject.ink = 0 + 128 + 100
drawObject.text([180, 200], text_, font=hwxk_font, fill="blue")
# drawObject.ink = 0 + 0 * 256 + 255 * 256 * 256
drawObject.text([180, 230], text__, font=hwls_font, fill=(255, 222, 111))

im_board.save("drawing_board.png", "PNG")

# Font.getsize(text)
# 返回一个二元素元组，为指定text在指定字体大小之后的size
print(hwxk_font.getsize(text))
