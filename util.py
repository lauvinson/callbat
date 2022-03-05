import csv


def csv2dic(path):
    with open(path, 'r', encoding="utf-8") as f:
        arr = []
        reader = csv.reader(f)
        fieldnames = next(reader)  # 获取数据的第一列，作为后续要转为字典的键名 生成器，next方法获取
        # print(fieldnames)
        csv_reader = csv.DictReader(f,
                                    fieldnames=fieldnames)
        # self._fieldnames = fieldnames   # list of keys for the dict 以list的形式存放键名
        for row in csv_reader:
            arr.append(row)
        return arr


def dic2csv(dic, file):
    with open(file, 'wb') as f:
        w = csv.DictWriter(f, fieldnames=[
            '数据ID', '大区', '代码', '店简称', '姓名', '性别', '联系方式', '科目', '职务', '是否内训导师', '意向日期', '意向班次', '指定酒店', '是否合住', '入住日',
            '退房日', '备注'])
        values = []
        for row in dic:
            values.append(row)
        w.writerows(values)
