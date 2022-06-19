from os import access
from turtle import bgcolor
from sympy import mod_inverse
import math
import tkinter as tk
from tkinter import CENTER, Spinbox, Variable, ttk


# class from Tk
cipher = tk.Tk()

# -------------- function -------------
def caesar_encode(text,key):
  result = ""
  for i in range(len(text)):
      char = text[i]
      if (char == ' '):
        result += char
      elif (char.isupper()):
          result += chr((ord(char) + key - 65) % 26 + 65)
      else:
          result += chr((ord(char) + key - 97) % 26 + 97)
      f1cipher_text.set(result)

def caesar_decode(text,key):
  result = ""
  for i in range(len(text)):
      char = text[i]
      if (char == ' '):
        result += char          
      elif (char.isupper()):
          result += chr(((ord(char) - key) - 65) % 26 + 65)
      else:
          result += chr(((ord(char) - key) - 97) % 26 + 97)
      f1plain_text.set(result)

def multiplicative_encode(text,key):
  result = ""
  for i in range(len(text)):
      char = text[i]
      if (char == ' '):
        result += char 
      elif math.gcd( 26,key) == 1:
        if (char.isupper()):
          
            result += chr(((ord(char) - 65) * key ) % 26 + 65)
        else:
            result += chr(((ord(char) - 97) * key ) % 26 + 97)

  f2cipher_text.set(result)

def multiplicative_decode(text,key):
  result = ""
  key = mod_inverse(key,26)
  for i in range(len(text)):
      char = text[i]
      if (char == ' '):
        result += char 
      elif (char.isupper()):
        
          result += chr(((ord(char) - 65) * key ) % 26 + 65)
      else:
          result += chr(((ord(char) - 97) * key ) % 26 + 97)
  f2plain_text.set(result)

def affine_encode(text, key1,key2):
  result = ""
  for i in range(len(text)):
      char = text[i]
      if (char == ' '):
        result += char 

      elif (char.isupper()):
        
          result += chr(((key1 * (ord(char) - 65) + key2)) % 26 + 65)
      else:
          result += chr(((key1 * (ord(char) - 97) + key2)) % 26 + 97)

  f3cipher_text.set(result)

def affine_decode(text, key1, key2):
  result = ""
  key1 = mod_inverse(key1,26)
  for i in range(len(text)):
      char = text[i]
      if (char == ' '):
        result += char 

      elif (char.isupper()):
          result += chr((  key1 * ((ord(char) - 65) - key2)) % 26 + 65)
      else:
          result += chr((  key1 * ((ord(char) - 97) - key2)) % 26 + 97)

  f3plain_text.set(result)  


# -------------- variable --------------
f1plain_text = tk.StringVar()
f1cipher_text = tk.StringVar()
f1sp = tk.IntVar()
f1sp.set(3)

f2plain_text = tk.StringVar()
f2cipher_text = tk.StringVar()
f2sp = tk.IntVar()

f2sp.set(7)

f3plain_text = tk.StringVar()
f3cipher_text = tk.StringVar()
f3sp_1 = tk.IntVar()
f3sp_2 = tk.IntVar()

# -------------- color --------------
primary_color = '#ff8822'
secandry_color = 'black'#'#00b1d1'
bg_frame_color = 'white'
bg_text_color = 'white'
fg_text_color = 'black'

# ----------- font style ----------
bold = 'bold'
calibre = 'calibre'
font_size_10=10
font_size_20=20

# configration
# resize config (width x height + left + top)
cipher.geometry("540x260+50+50")
# control size window (width, height)
cipher.resizable(False,False)
# cipher.minsize()
# cipher.maxsize()
# title name program
cipher.title("Cypto App")
# config background window
cipher.config(background='white')
# insert icon for my appliction
cipher.iconbitmap('cyptoIcon.ico')
# menu 
menubar = tk.Menu(cipher)
f = tk.Menu(menubar,tearoff=0)
f.add_command(label='Exit',command=cipher.quit)
menubar.add_cascade(label='File',menu=f)
cipher.config(menu=menubar)

notebook = ttk.Notebook(cipher)
notebook.pack()
# ------------- Frame 1 ------------------

f1 = tk.Frame(notebook,width='540',height="240",bg=bg_frame_color)
f1.place(x=0,y=0)
notebook.add(f1,text='Caesar Cipher')

labf1_1 = tk.Label(f1, text='Caesar Cipher',fg=primary_color,bg=bg_text_color,font=(calibre,font_size_20,bold))
labf1_1.place(x=270,y=18,anchor='center')

labf1_2 = tk.Label(f1, text='Plain text: ',fg=secandry_color,bg=bg_text_color)
labf1_2.place(x=185,y=50,anchor='center')

en1_2 = tk.Entry(f1,textvariable=f1plain_text,justify='left',font=10)
en1_2.place(x=270,y=70,anchor='center')

labf1_4 = tk.Label(f1, text='Key: ',fg=secandry_color,bg=bg_text_color)
labf1_4.place(x=180,y=120,anchor='center')

spf1 = Spinbox(f1,textvariable=f1sp,from_ = -25 ,to = 25,font=10,width=10)
spf1.place(x=270,y=120,anchor='center')

