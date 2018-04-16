class Player:

    def __init__(self, name):
        self.score = 0
        self.name = name
        self.lives = 5

    def __init__(self, score, name, lives):
        self.score = score
        self.name = name
        self.lives = lives

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_lives(self):
        return self.lives
