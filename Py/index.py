from tkinter import *

def key(e) : 
    entry_1.delete( 0 , END )
    entry_1.configure( fg = ( "black") )

root = Tk()

root.geometry("500x500")
root.title(' امور دانشجویی ')

label_0 = Label( root , text = " برنامه امور دانشجویی " , width = 20 , font = ( "bold" , 20 ) )
label_0.place( x = 90 , y = 30 )

btn = Button( root , text = ' افزودن دانشجو ' , width = 15 , bg = "#023047" , fg = 'white' )
btn.place( x = 320 , y = 126 )
btn = Button( root , text = ' انتخاب واحد ' , width = 15 , bg = "#005f73" , fg = 'white' )
btn.place( x = 200 , y = 126 )
btn = Button( root , text = ' کارنامه ' , width = 15 , bg = "#0a9396" , fg = 'white' )
btn.place( x = 80 , y = 126 )

label_1 = Label( root , text = " : شماره دانشجویی  " , width = 20 , font = ( "bold" , 13 ) )
label_1.place( x = 300 , y = 225 )
entry_1= Entry( root , font = ( "bold" , 9 ) , fg = ('gray') )
entry_1.insert( 0 , '       شماره دانشجویی را وارد کنید  ')
entry_1.bind( '<Button-1>' , key )
entry_1.place( x = 190 , y = 230 )
btn = Button( root , text = ' جستجو ' , width = 10 , bg = "green" , fg = 'white' )
btn.place( x = 100 , y = 226 )
  soxom bilan
    
