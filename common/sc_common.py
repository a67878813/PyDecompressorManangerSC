# -*- coding: UTF-8 -*-

import time
import os
server_addr = '127.0.0.1'
server_port = 5010
authkey_ =b'abcd'


filter_list = ['删除']
#重命名文件 删除指定词
def rename_filter_filenames_with_usercheck(contents):
    """ 过滤指定目录内所有文件名 ，去除词库内词语"""
    _s_list = []
    _d_list = []
    for root, dirs, files in os.walk(contents):
        nested_levels = root.split('\\')
        #if len(nested_levels) ==4:  #限制循环层数
        #    del dirs[:]
        #del dirs[:]将删除列表的内容，而不是用对新列表的引用替换dirs。这样做时，就地修改列表很重要。

        for name in files:
            filename_unfilt =  name[-4:]
            
            if need_unzip(filename_unfilt): #排除已知扩展名
            #if ('7z' in name[-4:] ) or('zip' in name[-4:] )  : #指定扩展名

                #print('         --------')
                END_ = 0
                #print(f'name ={name}')
                for _i in filter_list:
                    if _i in name:
                        source_ = root + '\\' + name
                        destnation_ = root + '\\' + name.replace(_i, '')
                        #os.rename( source_  ,  destnation_  )
                        _s_list.append(source_)
                        _d_list.append(destnation_)
                        #print(f'        rename destnation_ ={destnation_}')
    if len(_s_list ) != 0 :
        for i in range(len(_s_list)):
            print(_s_list[i])
        comm_= input('check to change names list, y/n  \n')
        if comm_ =='y':
            for i in range(len(_s_list)):
                os.rename(_s_list[i], _d_list[i])
            print('done')

def append_filename_(_filename):
    _dest = _filename + "_x"
    print("修改文件名")
    print(f"_dest =  {_dest}")
    time.sleep(2)

    os.rename(_filename, _dest)
    


def append_pass_list(pass_lists):
    _temp_list = []
    for i in pass_lists:
        j  = i.replace('星号','*').replace('[左斜]','/').replace('[冒号]',':')
        if "[]" in j:
            _temp_list.append(j.split('[]')[0].strip())
            
        if "或者" in j:
            _temp_list.append(j.split("或者")[0].strip())
            _temp_list.append(j.split("或者")[1].strip())
        if "或" in j and "或者" not  in j:
            _temp_list.append(j.split("或")[0].strip())
            _temp_list.append(j.split("或")[1].strip())
        if " " in j:
            _temp_list.append(j.split(" ")[0].strip())
            _temp_list.append(j.split(" ")[1].strip())
        _temp_list.append(j.replace(' ',''))
    # for i in pass_lists:
    #     j  = i.replace('星号','*')#.replace('&','^&')
    #     pass_lists2.append(j)
        
    return _temp_list

#append_pass_list(os.listdir("Z:\\b\\0020191211"))
#append_pass_list(os.listdir("B:\\密码"))
#append_pass_list(os.listdir("I:\\迅雷下载"))
#if contents != 'I:\\迅雷下载':

if 1== 0:
    append_pass_list(os.listdir(contents))

    print(pass_lists2)# 取得当前目录下密码列表



def delete_serial_files(_filename):
    #time.sleep(3)
    #print("")
    #print(f" filename = {_filename}")
    time.sleep(3)
    if _filename[-2:] == "01":
        #询问是否删除系列文件  001 002 003..
        if os.path.exists(_filename[:-1]+ '2'):
            print('存在可能的系列文件，是否删除====以下为当前目录文件列表')
            #print("")
            time.sleep(3)

            _root_dir = '\\'.join(_filename.split("\\")[:-1])
            for f in os.listdir(_root_dir):
                print(f"                filename = {f}")


            #criteria_ = input("存在可能的系列文件，是否删除 y /  else is not  ?")
            criteria_ = 'y'
            if criteria_ != 'y' :
                return 0

        for j in range(2,60):
            try:
                if j  < 10 :
                    os.remove(_filename[:-1] + str(j)  )
                else:
                    os.remove(_filename[:-2] + str(j)  )
            except:
                print(f"                 删除停止于 {j}")
                break
    if _filename[-6:] == "t1.rar":
        for j in range(2,99):
            try :
                if j  <= 10 :
                    os.remove(_filename[:-6] + "t" +  str(j)  + ".rar" )
                else:
                    os.remove(_filename[:-6] + "t" +  str(j)   + ".rar" )
            except:
                print(f"                 删除停止于 {j}")
                break
    if _filename[-6:] == "01.rar":
        for j in range(2,99):
            try :
                if j  <= 10 :
                    os.remove(_filename[:-6] + "0" +  str(j)  + ".rar" )
                else:
                    os.remove(_filename[:-6] +  str(j)   + ".rar" )
            except:
                print(f"                 删除停止于 {j}")
                break
    return 0 


