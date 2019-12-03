from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
b = TonalBuzzer(4)
b.play(Tone("A4"))
