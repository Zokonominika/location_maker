import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import NumericProperty
from plyer import compass
import math

# Force window size to phone-like dimensions for PC testing
Window.size = (400, 700)

class KibleApp(App):
    compass_angle = NumericProperty(0)
    qibla_angle = NumericProperty(153) # 153 degrees for Istanbul
    
    def build(self):
        try:
            compass.enable()
        except NotImplementedError:
            print("Uyari: Plyer Pusula(Compass) modulu bu isletim sisteminde desteklenmiyor (PC).")
        except Exception as e:
            print(f"Pusula sensoru baslatilamadi: {e}")
            
        # Update the UI every 1/30th of a second
        Clock.schedule_interval(self.update_compass, 1.0 / 30.0)
        return Builder.load_file('kible.kv')
        
    def update_compass(self, dt):
        try:
            # compass.orientation typically returns a tuple, we assume index 0 is azimuth (heading)
            field = compass.orientation
            if field and len(field) > 0 and field[0] is not None:
                self.compass_angle = field[0]
            else:
                # Mock simulation for PC
                self.compass_angle = (self.compass_angle + 0.5) % 360
        except Exception:
            # Fallback for PC
            self.compass_angle = (self.compass_angle + 0.5) % 360

    def on_stop(self):
        try:
            compass.disable()
        except:
            pass

if __name__ == '__main__':
    KibleApp().run()
