if __name__ == '__main__':
    from kivy.base import runTouchApp
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.garden.roulette import Roulette, CyclicRoulette, \
        TimeFormatCyclicRoulette
    b = BoxLayout()
    b.add_widget(Roulette(density=2.8, selected_value=2013))
    b.add_widget(CyclicRoulette(cycle=12, density=2.8, zero_indexed=False))
    b.add_widget(CyclicRoulette(cycle=30, density=2.8, zero_indexed=False))
    b.add_widget(TimeFormatCyclicRoulette(cycle=24))
    b.add_widget(TimeFormatCyclicRoulette(cycle=60)) 
    b.add_widget(TimeFormatCyclicRoulette(cycle=60)) 
    selected_value = Label()
    rolling_value = Label()
    for c in b.children:
        c.bind(selected_value=lambda _, val:
               selected_value.setter('text')(_,
                'selected_value:\n' + str(val)),
               rolling_value=lambda _, val:
               rolling_value.setter('text')(_,
                'rolling_value:\n' + str(val)))
    
    b.add_widget(selected_value)
    b.add_widget(rolling_value)
    
    runTouchApp(b)