def delete_serial_files_with_human_supervisor(_filename):
    #人工确认 #放subpopen 内不起作用
    if _filename[-2:] == "01":
        #询问是否删除系列文件  001 002 003..
        if os.path.exists(_filename[:-1]+ '2'):
            print('存在可能的系列文件，是否删除====以下为当前目录文件列表')

            _root_dir = '\\'.join(_filename.split("\\")[:-1])
            for f in os.listdir(_root_dir):
                print(f"filename = {f}")


            criteria_ = input("存在可能的系列文件，是否删除 y /  else is not  ?")
            #criteria_ = 'y'
            if criteria_ != 'y' :
                return 0

        for j in range(2,60):
            try:
                if j  < 10 :
                    os.remove(_filename[:-1] + str(j)  )
                else:
                    os.remove(_filename[:-2] + str(j)  )
            except:
                print(f"                 删除停止于 {j}")
                break
    if _filename[-6:] == "t1.rar":
        for j in range(2,99):
            try :
                if j  <= 10 :
                    os.remove(_filename[:-6] + "t" +  str(j)  + ".rar" )
                else:
                    os.remove(_filename[:-6] + "t" +  str(j)   + ".rar" )
            except:
                print(f"                 删除停止于 {j}")
                break
    if _filename[-6:] == "01.rar":
        for j in range(2,99):
            try :
                if j  <= 10 :
                    os.remove(_filename[:-6] + "0" +  str(j)  + ".rar" )
                else:
                    os.remove(_filename[:-6] +  str(j)   + ".rar" )
            except:
                print(f"                 删除停止于 {j}")
                break
    return 0 


def need_unzip(_name):
    name_ = _name.lower()
    if "ding" in name_:#downloading
        return 0
    if "rent" in name_:#torrent
        return 0
    if "mkv" in name_:
        return 0
    if "flv" in name_:
        return 0
    if "ssa" in name_:
        return 0
    if "wmv" in name_:
        return 0    
    if "mts" in name_:
        return 0    
    if "jfif" in name_:
        return 0    
    if "tiff" in name_:
        return 0  
    if ".me" in name_:
        return 0  
    if ".doc" in name_:
        return 0  
    if "3gp" in name_:
        return 0    
    if "wav" in name_:
        return 0    
    if ".csv" in name_:
        return 0    
    if ".log" in name_:
        return 0    
    if "rmvb" in name_:
        return 0    
    if "m4v" in name_:
        return 0    
    if "jpeg" in name_:
        return 0    
    if "docx" in name_:
        return 0    
    if "ini" in name_:
        return 0    
    if "htm" in name_:
        return 0    
    if "psd" in name_:
        return 0    
    if "mp4" in name_:
        return 0
    if "mp3" in name_:
        return 0
    if "jpg" in name_:
        return 0
    if ".cc" in name_:
        return 0
    if "jpeg" in name_:
        return 0
    if "webp" in name_:
        return 0
    if "ass" in name_:
        return 0
    if "heic" in name_:
        return 0
    if "png" in name_:
        return 0
    if "txt" in name_:
        return 0
    if ".ts" in name_:
        return 0
    if "avi" in name_:
        return 0
    if "mpg" in name_:
        return 0
    if "mov" in name_:
        return 0
    if "webm" in name_:
        return 0
    if "mobi" in name_:
        return 0
    if "srt" in name_:
        return 0
    if "bmp" in name_:
        return 0
    if "gif" in name_:
        return 0
    if "url" in name_:
        return 0
    if "lnk" in name_:
        return 0
    if "pdf" in name_:
        return 0
    if ".db" in name_:
        return 0
    if ".sh" in name_:
        return 0
    if ".py" in name_:
        return 0
    if ".exe" in name_:
        return 0
    if ".pyo" in name_:
        return 0
    if ".pyx" in name_:
        return 0
    if ".pyi" in name_:
        return 0
    if ".pyd" in name_:
        return 0
    if ".pyd" in name_:
        return 0
    if "rpyc" in name_:
        return 0
    if "rpy" in name_:
        return 0
    if "ttf" in name_:
        return 0
    if "pymc" in name_:
        return 0
    if "py" in name_:
        return 0
    if "px" in name_:
        return 0
    if "dll" in name_:
        return 0
    if "fest" in name_:
        return 0
    if "dat" in name_:
        return 0
    if "so" in name_:
        return 0
    if "egg" in name_:
        return 0
    if "js" in name_:
        return 0
    if "css" in name_:
        return 0
    if "ogg" in name_:
        return 0
    if "pak" in name_:
        return 0
    if "ject" in name_:
        return 0
        return 0
    if "vbs" in name_:
        return 0
    if "save" in name_:
        return 0
    if "rpg" in name_:
        return 0
    if "rpa" in name_:
        return 0
    if "rent" in name_:#torrent
        return 0
    if "flac" in name_:#torrent
        return 0
    if "cue" in name_:#torrent
        return 0
    if "log" in name_:#torrent
        return 0
    if "m3u" in name_:#torrent
        return 0
    if "wav" in name_:#torrent
        return 0
    if "ape" in name_:#torrent
        return 0
    if "tak" in name_:#torrent
        return 0
    if "jp2" in name_:#torrent
        return 0
    if "ding" in name_:#torrent
        return 0
    if "mka" in name_:#torrent
        return 0
    if "tif" in name_:#torrent
        return 0
    if "ttc" in name_:#torrent
        return 0
    if "ttf" in name_:#torrent
        return 0
    if "rm" in name_:#torrent
        return 0
    if "otf" in name_:#torrent
        return 0
    if "smi" in name_:#torrent
        return 0
    if "dts" in name_:#torrent
        return 0
    return 1



