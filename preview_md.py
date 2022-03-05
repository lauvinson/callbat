import os

import util

dic_arr = util.csv2dic('/Users/vinson/Desktop/电商/preview/价格表.csv')
pro_attr = {}
for v in dic_arr:
    pro_attr[v['货号']] = v

path = '/Users/vinson/Desktop/电商/preview/img'
md_file = open("/Users/vinson/Desktop/电商/preview/preview.md", "a", encoding="utf-8")  # 将w换成 a
files = os.listdir(path)
for dir in files:
    dir_path = path + '/' + dir
    if os.path.isdir(dir_path):
        dir_files = os.listdir(dir_path)
        for file in dir_files:
            md_file.write('| ' + dir + ' | ![]('+'./img/' + dir + '/' + file+') | ' + pro_attr[dir]['\ufeff品牌'] + ' | ' + pro_attr[dir]['尺码'] + ' | ' + pro_attr[dir]['进价（元）'] + ' | ' + pro_attr[dir]['颜色'] + ' | ')
            md_file.write('\n')
