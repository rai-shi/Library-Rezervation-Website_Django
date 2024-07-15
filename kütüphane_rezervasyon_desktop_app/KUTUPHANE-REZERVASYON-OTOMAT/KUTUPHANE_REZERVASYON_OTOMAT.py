from tkinter import *
from tkinter.font import Font
from tkinter import ttk 

from PIL import ImageTk
import PIL.Image

import os

from functions import *

#color
ktu_blue= "#1f5ba1"
light_grey = "#C6C7CA"
dark_grey= "#282A3A"
success_color ="#7AE070"
fail_color = "#F06767"


#margin options
general_margin_options = {'padx':5, 'pady':5}


root = Tk()
root.title("LIBRARY CHECK IN")
root.state('zoomed')
root.configure(bg=ktu_blue)

root.iconphoto(True, ImageTk.PhotoImage(PIL.Image.open("computer.png")))


# font options
font_button = Font(family = "Helvetica", size = 9)
font_header = Font(family = "Helvetica", size = 25, weight="bold")
font_labelText = Font(family = "Helvetica", size = 15)
font_info = Font(family = "Helvetica", size = 9)

canvas_list = list()

"""
place_forget

geri dönüş mesajlarını dictionaryde toplayabilirsin ve param olarak ulaşabilirsin
ya da hepsini yazar daha sonra istediğini yerleştirebilirsin

en üste db bağlantı kısmı
"""


menubar = Menu(root) 
root.config(menu=menubar) 



databaseMenu = Menu(menubar) 
menubar.add_cascade(label="Rezervasyonlar", menu=databaseMenu)
databaseMenu.add_command(label="Bugün Olan Rezervasyonlar", command=lambda: dbConnection(canvas_list))


databaseMenu = Menu(menubar) 
menubar.add_cascade(label="Kullanıcılar", menu=databaseMenu)
databaseMenu.add_command(label="Kütüphanedeki Kullanıcılar", command=ListUsers)





# homepage widgets

homePage_Button_Canvas = Canvas(root, bg=light_grey)
#homePage_Button_Canvas.place(relx=.5, rely=.5,anchor= CENTER)
# grid(row=0,column=0)
# homePageButtonCanvas.grid_propagate(False) 

# home page button padding options
homepage_button_padx_options = {'padx':100}
homepage_button_pady_options = {'pady':20}

EntryState_Button = Button(homePage_Button_Canvas, text="GİRİŞ", font=font_button, width = 30, height=2, bg= dark_grey, fg="white", command=lambda: openLibEntryState(canvas_list))
EntryState_Button.grid(row=0,column=0, **homepage_button_padx_options, pady=(150,20))

ExitState_Button = Button(homePage_Button_Canvas, text="ÇIKIŞ", font=font_button, width = 30, height=2, bg= dark_grey, fg="white", command = lambda: openLibExitState(canvas_list) )
ExitState_Button.grid(row=1,column=0, **homepage_button_padx_options, **homepage_button_pady_options)

TakeBreakState_Button = Button(homePage_Button_Canvas, text="MOLAYA ÇIKIŞ", font=font_button, width = 30, height=2, bg= dark_grey, fg="white", command= lambda: openLibTakeBreakState(canvas_list) )
TakeBreakState_Button.grid(row=2,column=0, **homepage_button_padx_options, **homepage_button_pady_options)

ReturnBreakState_Button = Button(homePage_Button_Canvas, text="MOLADAN DÖNÜŞ", font=font_button, width = 30, height=2, bg= dark_grey, fg="white", command= lambda: openLibReturnBreakState(canvas_list) )
ReturnBreakState_Button.grid(row=3,column=0, **homepage_button_padx_options, pady=(20,150))



# library entry state page widgets


libEntryState_Canvas = Canvas(root, bg=light_grey)
#libEntryState_Canvas.place(relx=.5, rely=.5,anchor= CENTER)

libEntryState_padx_options = {'padx':100}

libEntryState_header_Text = Label(libEntryState_Canvas, text= "GİRİŞ YAP", font=font_header, bg=light_grey, fg=dark_grey)
libEntryState_header_Text.grid(row=0,column=0, **libEntryState_padx_options, pady=(50,75) )