def get_all_unziped_sub_folder(contents):
    # in folder
    #return folder list
    #遍历全部文件夹，剪枝 母文件夹相同路径
    #查找使用字典key   O log(n)? O(n)?
    need_re_unzip_folders = {}
    for root, dirs, files in os.walk(contents):#遍历
        nested_levels = root.split('\\')
        # if len(nested_levels) ==   >= 4:  #限制循环层数
        #     del dirs[:] 

        for name in files:

            filename_unfilt =  name[-6:]
            # print(name)
            #if ('7z' in name[-4:] ) or('zip' in name[-4:] )  : #指定扩展名
            if need_unzip(filename_unfilt): #排除已知扩展名，
                #需要解压的文件继续如下逻辑

                #print(root)
                #print(dirs)
                #print(files)
                #print(name)
                #_temp_dir = name.split('\\')[:-1].join()
                if os.path.isdir(root):
                    if need_re_unzip_folders.get(root) ==None:#字典没有对应key(目录内有未解压完毕文件)
                        need_re_unzip_folders[root] = 1 #增加key
                    else:
                        pass
                    #print(root)
                    #print(type(root))
                    #print(len(root.split('\\')))
                    #删除字典内的父文件夹key
                    for i in range(len(root.split('\\'))-1  ): #剪枝
                        # print(i)
                        """  
                        1
                            B:\baidu\秒\谢谢谢谢\我的资源新2\套图4
                            2
                            B:\baidu\秒\谢谢谢谢\我的资源新2
                            3
                            B:\baidu\秒\谢谢谢谢
                            4
                            B:\baidu\秒
                            5
                            B:\baidu
                            6
                        
                        """
                        # print('\\'.join(root.split('\\')[:-i] )   )
                        __temp_key ='\\'.join(root.split('\\')[:-i] )
                        if need_re_unzip_folders.get(__temp_key ) !=None:
                            #字典内有父文件夹，删除对应key
                            need_re_unzip_folders.pop(__temp_key)


    #print("整理好的待解压目录，仅保留最深层待解压目录")
    return_list = []
    for i in need_re_unzip_folders.keys():
        #print(i)
        return_list.append(i)
    return return_list
#print(need_re_unzip_folders.keys())
            # time.sleep(0.1)




def get_all_unziped_sub_folder_with_IN_list(_inlist):
    # in file list
    #return folder list
    #list输入的遍历及剪枝
    need_re_unzip_folders = {}
    __in_temp_list = []
    for __i in _inlist:
        __temp_04 = '\\'.join(__i.split('\\')[:-1]) 
        __in_temp_list.append(__temp_04)

    __middle_temp_list = []
    converted_set = set(__in_temp_list)
    for __j in converted_set:
        #列表合并  -》 扁平列表
        __middle_temp_list.extend(get_all_unziped_sub_folder(__j))
    
    __end_temp_set = set(__middle_temp_list)
    __end_temp_list = list(__end_temp_set)

    return __end_temp_list
    
#print(need_re_unzip_folders.keys())
            # time.sleep(0.1)
