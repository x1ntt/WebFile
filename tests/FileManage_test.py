import sys
import os
sys.path.append(os.getcwd())

from BrowseFile.FileManage import FileManage

print (FileManage.get_list("/home/st/d/2/BrowseFile/"))