libEntryState_Email_Frame = Frame(libEntryState_Canvas, width=100, bg=light_grey)
libEntryState_Email_Frame.grid(row=1,column=0, **libEntryState_padx_options, pady=15)

libEntryState_Email_Label = Label(libEntryState_Email_Frame, text = "Email: ", font= font_labelText , bg=light_grey, fg=dark_grey, width=5)
libEntryState_Email_Label.grid(row=0,column=0)

libEntryState_Email_InputBox = Entry(libEntryState_Email_Frame, width=25)
libEntryState_Email_InputBox.grid(row=0,column=1, ipady=3)



libEntryState_Password_Frame = Frame(libEntryState_Canvas, width=100, bg=light_grey)
libEntryState_Password_Frame.grid(row=2,column=0, **libEntryState_padx_options, pady=15)

libEntryState_Password_Label = Label(libEntryState_Password_Frame, text = "Şifre: ", font= font_labelText , bg=light_grey, fg=dark_grey, width=5)
libEntryState_Password_Label.grid(row=0,column=0)

libEntryState_Password_InputBox = Entry(libEntryState_Password_Frame, width=25)
libEntryState_Password_InputBox.grid(row=0,column=1, ipady=3)



Enter_Btn = Button(libEntryState_Canvas, text="Kütüphanedeyim", font=font_button, width = 30, height=2, bg= dark_grey, fg="white", command=lib_Enter)
Enter_Btn.grid(row=3,column=0, **libEntryState_padx_options, pady=20)


EntryState_success_Text = Label(libEntryState_Canvas, text= "İYİ ÇALIŞMALAR DİLERİZ", font= font_info , bg=success_color, fg="white", width=40, height=3)
EntryState_success_Text.grid(row=4,column=0, **libEntryState_padx_options, pady=(75,50))


EntryState_failText = Label(libEntryState_Canvas, text= "KULLANICI BULUNAMADI", font= font_info , bg=fail_color, fg="white", width=40, height=3)
#EntryState_failText.grid(row=4,column=0, **libEntryState_padx_options, pady=(75,50))


libEntryState_returnHomePage_Btn = Button(libEntryState_Canvas, text="Anasayfaya Dön", font=font_button, width = 30, height=2, bg= dark_grey, fg="white", command= lambda: EntryState_returnHomePage(canvas_list))
libEntryState_returnHomePage_Btn.grid(row=5,column=0, **libEntryState_padx_options, pady=10)


# library exit state page widgets


libExitState_Canvas = Canvas(root, bg=light_grey)
#libExitState_Canvas.place(relx=.5, rely=.5,anchor= CENTER)

libExitState_padx_options = {'padx':100}

libExitState_header_Text = Label(libExitState_Canvas, text= "KÜTÜPHANEDEN ÇIKIŞ YAP", font=font_header, bg=light_grey, fg=dark_grey)
libExitState_header_Text.grid(row=0,column=0, padx=10, pady=(50,75) )



libExitState_Email_Frame = Frame(libExitState_Canvas, width=100, bg=light_grey)
libExitState_Email_Frame.grid(row=1,column=0, **libExitState_padx_options, pady=15)

libExitState_Email_Label = Label(libExitState_Email_Frame, text = "Email: ", font= font_labelText , bg=light_grey, fg=dark_grey, width=5)
libExitState_Email_Label.grid(row=0,column=0)

libExitState_Email_InputBox = Entry(libExitState_Email_Frame, width=25)
libExitState_Email_InputBox.grid(row=0,column=1, ipady=3)



libExitState_Password_Frame = Frame(libExitState_Canvas, width=100, bg=light_grey)
libExitState_Password_Frame.grid(row=2,column=0, **libExitState_padx_options, pady=15)

libExitState_Password_Label = Label(libExitState_Password_Frame, text = "Şifre: ", font= font_labelText , bg=light_grey, fg=dark_grey, width=5)
libExitState_Password_Label.grid(row=0,column=0)

libExitState_Password_InputBox = Entry(libExitState_Password_Frame, width=25)
libExitState_Password_InputBox.grid(row=0,column=1, ipady=3)



