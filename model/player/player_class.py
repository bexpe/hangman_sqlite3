class Player:

    def __init__(self, name, score=0, lives=5):
        self.score = score
        self.name = name
        self.lives = lives

    def get_name(self):
        print(self.name)
        return self.name

    def get_score(self):
        return self.score

    def get_lives(self):
        print(self.lives)
        return self.lives
