from PIL import Image
from PIL import ImageDraw, ImageFont

# 字体位置
BASE_PATH = "/Users/ruiweifang/softwares/images/"
# 处理后图片目录
process_path = "images/process/"

im = Image.open('images/d.jpg')
print(im.format, im.size, im.mode)

draw = ImageDraw.Draw(im)
# 字体 路径 文字大小
fnt = ImageFont.truetype(r'/Users/ruiweifang/softwares/images/STZHONGS.TTF', 100)
fnt2 = ImageFont.truetype(r'/Users/ruiweifang/softwares/images/SIMSUN.TTC', 50)
font = ImageFont.truetype(r'/Users/ruiweifang/softwares/images/STZHONGS.TTF', 40, encoding="unic")  # 设置字体
draw.text((200, 100), u'中国加油\n\t武汉加油', fill='red', align="center", stroke_width=20, stroke_fill="black", font=fnt)
draw.text((700, 800), u'团车加油', fill='red', font=fnt2)
draw.text((100, 50), u'汉字水印测试', 'fuchsia', font)
# draw.ink = 0 + 0 * 256 + 255 * 256 * 256
draw.text((600, 500), "I love china!!!", fill="red", direction="ltr", language="en", stroke_width=10,
          stroke_fill="yellow", font=fnt)
im.save(process_path + "d_watermark_text.jpg")
im.show()

# 缩略图
# size = 128, 128
# im.thumbnail(size)
# im.save(process_path + "e_thumbnail_128x128.jpg")

# 批量生成缩略图 glob(文件名模式匹配，不用遍历整个目录判断每个文件是不是符合)
# for infile in glob.glob("images/*.jpg"):
#     path, filename = os.path.split(infile)
#     im = Image.open(infile)
#     im.thumbnail(size, Image.ANTIALIAS)
#     im.save(process_path + "thumbnail_" + filename, "JPEG")


# 调整图片大小 resize
# im.resize((200,100))
# im.save(process_path + "ie_resize.jpg")

# 模糊效果 BLUR(模糊操作),GaussianBlur(高斯模糊),MedianFilter(中值过滤器)，FIND_EDGES(查找边)
# im_blur = im.filter(ImageFilter.BLUR)
# im_blur.save(process_path + "d_blur.jpg", "jpeg")
# im_blur.show()

# 裁剪
# box = (100, 100, 400, 400)
# im_crop = im.crop(box)
# im_crop.save(process_path + "e_crop.jpg")

# 旋转 expand放大了图像尺寸 ,使得边角的图像不被裁剪四个角刚好贴着图像边缘
# im_rotate = im.rotate(45, expand=True)
# im_rotate.save(process_path + "d_rotate45_true.jpg")
# 打开 open 旋转 rotate 显示 show
# im.rotate(45).show()
# 水平反转
# im.transpose(Image.FLIP_LEFT_RIGHT).save(process_path + "flip_left_right.jpg", "JPEG")
# im.transpose(Image.FLIP_TOP_BOTTOM).save(process_path + "flip_top_bottom.jpg", "JPEG")

# im.transpose(Image.ROTATE_180).show()

# im.rotate(20).save(process_path + "d_rotate20.jpg", "JPEG")
# im.rotate(90).save(process_path + "d_rotate90.jpg", "JPEG")
# im.rotate(180).save(process_path + "d_rotate180.jpg", "JPEG")
# im.rotate(270).save(process_path + "d_rotate270.jpg", "JPEG")

# 图片水印
# mask = Image.open("images/watermark.png")
# layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
# layer.paste(mask, (im.size[0] - 100, im.size[1] - 100))
# out = Image.composite(layer, im, layer).show()

# 粘贴
# im.paste(mask, (800, 800), None)
# im.show()

# 灰度图片
# im = im.convert("L")
# im.show()
# plt.imshow(im)
# plt.show()

#
# # 将原来的图片转换为RGBA模式
# im = im.convert('RGBA')
# # 新建一个图片，尺寸与上面的尺寸一样，透明度为0即完全透明
# txt = Image.new('RGBA', im.size, (0, 0, 0, 0))
# # 设置要写文字的字体，注意有的字体不能打汉字,这里用的微软雅黑可以
# fnt = ImageFont.truetype(r'/Users/ruiweifang/softwares/images/STZHONGS.TTF', 30)
# # 打汉字
# d = ImageDraw.Draw(txt)
# # 写要打的位置，内容,用的字体，文字透明度
# d.text((txt.size[0] - 385, txt.size[1] - 80), "中国加油,武汉加油\n团车加油", font=fnt, fill=(255, 255, 255, 150))
# # 两个图片复合
# out = Image.alpha_composite(im, txt)
# out.show()
# 保存加水印后的图片
# out.save(BASE_PATH+"composite.jpg")