Exit_Btn = Button(libExitState_Canvas, text="Çıkıyorum", font=font_button, width = 30, height=2, bg= dark_grey, fg="white", command=lib_Exit)
Exit_Btn.grid(row=3,column=0, **libExitState_padx_options, pady=20)


libExitState_success_Text = Label(libExitState_Canvas, text= "İYİ GÜNLER DİLERİZ", font= font_info , bg=success_color, fg="white", width=40, height=3)
libExitState_success_Text.grid(row=4,column=0, **libExitState_padx_options, pady=(55,2))

ExitState_request_Text = Label(libExitState_Canvas, text= "Lütfen Önerilerinizi Ve Dileklerinizi Websitemizden Bizimle Paylaşınız", wraplength=200, justify="center" ,
                               font= font_info , bg=success_color, fg="white", width=40, height=3)
ExitState_request_Text.grid(row=5,column=0, **libExitState_padx_options, pady=(2,40))

ExitState_fail_Text = Label(libExitState_Canvas, text= "KULLANICI BULUNAMADI", font= font_info , bg=fail_color, fg="white", width=40, height=3)
#ExitState_fail_Text.grid(row=4,column=0, **libEntryState_padx_options, pady=(75,50))


libExitState_returnHomePage_Btn = Button(libExitState_Canvas, text="Anasayfaya Dön", font=font_button, width = 30, height=2, bg= dark_grey, fg="white", command= lambda: ExitState_returnHomePage(canvas_list))
libExitState_returnHomePage_Btn.grid(row=6,column=0, **libExitState_padx_options, pady=10) 


# library take break state page widgets


libTakeBreakState_Canvas = Canvas(root, bg=light_grey)
#libTakeBreakState_Canvas.place(relx=.5, rely=.5,anchor= CENTER)

libTakeBreakState_padx_options = {'padx':100}

libTakeBreakState_header_Text = Label(libTakeBreakState_Canvas, text= "MOLAYA ÇIKIŞ", font=font_header, bg=light_grey, fg=dark_grey)
libTakeBreakState_header_Text.grid(row=0,column=0, **libTakeBreakState_padx_options, pady=(50,75) )



libTakeBreakState_Email_Frame = Frame(libTakeBreakState_Canvas, width=100, bg=light_grey)
libTakeBreakState_Email_Frame.grid(row=1,column=0, **libTakeBreakState_padx_options, pady=15)

libTakeBreakState_Email_Label = Label(libTakeBreakState_Email_Frame, text = "Email: ", font= font_labelText , bg=light_grey, fg=dark_grey, width=5)
libTakeBreakState_Email_Label.grid(row=0,column=0)

libTakeBreakState_Email_InputBox = Entry(libTakeBreakState_Email_Frame, width=25)
libTakeBreakState_Email_InputBox.grid(row=0,column=1, ipady=3)



libTakeBreakState_Password_Frame = Frame(libTakeBreakState_Canvas, width=100, bg=light_grey)
libTakeBreakState_Password_Frame.grid(row=2,column=0, **libTakeBreakState_padx_options, pady=15)

libTakeBreakState_Password_Label = Label(libTakeBreakState_Password_Frame, text = "Şifre: ", font= font_labelText , bg=light_grey, fg=dark_grey, width=5)
libTakeBreakState_Password_Label.grid(row=0,column=0)

libTakeBreakState_Password_InputBox = Entry(libTakeBreakState_Password_Frame, width=25)
libTakeBreakState_Password_InputBox.grid(row=0,column=1, ipady=3)



takeBreak_Btn = Button(libTakeBreakState_Canvas, text="Molaya Çıkıyorum", font=font_button, width = 30, height=2, bg= dark_grey, fg="white", command=lib_TakeBreak)
takeBreak_Btn.grid(row=3,column=0, **libTakeBreakState_padx_options, pady=20)



TakeBreakState_success_Text = Label(libTakeBreakState_Canvas, text= "İYİ DİNLENMELER DİLERİZ", font= font_info , bg=success_color, fg="white", width=40, height=3)
TakeBreakState_success_Text.grid(row=4,column=0, **libTakeBreakState_padx_options, pady=(75,50))

