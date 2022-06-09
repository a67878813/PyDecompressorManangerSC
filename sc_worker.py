# -*- coding: UTF-8 -*-
# task_worker.py
from distutils.log import error
import os
if os.name == "nt":
    os.system("")
    pass
import time, sys, queue
from multiprocessing.managers import BaseManager

import subprocess
import sys
import threading
from  common.sc_common import *

from random import randint
# from pkg.cmdcolor import *   #windows
from termcolor import colored   #linux


client_name = 'S_'
#print(os.environ)
#name = os.environ.get("USER")

client_name = client_name #+ name



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




#server_addr = '127.0.0.1'
def try_to_be_as_client():
    # printDarkGreen(f'        客户端启动中.. {client_name}')
    print(colored(f'        尝试连接服务端.. {client_name}',"green")  )


    global QueueManager
    global m
    global _work_queue
    global _done_queue
    global shared_value
    global _pass_dict

    # 创建类似的QueueManager:
    class QueueManager(BaseManager):
        pass

    # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
    QueueManager.register('get_work_queue')
    QueueManager.register('get_done_queue')
    QueueManager.register('get_shared_value')
    QueueManager.register('get_pass_dict')

    # 连接到中继服务器:

    print('Connect to server %s...' % server_addr)
    # 端口和验证码注意保持与task_master.py设置的完全一致:

    m = QueueManager(address=(server_addr, server_port), authkey=authkey_)
        # 从网络连接:
    try:
        m.connect()
        print(colored(f'        连接到服务端成功 ',"green")  )
    except TimeoutError:
        print(colored(f'        未找到服务端，将自身作为服务端... ',"red")  )
        
        del QueueManager
        return 0
    except KeyboardInterrupt:
        print('key interrupt')
        exit()
        
        
    # 获取Queue的对象:
    _work_queue = m.get_work_queue()#接受任务队列
    _done_queue = m.get_done_queue()#结果写入
    shared_value = m.get_shared_value()#共享value
    _pass_dict = m.get_pass_dict()#共享字典# 功能不正常
    return 1






# 从task队列取任务,并把结果写入result队列:
contents = "/mnt"
def my_worker00__when_error_return_1():
    """ flv文件index修复 """
    try:
        print('获取工作队列中..5s后超时')
        line = _work_queue.get(timeout=5)
        # printDarkYellow(f'        running task... ')
        print(colored(f'        running task... ',"yellow")  )
        
        print(line)
        sys.stdout.flush()
        
        
        time.sleep(0.5)
        #if type(line)== type(""):

    except queue.Empty:
        # printDarkGreen('task queue is empty. exit')
        print(colored(f'task queue is empty. exit after 5 seconds',"green")  )
        shared_value = 0
        time.sleep(5)
        
        #exit()
        return 1
    except MyException:
        #printDarkGreen('exit,try again agter 410s')
        print(colored(f'task queue is MyException. exit',"green")  )
        time.sleep(410)
    except MyException2:
        #printYellow('terminal end, close after 20s')
        print(colored(f'terminal end, close after 20s',"green")  )
        time.sleep(20)
        return 1
    
    if 1 == 1:
        ctime = os.path.getctime(line)
    #except :
    #    print("c time error")
    #    break
    
    salt_ = randint(10000, 90000)
    print(colored("进行meta注入 = "+str(line),"green"))
    if 1 == 1 :
        _pr1 = subprocess.Popen(["/usr/bin/yamdi","-i",line,"-o",contents+"/_temp/output.tmp_"+str(salt_)],stderr=subprocess.STDOUT,
                                stdout = subprocess.PIPE,  encoding = 'utf-8')
        print("         _pr1 pid = ",  _pr1.pid)
        _result_1 ,_result_2 = _pr1.communicate()
        print(f"len_result_1 = {len(_result_1)}")
        if _result_2 == None:
            print(f"_result_2 is null")
        else:
            print('error::::::::::::::::::::::')
            print(_result_2)
            
        _mediate = _result_1.split('\n')
        for _ in _mediate:
            print(_)
        print(f" -- DONE -- _pr1 pid = {_pr1.pid}")
        print("         --------------------")
    
    time.sleep(2)
    
    if 1 == 1 :
        _pr2 = subprocess.Popen(["mv","-f",contents+"/_temp/output.tmp_"+ str(salt_) ,line],stderr=subprocess.STDOUT,
                                stdout = subprocess.PIPE,  encoding = 'utf-8')
        #print(f"_pr2 pid = {_pr2.pid}")
        # print("         _pr2 pid = ",  _pr2.pid)
        #_pr2.wait()    #等待子进程结束，父进程继续
        
        _result_1 ,_result_2 = _pr2.communicate()
        

        #print("===================")
        print(f"len_result_1 = {len(_result_1)}")
        #print(len(_result_1))
        if _result_2 == None:
            print(f"_result_2 is null")
            
        else:
            print('error::::::::::::::::::::::')
            print(_result_2)
            print(f"_result_2 = {_result_2}")
        
        print(f"_pr2.returncode = {_pr2.returncode}")
        
        
        
        #print(test_result)
        #time.sleep(1)
        _mediate = _result_1.split('\n')
        for _ in _mediate:
            print(_)
        # print("     -1 done")
        print(f" -- DONE -- _pr2 pid = {_pr1.pid}")
        if _pr2.returncode == 1:
            
            print(colored("     mv 错误","red"))
            os.remove(contents+"/_temp/output.tmp_"+ str(salt_))
            print(colored("     temp_file deleted","yellow"))
            print("===================")
            return 0 
        print("===================")


        time.sleep(4)
    try:
        os.utime(line, (ctime,ctime))
    except:
        #print("")
        print(colored("write utime 错误","red"))
        return 0 
    
    
    try:
        _done_queue.put(line,block=True,timeout=10)
    except:
        print("put done_queue error")
        return 0
    
    print(colored("meta注入完成 = "+str(line),"green"))
    


