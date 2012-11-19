from server import *
from settings import *
from PIL import Image
import sys,os,PIL


def pic_resizer():
    basewidth = 150
    pic_files = os.listdir(tools.config['Photo_Folder'])
    # loop through image folder
    pic_list = ['png','jpg','PNG','JPG','jpeg','JPEG','bmp','BMP']
    for pic in pic_files:
        for check in pic_list:
            if check in pic:
                img = Image.open(str(tools.config['Photo_Folder']+"/"+pic))
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
                img.save(str(tools.config['Thumbs_Folder']+"/"+pic))
    return True
    