TakeBreakState_fail_Text = Label(libTakeBreakState_Canvas, text= "KULLANICI BULUNAMADI", font= font_info , bg=fail_color, fg="white", width=40, height=3)
#TakeBreakState_fail_Text.grid(row=4,column=0, **libEntryState_padx_options, pady=(75,50))



libTakeBreakState_returnHomePage_Btn = Button(libTakeBreakState_Canvas, text="Anasayfaya Dön", font=font_button, width = 30, height=2, bg= dark_grey, fg="white",  command= lambda: TakeBreakState_returnHomePage(canvas_list))
libTakeBreakState_returnHomePage_Btn.grid(row=6,column=0, **libTakeBreakState_padx_options, pady=10)




# library return break state page widgets



libReturnBreakState_Canvas = Canvas(root, bg=light_grey)
#libReturnBreakState_Canvas.place(relx=.5, rely=.5,anchor= CENTER)

libReturnBreakState_padx_options = {'padx':100}

libReturnBreakState_header_Text = Label(libReturnBreakState_Canvas, text= "MOLADAN DÖNÜŞ", font=font_header, bg=light_grey, fg=dark_grey)
libReturnBreakState_header_Text.grid(row=0,column=0, **libReturnBreakState_padx_options, pady=(50,75) )



libReturnBreakState_Email_Frame = Frame(libReturnBreakState_Canvas, width=100, bg=light_grey)
libReturnBreakState_Email_Frame.grid(row=1,column=0, **libReturnBreakState_padx_options, pady=15)

libReturnBreakState_Email_Label = Label(libReturnBreakState_Email_Frame, text = "Email: ", font= font_labelText , bg=light_grey, fg=dark_grey, width=5)
libReturnBreakState_Email_Label.grid(row=0,column=0)

libReturnBreakState_Email_InputBox = Entry(libReturnBreakState_Email_Frame, width=25)
libReturnBreakState_Email_InputBox.grid(row=0,column=1, ipady=3)



libReturnBreakState_Password_Frame = Frame(libReturnBreakState_Canvas, width=100, bg=light_grey)
libReturnBreakState_Password_Frame.grid(row=2,column=0, **libReturnBreakState_padx_options, pady=15)

libReturnBreakState_Password_Label = Label(libReturnBreakState_Password_Frame, text = "Şifre: ", font= font_labelText , bg=light_grey, fg=dark_grey, width=5)
libReturnBreakState_Password_Label.grid(row=0,column=0)

libReturnBreakState_Password_InputBox = Entry(libReturnBreakState_Password_Frame, width=25)
libReturnBreakState_Password_InputBox.grid(row=0,column=1, ipady=3)



ReturnBreak_Btn = Button(libReturnBreakState_Canvas, text="Döndüm", font=font_button, width = 30, height=2, bg= dark_grey, fg="white", command=lib_ReturnBreak)
ReturnBreak_Btn.grid(row=3,column=0, **libReturnBreakState_padx_options, pady=20)


ReturnBreakState_success_Text = Label(libReturnBreakState_Canvas, text= "İYİ ÇALIŞMALAR DİLERİZ", font= font_info , bg=success_color, fg="white", width=40, height=3)
ReturnBreakState_success_Text.grid(row=4,column=0, **libReturnBreakState_padx_options, pady=(75,50))

ReturnBreakState_fail_Text = Label(libReturnBreakState_Canvas, text= "KULLANICI BULUNAMADI", font= font_info , bg=fail_color, fg="white", width=40, height=3)
#ReturnBreakState_fail_Text.grid(row=4,column=0, **libEntryState_padx_options, pady=(75,50))



libReturnBreakState_returnHomePage_Btn = Button(libReturnBreakState_Canvas, text="Anasayfaya Dön", font=font_button, width = 30, height=2, bg= dark_grey, fg="white",  command= lambda: ReturnBreakState_returnHomePage(canvas_list))
libReturnBreakState_returnHomePage_Btn.grid(row=6,column=0, **libReturnBreakState_padx_options, pady=10)



