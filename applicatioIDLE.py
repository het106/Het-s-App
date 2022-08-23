#importng KIVY modules and files
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


# Class that inherits App
class SayHello(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}


        # image widgte
        self.photo = Image(
                     source = "basketball.png",
            )
        self.window.add_widget(self.photo) #displaying the image of a basketball

        # label widget
        self.greeting = Label(
                        text= "Enter a baskeball team to see the amount of titles they have won: ",
                        size_hint = (0.7,0.6),
                        font_size= 14,
                        font_name = 'Arial',
                        color= '#00FFCE'                  
                    
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text= "Enter",
                      size_hint= (1,0.3),
                      bold= True,
                      background_color ='#00FFCE',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        return self.window

    def callback(self, instance):
        # checking inputs depending on the 30 NBA teams
        if self.user.text == "Los Angeles Lakers" or self.user.text == "lakers" or self.user.text == "Lakers":
            self.label = Label(text = "Lakers have won won: 17 titles")
            self.window.add_widget(self.label)      
        elif self.user.text == "Boston Celtics" or self.user.text == "celtic" or self.user.text == "Celtics":           
            self.label = Label(text = "Celtics have won 17 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Chicago Bulls":
            self.label = Label(text = "Bulls have won: 6 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Golden State Warriors" or self.user.text == "GSW" or self.user.text == "gsw":
            self.label = Label(text = "GSW have won: 6 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "San Antonio Spurs" or self.user.text == "Spurs":      
            self.label = Label(text = "San Antanio have won: 6 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Philadelphia 76ers" or  self.user.text == "76ers":
            self.label = Label(text = "76ers have won: 3 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Detroit Pistons":
            self.label = Label(text = "Pistons have won: 3 titles")
            self.window.add_widget(self.label)       
        elif self.user.text == "Miami Heat":
            self.label = Label(text = "Heat have won: 3 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "New York Knicks" or  self.user.text == "Knicks":
            self.label = Label(text = "Knicks have won: 2 titles")
            self.window.add_widget(self.label)        
        elif self.user.text == "Houston Rockets" or self.user.text == "Rockets":
            self.label = Label(text = "Rockets have won: 2 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Milwaukee Bucks":
            self.label = Label(text = "Bucks have won: 2 titles")
            self.window.add_widget(self.label)        
        elif self.user.text == "Cleveland Cavaliers":
            self.label = Label(text = "The  Cavs have won: 1 titles")
            self.window.add_widget(self.label)   
        elif self.user.text == "Atlanta Hawks":
            self.label = Label(text = "The Hawks have won: 1 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "OKC" or self.user.text == "Oklahoma City Thunder":
            self.label = Label(text = "OKC have won: 1 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Washington Wizards":
            self.label = Label(text = "The Rockets have won: 1 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Portland Trail Blazers":
            self.label = Label(text = "The Trail Blaxers have won: 1 titles")
            self.window.add_widget(self.label)        
        elif self.user.text == "Dallas Mavericks":
            self.label = Label(text = "The  mavericks have won: 1 titles")
            self.window.add_widget(self.label)   
        elif self.user.text == "Toronto Raptors":
            self.label = Label(text = "The raptors have won: 1 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Sacramento Kings" or self.user.text == "kings":
            self.label = Label(text = "OKC have won: 1 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Phoenix Suns":
            self.label = Label(text = "The suns have won: 0 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Utah jazz":
            self.label = Label(text = "The Trail Blaxers have won: 0 titles")
            self.window.add_widget(self.label)        
        elif self.user.text == "Orlanda Magic":
            self.label = Label(text = "The magic have won: 0 titles")
            self.window.add_widget(self.label)   
        elif self.user.text == "Brooklyn Nets":
            self.label = Label(text = "The nets have won: 0 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Indiana Pacers" or self.user.text == "Pacers":
            self.label = Label(text = "Pacers have won: 0 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Denver Nuggets":
            self.label = Label(text = "The nuggets have won: 0 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Los Angeles Clippers" or self.user.text == "clippers":
            self.label = Label(text = "The clippers  have won: 0 titles")
            self.window.add_widget(self.label)        
        elif self.user.text == "Minnesota Timberwolves":
            self.label = Label(text = "The timbervolves have won: 0 titles")
            self.window.add_widget(self.label)   
        elif self.user.text == "New Orleans Pelicans":
            self.label = Label(text = "The pelicans have won: 0 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Memphis Grizzlies" or self.user.text == "Grizzlies":
            self.label = Label(text = "grizzlies have won: 0 titles")
            self.window.add_widget(self.label)
        elif self.user.text == "Charlotte Hornets" or self.user.text == "Hornets":
            self.label = Label(text = "Hornets have won: 0 titles")
            self.window.add_widget(self.label)
        else:
            self.label = Label(text = "Please enter a valid name (it is cap sensitive)")    
            self.window.add_widget(self.label)
        
           
# run application class
if __name__ == "__main__":
    SayHello().run()



    
