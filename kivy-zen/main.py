import kivy
import random
import time
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


quotes = {
    "Maestro A": [
        "Cuando los mortales están vivos, se preocupan por la muerte. Cuando están satisfechos, se preocupan por el hambre. De ellos es la gran incertidumbre. Los sabios no consideran el pasado. Y no se preocupan por el futuro. Tampoco se apegan al presente. Y de momento en momento siguen el camino.",
        "Si ves tu naturaleza, no necesitas leer sutras o invocar a los buddhas. La erudición y el conocimiento no son solo inútiles sino que tambien opacan tu atención. Las doctrinas son solo para señalar a la mente. Una vez que observas tu mente, para que poner atención a doctrinas?",
        "Todo lo bueno y lo malo viene de tu propia mente. Encontrar algo más allá de la mente es imposible."
    ],
    "Maestro B": [
        "Al inicio, el dinero es como una gema que cumple todos tus deseos. Luego, se convierte indispensable. Al final, te sientes como un mendigo. Esos son mis pensamientos y sentimientos acerca del dinero. Así que renuncie a bienes y riquezas.",
        "Mi religion es vivir - y morir - sin arrepentimiento.",
        "Necesito nada. Busco nada. Deseo nada."
    ],
    "Maestro C": [
        "No veas a las montañas desde la escala de pensamiento humano.",
        "Lo que crees en tu propia mente que será bueno, o lo que las personas del mundo creen que es bueno, no es necesariamente bueno.",
        "Elige ser derrotado en presencia de los sabios que sobresalir entre tontos."
    ]
}

class HomeWindow(Screen):
    pass

class UserWindow(Screen):
    pass

class MaestroScreen(Screen):
    def show_quote(self, maestro):
        quote = random.choice(quotes[maestro])
        self.manager.get_screen("quotescreen").ids.quote_text.text = quote
        self.manager.current = "quotescreen"
        self.display_quote_with_effect(quote)

    def display_quote_with_effect(self, quote):
        self.ids.quote_text.text = ""
        for i, char in enumerate(quote):
            delay = i * 0.1
            Clock.schedule_once(lambda dt, char=char: self.display_quote_char(char), delay)

    def display_quote_char(self, char):
        self.ids.quote_text.text += char

class WindowManager(ScreenManager):
    pass

class MaquinaZen(App):
    pass
    
MaquinaZen().run()