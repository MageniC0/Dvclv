#awa

from PIL import Image,ImageDraw
image_name = input("素材文件路径: ")
image_original = Image.open(image_name)
enlarge = int(input("放大倍数: "))
w = enlarge *  image_original.width
h = enlarge *  image_original.height
name = input("生成文件路径: ")

print("正在生成...")
image_enlarge = Image.new('RGB', (w, h), (0, 0, 0, 0))
draw = ImageDraw.Draw(image_enlarge)
for j in range(image_original.width):
    for i in range(image_original.height):
        draw.rectangle([enlarge * j, enlarge * i, enlarge * (j + 1), enlarge * (i + 1)], fill = image_original.getpixel((j, i)))
        
print("完成")
image_enlarge.save(name)
