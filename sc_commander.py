
# task_worker.py
import os
if os.name == "nt":
    os.system("")
    pass
import time, sys, queue
from multiprocessing.managers import BaseManager

import subprocess
import sys
import threading
#from termcolor import colored

from random import randint
# from pkg.cmdcolor import *   #windows
from termcolor import colored   #linux
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--x", help="解压源", type=str,default="default")
parser.add_argument("--target", help="解压目标", type=str,default="default")
parser.add_argument("--addpasswd", action='store_true',required =False, help="add解压密码",default=False)
parser.add_argument("--delpasswd", action='store_true',required =False, help="del密码",default=False)
parser.add_argument("--test", action='store_true',required =False, help="test",default=False)



args = parser.parse_args()


from  common.sc_common import *
client_name = 'S_'
#print(os.environ)
#name = os.environ.get("USER")
name = "winuser01"
client_name = client_name + str(name)


# printDarkGreen(f'        客户端启动中.. {client_name}')
print(colored(f'        push客户端启动中.. {client_name}',"green")  )

class MyException(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message    

class MyException2(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message        

def build_return_list(str_1,str_2,color_):
    
    '''
    构建 返回列表
    '''
    list_ = []
    list_.append(str_1)
    list_.append(str_2)
    list_.append(color_)
    return list_

# 创建类似的QueueManager: #client侧
class QueueManager(BaseManager):
    pass
# QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_work_queue')
QueueManager.register('get_done_queue')
QueueManager.register('get_shared_value')
QueueManager.register('get_pass_dict')


# 连接到中继服务器:
#change in sc_common
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, server_port), authkey=authkey_)
# 从网络连接:
m.connect()
# 获取Queue的对象:
_work_queue = m.get_work_queue()#接受任务队列
_done_queue = m.get_done_queue()
shared_value = m.get_shared_value()
_pass_dict = m.get_pass_dict()#共享字典


def my_push(_line):
    try:
        _work_queue.put(_line,block=True,timeout=10)
    except:
        print("put _work_queue error")
        return 0
    




if 1 ==0:
    #一键Insert开关
    #short cut keys
    # -*- coding=utf-8 -*-
    import sys,os

    #线程
    import win32api
    import win32con
    from threading import Timer
    from pywinauto.win32_hooks import Hook
    from pywinauto.win32_hooks import KeyboardEvent
    from pywinauto.win32_hooks import MouseEvent
    import pywinauto 
    import threading
    import pyperclip
    #线程结束

    import json





    def on_event(args):
        global monitor_thread_id
        global hk
        import json
        """Callback for keyboard and mouse events"""
        if isinstance(args, KeyboardEvent):


            if args.current_key == 'E' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                print("Ctrl + e was pressed")
                win32api.PostThreadMessage(monitor_thread_id, win32con.WM_QUIT, 0, 0);
                
                #win32api.PostThreadMessage(monitor_thread_id2, win32con.WM_QUIT, 0, 0);
            if  args.current_key == "Insert" and args.event_type == 'key down':
                print("insert was pressed")
                time.sleep(0.1)
                #pywinauto.keyboard.send_keys("{VK_MENU up}")
                #time.sleep(0.2)
                #pywinauto.keyboard.send_keys("{F6 down}")
                #time.sleep(0.2)
                #pywinauto.keyboard.send_keys("{F6 up}")
                #time.sleep(0.5)
                # pywinauto.keyboard.send_keys('%d')
                # time.sleep(0.1)
                # pywinauto.keyboard.send_keys('^c')
                # time.sleep(0.05)
                # pywinauto.keyboard.send_keys("{TAB}")
                line = pyperclip.paste()
                print(line)
                
                if "youtube" in line:
                    my_push(line)
                    print(f"find youtube address pushed")

        if isinstance(args, MouseEvent):
            if args.current_key == 'RButton' and args.event_type == 'key down':
                print ("Right button pressed")

            if args.current_key == 'WheelButton' and args.event_type == 'key down':
                print("Wheel button pressed")




    def mouse_key_hook():
        global monitor_thread_id
        global hk
        global CP_1
        global CP_2
        CP_1 = ""
        CP_2 = ""
        monitor_thread_id = win32api.GetCurrentThreadId()
        hk = Hook()
        hk.handler = on_event
        
        hk.hook(keyboard=True, mouse=False)
        





    def mouse_key_hook_helper():
        monitor_thread = threading.Thread(target=mouse_key_hook,name='monitor01')
        monitor_thread.start()

        #grab_screen_thread = threading.Thread(target=grab_screen_hook,name='monitor02')
        #grab_screen_thread.start()

        
        main_thread_id = win32api.GetCurrentThreadId()
        #monitor_thread.join()#zu se
        #thread2.join()#zu se
        #print(threading.active_count())
        #print(threading.enumerate())
        #print(threading.current_thread())
        print('mouse_key_hook_helper begin success!')




    # if __name__ == "__main__":
    #     print("short key to working system")
    #     print("version 0.2")
        
    #     mouse_key_hook_helper()

    # print('worker exit.')






test_address = r""
test_folder = ""

if args.target != 'default':
    pass
    test_folder =args.target

if args.addpasswd == True:
    pass
    for line in open("密码.txt"):
        print(line)
        __temp_pass_dic = _pass_dict.get('pass')
        __temp_pass_dic[line] = 1
        #BaseManager字典无法联网共享修改？

    

if args.delpasswd == True:
    pass
    for line in open("密码.txt"):
        print(line)
        __temp_pass_dic = _pass_dict.get('pass')
        __temp_pass_dic.pop(line)
    #BaseManager字典无法联网共享修改？






if __name__ == "__main__":
    #my_push(test_folder)
    o_list = get_all_unziped_sub_folder(test_folder)
    for i in o_list:
        print(f"put {i}")
        if args.test == False:
            my_push(i)
    print("success push")