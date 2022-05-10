from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from pyperclip import copy

class Lyrics_FaithACAApp(App):#Calls everything and this is the title of the Window
    def build(self):
        self.icon = 'logo.png'#image to be in 256x256 and in png/ico format
        return MyGridLayout()

class MyGridLayout(GridLayout):#Default Layout
    def __init__(self,**kwargs):
        super(MyGridLayout,self).__init__(**kwargs)
        self.cols=1
        #For Submit to be in two columns
        self.top_grid=GridLayout()
        self.top_grid.cols=2
        #TextBox For Tamil
        self.tamil_box=Label(text='Tamil/தமிழ்: ',font_size=32,font_name='arial-unicode-ms',size_hint_x=0)
        self.top_grid.add_widget(self.tamil_box)
        #Tamil Text Input Box
        self.tamil=TextInput(multiline=True,font_name='arial-unicode-ms',cursor_color='white',background_color='gray',foreground_color='white',font_size=20)
        self.top_grid.add_widget(self.tamil)
        #TextBox for English
        self.english_box=Label(text='English: ',font_size=32,font_name='Times')
        self.top_grid.add_widget(self.english_box)
        #English Text Input Box
        self.english=TextInput(multiline=True,cursor_color='white',background_color='gray',foreground_color='white',font_size=19)
        self.top_grid.add_widget(self.english)
        #Submit Button
        self.add_widget(self.top_grid)
        self.submit=Button(text='[b]Submit',markup=True,font_size=32,font_name="Times",size_hint_y=None, height=int(Window.height)/8.9,background_color='magenta')#The Submit Button
        self.submit.bind(on_press=self.press)#this will bind it to the function press(self,instance)
        self.add_widget(self.submit)
        #Info on how this works
        self.output=Label(text='*[i]The Lyrics will be copied to your clipboard after you click on "Submit"',markup=True, font_size=14,size_hint_y=None,height=int(Window.height)/14.9)
        self.add_widget(self.output)
        #Credits to myself(narcissist)
        self.credits=Label(text='Developed by Sam Godson. Contact me: contact.samgodson@gmail.com',color=(255/255,255/255,255/255, 1),markup=True, font_size=12,size_hint_y=None,height=int(Window.height)/17.9)
        self.add_widget(self.credits)
    def press(self,instance):#this is the 'Main Script' Code
        tamil=self.tamil.text
        tamil_list=list(tamil.split('\n'))
        english=self.english.text
        english_list=list(english.split('\n'))
        #To remove blank lines
        tam=len(tamil_list)-1
        if tam>0:
            while tam>-1:
                if tamil_list[tam]=='':
                    tamil_list.pop(tam)
                tam-=1
        eng=len(english_list)-1
        if eng>0:
            while eng>=-1:
                if english_list[eng]=='':
                    english_list.pop(eng)
                eng-=1;
        #To output tamil, english
        final_text=''
        for val_tamil,val_english in zip(tamil_list,english_list):
            final_text=final_text+val_tamil.strip()#to strip(jk just the blank spaces)
            final_text=final_text+'\n'
            final_text=final_text+(val_english.title()).strip()#same as before to strip(spaces)
            final_text=final_text+'\n'
        copy(final_text)#This is what copies the final text to clipboard

if __name__=='__main__':
    Lyrics_FaithACAApp().run()