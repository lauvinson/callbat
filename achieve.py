import os
import shutil

path = "/Users/vinson/Desktop/图片素材/24款短袖0228"
target = '/Users/vinson/Desktop/图片素材/adjusted'
files = os.listdir(path)
for dir in files:
    dir_path = path + '/' +dir
    if os.path.isdir(dir_path):
        if not os.path.exists(target + '/' + dir):
            os.mkdir(target + '/' + dir)
        dir_files = os.listdir(dir_path)
        for file in dir_files:
            if os.path.exists(target + '/' + file.replace('jpg', 'jpeg')):
                shutil.move(target + '/' + file.replace('jpg', 'jpeg'), target + '/' + dir + '/' + file.replace('jpg', 'jpeg'))
