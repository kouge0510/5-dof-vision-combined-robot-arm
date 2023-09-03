# 机械臂跟摄像头配合部分
# 机械臂部分使用uart控制，单片机部分使用serial控制
import serial.tools.list_ports
import serial
import uart as uart  # 通信协议
# import time
# import arm_control as control  # 控制函数,此为方法2调用方案，一般情况下不用
import sys
from io import StringIO
import cluster as clu  # 整合聚类算法

ports = list(serial.tools.list_ports.comports())


# if not ports:
#     print("没有检测到任何串口设备。")
#
# for port in ports:
#     print("设备名:", port.device)
#     print("描述:", port.description)
#     print("硬件ID:", port.hwid)
#     print("-----")

# 识别端口号，如果换了环境只要修改port即可

# 定义串口参数
# port = '/dev/ttyUSB0'  # 更改为你的串口号，此处跟setup_uart无关，是单片机的串口号
# baudrate = 115200
# timeout = 1  # 以秒为单位
#
# # 打开串口
# ser = serial.Serial(port, baudrate, timeout=timeout)
uart.setup_uart(115200)


class CapturePrint:  # 检测文字类
    def __enter__(self):
        self.original_stdout = sys.stdout
        sys.stdout = self.captured = StringIO()
        return self

    def __exit__(self, *args):
        sys.stdout = self.original_stdout

    def getvalue(self):
        return self.captured.getvalue()

    def count_occurrences(self, term):
        return self.getvalue().count(term)  # 计算出现次数


with CapturePrint() as c:
    clu.main()
    output = c.getvalue()

# 判断机械臂执行条件

if c.count_occurrences('红球距离') > 3 and c.count_occurrences('0.05') > 3:  # 检测球类

    '等待刘鹏完成机械臂动作'
    uart.uart_send_str()  # 发送命令,使用机械臂

    print("已完成红球抓取动作")  # 自检程序

elif c.count_occurrences('黄球距离') > 3 and c.count_occurrences('0.05') > 3:
    uart.uart_send_str()
    print("已完成黄球抓取动作")

elif c.count_occurrences('蓝球距离') > 3 and c.count_occurrences('0,05') > 3:
    uart.uart_send_str()
    print("已完成蓝球抓取动作")
elif c.count_occurrences('Rectangle') > 2:  # 检测长方形
    if c.count_occurrences('Blue') > 2:
        uart.uart_send_str()
        print("已完成蓝色长方形抓取动作")
    elif c.count_occurrences('Red') > 2:
        uart.uart_send_str()
        print("已完成红色长方形抓取动作")
elif c.count_occurrences('Square') > 2:  # 检测正方形
    if c.count_occurrences('Blue') > 2:
        uart.uart_send_str()
        print("已完成蓝色正方形抓取动作")
    elif c.count_occurrences('Red') > 2:
        uart.uart_send_str()
        print("已完成红色正方形抓取动作")
else:
    print("fuck you")
