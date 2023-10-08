# encoding:utf-8

import time
import ctypes

# 定义鼠标事件常量
MOUSE_EVENT_LEFT_DOWN = 0x0002
MOUSE_EVENT_LEFT_UP = 0x0004


# 定义鼠标输入结构体
class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]


# 定义输入结构体
class Input(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [("mi", MouseInput)]

    _anonymous_ = ("_input",)
    _fields_ = [("type", ctypes.c_ulong),
                ("_input", _INPUT)]


# 定义SendInput函数的参数类型
SendInput = ctypes.windll.user32.SendInput
SendInput.argtypes = (ctypes.c_uint, ctypes.POINTER(Input), ctypes.c_int)
SendInput.restype = ctypes.c_uint


# 定义鼠标点击函数
def click_mouse(count: int = 10):
    """模拟鼠标点击事件"""

    for i in range(count):
        # 创建一个鼠标左键按下事件
        mouse_down = Input()
        mouse_down.type = 0
        mouse_down.mi.dwFlags = MOUSE_EVENT_LEFT_DOWN

        # 创建一个鼠标左键释放事件
        mouse_up = Input()
        mouse_up.type = 0
        mouse_up.mi.dwFlags = MOUSE_EVENT_LEFT_UP

        # 将事件打包为输入结构体数组
        events = (Input * 2)()
        events[0] = mouse_down
        events[1] = mouse_up

        # 发送输入事件
        SendInput(2, events, ctypes.sizeof(Input))
        # 暂停一下
        time.sleep(0.01)


if __name__ == '__main__':
    time.sleep(2)
    click_mouse(count=300)
