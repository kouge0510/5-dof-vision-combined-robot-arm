"""刘鹏需要调试该文件，此文件为纯机械臂通信内容


"""
import serial.tools.list_ports
import serial
import uart as uart  # 通信协议
import time
import arm_control as control  # 控制函数

ports = list(serial.tools.list_ports.comports())

if not ports:
    print("没有检测到任何串口设备。")

for port in ports:
    print("设备名:", port.device)
    print("描述:", port.description)
    print("硬件ID:", port.hwid)
    print("-----")

# 识别端口号，如果换了环境只要修改port即可

# 定义串口参数
# port = '/dev/ttyUSB1'  # 更改为你的串口号，此处跟setup_uart无关，是单片机的串口号
# baudrate = 115200
# timeout = 1  # 以秒为单位
#
# # 打开串口
# ser = serial.Serial(port, baudrate, timeout=timeout)
# ser.close()

uart.setup_uart(115200)
control.setup_kinematics(110, 105, 75, 185)
# 发送数据

# control.modified_kinematics_move(0, 100, 150, 1000,1000,1000)  # 运用(方法2，两种方法均可)
time.sleep(4)
# uart.uart_send_str("{#000P1500T2000!#001P0903T2000!#002P2171T2000!#003P2094T2000!}")
uart.uart_send_str('{#000P1500T0500!#001P2150T0500!#002P2300T0500!#003P1000T0500!#004P1200T0500!#005P1100T0500!}')
time.sleep(3)
uart.uart_send_str('{#000P2000T0500!#001P2200T0500!#002P2200T0500!#003P0850T0500!#004P1500T0500!#005P1800T0500!}')
# ser.write(data.encode("utf-8"))
time.sleep(2)
uart.uart_send_str("#255P1500T2000!")  # 复位
# 关闭串口

