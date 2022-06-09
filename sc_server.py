

# task_worker.py
import os
if os.name == "nt":
    os.system("")
    pass


import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
from multiprocessing import Value
# from pkg.cmdcolor import *   #windows
from termcolor import colored   #linux
import sys

from  common.sc_common import *











import os
import os.path
import json
import random
import pickle
contents = "/mnt"
def get_work_list():
    #'服务端自身添加工作队列'
    
    s =[]
    for root, dirs, files in os.walk(contents):
        for name in files:
            s.append(os.path.join(root, name))
    end_list = []
    try:
        with open(contents+'/done_list.json', 'r') as r:
            done_list = json.load(r)

        
    except FileNotFoundError:
        print("donelist is not exist")
        done_list = []
        with open(contents+'/done_list.json', 'w') as f:
            f.write(json.dumps(done_list))
        
    for line in s:
    #未修复的flv文件，追加到end_list中
        if (".flv" in line) and (line not in done_list):
            end_list.append(line)
    print_list=end_list[:3]
    for i in print_list:
        print(i)
    print(colored(("	未添加meta数据的flv文件数 =  " + str(len(end_list))),"cyan"))

    #判断临时目录是否存在
    if os.path.isdir(contents+"/_temp"):
        pass
    else:
        os.mkdir(contents+"/_temp")
        print("临时目录已建立")
        
    return end_list

