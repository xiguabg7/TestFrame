class Game:
    __top_score__ = 0

    def __init__(self, player_name):
        self.__player_name__ = player_name

    @staticmethod
    def showHelp():
        print("help")

    @classmethod
    def showTopScore(cls):
        return cls.__top_score__

    @classmethod
    def setTopScore(cls, score):
        cls.__top_score__ = score

    # @property
    # def score(self):
    #     return self.__top_score__
    #
    # @score.setter
    # def score(self, score):
    #     self.__top_score__ = score

    def startGame(self, score):
        print(f"{self.__player_name__}开始玩游戏")
        if score > self.__top_score__:
            self.setTopScore(score)


player1 = Game("nigo")
player1.showHelp()
print(player1.showTopScore())
player1.startGame(80)
print(player1.showTopScore())
