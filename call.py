import os
import random
from time import sleep


# 执行拨打
def call(n):
    os.popen('adb shell am start -a android.intent.action.CALL -d tel:{}'.format(n))


# 执行挂断
def call_end():
    os.popen('adb shell input keyevent 6')

#
# # 读取拨打数据
# numbers = []
# with open('C:/Users/sun/Desktop/phone.txt', 'r') as f:
#     for line in f:
#         numbers.append(list(line.strip('\n').split(',')))
# # 循环拨打，显示信息
# for number in numbers:
#     remain = len(numbers) - numbers.index(number) - 1
#     remain = str(remain)
#     # 拨打电话
#     call(number)
#
#     # 假装通话，停顿
#     tel_time = random.randint(20, 36)
#     sj = "随机等待"
#     print("还剩" + remain + "个" + sj + str(tel_time) + "秒")
#     sleep(tel_time)
#     # 挂断电话
#     call_end()
#     sleep(2)
