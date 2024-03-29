import pygame

from game import Tank

BLACK = 0, 0, 0
WHITE = 255, 255, 255
YELLOW = 255, 255, 0


class TankGame:
    def __init__(self):
        """
        init a game
        """
        pygame.init()
        self.size = self.width, self.height = 600, 400
        self.speed = [1, 1]
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("tank")
        self.fps = 300
        self.fclock = pygame.time.Clock()
        self.uevent = []
        self.tank1 = Tank(env=self, path="assets/tank1.png", para_pos=[70, 70], para_angle=0)
        self.tank2 = Tank(env=self, path="assets/tank2.png", para_pos=[300, 300], para_angle=180)
        pygame.display.set_icon(self.tank1.surf)
        pygame.mixer.music.load("assets/bgm.wav")
        pygame.mixer.music.play(-1, 0.0)
        self.bulletQueue = []
        self.score1 = Score(self, 0, [500, 100])
        self.score2 = Score(self, 0, [500, 200])
        self.text1 = Text(self, "assets/comic.ttf", 36, WHITE, "Tank1:", [400, 100])
        self.text2 = Text(self, "assets/comic.ttf", 36, WHITE, "Tank2:", [400, 200])
        self.startFlag = 0
        self.titleText = Text(self, "assets/comic.ttf", 64, YELLOW, "TANK!", [300, 100])
        self.desciptionText1 = Text(self, "assets/comic.ttf", 20, WHITE, "Press 1 to play in single player mode", [300, 200])
        self.desciptionText2 = Text(self, "assets/comic.ttf", 20, WHITE, "Press 2 to play in double player mode", [300, 300])
        self.clock = 0



    def restart(self):
        """
        restart a game when a tank being attacked
        :return: none
        """
        self.tank1 = Tank(env=self, path="assets/tank1.png", para_pos=[70, 70], para_angle=0)
        self.tank2 = Tank(env=self, path="assets/tank2.png", para_pos=[300, 300], para_angle=180)


    def titleStart(self):
        """
        return to title page
        :return: none
        """
        self.restart()
        self.score1.set(0)
        self.score2.set(0)
        self.screen.fill(BLACK)
        self.titleText.update()
        self.desciptionText1.update()
        self.desciptionText2.update()
        self.bulletQueue = []


    def update(self):
        """
        update all elements
        :return: none
        """
        self.tank1.update()
        self.tank2.update()
        self.text1.update()
        self.text2.update()
        self.score1.update()
        self.score2.update()

class Text:
    def __init__(self, game, font, size, color, str, pos):
        """
        this is a class to store text type data
        :param game: runtime environment
        :param font: font
        :param size: size
        :param color: front color
        :param str: content stored
        :param pos: position
        """
        self.content = str
        self.env = game
        self.fontObj = pygame.font.Font(font, size)
        self.color = color
        self.surf = self.fontObj.render(self.content, True, color)
        self.pos = pos

    def reRender(self):
        """
        render the text
        :return: none
        """
        self.surf = self.fontObj.render(self.content, True, self.color)

    def update(self):
        """
        update the content
        :return: none
        """
        self.rect = self.surf.get_rect()
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]
        self.env.screen.blit(self.surf, self.rect)

    def get(self):
        """
        get the content
        :return: the content
        """
        return self.content

class Score(Text):
    """
    class storing Score. Adapted from Text
    """
    def __init__(self, game, score, pos):
        """
        init
        :param game:runtime environment
        :param score: score
        :param pos: position
        """
        Text.__init__(self, game, "assets/comic.ttf", 36, WHITE, str(score), pos)
        self.val = score

    def add(self, val):
        """
        add score
        :param val: the value to be added on the score
        :return: none
        """
        self.val += val
        self.content = str(self.val)
        self.reRender()
        self.update()

    def inc(self):
        """
        increase the score
        :return: none
        """
        self.add(1)

    def getScore(self):
        """
        get the score
        :return: score
        """
        return self.val

    def set(self, val):
        """
        set the score
        :param val: value to be set
        :return: none
        """
        self.val = val
        self.content = str(self.val)
        self.reRender()
        self.update()