labf1_3 = tk.Label(f1, text='Cipher text: ',fg=secandry_color,bg=bg_text_color)
labf1_3.place(x=190,y=170,anchor='center')

en1_3 = tk.Entry(f1,textvariable=f1cipher_text,justify='left',font=10)
en1_3.place(x=270,y=190,anchor='center')

        
# create button
encrypt_f1 = tk.Button(f1,text="encrypt",fg=fg_text_color,bg=bg_text_color,font=0,height=1,command=lambda: caesar_encode(text=f1plain_text.get(),key=f1sp.get()))
encrypt_f1.place(x=30,y=100)


decrypt_f1 = tk.Button(f1,text="decrypt",fg=fg_text_color,bg=bg_text_color,font=0,height=1,command=lambda: caesar_decode(text=f1cipher_text.get(),key=f1sp.get()))
decrypt_f1.place(x=410,y=100)

# -------------- Frame 2 ---------------
f2 = tk.Frame(notebook,width='540',height="240",bg=bg_frame_color)
f2.place(x=0,y=0)
notebook.add(f2,text='Multiplication Cipher')

labf2_1 = tk.Label(f2, text='Multiplication Cipher',fg=primary_color,bg=bg_text_color,font=(calibre,font_size_20,bold))
labf2_1.place(x=270,y=18,anchor='center')

labf2_2 = tk.Label(f2, text='Plain text: ',fg=secandry_color,bg=bg_text_color)
labf2_2.place(x=185,y=50,anchor='center')

en1_2 = tk.Entry(f2,textvariable=f2plain_text,justify='left',font=10)
en1_2.place(x=270,y=70,anchor='center')

labf2_4 = tk.Label(f2, text='Key: ',fg=secandry_color,bg=bg_text_color)
labf2_4.place(x=180,y=120,anchor='center')

spf2 = Spinbox(f2,textvariable=f2sp,from_ = -25 ,to = 25,font=10,width=10)
spf2.place(x=270,y=120,anchor='center')

labf2_3 = tk.Label(f2, text='Cipher text: ',fg=secandry_color,bg=bg_text_color)
labf2_3.place(x=190,y=170,anchor='center')

en1_3 = tk.Entry(f2,textvariable=f2cipher_text,justify='left',font=10)
en1_3.place(x=270,y=190,anchor='center')

        
# create button
encrypt_f2 = tk.Button(f2,text="encrypt",fg=fg_text_color,bg=bg_text_color,font=0,height=1,command=lambda: multiplicative_encode(text=f2plain_text.get(),key=f2sp.get()))
encrypt_f2.place(x=30,y=100)


decrypt_f2 = tk.Button(f2,text="decrypt",fg=fg_text_color,bg=bg_text_color,font=0,height=1,command=lambda: multiplicative_decode(text=f2cipher_text.get(),key=f2sp.get()))
decrypt_f2.place(x=410,y=100)


# -------------- Frame 3 ---------------
f3 = tk.Frame(notebook,width='540',height="240",bg=bg_frame_color)
f3.place(x=0,y=0)
notebook.add(f3,text='Affine Cipher')

labf3_1 = tk.Label(f3, text='Affine Cipher',fg=primary_color,bg=bg_text_color,font=(calibre,font_size_20,bold))
labf3_1.place(x=270,y=18,anchor='center')

labf3_2 = tk.Label(f3, text='Plain text: ',fg=secandry_color,bg=bg_text_color)
labf3_2.place(x=185,y=50,anchor='center')

en1_2 = tk.Entry(f3,textvariable=f3plain_text,justify='left',font=10)
en1_2.place(x=270,y=70,anchor='center')

labf3_4 = tk.Label(f3, text='Key: ',fg=secandry_color,bg=bg_text_color)
labf3_4.place(x=180,y=120,anchor='center')

spf3_1 = Spinbox(f3,textvariable=f3sp_1,from_ = -25 ,to = 25,font=10,width=2)
spf3_1.place(x=240,y=120,anchor='center')

spf3_2 = Spinbox(f3,textvariable=f3sp_2,from_ = -25 ,to = 25,font=10,width=2)
spf3_2.place(x=290,y=120,anchor='center')

labf3_3 = tk.Label(f3, text='Cipher text: ',fg=secandry_color,bg=bg_text_color)
labf3_3.place(x=190,y=170,anchor='center')

en1_3 = tk.Entry(f3,textvariable=f3cipher_text,justify='left',font=10)
en1_3.place(x=270,y=190,anchor='center')

        
# create button
encrypt_f3 = tk.Button(f3,text="encrypt",fg=fg_text_color,bg=bg_text_color,font=0,height=1,command=lambda: affine_encode(text=f3plain_text.get(),key1=f3sp_1.get(),key2=f3sp_2.get()))
encrypt_f3.place(x=30,y=100)


decrypt_f3 = tk.Button(f3,text="decrypt",fg=fg_text_color,bg=bg_text_color,font=0,height=1,command=lambda: affine_decode(text=f3cipher_text.get(),key1=f3sp_1.get(),key2=f3sp_2.get()))
decrypt_f3.place(x=410,y=100)



def helloCallBack():
   print('hello')
cipher.mainloop()