def remove_temp_files():
    del_list = os.listdir(contents + "/_temp")
    for f in del_list:
        file_path = os.path.join(contents + "/_temp"  ,f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        time.sleep(1)
    print("temp files removed.")
        


import signal#

def myHandler(signum, frame):
    print("receeived: ", signum)
    #remove_temp_files()
    print("========")
    
signal.signal(signal.SIGTERM, myHandler)



# global IP2_enable
#print('   server initiateing...')
IP_str = server_addr
port_int = server_port

IP2_enable = 0
if IP2_enable ==0:# 不启动第二ip
    IP_str2 = '192.168.10.78'
    port_int2 = 5001


authkey_str = authkey_

work_queue =  queue.Queue()  # 发送任务的队列:
done_queue = queue.Queue() # 接收结果的队列:

task_queue2 =  queue.Queue()  # 发送任务的队列2:
result_queue2 = queue.Queue() # 接收结果的队列2:

#共享的密码字典
password_dict = {}
password_dict['target'] = "default"
password_dict['pass'] ={}


for line in open("密码.txt"):
    print(line)
    line2 = line.replace('\n','')
    __temp_pass_dic = password_dict['pass']
    __temp_pass_dic[line2] = 1


def return_pass_dict():
    global password_dict
    return password_dict


shared_value = Value('i',1)

#服务端自身添加工作队列
#file_list  = get_work_list()
#空工作队列
file_list = []


# print("File_list's length  = ",len(file_list))
# print(colored(f"File_list's length  {len(file_list)} ","cyan"))
# for i in file_list:
#     work_queue.put(i)
# print("work_queue's size =  ",work_queue.qsize())



if IP2_enable == 1:
    def return_task_queue2():
        global task_queue2
        return task_queue2  # 返回发送任务队列
    def return_result_queue2 ():
        global result_queue2
        return result_queue2 # 返回接收结果队列


class QueueManager(BaseManager):  # 从BaseManager继承的QueueManager:
    pass
# if IP2_enable ==1:
class QueueManager2(BaseManager):  # 从BaseManager继承的QueueManager:
    pass


# windows下运行
def return_work_queue():
    global work_queue
    return work_queue  # 返回发送任务队列
def return_done_queue ():
    global done_queue
    return done_queue # 返回接收结果队列


def return_shared_value():
    global shared_value
    return shared_value


def update_done_list(_appenedix_str):

    
    try:
        with open(contents+'/done_list_temp.json', 'r') as r:
            done_list = json.load(r)
    except:
        return 1
    #for i in _appenedix_list:
    #    done_list.append(i)
    
    done_list.append(_appenedix_str)
    
    with open(contents+'/done_list_temp.json', 'w') as f:  
        f.write(json.dumps(done_list))
        
    try:
        with open(contents+'/done_list_temp.pik', 'wb') as f:  
            pickle.dump(done_list,f)
    except:
        return 1
    
    return 0 


'''
def get_result2():
    global result2
    global threadLock
    try:
        r = result2.get()
    
        if type(r) == type([]):
            my_style = r[0].split('，。')
            my_style = '\n\t'.join(my_style)
            if r[2] == 0:
                printDarkGray(f'    {r[0]}')
            if r[2] == 1:
                printDarkGreen(f'    {my_style}')
            if r[2] == 2:
                printRed(f'    {r[0]}')
            printDarkYellow(f'                                                          -From {r[1]}')


            #speak
            #print('speaking')
            SpeakThread(threadLock,"myspeak",r[0]).start()



            sys.stdout.flush()
        else:
        
            printDarkWhite(f'        {r}')
            sys.stdout.flush()
    except queue.Empty:
            print('result queue is empty.')
'''

def server_mode():
    '''
    多线程
    无阻塞 版'''
    global result
    global result2
    global shared_value
    
    global threadLock
    print('server mode')
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象,它们用来进行进程间通信，交换对象
    #QueueManager.register('get_task_queue', callable=lambda: task_queue)
    #QueueManager.register('get_result_queue', callable=lambda: result_queue)
    QueueManager.register('get_work_queue', callable=return_work_queue)
    QueueManager.register('get_done_queue', callable=return_done_queue)
    QueueManager.register('get_shared_value', callable=return_shared_value)
    QueueManager.register('get_pass_dict', callable=return_pass_dict)

    # 绑定端口5000, 设置验证码'abc':
    #manager = QueueManager(address=('', 5000), authkey=b'abc')
    # windows需要写ip地址
    manager = QueueManager(address=(IP_str,port_int ), authkey=authkey_str)
    manager.start()  # 启动Queue:
    # 获得通过网络访问的Queue对象:
    task = manager.get_work_queue()
    result = manager.get_done_queue()
    #    for i in range(10):   # 放几个任务进去:
    #        n = random.randint(0, 10000)
    #        print('Put task %d...' % n)
    #        task.put(n)
    # 从result队列读取结果:c
    


    #绑定第二IP


    if IP2_enable == 1:
        QueueManager2.register('get_task_queue', callable=return_task_queue2)
        QueueManager2.register('get_result_queue', callable=return_result_queue2)
        manager2 = QueueManager2(address=(IP_str2,port_int2 ), authkey=authkey_str)
        manager2.start()
        #网络取queue
        task2 = manager2.get_task_queue()
        result2 = manager2.get_result_queue()



    #speak 线程锁
    threadLock = threading.Lock()
    

    #printYellow('以下为返回消息...')
    print(colored(f'等待返回队列...',"yellow")) 

    
    #while 1:
    slot1 = GetResultThread('slot1', result  , threadLock)
    slot1.start()

    
    if IP2_enable == 1:
        slot2 = GetResultThread('slot2', result2  , threadLock)
        slot2.start()
        slot2.join()
        #
        #SpeakThread(threadLock,"myspeak",r[0]).start()
        
        
        
        
        
    slot1.join()
    # 关闭:
    #manager.shutdown()
    print('master exit.')
    





#region 语音播报线程

import threading
import time

#import pyttsx3

class SpeakThread (threading.Thread):
    def __init__(self,lock, threadName, _str):


        threading.Thread.__init__(self)


        self.name = threadName
        self.speak_str = _str
        self.lock = lock


    def run(self):
        #print ("开始线程：" + self.name)
        # 获取锁，用于线程同步
        self.lock.acquire()
        self.speak()
        # 释放锁，开启下一个线程
        self.lock.release()
        #print ("结束线程：" + self.name)

    def speak(self):
        '''
        播报线程 threadName, 播放str， 延迟
        '''
        mystr = str(self.speak_str)
        #print('1')
        #engine = pyttsx3.init()
        #print('2')
        #engine.say(mystr.replace('\n',""))
        #print()
        print ("        speaking at %s" % ( time.ctime(time.time())))

        
        #engine.runAndWait()
        #time.sleep(0.1)
    


class GetResultThread (threading.Thread):
    def __init__(self, _threadName, _result , _threadLock):


        threading.Thread.__init__(self)


        self.name = _threadName
        self.result = _result
        
        self.threadLock = _threadLock
        #self.lock = lock
        
    def run(self):
        #start 自动运行
        #print ("开始线程：" + self.name)
        # 获取锁，用于线程同步
        #self.lock.acquire()
        #self.speak()
        # 释放锁，开启下一个线程
        #self.lock.release()
        #print ("结束线程：" + self.name)
        while 1 :
            try:
                self.get_result()
            except KeyboardInterrupt:
                print("key Interrupt")
                break
                #remove_temp_files()
            except Exception:
                print("Exception")
                break
                #remove_temp_files()

    def get_result(self):
        # try:
        if 1 == 1:
            #print('1')
            r = self.result.get()
            #print('2')
            if type(r) == type(""):
                update_done_list(r)
                print(colored(f'已完成  {r}',"green")  )
                
                
            
            """ 返回类型为列表时， 用于语音播报等 """
            if type(r) == type([]):
                SpeakThread(self.threadLock,"myspeak",r[0]).start()
                #先说

                my_style = r[0].split('，。')
                my_style = '\n\t'.join(my_style)
                if r[2] == 0:
                    #printDarkGray(f'    {r[0]}')
                    print(colored(f'    {r[0]}',"gray") )
                if r[2] == 1:
                    # printDarkGreen(f'    {my_style}')
                    print(colored(f'    {my_style}',"green")  )

                if r[2] == 2:
                    #printRed(f'    {r[0]}')
                    print(colored(f'    {r[0]}',"red")  )
                    
                # printDarkYellow(f'                                                          -From {r[1]}')
                print(colored(f'         -From {r[1]}',"yellow")) 

                #speak
                #print('speaking')
                



                sys.stdout.flush()
            # else:
            
            #     #printDarkWhite(f'        {r}')
            #     print(colored(f'        {r}',"gray")  )
            #     sys.stdout.flush()
        # except KeyboardInterrupt:
        #     print("keyff")
        #     remove_temp_files()
        # except queue.Empty:
        #         print('result queue is empty.')
        # except Exception:
        #     print("exception")
        #     remove_temp_files()
    '''
    def speak(self):
        #
        #播报线程 threadName, 播放str， 延迟
        #
        time.sleep(1)
        #print()
        print ("'speaking' %s" % ( time.ctime(time.time())))
        mystr = str(self.speak_str)
        engine = pyttsx3.init()
        engine.say(mystr.replace('\n',""))
        engine.runAndWait()
    '''




#endregion












if __name__=='__main__':

    try:
        freeze_support()
        #printGreen(f'开启服务器 {IP_str}:{port_int}')
        print(colored(f'开启服务器 {IP_str}:{port_int}',"green"))
        if IP2_enable == 1:
            #printGreen(f'开启服务器 {IP_str2}:{port_int2}')
            print(colored(f'开启服务器 {IP_str2}:{port_int2}',"green"))
        
        
        
    
        server_mode()
    except KeyboardInterrupt:
        #remove_temp_files()
        pass
    except Exception:
        print("in exception")
        
    