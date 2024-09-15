from PIL import Image
image_original = Image.open(input("素材文件路径: "))
width, height = image_original.size
enlarge = int(input("放大倍数: "))
image_original.resize((width * enlarge, height * enlarge), Image.NEAREST).save(input("生成文件路径: "))
print("完成.")
