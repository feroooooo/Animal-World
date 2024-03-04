import os
from PIL import Image

def convert_png_to_jpg(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png"):
                # 构建完整的文件路径
                file_path = os.path.join(root, file)
                # 打开并转换图像
                image = Image.open(file_path)
                # 构建JPG文件路径，替换扩展名
                jpg_path = os.path.splitext(file_path)[0] + ".jpg"
                # 转换并保存为JPG
                rgb_im = image.convert('RGB')
                rgb_im.save(jpg_path, quality=95)
                # 如果需要，可以在这里删除原PNG文件
                os.remove(file_path)

# 指定要转换的目录
directory = 'C:/Custom/DataSet/WildLife'
convert_png_to_jpg(directory)