"""
# veritabanı bağlantısı



dbConnection_Canvas = Canvas(root, bg=light_grey)
#dbConnection_Canvas.place(relx=.5, rely=.5,anchor= CENTER)

dbConnection_padx_options = {'padx':100}

dbConnection_header_Text = Label(dbConnection_Canvas, text= "GÖREVLİ GİRİŞİ", font=font_header, bg=light_grey, fg=dark_grey)
dbConnection_header_Text.grid(row=0,column=0, **libReturnBreakState_padx_options, pady=(50,75) )



dbConnection_Email_Frame = Frame(dbConnection_Canvas, width=100, bg=light_grey)
dbConnection_Email_Frame.grid(row=1,column=0, **libReturnBreakState_padx_options, pady=15)

dbConnection_Email_Label = Label(dbConnection_Email_Frame, text = "Email: ", font= font_labelText , bg=light_grey, fg=dark_grey, width=5)
dbConnection_Email_Label.grid(row=0,column=0)

dbConnection_Email_InputBox = Entry(dbConnection_Email_Frame, width=25)
dbConnection_Email_InputBox.grid(row=0,column=1, ipady=3)



dbConnection_Password_Frame = Frame(dbConnection_Canvas, width=100, bg=light_grey)
dbConnection_Password_Frame.grid(row=2,column=0, **libReturnBreakState_padx_options, pady=15)

dbConnection_Password_Label = Label(dbConnection_Password_Frame, text = "Şifre: ", font= font_labelText , bg=light_grey, fg=dark_grey, width=5)
dbConnection_Password_Label.grid(row=0,column=0)

dbConnection_Password_InputBox = Entry(dbConnection_Password_Frame, width=25)
dbConnection_Password_InputBox.grid(row=0,column=1, ipady=3)



dbConnection_Btn = Button(dbConnection_Canvas, text="GİRİŞ YAP", font=font_button, width = 30, height=2, bg= dark_grey, fg="white")
dbConnection_Btn.grid(row=3,column=0, **libReturnBreakState_padx_options, pady=(50,20))


dbConnection_success_Text = Label(dbConnection_Canvas, text= "", font= font_info , bg=success_color, fg="white", width=40, height=3)
#dbConnection_success_Text.grid(row=4,column=0, **libReturnBreakState_padx_options, pady=(75,50))

dbConnection_fail_Text = Label(dbConnection_Canvas, text= "BAĞLANAMADI", font= font_info , bg=fail_color, fg="white", width=40, height=3)
#ReturnBreakState_fail_Text.grid(row=4,column=0, **libEntryState_padx_options, pady=(75,50))
"""

tarihlabel = Label(root, text="KÜTÜPHANEDEKİ KULLANICILAR", font=50, bg=ktu_blue, fg="white") 
tarihlabel.grid(row=0,column=0, padx=600, pady=(100,50))

listing_Canvas = Canvas(root, bg=light_grey)
listing_Canvas.grid(row=1,column=0, padx=400, pady=(0,))


listing_Frame = Frame (listing_Canvas, border=3)
listing_Frame.grid(row=0,column=0)

listing_width:int
listing_width = 20
listing_font =10
_border = 3

Label1 = Label(listing_Frame, text = "ID", font=listing_font  , bg=light_grey, fg=dark_grey, width=5 )
Label1.grid(row=0,column=0)

Label2 = Label(listing_Frame, text = "AD SOYAD", font= listing_font , bg=light_grey, fg=dark_grey, width=listing_width )
Label2.grid(row=0,column=1)

Label3 = Label(listing_Frame, text = "DURUM", font= listing_font , bg=light_grey, fg=dark_grey, width=listing_width )
Label3.grid(row=0,column=2)

Label4 = Label(listing_Frame, text = "KALAN MOLA HAKKI", font= listing_font , bg=light_grey, fg=dark_grey, width=listing_width )
Label4.grid(row=0,column=3)


canvas_list = [homePage_Button_Canvas, libEntryState_Canvas, libExitState_Canvas, libTakeBreakState_Canvas, libReturnBreakState_Canvas] # dbConnection_Canvas]


root.mainloop()