
from kivy.app import App
from kivy.uix.button import Button




from kivy.uix.floatlayout import FloatLayout

class myApp(App):
    def build(self):

        
        fl=FloatLayout(size=(300, 300))
       
        fl.add_widget(Button(
            text="Это кнопка",
            font_size=29,
            on_press=self.btn_press,
            background_color=[1,0,0,1],
            background_normal='',
            size_hint=(.7, .25),
            pos=(120, 120)));
        fl.add_widget(Button(
            text="Это кнопка2",
            font_size=29,
            on_press=self.btn_press,
            background_color=[1,1,0,1],
            background_normal='',
            size_hint=(.7, .25),
            pos=(120, 320)));
        return fl
    def btn_press(self, instance):        
        if instance.text=='Это кнопка':
            instance.text='Click'
        elif instance.text=='Это Кнопка2':
            instance.text='Click2'
            
                
        
if __name__=="__main__":
    myApp().run()
