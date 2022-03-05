import random
import tkinter
from tkinter import StringVar

from pypinyin import pinyin

import call
import util as util

dic_arr = util.csv2dic('/Users/vinson/Desktop/call.csv')
dic_arr_len = len(dic_arr)
dic_arr_select_index = 0

win = tkinter.Tk()
# 窗口大小
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
win.geometry("%dx%d" % (w, h))
title = '813呼叫中心'
win.title(title)

name_pinyin = StringVar()
name = StringVar()
gender = StringVar()
tel = StringVar()
group = StringVar()
intention = StringVar()
come = StringVar()
out = StringVar()
label = StringVar()
label_dic = {}
label_dic_output = '/Users/vinson/Desktop/call_label.csv'


label_name_pinyin = tkinter.Label(win, textvariable=name_pinyin, bg="SkyBlue", font=('黑体', 50, 'bold'))
label_name = tkinter.Label(win, textvariable=name, bg="SkyBlue", font=('黑体', 200, 'bold'))
label_group = tkinter.Label(win, textvariable=group, font=('黑体', 100))
label_tel = tkinter.Label(win, textvariable=tel, font=('黑体', 80))
label_intention = tkinter.Label(win, textvariable=intention, font=('黑体', 80))
label_come = tkinter.Label(win, textvariable=come, font=('黑体', 80))
label_input = tkinter.Entry(win, textvariable=label)
button = tkinter.Button(win, text='下一个', height=10, bg="blue",
                        width=20, comman=lambda: start())


def start():
    # 挂断电话
    # call.call_end()
    # 循环拨打，显示信息
    global dic_arr_select_index
    index = dic_arr_select_index
    if index >= dic_arr_len:
        return
    if label.get() != '':
        label_dic[str(name.get()) + str(tel.get())] = str(label.get())
        label_input.delete('0', 'end')
        # util.dic2csv(label_dic, label_dic_output)
        file = open(label_dic_output, 'w')
        file.write(str(label_dic))
        file.close()
    left = dic_arr_len - index - 1
    win.title("%s - 剩余%d个" % (title, int(left)))
    dic = dic_arr[index]
    name.set(dic['姓名'])
    name_pinyin.set(pinyin(name.get()))
    gender.set(dic['性别'])
    group.set(dic['店简称'])
    tel.set(dic['联系方式'])
    intention.set('意向日期：' + dic['意向日期'])
    come.set('入住日期：' + dic['入住日'])
    if gender.get() == '女':
        label_name["background"] = "pink"
        label_name_pinyin["background"] = "pink"

    # 拨打电话
    call.call(dic['联系方式'])

    # 假装通话，停顿
    # tel_time = random.randint(5, 10)
    # sleep(tel_time)
    dic_arr_select_index += 1


label_name_pinyin.grid(row=0, column=0, columnspan=1, sticky='se')
label_name.grid(row=1, column=0, columnspan=1, sticky='se')
label_tel.grid(row=1, column=1, sticky='sw')
label_group.grid(row=1, column=1, sticky='nw')
label_intention.grid(row=3, column=0, sticky='nw')
label_come.grid(row=4, column=0, sticky='nw')
label_input.grid(row=5, column=1, sticky='nw')
button.grid(row=6, column=1, sticky='nw')
# win.bind("<Key>", start)
win.mainloop()
