# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:00:20 2024

@author: cough
"""

import simpleGE, pygame, random

class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect((255,255, 0), (25,25))
        self.setSize(50, 50)
        self.x = random.randint(0, self.screenWidth)
        self.y = random.randint(0, self.screenHeight)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
class Mickey(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Mickey_Mouse.jpg")
        self.setSize(50, 50)
        
        #setBoundAction(BOUNCE) 
        
    def process(self):   
        if self.isKeyPressed(pygame.K_a):
            self.x -= 10
        if self.isKeyPressed(pygame.K_d):
            self.x += 10
        if self.isKeyPressed(pygame.K_w):
            self.y -= 10
        if self.isKeyPressed(pygame.K_s):
            self.y += 10
        
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: 10"
        self.center = (500, 30)



                
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        pygame.init()
        scene = simpleGE.Scene()
        scene.setCaption("Game")
        self.score = 0
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.setImage("sky.jpeg")
        self.sndCoin = simpleGE.Sound("coin.wav")
        self.mickey = Mickey(self)
        self.coin = Coin(self)
        self.coins = []
        for i in range(10):
            self.coins.append(Coin(self))
        self.lblScore = LblScore()
        self.lblTime = LblTime()
        
        self.sprites = [self.mickey,
                        self.coins,
                        self.lblScore, 
                        self.lblTime]

    def process(self):
        for coin in self.coins:
            if self.mickey.collidesWith(coin):
                self.sndCoin.play()
                coin.reset()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Final Score: {self.score}")
            self.stop()
class Instructions(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        #self.setImage("sky.jpg")
        
        self.response = "Play"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
        "You are Mickey Mouse (not from the clubhouse).",
        "Move with the W A S D Keys",
        "and catch as much cash as you can",
        "in only ten seconds",
        "",
        "Good Luck!"]
        
        self.instructions.center = (320, 240)
        self.instructions.size = (500, 250)
        
        self.prevScore = score
        self.lblScore = simpleGE.Label()
        self.lblScore.text = f"Last score: {self.prevScore}"
        self.lblScore.center = (320, 400)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play (up)"
        self.btnPlay.center = (100, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit (down)"
        self.btnQuit.center = (550, 400)
        
        self.sprites = [self.instructions,
                        self.lblScore,
                        self.btnQuit,
                        self.btnPlay]
        
    def process(self):

        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()


        if self.isKeyPressed(pygame.K_UP):
            self.response = "Play"
            self.stop()
        if self.isKeyPressed(pygame.K_DOWN):wwaawa
            self.response = "Quit"
            self.stop()

def main():
    
    keepGoing = True
    score = 0
    while keepGoing:
        
        instructions = Instructions(score)
        instructions.start()
                
        if instructions.response == "Play":    
            game = Game()
            game.start()
            score = game.score
        else:
            keepGoing = False
    
if __name__ == "__main__":
    main()
