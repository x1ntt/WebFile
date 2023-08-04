from BrowseFile.Exception import NotIsDirException

import os
import time
import shutil

class FileManage:
    def __init__():
        pass

    @classmethod
    def convertFileSize(cls, size):
        # 定义单位列表
        units = 'Bytes', 'KB', 'MB', 'GB', 'TB'
        # 初始化单位为Bytes
        unit = units[0]
        # 循环判断文件大小是否大于1024，如果大于则转换为更大的单位
        for i in range(1, len(units)):
            if size >= 1024:
                size /= 1024
                unit = units[i]
            else:
                break
        # 格式化输出文件大小，保留两位小数
        return '{:.2f} {}'.format(size, unit)

    @classmethod
    def get_list(cls, path):
        if not os.path.isdir(path):
            raise NotIsDirException(f"访问的不是目录: {path}")

        nodes = os.scandir(path)
        node_list = []
        for node in nodes:
            node_list.append({"name":node.name, "isDir":node.is_dir(), "size":cls.convertFileSize(node.stat().st_size), "mtime":time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(node.stat().st_mtime))})
        return node_list
    
    @classmethod
    def delele(cls, path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        