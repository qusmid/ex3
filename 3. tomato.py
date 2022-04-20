a = 0
class Tomato:
    states = {0: 0, 1: 1, 2: 2}
    stageTomato = states[0]
    tomatoes = 5
    def __init__(self):
        self._index = 0
        self._state = Tomato.states[0]
    def grow(self):
        self.stageTomato = Tomato.states[+1]
    def is_ripe(self):
        if self.stageTomato == Tomato.states[-1]:
            print("Ready")

class TomatoBush:
    def __init__(self):
        self.tomatoes = dict([(Tomato.tomatoes, Tomato.stageTomato)])
    def grow_all(self):
        for i in range(len(self.tomatoes)):
            self.tomatoes[i][Tomato.stageTomato] = +1
    def all_are_ripe(self):
        pass
    def give_away_all(self):
        pass

class Gardener:
    def __init__(self):
        pass
    def work(self):
        pass
    def harvest(self):
        pass

    @staticmethod
    def knowledge_base():
        pass
