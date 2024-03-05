import os
import shutil
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


def copy_images(src_dir, dst_dir):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith('.jpg'):
                src_path = os.path.join(root, file)
                dst_path = os.path.join(dst_dir, file)
                # 检查目标路径是否存在同名文件
                if os.path.exists(dst_path):
                    # 创建一个唯一的新文件名
                    base, extension = os.path.splitext(file)
                    i = 1
                    while os.path.exists(dst_path):
                        new_filename = f"{base}_{i}{extension}"
                        dst_path = os.path.join(dst_dir, new_filename)
                        i += 1
                shutil.copy2(src_path, dst_path)
                print(f"Copied: {src_path} to {dst_path}")

# 源目录和目标目录路径
source_directory = r'C:\Custom\DataSet\WildLife\human'
destination_directory = r'C:\Custom\DataSet\AnimalOrNot\True'

# 执行复制操作
copy_images(source_directory, destination_directory)


# # 指定要转换的目录
# directory = 'C:/Custom/DataSet/WildLife'
# convert_png_to_jpg(directory)