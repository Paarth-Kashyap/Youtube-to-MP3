import tkinter as tk
from music import *


###########################################
#save class Tk
root=tk.Tk()
#title of window
root.title("Youtube to Music Downlader")
#size of window
root.geometry("700x400")
#background colour
root.config(bg="#152b3d") 
root.iconbitmap("music.ico") #icon 
root.resizable(False, False) #not resizable 
#info icon
info=tk.PhotoImage(file="info.png")
#download icon
down=tk.PhotoImage(file="download.png")
###########################################

#clearing place holder text
def clear(e):
  #delete text if that is entrySong
  if entrySong.get() =="Enter Song Title":entrySong.delete(0,"end")
  
#clear listbox
def clear_box():
  listSongs.delete(0,'end')  

#adding songs to listbox
def add_song():
  #if specific text in entry dont add to listbox
  if entrySong.get()=="Enter Song Title":pass
  #if no text in entry dont add to listbox
  elif entrySong.index("end")==0:pass
  else:
    listSongs.insert("end",entrySong.get()) #adds to listbox
    entrySong.delete(0,"end") #erase textbox text after input
#adds to listbox using enter key
def add_enter(e):
     add_song()
#deleting songs from listbox
def delete_song():
  #if listbox empty dont do anything
  if listSongs.index("end")==0:pass
  else:listSongs.delete(listSongs.curselection()) #deletes the entry that is selected
#download button action
def download_song():
  songs=[] 
  #adds every value from list box to list
  for i in listSongs.get(0,"end"):songs.append(i) 
  #if list empty dont download
  if len(songs)==0:pass
  else:
    Music.musicLoop(songs)
    
#output button fucntion
def show_song():    
  result=[]
  result.append(Music.output())
  print(result)
  
  #label text changes depending on songs download status
  # result_label.config(text=result)
  # result_label.place(x=10,y=250) #location of label
      
#show label method (instructions)
def hover(e):
  inst["bg"]="#5c5c5c" #while hover bg colour
  instruc_label.config(text="Enter songs you wish to download from youtube as such:\nsong title-artist\n\nDo Not Interfere After Clicking Download") #label output
#hide label method (instructions) 
def notHover(e):
  inst["bg"]="#152b3d" #while not hover bg colour
  instruc_label.config(text="") #no text
######################################################3

#title label
label=tk.Label(root, text="Music Downloader",bg='#152b3d',fg="#ffffff",font=('Comic Sans MS',40))
label.place(x=25,y=50) #location of title
#listbox label
listLabel=tk.Label(root,bg="#152b3d",fg="#ffffff",font=('Comic Sans MS',20),text="Chosen Songs",width=11)
listLabel.place(x=510,y=5) #location of listbox title
#info btn
inst=tk.Label(root,text='Instructions',image=info,pady=5,padx=5,font=("Comic Sans Ms",10),width=20,bg="#152b3d",cursor="hand2")
inst.place(x=10,y=10) #location of button
inst.bind("<Enter>", hover) #bind hover method if "enter"
inst.bind("<Leave>", notHover) #bind notHover method if "leave"
#instruction lbl
instruc_label=tk.Label(root,text="",bg="#152b3d",fg="#ff0000",font=('Comic Sans MS',12))
instruc_label.place(x=40,y=300) #location of label
#result label of songs downloaded
result_label=tk.Label(root,text="",bg="#152b3d",fg="#ff0000",font=('Comic Sans MS',12))
result_label.place(x=40,y=300) #location of label)
#Listbox
listSongs= tk.Listbox(root,bg="#5c5c5c",fg="#ffffff",font=("Comic Sans Ms",15),justify="left",width=15,height=10,cursor="hand2")
listSongs.place(x=510,y=50) #location of listbox


#Entry box
entrySong= tk.Entry(root,fg="#ffffff",bg="#5c5c5c",font=("Comic Sans Ms",15),justify="center",width=30)
entrySong.insert(0,"Enter Song Title") #placeholder text
entrySong.bind("<Button-1>",clear) #bind clear method
entrySong.bind("<Return>",add_enter)


entrySong.place(x=50,y=150) #location of entry box
#add button
addSong=tk.Button(root, text="Add",pady=5,padx=5,command=add_song,font=("Comic Sans Ms",10),width=18,cursor="hand2")
addSong.place(x=50,y=190) #location of button
#delete button
deleteSong=tk.Button(root,bg="#5c5c5c", fg='#ffffff', padx=8,text="Delete",command=delete_song,font=("Comic Sans Ms",10),width=7,cursor="hand2")
deleteSong.place(x=510,y=350) #location of button
#clear button
deleteSong=tk.Button(root,bg="#5c5c5c", fg='#ffffff', padx=8,text="Clear All",command=clear_box,font=("Comic Sans Ms",10),width=7,cursor="hand2")
deleteSong.place(x=615,y=350) #location of button
#download button
download=tk.Button(root,text="Download All",pady=5,padx=5,command=download_song,font=("Comic Sans Ms",10),width=18,cursor="hand2")
download.place(x=252,y=190) #location of button
#music download status button
status=tk.Button(root,image=down,pady=5,padx=5,width=30,bg="#152b3d",bd=0,command=show_song,cursor="hand2")
status.place(x=40,y=10) #location of button

##################################################

root.mainloop()