def my_worker01__when_error_return_1():
    """ youtube 单任务多线程下载 """
    try:
        print('获取工作队列中..30s后超时',end= "\r")
        line = _work_queue.get(timeout=30)
        # printDarkYellow(f'        running task... ')
        
        print(colored(f'              running task... ',"yellow")  )
        
        print(line)
        sys.stdout.flush()
        
        
        time.sleep(0.5)
        #if type(line)== type(""):

    except queue.Empty:
        # printDarkGreen('task queue is empty. exit')
        print(colored(f'task queue is empty. retry after 30 seconds',"green") ,end = '\r' )
        shared_value = 0
        time.sleep(30)
        
        #exit()
        return 0
    except MyException:
        #printDarkGreen('exit,try again agter 410s')
        print(colored(f'task queue is MyException. exit',"green")  )
        time.sleep(410)
    except MyException2:
        #printYellow('terminal end, close after 20s')
        print(colored(f'terminal end, close after 20s',"green")  )
        time.sleep(20)
        return 1
    


    
    salt_ = randint(10000, 90000)
    print(colored("开始下载 = "+str(line),"green"))
    if 1 == 1 :
        
        """  
        youtube-dl -o '/mnt/youtube//%(title)s.%(ext)s' -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'   --proxy "socks5://192.168.2.27:2099" 'https://www.youtube.com/watch?v=3PcIJKd1PKU&ab_channel=xmdi'  --cookies /mnt/youtube.com_cookies.txt 
        """
        _directory = r'/mnt/youtube/test/%(title)s.%(ext)s'
        _format = r'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        _proxy = r'https://192.168.2.27:3334'
        _address = 'https://www.youtube.com/watch?v=3PcIJKd1PKU&ab_channel=xmdi'
        _cookies = r"/mnt/youtube.com_cookies.txt"
        
        _pr1 = subprocess.Popen(["/usr/local/bin/youtube-dl","-o",_directory,
                                "-f",_format,
                                "--proxy",_proxy,
                                line,
                                "--cookies", _cookies,
                                "--external-downloader","aria2c",
                                "--external-downloader-args","-x16 -k 1M"
                                ],
                                stderr=subprocess.STDOUT,stdout = subprocess.PIPE,  encoding = 'utf-8')
        print("         _pr1 pid = ",  _pr1.pid)
        #实时显示输出
        for _inst_print in iter(_pr1.stdout.readline, b'\r'):
            print(_inst_print,end = "")
            if not subprocess.Popen.poll(_pr1) is None:
                if _inst_print == "":
                    break


        #print(subprocess.Popen.poll(_pr1))



        _result_1 ,_result_2 = _pr1.communicate()
        print(f"len_result_1 = {len(_result_1)}")
        if _result_2 == None:
            print(f"_result_2 is null")
        else:
            print('error::::::::::::::::::::::')
            print(_result_2)
            
        _mediate = _result_1.split('\n')
        for _ in _mediate:
            print(_)

            
        print(f" -- DONE -- _pr1 pid = {_pr1.pid}")
        print("         --------------------")
    
    time.sleep(2)
    """ 不执行后续操作  """
    if 1 == 0 :#
        _pr2 = subprocess.Popen(["mv","-f",contents+"/_temp/output.tmp_"+ str(salt_) ,line],stderr=subprocess.STDOUT,
                                stdout = subprocess.PIPE,  encoding = 'utf-8')
        #print(f"_pr2 pid = {_pr2.pid}")
        # print("         _pr2 pid = ",  _pr2.pid)
        #_pr2.wait()    #等待子进程结束，父进程继续
        
        _result_1 ,_result_2 = _pr2.communicate()
        

        #print("===================")
        print(f"len_result_1 = {len(_result_1)}")
        #print(len(_result_1))
        if _result_2 == None:
            print(f"_result_2 is null")
            
        else:
            print('error::::::::::::::::::::::')
            print(_result_2)
            print(f"_result_2 = {_result_2}")
        
        print(f"_pr2.returncode = {_pr2.returncode}")
        
        
        
        #print(test_result)
        #time.sleep(1)
        _mediate = _result_1.split('\n')
        for _ in _mediate:
            print(_)
        # print("     -1 done")
        print(f" -- DONE -- _pr2 pid = {_pr1.pid}")
        if _pr2.returncode == 1:
            
            print(colored("     mv 错误","red"))
            os.remove(contents+"/_temp/output.tmp_"+ str(salt_))
            print(colored("     temp_file deleted","yellow"))
            print("===================")
            return 0 
        print("===================")


        time.sleep(4)

    
    
    try:
        _done_queue.put(line,block=True,timeout=10)
    except:
        print("put done_queue error")
        return 0
    
    
    
    print(colored("下载完成 = "+str(line),"green"))
    



