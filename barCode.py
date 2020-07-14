# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 01:07:03 2020

@author: kach
"""


import barcode
from barcode.writer import ImageWriter

print(barcode.PROVIDED_BARCODES)

from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry('330x220')
root.title('India Post - Barcode generator')


acc=StringVar()
def getAcc(event=None):
    acc=str(entry1.get())
    
    BC = barcode.get_barcode_class('gs1_128') #itf, code39, gs1_128, code128
    BC_img = BC(acc, writer=ImageWriter())
    filename = BC_img.save('barcode', options={"write_text": False,"text": acc+'\n'+acc}) 

    im = Image.open(r"barcode.png") 
    width, height = im.size 
    load = im.crop((10, height/3, width-10, height)) #Left,Top,Right,Bottom


    #load = Image.open(filename)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render) #, height=40)
    img.image = render
    img.place(x=3, y=50)

#account number
Label_0=Label(root, text='Acc No:', width=7, font=("bold",13))
Label_0.place(x=3, y=15)

entry1=Entry(root,width=13, font=("bold",13))
entry1.place(x=80, y=15)

# #Branch
# Label_0=Label(root, text='Acc No:', width=7, font=("bold",13))
# Label_0.place(x=3, y=15)

# entry2=Entry(root,width=13, font=("bold",13))
# entry2.place(x=80, y=15)

# #account type
# Label_0=Label(root, text='Acc No:', width=7, font=("bold",13))
# Label_0.place(x=3, y=15)

# entry3=Entry(root,width=13, font=("bold",13))
# entry3.place(x=80, y=15)


Button(root, text='Generate', width=11, bg='brown', fg='white', command=getAcc).place(x=220,y=15)
root.bind('<Return>',getAcc)

mainloop()




# for c in barcode.PROVIDED_BARCODES:    
#     try:
#         acc=str('0851840442')
#         BC = barcode.get_barcode_class(c) #itf, code39
#         BC_img = BC(acc, writer=ImageWriter())
#         filename = BC_img.save(c, options={"write_text": False,"text": acc}) 
#         print(c)
#     except:
#         print('except ',c)
#         continue



# from PIL import Image 
# # Opens a image in RGB mode 
# im = Image.open(r"barcode.png") 

# width, height = im.size 
# #im1 = im.crop((left, top, right, bottom)) 
# im1 = im.crop((50, height/2, width-50, height)) 

# # Shows the image in image viewer 
# im1.show() 