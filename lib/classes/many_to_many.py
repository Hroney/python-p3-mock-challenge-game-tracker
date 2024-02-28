class Game:

    def __init__(self, title):
        self._title = None
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value):
            if not hasattr(self, '_title') or self._title is None:
                self._title = value
            else:
                raise ValueError("Title is immutable once set")

    def results(self):
        returnlist = []
        for value in Result.all:
            if value.game.title == self.title:
                returnlist.append(value)
        return returnlist

    def players(self):
        returnlist = []

        for value in Result.all:
            if value.game.title == self.title:
                if value.player not in returnlist:
                    returnlist.append(value.player)
        return returnlist

    def average_score(self, player):
        num_list = []
        for value in Result.all:
            if value.player is player:
                num_list.append(value.score)
        return sum(num_list)/len(num_list)

class Player:

    def __init__(self, username):
        self._username = None
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if isinstance(value, str) and (len(value) >= 2 and len(value) <= 16):
            self._username = value

    def results(self):
        returnlist = []
        for value in Result.all:
            if value.player.username == self.username:
                returnlist.append(value)
        return returnlist

    def games_played(self):
        games = []
        for value in Result.all:
            if value.player is self:
                if value.game not in games:
                    games.append(value.game)
        return games

    def played_game(self, game):
        for value in Result.all:
            if value.game is game and value.player is self:
                return True
        return False

    def num_times_played(self, game):
        num = 0
        for value in Result.all:
            if value.game is game and value.player is self:
                num += 1
        return num

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if isinstance(value, int) and (value >= 1 and value <= 5000):
            if not hasattr(self, '_score') or self._score is None:
                self._score = value
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, value):
        self._player = value

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, value):
        self._game = value