def my_worker02__when_error_return_1():
    import time
    import sys
    """ 单文件夹密码解压 """
    try:
        print('获取工作队列中..30s后超时',end= "\r")
        line = _work_queue.get(timeout=30)
        # printDarkYellow(f'        running task... ')
        
        print(colored(f'              running task... ',"yellow")  )
        
        print(line)
        sys.stdout.flush()
        
        
        time.sleep(0.5)
        #if type(line)== type(""):

    except queue.Empty:
        # printDarkGreen('task queue is empty. exit')
        print(colored(f'task queue is empty. retry after 30 seconds',"green") ,end = '\r' )
        shared_value = 0
        time.sleep(30)
        
        #exit()
        return 0
    except MyException:
        #printDarkGreen('exit,try again agter 410s')
        print(colored(f'task queue is MyException. exit',"green")  )
        time.sleep(410)
    except MyException2:
        #printYellow('terminal end, close after 20s')
        print(colored(f'terminal end, close after 20s',"green")  )
        time.sleep(20)
        return 1
    


    
    # salt_ = randint(10000, 90000)
    print(colored("开始解压 = "+str(line),"green"))
    
    #======================================
    import os
    if os.name == "nt":
        os.system("")
        pass
    import os.path
    import time
    import sys
    import subprocess
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", help="解压源", type=str,default="default")
    parser.add_argument("--target", help="解压目标", type=str,default="default")
    args = parser.parse_args()

    #contents = "I:\\迅雷下载"
    if args.x == 'default':
        contents = line  #继承服务器下发目录
    else:
        contents = args.x
        
    #print(contents)
    if _pass_dict.get('target') == 'default':
        aim = "default"
    else:
        aim = _pass_dict.get('target')
    
    pass_lists2 =[]
    #pass_lists2.append('哥特动漫王国@倩馨儿')
    delete_list = []

    s =[]
    error_files=[]
    #pass_lists = os.listdir("I:\\迅雷下载")# 密码从此路径的文件夹生成

    #filter_list = ['删除']

    #重命名文件 删除指定词



    pass_lists1 = append_pass_list(os.listdir(contents))

    #print(f"当前目录下密码列表 {pass_lists1}")# 取得当前目录下密码列表
    pass_list2 = []
    pass_list2.extend(_pass_dict.get('pass').keys())
    print("pass_dict")
    print(_pass_dict.get('pass').keys())

    pass_list2.extend(pass_lists1)




    for root, dirs, files in os.walk(contents):
        nested_levels = root.split('\\')
        #if len(nested_levels) ==4:  #限制循环层数
        #    del dirs[:]
        #del dirs[:]将删除列表的内容，而不是用对新列表的引用替换dirs。这样做时，就地修改列表很重要。

        for name in files:
            filename_unfilt =  name[-6:]
            
            if need_unzip(filename_unfilt): #排除已知扩展名
            #if ('7z' in name[-4:] ) or('zip' in name[-4:] )  : #指定扩展名

                #print('         --------')
                END_ = 0
                #print(f'name ={name}')
                #print(f'dirs ={dirs}')
                #print(f'root ={root}')
                a_ = root[len(contents):]
                #print(f'a_ ={a_}')
                a2_ = a_.split('\\')
                if len(a2_) == 1 :#无上级目录时 使用密码
                    pass
                else:
                    if a2_[1] not in pass_list2:
                        pass_list2.append( a2_[1])
                
                
                
                #PASSWORD1_ = PASSWORD1_.replace('星号','*').replace('[左斜]','/').replace('[冒号]',':')
                #print(f'        password ={PASSWORD1_}')
                PASSWORD1_ = pass_list2[0]
                ex_dir = root  +"\\"
                ex_dir = '\"' + ex_dir  + '\"'
                
                
                if aim != "default":#未指定解压目录时，解压到当前目录
                
                
                    #print(root[len(contents):].split('\\')   )
                    #temp_list = root[len(contents):].split('\\')
                    #temp_list[1] = 'test'
                    #print(temp_list)
                    #dd = "\\".join(temp_list)
                    #print(dd)
                    #print(root[len(contents):].split('\\')   )
                    
                    ex_dir = '\"' + aim  +root[len(contents):]  + '\"'#目标文件夹
                FILENAME1_ = root +'\\'+ name
                FILENAME2_ = '\"' + FILENAME1_  + '\"'
                print('         --------')
                print(f'        filename1 ={FILENAME1_}')

                #解压流程





                print(f"总密码列表 {pass_list2}")# 取得当前目录下密码列表
                print("")
                SSTR = ' '.join(["7z.exe","x -aoa ",FILENAME2_,f"-p{PASSWORD1_}",f"-o{ex_dir}",])
                print(f"        SSTR = {SSTR}")
                #continue
                
                obj = subprocess.Popen(SSTR,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                cmd_out,cmd_error = obj.communicate()
                #print("")
                #print("")
                #print("")
                #print(cmd_out)
                #time.sleep(3)
                #print("")
                #print("")
                #print("")
                #print(cmd_error)
                time.sleep(1)
                #print(cmd_out)
                if "Everything is Ok" in cmd_out:
                    #print(f'解压成功      ')
                    print('\033[1;32m' + '解压成功' + '\033[0m')
                    #print(f'删除文件{FILENAME1_}')
                    delete_list.append(FILENAME1_)


                    os.remove(FILENAME1_)#bu 延后删除动作
                    #print("ffffffff",FILENAME1_[-6:])
                    delete_serial_files(FILENAME1_)#系列文件删除
                else:
                    if "系统找不到指定的文件" in cmd_error :#or "Can't open as archive" in cmd_error:
                        continue
                    errot_2 = cmd_error.strip()[:100]
                    print("         EERROO:",errot_2,"   ...")
                    time.sleep(3)
                    #print(f'                文件夹密码失效 ')
                    #print('here')
                    if "Wrong password" in errot_2 or "not open encrypted archive" in errot_2:
                        #print(pass_list2[:10])
                        time.sleep(2)
                        #print('here2')
                        #print(len(pass_list2))

                        for i in pass_list2:
                            if i == PASSWORD1_:#与之前尝试密码相同，略过
                                print('     略过已试密码',end = '\r')
                                continue
                            if aim != "default":
                                #print(root[len(contents):].split('\\')   )
                                temp_list = root[len(contents):].split('\\')
                                temp_list[1] = i.replace('*','星号').replace(':','[冒号]').replace('/','[左斜]')
                                #print(temp_list)
                                dd = "\\".join(temp_list)
                                #print(dd)
                                ex_dir = '\"' + aim  +dd  + '\"'
                                #ex_dir = '\"' + aim  + i.replace('*','星号') + '\"'
                            
                            #print('here4')
                            SSTR = ' '.join(["7z.exe","x -aoa ",FILENAME2_,f"-p{i}",f"-o{ex_dir}",])
                            print(f"                                   尝试密码  {i}                ",end='\r')
                            obj = subprocess.Popen(SSTR,bufsize=1 , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                            cmd_out,cmd_error = obj.communicate()
                            #print(cmd_error)
                            if "Everything is Ok" in cmd_out:
                                print("")
                                print("")
                                print("")
                                print('\033[1;32m' + '解压成功' + '\033[0m')
                                #print(f'解压成功！！！！！！！密码={i}！！！！！！！！')
                                with open(FILENAME1_+f"成功密码{i.replace('*','星号').replace('/','[左斜]').replace(':','[冒号]')}.txt",mode="w",encoding="utf-8") as f:  #写文件,当文件不存在时,就直接创建此文件
                                    pass
                                #print(f'删除文件{FILENAME1_}')
                                delete_list.append(FILENAME1_)
                                
                                
                                #print("ffffffff",FILENAME1_[-10:])
                                #print("")
                                delete_serial_files(FILENAME1_)

                                os.remove(FILENAME1_)
                                END_ =1
                                print('')
                                time.sleep(1)
                                break
                            # elif 1== 1 :
                            #     print(cmd_error)
                            #     print('==================')
                            #     time.sleep(10)
                            # 报错信息兼容 21.09
                            elif  "ERROR: Can not delete output file" in cmd_error  or "ERROR: Cannot delete output file" in cmd_error:
                                print("")
                                print("")
                                print(f"                解压失败 解压文件名与压缩包相同，已尝试重命名此文件（增加_x后缀")
                                append_filename_(FILENAME1_)
                                time.sleep(1)
                                #error_files.append(FILENAME1_)
                                break


                            else:
                                pass
                        #密码组均尝试了一遍
                        if END_ == 1:
                            continue #下一文件
                        if END_ == 0:#尝试无密码解压
                            print("")
                            print("")
                            
                            SSTR = ' '.join(["7z.exe","x -aoa ",FILENAME2_,f"-o{ex_dir}",])
                            #print(f"                                 尝试无密码解压                ",end='\r')
                            obj = subprocess.Popen(SSTR,bufsize=1 , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                            cmd_out,cmd_error = obj.communicate()
                            #print(cmd_error)
                            if "Everything is Ok" in cmd_out:
                                print('\033[1;32m' + '解压成功' + '\033[0m')
                                #print(f'解压成功')
                                #print(f'！！！！！！！！无密码！！！！！！！！')
                                with open(FILENAME1_+f"无密码.txt",mode="w",encoding="utf-8") as f:  #写文件,当文件不存在时,就直接创建此文件
                                    pass
                                #print(f'删除文件{FILENAME1_}')
                                delete_list.append(FILENAME1_)
                                os.remove(FILENAME1_)
                                continue##下一文件
                            else:
                                print("")
                                print("")
                                print("")
                                print(f"                ")
                                error_files.append(FILENAME1_)
                                continue#下一文件
                        #print("此行")

                    #解压文件名与压缩包相同时报错处理 同名错误
                    # 报错信息兼容 21.09
                    elif  "ERROR: Can not delete output file" in cmd_error  or "ERROR: Cannot delete output file" in cmd_error:

                        #print("")
                        #print("")
                        print("")
                        print(f"                解压失败 解压文件名与压缩包相同，已尝试重命名此文件（增加_x后缀")
                        append_filename_(FILENAME1_)
                        time.sleep(1)
                        continue#下一文件
                    
                    #其他报错处理


    print('===end=====未解压文件如下====================')
    #print('      未解压文件如下')
    for i in error_files:
        print(i)
    time.sleep(1)
    if len(error_files)>=1:
        #有未解压文件 放入_work_queue继续处理
        #_work_queue.put(line,block=True,timeout=10)
        out_list = get_all_unziped_sub_folder_with_IN_list(error_files)
        for _k in out_list:
            _work_queue.put(_k,block=True,timeout=2)
            print(f' re_puted {_k} \n')

    #======================================

    #常规工作结束 方入完成queue
    try:
        _done_queue.put(line,block=True,timeout=10)
    except:
        print("put done_queue error")
        return 0
    
    
    
    print(colored("woker任务完成 = "+str(line),"green"))
    print('===============')
    print('')
    time.sleep(1)
    


#==========================================================
print(__name__)
if __name__ == '__main__' :
    # if 1 ==0:
    if try_to_be_as_client() ==1 :
        #do clients
        # exit()
        print("i'm client")
        while 1:
            #重复worker02工作
            if my_worker02__when_error_return_1() :
                #错误处理
                break
            
        # 处理结束:


        print('worker exit. exit after 10 seconds')
        time.sleep(2)
        exit()
    else:
        print('need server, exit after 5 seconds.')
        print('i am server')
        #server&client多线程多进程混用会报错，
        # 可能由于window spawn机制 及对__name__ == '__main__' 处理 与linux不同。 多__name__ == __mp_main__ ?
        # 故分开worker /server

        time.sleep(5)
        exit()