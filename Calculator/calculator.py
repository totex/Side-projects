
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("KV-files/calculator.kv")


class CalculatorLayout(BoxLayout):

    clear = False

    def calculate(self):
        expression = self.ids["display"].text

        try:
            exp = str(eval(expression))
        except:
            exp = "Invalid operation!"
            self.clear = True

        self.ids["display"].text = exp

    def button_pressed(self, btn):
        if self.clear:
            self.ids["display"].text = ""
            self.clear = False

        text = btn.text
        self.ids["display"].text += text



class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()




CalculatorApp().run()

