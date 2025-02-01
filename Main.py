import pygame
import math
import time
import random
import EnemyScripts
import PlayerDashNSmash
import StaticObjColliders
import StaticObjManager
import MapLoader
from os import path
directory = path.dirname(path.abspath(__file__))
#All the stuff to do with debugging goes up here
Debug = False
ColVisualRight = pygame.image.load(path.join(directory, "OldStuff//ColVisualRight.png"))
ColVisualLeft = pygame.image.load(path.join(directory, "OldStuff//ColVisualLeft.png"))
ColVisualFloor = pygame.image.load(path.join(directory, "OldStuff//ColVisualFloor.png"))    
ColVisualRoof = pygame.image.load(path.join(directory, "OldStuff//ColVisualRoof.png"))
ColGeneral = pygame.image.load(path.join(directory, "OldStuff//ColGeneral.png"))
GameTickFactor = 2
clock = pygame.time.Clock() 


BgColorList = [67, 64, 143], [165, 191, 230], [0, 0, 0]

#USE AS BG COLOR FOR SNOW LEVEL [230, 204, 165]

#Manges Sounds and Music
pygame.mixer.init()


pygame.init()
OldReplace = [], [], [], []
BgReplace = pygame.image.load(path.join(directory, "Sprites//AnimationReplacements//BGREPLACE.png"))
PortalCalled = False

#Everything to do with title, icon, etc...
pygame.display.set_caption("Monty Python")
icon = pygame.image.load(path.join(directory, "PHIcon.webp"))
pygame.display.set_icon(icon)
Screen_Width = 960
Screen_Height = 704
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
Block = pygame.image.load(path.join(directory, "Sprites//Tiles_L1//Tile_RingBox.png"))
MenuRun = True
run = True


#Initializes everything to do with the player
BottomGameBar = pygame.image.load(path.join(directory, "Sprites//BottomBar.png"))
HPpoint = pygame.image.load(path.join(directory, "HP point.png"))
PlayerIframesAndHP = [0, 100, 0, 0, 0, 0]
PlayerSpeed = [0, 0]
PlayerAcc = [0, 0]
IsPlayerTouchingFloor = 0
IsPlayerTouchingRight = 0
IsPlayerTouchingLeft = 0
IsPlayerTouchingRoof = 0
PlayerStaticBool = False
DashFrameTimer = 0
HasPlayerDashed = False
NumberSpriteList = [pygame.image.load(path.join(directory, "Sprites//Numbers//0.png")), 
                    pygame.image.load(path.join(directory, "Sprites//Numbers//1.png")), 
                    pygame.image.load(path.join(directory, "Sprites//Numbers//2.png")), 
                    pygame.image.load(path.join(directory, "Sprites//Numbers//3.png")), 
                    pygame.image.load(path.join(directory, "Sprites//Numbers//4.png")), 
                    pygame.image.load(path.join(directory, "Sprites//Numbers//5.png")), 
                    pygame.image.load(path.join(directory, "Sprites//Numbers//6.png")), 
                    pygame.image.load(path.join(directory, "Sprites//Numbers//7.png")), 
                    pygame.image.load(path.join(directory, "Sprites//Numbers//8.png")), 
                    pygame.image.load(path.join(directory, "Sprites//Numbers//9.png"))]
PlayerBlockFactor = [1, 1]
PlayerSpawnPos = [0, 0], [0]


CurrentGlobalLevel = 2
#PlayerSpawnPos = [1200, 0], [4]
PlayerX = PlayerSpawnPos[0][0]
PlayerY = PlayerSpawnPos[0][1]


#Player's Attacks
#DashHitboxList is a 2D array that stores the X and Y positions of every individual dash collider
DashHitboxList = [-100, 0, 0, 0, 0, 0, 0], [-100, 0, 0, 0, 0, 0, 0], [1, 3, 3, 5, 5, 5, 2]
PlayerCharge = 0
PlayerChargeTimer = 0
WhichCharge = 0

#Loads Font
Font = pygame.image.load(path.join(directory, "Sprites//Numbers//Font.png"))

#DOIS must be called at the beginning. Refresh this along witht the function LoadDynamicObjectsList
#DOIS and DynamicTag (DynamicTags are unique to each object and are stored in DOIS[0]) are what control everything to do with dynamic, or moving, objects and how they behave. This, along with DACL, controls and renders dynamic objects.
#SpawnList allows objects to be spawned into DOIS
DOIS = [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]
SpawnList = []

#This variable handles scrolling
XOffsetForScrolls = 0

#GameRow0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#GameRow1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#GameRow2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#GameRow3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 1], [3, 3, 1, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#GameRow4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1], [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#GameRow5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 0, 0, 0, 1, 1], [1, 3, 3, 1, 1, 3, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#GameRow6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1], [2, 0, 0, 0, 2, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 3, 2, 1, 3, 3, 2, 2, 1], [1, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#GameRow7 = [0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 3, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1], [2, 0, 0, 0, 2, 2, 2, 0, 2, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1], [2, 2, 2, 2, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 1, 3, 2, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#GameRow8 = [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1, 3, 1, 1, 3, 2, 2, 2, 1], [2, 0, 0, 0, 2, 2, 2, 0, 2, 1, 1, 1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1], [2, 2, 2, 2, 0, 1, 2, 2, 0, 0, 2, 1, 1, 1, 1, 2], [1, 3, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#GameRow9 = [2, 2, 2, 3, 3, 3, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1], [3, 3, 3, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [2, 2, 2, 2, 1, 2, 1, 3, 3, 2, 2, 2, 1, 3, 1, 1, 2, 2, 2, 1, 1, 1, 3, 1, 1, 1], [1, 1, 1, 2, 3, 3, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
#MovObjectsList = ["6, 640, 384, 0, 0, 0"], ["6, 448, 384, 0, 0, 0", "6, 576, 128, 0, 0, 0"], ["0, 704, 128, 0, 0, 0.2, 0", "6, 448, 256, 0, 0, 0", "6, 256, 256, 0, 0, 0"], ["0, 128, 128, 0, 0, 0.2, 0",  "0, 568, 64, 0, 0.4, 0, 0", "6, 700, 128, 0, 0, 0"], ["7, 512, 448, 0, 0.1, 500, 0, 512, 1", "6, 956, 384, 0, 0, 0", "0, 1344, 192, 0, 0, 0.2, 0"], ["9, 1472, 64", "6, 1278, 256, 0, 0, 0", "0, 1080, 128, 0, 0, 0.2, 0", "0, 770, 320, 0, -0.4, 0.4, 0", "7, 512, 448, 0, 0.1, 500, 0, 512, 1"], []

#YList controls the rows and columns of the game, CurrentScene is the current scene in a level, and CurrentGlobalLevel is the level
YList = [[],[],[],[],[],[],[],[],[],[]]

CurrentScene = PlayerSpawnPos[1][0]

#Loads in a level
MovObjectsList, BlockAppendix = MapLoader.LoadLevel(CurrentGlobalLevel)

#YOU DIED BADUMMM!!
youdiedblit = pygame.image.load(path.join(directory, "Sprites//YOUDIED.png"))


#Everything to do with the animations of each dynamic object!
DynamicAnimationsAppendix = ["Sprites//DEATHANIM.png", "Sprites//FLAG.png", "Sprites//DynamicObjects//Floater.png", "Sprites//NoneList//None.png", "Sprites//DynamicObjects//Drill_Vertical.png", "Sprites//DynamicObjects//Buzz.png", "Sprites//DynamicObjects//Goblin.png", "Sprites//DynamicObjects//Dark_Knight.png", "Sprites//DynamicObjects//Dark_Knight_Projectile.png", "Sprites//DynamicObjects//Goblin_Abuser.png", "Sprites//DynamicObjects//HealPad.png", "Sprites//DynamicObjects//Pellet_1.png", "Sprites//DynamicObjects//Ghost.png", "Sprites//DynamicObjects//Crow.png", "Sprites//DynamicObjects//Cannon.png", "Sprites//DynamicObjects//CannonBall.png", "Sprites//DynamicObjects//HONCH.png", "Sprites//DynamicObjects//AirSlash.png", "Sprites//DynamicObjects//Tornado.png", "Sprites//NoneList//None.png", "Sprites//DynamicObjects//SUPER_IMPORTANT.png", "Sprites//DynamicObjects//PORTAL.png", "Sprites//DynamicObjects//ALLURIAN.png", "Sprites//DynamicObjects//WILLOWISP.png", "Sprites//DynamicObjects//LINGERINGPURPLE.png", "Sprites//DynamicObjects//CLOAK.png", "Sprites//DynamicObjects//FIRERING.png", "Sprites//DynamicObjects//FIRETHINGY.png", "Sprites//DynamicObjects//SPEARTIP.png"]
DynamicAnimationStringAppendix = ["START, 0, 25, 50, 75, 100, 250, END", "START, 0, 500, START, 1, 15, 30, 60, 200, START, 4, 35, 70, 105, 140, END", "START, 0, 50, 10, 150, START, 3, 25, 50, 75, END", "START, 0, 500, END", "START, 0, 500, END", "", "START, 0, 100, 150, 200, START, 6, 20, 40, START, 3, 10, 20, 40, END", "START, 0, 50, 100, 150, 200, 250, 300, START, 6, 50, 100, 150, 200, 250, 300, START, 12, 25, 50, 150, 165, 180, 195, 400, END", "START, 0, 20, 40, 60, 250, END", "START, 0, 25, 50, 75, 100, 125, 150, START, 6, 50, 100, 120, 140, 150, 160, 190, 230, END", "START, 0, 50, 100, 150, 200, END", "START, 0, 25, 50, 75, 100, 75, END", "START, 0, 25, 50, 75, END", "START, 0, 100000, START, 1, 25, 50, 75, START, 4, 15, 30, END", "START, 0, 500, 525, 550, 575, 600, 625, START, 6, 25, 50, 75, 100, 130, 350, END", "START, 0, 18, 35, 45, 60, START, 5, 25, 50, 75, END", "START, 0, 25, 58, 85, 120, 125, START, 0, 17, 38, 56, 78, 82, END", "START, 0, 20, 40, 60, END", "START, 0, 15, 30, END", "START, 0, 800, END", "START, 0, 50, 100, 150, 200, END", "START, 0, 100, END", "START, 0, 40, 80, START, 8, 50, 100, START, 3, 10, 20, 30, 40, 200, START, 10, 100, 200, START, 12, 10, 20, 150, 120, 125, 130, 145, 800, START, 21, 10, 20, 150, 180, 210, 240, END", "START, 0, 10, 20, 30, 40, 50, END", "START, 0, 100, 200, END", "START, 0, 30, 60, 90, 120, START, 4, 100, 115, 130, 145, 260, START, 9, 30, 45, 70, 130, END", "START, 0, 20, 40, END", "START, 0, 20, 40, 60, 80, 100, 120, END", "START, 0, 15, 30, 855, END"]
DynamicAniimationScaleFactorYAppendix = [1, 3, 1, 1, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1, 3, 2]
DynamicAniimationScaleFactorXAppendix = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 3, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1]
for i in range(len(DynamicAniimationScaleFactorXAppendix)):
    DynamicAniimationScaleFactorXAppendix[i] -= 1
    DynamicAniimationScaleFactorYAppendix[i] -= 1
#DACL controls dynamic object animation, SpecificStaticObjects controls how they behave with static objects in the screen to avoid overlap. OldReplace covers the tracks of moving objects!
DACL = [[], [], [], []]
OldReplace = [], [], [], []
SpecificStaticObjects = [0], [0]
#Below is a list of the dynamic objects!

#AppointSpecificStaticObjects deals with Animation
def AppointSpecificStaticObjects(X, Y):
    SpecificStaticObjects[1].append(round((Y)/64))
    SpecificStaticObjects[0].append(round((X - 64)/64))
    SpecificStaticObjects[1].append(round((Y)/64))
    SpecificStaticObjects[0].append(round((X)/64))
    SpecificStaticObjects[1].append(round((Y - 64)/64))
    SpecificStaticObjects[0].append(round((X - 64)/64))
    SpecificStaticObjects[1].append(round((Y - 64)/64))
    SpecificStaticObjects[0].append(round((X)/64))

def TypeNStuff(String, StartingX, StartingY, MaxCharacters):
    StringList = [(ord(String[i]) - 65) for i in range(len(String))]
    LetterOffset = 0
    for i in range(len(StringList)):
        LetterOffset += 1
        NoneFont = pygame.image.load(path.join(directory, "Sprites//NoneList//NoneFont.png"))
        NoneFont.blit(Font, (-24*StringList[i], 0))
        screen.blit(NoneFont, (StartingX + 32*LetterOffset, StartingY))
        if LetterOffset > MaxCharacters:
            LetterOffset = 0
            StartingY += 40

def YOUDIED():
    DeathScreen = True
    while DeathScreen:
        print("HAHAHAHAHA")

#LoadDynamicObjectsList takes the strings from MovObjectsList, splits them and stores them in DOIS

#Handles Animations

#READ BEFORE LOOKING AT NewAnimate
#Animations are dont with lists and classes. The list ACL contains the necessary information to call all the player animations. 
#The first term of ACL is the definition of the class, the second term is the timer, the third term is the animation type, and the fourth term is a value to check if the sprite is flipped or not.
#First the animation is initialized using the class NewAnimate. The spritesheet is loaded, along with a string and ScaleFactorX and ScaleFactorY. The string tells NewAnimate how 
#to divide the class. START tells it that it is starting a new animation. The first number after the START is the frame at which that animation starts, and the following ones until the next STARTs or the END are frame intervals.
#Every single animation loops, so when it reaches the final number before the next START or END, it will loop back to frame 0
#For example, if a string goes (START, 0, 100, 200, 300, END) it will start at frame 0, run its internal timer at every tick, at 100 ticks it will swap to frame 1, at 200 frame 3, and when it reacher 300 it will go back to the starting frame, or 0
#Another example, (START, 0, 100, 200, START, 2, 150, 300, END) will storre 2 different animations. One starts at frame 0 and changes at ticks 100, 200 and the other one starts at frame 1 and changes at ticks 150, 300. These are 2 separate animations, and each indiviual object that is called this way can choose which animation it wants.
#ScaleFactorX and ScaleFactorY are for deciding how large each sprite is, since it messes with the animation. The resolution of any animated object is (64*ScaleFacrotX, 64*ScaleFactorY)

#Animations are done 
#TrueNone is suuuper important for animating!
TrueNone = pygame.image.load(path.join(directory, "Sprites//NoneList//None.png"))
class NewAnimate:
        def __init__(self, AnimatedSprite, string, ScaleFactorY, ScaleFactorX) -> None:
            self.AnimatedSprite = AnimatedSprite
            self.timer = 0
            StringList = string.split(", ")
            ListOfAnimations = []
            for i in range(len(StringList)):
                if StringList[i] == "START":
                    AnimateIntervalTimer = i + 1
                    CurrentAnimation = []
                    while StringList[AnimateIntervalTimer] != "START":
                        CurrentAnimation.append(float(StringList[AnimateIntervalTimer]))
                        AnimateIntervalTimer = AnimateIntervalTimer + 1
                        if StringList[AnimateIntervalTimer] == "END":
                            break
                    ListOfAnimations.append(CurrentAnimation)
            self.ExampleAnimationsList = ListOfAnimations
            self.ScaleFactorY = ScaleFactorY
            self.ScaleFactorX = ScaleFactorX
            self.OldX = 0
            self.OldY = 0
            self.Alpha = 256
            self.Angle = 0
        def PlayAnimation(self, X, Y, timer, WhichAnimation, IsFlipped):
            nonesprite = pygame.transform.scale_by(TrueNone, (1 + self.ScaleFactorX, 1 + self.ScaleFactorY))
            CurrentFrame = self.ExampleAnimationsList[WhichAnimation][0]
            for i in range(1, len(self.ExampleAnimationsList[WhichAnimation])):
                if timer >= self.ExampleAnimationsList[WhichAnimation][i]:
                    CurrentFrame += 1
                if timer >= self.ExampleAnimationsList[WhichAnimation][len(self.ExampleAnimationsList[WhichAnimation]) - 1]:
                    timer = 0

            OldReplace[0].append(self.OldX)
            OldReplace[1].append(self.OldY)
            OldReplace[2].append(self.ScaleFactorY)
            OldReplace[3].append(self.ScaleFactorX)
            for i in range(0, self.ScaleFactorY + 1):
                AppointSpecificStaticObjects(X + 32, Y + 32 + 64*self.ScaleFactorY)  
            nonesprite.blit(self.AnimatedSprite, (0 - 64*CurrentFrame*(self.ScaleFactorX + 1), 0))
            if IsFlipped == 1:
                nonesprite = pygame.transform.flip(nonesprite, 1, 0)
            if self.Angle != 0:
                nonesprite = pygame.transform.rotate(nonesprite, self.Angle)
            screen.blit(nonesprite, (X - XOffsetForScrolls, Y))
            self.OldX = X + 32
            self.OldY = Y + 32
            return(timer)
        def ChangeOpacity(self, NewAlpha):
            self.Alpha = NewAlpha
            self.AnimatedSprite.set_alpha(NewAlpha)
        def GetScaleFactors(self):
            return([self.ScaleFactorX, self.ScaleFactorY])
        def ChangeAngle(self, NewAngle):
            self.Angle = NewAngle
            

AnimationsList = [NewAnimate(pygame.image.load(path.join(directory, "Sprites//Player_Spritesheet.png")), "START, 0, 100, 200, 300, START, 2, 36, 72, 108, START, 5, 25, 150, 300, START, 8, 500, START, 9, 160, 310, START, 11, 110, 210, START, 13 , 75, END", 0, 0), NewAnimate(pygame.image.load(path.join(directory, "Sprites//Dash_Spritesheet.png")), "START, 0, 10, 20, 30, 40, 50, 55, 500, END", 0, 0), NewAnimate(pygame.image.load(path.join(directory, "Sprites//BAM.png")), "START, 0, 5, 10, 30, 45, 60, 68, 75, 200, END", 0, 0), NewAnimate(pygame.image.load(path.join(directory, "Sprites//BOOM.png")), "START, 0, 5, 15, 25, 35, 43, 50, 58, 500, END", 1, 0)]
AnimationsListDynamic = [NewAnimate(pygame.image.load(path.join(directory, "Sprites//DynamicObjects//Pellet_1.png")), "START, 0, 75, 150, 225, 300, END", 0, 0)]
AnimationsTimer = [0, 0, 0, 0]
AnimationsTimerDynamic = [0]
AnimationsMode = [0, 0, 0, 0]
AnimationsModeDynamic = [0]
AnimationsIsFlipped = [0, 0, 0, 0]
AnimationsIsFlippedDynamic = [0]
ACL = []
ACL.append(AnimationsList)
ACL.append(AnimationsTimer)
ACL.append(AnimationsMode)
ACL.append(AnimationsIsFlipped)
#RUNS MENU//////////////////////////////////////////////////////////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7
Menu_ParticlesList = [], [], [], [], [], []
Menu_Timer = 0
#For Menu_ParticlesList: X, Y, FinalY, Rotation, Scale
Menu_WhichItem_Global = 0
MenuAnimationsList = [[NewAnimate(pygame.image.load(path.join(directory, "Menu//MenuSelectorSpriteSheet.png")), "START, 0, 20, 40, 60, 80, 100, 120, END", 1, 4)], [0, 0], [0, 0], [0, 0]]
MenuFrame = pygame.image.load(path.join(directory, "Menu//Menu_Frame.png"))
PISOULS = pygame.image.load("Menu//PISOULS.png")
Menu_Particle = [pygame.transform.rotate(pygame.image.load(path.join(directory, "Menu//Menu_Particle_2.png")), 90*i) for i in range(0, 4)]
#pygame.mixer.music.load("Music//MENU.mp3")
#pygame.mixer.music.play(-1)
while MenuRun:
    if Menu_Timer <= 509:
        Menu_Timer += 1
    clock.tick(500)
    screen.fill((10, 0, 0))
    for i in range(0, len(Menu_ParticlesList[0])):
        Menu_PHParticle = pygame.transform.scale_by(Menu_Particle[Menu_ParticlesList[3][i]], Menu_ParticlesList[4][i])
        Menu_PHParticle.set_alpha(256 - 246*(Menu_ParticlesList[2][i]/Menu_ParticlesList[1][i])**2)
        screen.blit(Menu_PHParticle, (Menu_ParticlesList[0][i], Menu_ParticlesList[1][i]))
    screen.blit(MenuFrame, (223, 152))
    screen.blit(PISOULS, (203, 10))
    if Menu_Timer <= 510:
        MenuAnimationsList[0][0].ChangeOpacity(Menu_Timer/2)
        PISOULS.set_alpha(Menu_Timer/2)
    MenuAnimationsList[1][0] = MenuAnimationsList[0][0].PlayAnimation(320, 302 + 127*Menu_WhichItem_Global, MenuAnimationsList[1][0] + 1, 0, MenuAnimationsList[3][0])
    if random.randint(1, 2) == 2:
        Menu_ParticlesGenerated_SizeStore = random.randint(2, 10)/10
        Menu_ParticlesList[4].append(Menu_ParticlesGenerated_SizeStore)
        Menu_ParticlesList[5].append(0.2/Menu_ParticlesGenerated_SizeStore)
        Menu_ParticlesGenerated_X_store = random.randint(1, 236)
        Menu_ParticlesList[0].append(Menu_ParticlesGenerated_X_store)
        Menu_ParticlesList[1].append(960)
        Menu_ParticlesList[2].append(700 - 500*(Menu_ParticlesGenerated_X_store/256)*random.randint(0, 20)/(20*(Menu_ParticlesGenerated_SizeStore**(1/4))))
        Menu_ParticlesList[3].append(random.randint(0, 3))
        Menu_ParticlesGenerated_SizeStore = random.randint(2, 10)/10
        Menu_ParticlesList[4].append(Menu_ParticlesGenerated_SizeStore)
        Menu_ParticlesList[5].append(0.2/Menu_ParticlesGenerated_SizeStore)
        Menu_ParticlesGenerated_X_store = random.randint(740, 940)
        Menu_ParticlesList[0].append(Menu_ParticlesGenerated_X_store)
        Menu_ParticlesList[1].append(960)
        Menu_ParticlesList[2].append(700 - 500*(abs(940 - Menu_ParticlesGenerated_X_store)/200)*random.randint(0, 20)/(20*(Menu_ParticlesGenerated_SizeStore**(1/6))))
        Menu_ParticlesList[3].append(random.randint(0, 3))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_x or event.key == pygame.K_SPACE or event.key == pygame.K_k):
                if Menu_WhichItem_Global == 0:
                    Menu_ParticlesList = [], [], [], [], [], []
                    MenuRun = False
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.image.load("Menu//loading....png"), (0, 0))
                    f = open("Save.txt", "r")
                    CurrentGlobalLevel = int(f.readline())
                    PlayerIframesAndHP[2] = int(f.readline())
                    PlayerSpawnPos[0][0] = float(f.readline())
                    PlayerSpawnPos[0][1] = float(f.readline())
                    PlayerSpawnPos[1][0] = int(f.readline())
                    f.close()
                    PlayerX = PlayerSpawnPos[0][0]
                    PlayerY = PlayerSpawnPos[0][1]
                    CurrentScene = PlayerSpawnPos[1][0]
                    MovObjectsList, BlockAppendix = MapLoader.LoadLevel(CurrentGlobalLevel)
                    YList, BgColor = MapLoader.LoadScene(YList, CurrentScene, CurrentGlobalLevel, PlayerSpawnPos)
                    break
                if Menu_WhichItem_Global == 1:
                    f = open("Save.txt", "w")
                    f.write("1\n0\n50\n500\n0\n")
                    f.close()  
                    PlayerSpawnPos = [50, 500], [0]
                    PlayerX = PlayerSpawnPos[0][0]
                    PlayerY = PlayerSpawnPos[0][1]
                    CurrentScene = 0
                    PlayerIframesAndHP[2] = 0
                    CurrentGlobalLevel = 1
                    MovObjectsList, BlockAppendix = MapLoader.LoadLevel(CurrentGlobalLevel)
                    YList, BgColor = MapLoader.LoadScene(YList, CurrentScene, CurrentGlobalLevel, PlayerSpawnPos)
                    Menu_ParticlesList = [], [], [], [], [], []
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.image.load("Menu//loading....png"), (0, 0))
                    MenuRun = False
                    break
                if Menu_WhichItem_Global == 2:
                    pygame.quit()
            if event.key == pygame.K_DOWN and Menu_WhichItem_Global <= 1 and Menu_Timer >= 510:
                Menu_WhichItem_Global += 1
            if event.key == pygame.K_UP and Menu_WhichItem_Global >= 1 and Menu_Timer >= 510:
                Menu_WhichItem_Global -= 1
        if event.type == pygame.QUIT:
            pygame.quit()
            DeathRun = False
            run = False
            GlobalRun = False
    if len(Menu_ParticlesList[0]) > 0:
        Menu_ParticlesToBeDeleted = []
        for i in range(0, len(Menu_ParticlesList[0])):
            Menu_ParticlesList[1][i] -= Menu_ParticlesList[5][i]
            if Menu_ParticlesList[1][i] <= Menu_ParticlesList[2][i]:
                Menu_ParticlesToBeDeleted.append(i)
        for i in range(len(Menu_ParticlesToBeDeleted)):
            for a in range(0, len(Menu_ParticlesList)):
                Menu_ParticlesList[a].pop(Menu_ParticlesToBeDeleted[i])
    pygame.display.update()   

#Initializes DOIS YList and bg for the first level
DOIS = StaticObjManager.LoadDynamicObjectsList(MovObjectsList, CurrentScene)
BgReplace.fill(BgColor)
screen.fill(BgColor)
StaticObjManager.LoadStaticObjects(YList[0], YList[1], YList[2], YList[3], YList[4], YList[5], YList[6], YList[7], YList[8], YList[9], screen, BlockAppendix, XOffsetForScrolls)

for i in range(len(DOIS[0])):
    DACL[0].append(NewAnimate(pygame.image.load(path.join(directory, DynamicAnimationsAppendix[int(DOIS[0][i])])), DynamicAnimationStringAppendix[int(DOIS[0][i])], DynamicAniimationScaleFactorYAppendix[int(DOIS[0][i])], DynamicAniimationScaleFactorXAppendix[int(DOIS[0][i])]))
    DACL[1].append(0)
    DACL[2].append(0)
    DACL[3].append(0)

#Blits things the first time the level is loaded
screen.blit(HPpoint, (2*PlayerIframesAndHP[1] -89, 640))
screen.blit(BottomGameBar, (0, 640))
#TypeNStuff("USE WASD OR ARROW KEYS TO MOVE                     PRESS SPACE OR X TO JUMP", 20, 20, 16)
#Runs Game ///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7///////////////////////////////////////////////////7
GlobalRun = True
while GlobalRun:
    DeathRun = True

#SHOW MAP
    GetRidOfRandomStuff = 0
#GAME BEGINS
    while run:
        #Sets FPS
        clock.tick(150)
        if GetRidOfRandomStuff < 5:
            GetRidOfRandomStuff += 1
        if GetRidOfRandomStuff == 5:
            screen.fill(BgColor)
            StaticObjManager.LoadStaticObjects(YList[0], YList[1], YList[2], YList[3], YList[4], YList[5], YList[6], YList[7], YList[8], YList[9], screen, BlockAppendix, XOffsetForScrolls)
            GetRidOfRandomStuff += 1
            screen.blit(HPpoint, (2*PlayerIframesAndHP[1] -89, 640))
            screen.blit(BottomGameBar, (0, 640))
        #Blits Attack Colliders if debug is turned on and other random debug things
        if Debug:
            for i in range(len(DashHitboxList[0])):
                screen.blit(ColGeneral, (DashHitboxList[0][i] - XOffsetForScrolls, DashHitboxList[1][i]))
        if Debug:
            screen.blit(ColGeneral, (PlayerX + 32 - XOffsetForScrolls, PlayerY + 32))
            for i in range(0, len(DashHitboxList)):
                screen.blit(ColGeneral, (DashHitboxList[0][i], DashHitboxList[1][i]))
        #For level construction
       #print(round((PlayerX)/64), round((PlayerY)/64), CurrentScene)

        #Sets all the variables that must be set
        PlayerStaticBool = False
        SpecificStaticObjects = [], []        

        #Replaces old dynamic object positions
        for i in range(len(OldReplace[0])):
            if OldReplace[0][i] >= 0 and OldReplace[1][i] >= 0:
                for e in range(0, OldReplace[3][i] + 1):
                    for a in range(0, OldReplace[2][i] + 1):
                        AppointSpecificStaticObjects(OldReplace[0][i] + 64*e, OldReplace[1][i] + 64*a)
            screen.blit(pygame.transform.scale_by(BgReplace, (1 + OldReplace[3][i], 1 + OldReplace[2][i])), (OldReplace[0][i] - XOffsetForScrolls - 32, OldReplace[1][i] - 32  ))
        #OldReplace must be cleared after replacing old dynamic objects
        OldReplace = [], [], [], []

        #Handles Dashing Animations
        if DashFrameTimer != 0:
            ACL[1][1] = ACL[0][1].PlayAnimation(DashHitboxList[0][0] - 32, DashHitboxList[1][0] - 32, ACL[1][1] + 1, ACL[2][1], ACL[3][1])


        #EVERYTHING TO DO WITH DYNAMIC OBJECTS!!! (Except replacing old positions)
        #Renders Dynamic Objects and runs scripts
        for i in range(len(DOIS[0])):
            DOIS, SpawnList, PlayerSpawnPos, PlayerY, PlayerX, MovObjectsList, BlockAppendix, BgColor, BgReplace, PortalCalled = EnemyScripts.DynamicObjectScripts(i, DOIS, DACL, PlayerX, PlayerY, PlayerIframesAndHP, SpawnList, DashHitboxList, YList, Debug, screen, ColVisualFloor, XOffsetForScrolls, PlayerSpawnPos, CurrentScene, BlockAppendix, HPpoint, BottomGameBar, BgColor, CurrentGlobalLevel, MovObjectsList, BgReplace)
        #Spawns in new dynamic objects
        if 1000 not in DOIS[0]:
            for a in range(0, len(SpawnList)):
                for i in range(0, len((SpawnList[a].split(", ")))):
                    DOIS[i].append(round(float((SpawnList[a].split(", "))[i])))
                for i in range(len((SpawnList[a].split(", "))), len(DOIS)):
                    DOIS[i].append("")
                DACL[0].append(NewAnimate(pygame.image.load(path.join(directory, DynamicAnimationsAppendix[int(SpawnList[a].split(", ")[0])])), DynamicAnimationStringAppendix[int(SpawnList[a].split(", ")[0])], DynamicAniimationScaleFactorYAppendix[int(SpawnList[a].split(", ")[0])], DynamicAniimationScaleFactorXAppendix[int(SpawnList[a].split(", ")[0])]))
                DACL[1].append(0)   
                DACL[2].append(0)
                DACL[3].append(0)
            SpawnList = []
        #Deletes dynamic objects with a tag of 1000
        DOIS, DACL = EnemyScripts.DOIS_Delete(DOIS, DACL)


        #Changes Player Variables
        PlayerX = PlayerX + PlayerSpeed[0]
        PlayerY = PlayerY + PlayerSpeed[1]
        if PlayerSpeed[1] >= 2.8:
            PlayerSpeed[1] = 2.8
        if PlayerX <= 0:
            PlayerX = 0
        if PlayerY >= 570: 
            PlayerIframesAndHP[4] = 100
            PlayerIframesAndHP[0] = 1
        PlayerSpeed[1] += PlayerAcc[1] 
        
        #Handles player collision in another script (StaticObjColliders)
        PlayerSpeed, PlayerY, IsPlayerTouchingFloor, IsPlayerTouchingRoof, IsPlayerTouchingLeft, IsPlayerTouchingRight, HasPlayerDashed = StaticObjColliders.InitCollider(PlayerSpeed, PlayerY, XOffsetForScrolls, PlayerX, BlockAppendix, Debug, screen, ColVisualRight, ColVisualLeft, YList, ColVisualFloor, ColVisualRoof, HasPlayerDashed)


        #Manages Player HP and Iframes
        if PlayerIframesAndHP[0] >= 1:
            PlayerStaticBool = True
            if PlayerIframesAndHP[0] == 1:
                PlayerSpeed[0] = 0
                DashFrameTimer = 0
                PlayerIframesAndHP[1] = PlayerIframesAndHP[1] - PlayerIframesAndHP[4]*PlayerBlockFactor[0]
            PlayerIframesAndHP[0] += 2
            if 1 <= PlayerIframesAndHP[0] < 24 and IsPlayerTouchingLeft == 0 and IsPlayerTouchingRight == 0:
                PlayerSpeed[0] = PlayerIframesAndHP[3]*PlayerBlockFactor[1]
                PlayerSpeed[1] = PlayerIframesAndHP[5]
        if PlayerIframesAndHP[0] >= 25:
            PlayerStaticBool = False
        if PlayerIframesAndHP[0] >= 450:
            PlayerIframesAndHP[0] = 0
        if PlayerIframesAndHP[1] <= 0:
            run = False
        if PlayerIframesAndHP[1] > 100:
            PlayerIframesAndHP[1] = 100
        #Manages constant key inputs
        key = pygame.key.get_pressed()
        if (key[pygame.K_z] == True or key[pygame.K_l] == True) and IsPlayerTouchingFloor and PlayerStaticBool == False and PlayerSpeed[0] == 0:
            PlayerStaticBool = True
            PlayerSpeed[0] = 0
            if PlayerCharge <= 1670:
                PlayerCharge += 1
        else:
            if PlayerCharge!= 0:
                PlayerChargeTimer += 1
            PlayerCharge = 0
        #This stuff flips the player too
        if key[pygame.K_RIGHT] == True and key[pygame.K_LEFT] == False and IsPlayerTouchingRight == False and PlayerStaticBool == False and DashFrameTimer == 0 and PlayerChargeTimer == 0:
            PlayerSpeed[0] = 0.6*GameTickFactor
            if IsPlayerTouchingFloor:
                ACL[2][0] = 1
            ACL[3][0] = 0
            ACL[3][1] = 0
        elif key[pygame.K_LEFT] == True and key[pygame.K_RIGHT] == False and IsPlayerTouchingLeft == False and PlayerStaticBool == False and DashFrameTimer == 0 and PlayerChargeTimer == 0:
            PlayerSpeed[0] = -0.6*GameTickFactor
            if IsPlayerTouchingFloor:
                ACL[2][0] = 1
            ACL[3][0] = 1
            ACL[3][1] = 1
        elif key[pygame.K_d] == True and key[pygame.K_a] == False and IsPlayerTouchingRight == False and PlayerStaticBool == False and DashFrameTimer == 0:
            PlayerSpeed[0] = 0.6*GameTickFactor
            if IsPlayerTouchingFloor:
                ACL[2][0] = 1
            ACL[3][0] = 0
            ACL[3][1] = 0
        elif key[pygame.K_a] == True and key[pygame.K_d] == False and IsPlayerTouchingLeft == False and PlayerStaticBool == False and DashFrameTimer == 0:
            PlayerSpeed[0] = -0.6*GameTickFactor
            if IsPlayerTouchingFloor:
                ACL[2][0] = 1
            ACL[3][0] = 1
            ACL[3][1] = 1
        elif ((key[pygame.K_RIGHT] == False and key[pygame.K_LEFT] == False) or (key[pygame.K_RIGHT] == True and key[pygame.K_LEFT] == True)) and DashFrameTimer == 0 and PlayerStaticBool == 0:
            PlayerSpeed[0] = 0
            if PlayerCharge == 0:
                ACL[2][0] = 0
        if (key[pygame.K_s] == True or key[pygame.K_DOWN] == True) and IsPlayerTouchingFloor and PlayerStaticBool == False and PlayerIframesAndHP[0] == 0:
            PlayerBlockFactor = [0.5, 0.2]
            PlayerSpeed[0] = 0
            PlayerChargeTimer = 0
            ACL[2][0] = 6
        elif PlayerIframesAndHP[0] == 0:
            PlayerBlockFactor = [1, 1]
        DashHitboxList, PlayerStaticBool, PlayerSpeed, DashFrameTimer = PlayerDashNSmash.PlayerDash(DashFrameTimer, DashHitboxList, PlayerX, PlayerY, PlayerSpeed, IsPlayerTouchingFloor, PlayerStaticBool, PlayerIframesAndHP)
        if ACL[2][0] != 6:
            WhichCharge, ACL, DashHitboxList, PlayerSpeed, PlayerStaticBool, PlayerChargeTimer = PlayerDashNSmash.PlayerSmash(PlayerChargeTimer, PlayerCharge, ACL, WhichCharge, PlayerSpeed, DashHitboxList, PlayerX, PlayerY, PlayerStaticBool)
       #This must be called after key inputs. Why? only god knows now :)
        if IsPlayerTouchingFloor:
            PlayerAcc[1] = 0
            PlayerSpeed[1] = 0
        else:
            PlayerAcc[1] = 0.016*GameTickFactor**(3/2)
            if DashFrameTimer == 0:
                ACL[2][0] = 2
            else:
                ACL[2][0] = 3
            IsPlayerTouchingFloor = False

        #Single Key Inputs and other events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_x or event.key == pygame.K_SPACE or event.key == pygame.K_k) and IsPlayerTouchingFloor and PlayerStaticBool == False and DashFrameTimer == 0:
                    PlayerSpeed[1] = -1.75*GameTickFactor
                    PlayerY -= 5
                    IsPlayerTouchingFloor = False
                if (event.key == pygame.K_z or event.key == pygame.K_l) and PlayerStaticBool == False and HasPlayerDashed == False and IsPlayerTouchingFloor == False and PlayerSpeed[0] != 0:
                    HasPlayerDashed = True
                    PlayerStaticBool = True
                    DashFrameTimer = 1
                    ACL[1][0] = 0
                    ACL[1][1] = 0
                if event.key == pygame.K_n and Debug:
                    Debug = False
                elif event.key == pygame.K_n and Debug == False:
                    Debug = True
            if event.type == pygame.QUIT:
                run = False
                GlobalRun = False
                DeathRun = False

        #SCROLLING;
        #Handles Scrolling Forwards
        if PlayerX - XOffsetForScrolls >= 400 and  XOffsetForScrolls <= 64*(len(YList[0])-17) + 1:
            XOffsetForScrolls += 4
            screen.fill(BgColor)
            screen.blit(HPpoint, (2*PlayerIframesAndHP[1] -89, 640))
            screen.blit(BottomGameBar, (0, 640))
            StaticObjManager.LoadStaticObjects(YList[0], YList[1], YList[2], YList[3], YList[4], YList[5], YList[6], YList[7], YList[8], YList[9], screen, BlockAppendix, XOffsetForScrolls)
            for i in range(len(DOIS[0])):
                if abs(DOIS[1][i] - PlayerX) <= 1000:
                    DACL[1][i] = DACL[0][i].PlayAnimation(DOIS[1][i] + 1, DOIS[2][i] + 1, DACL[1][i] + 1, DACL[2][i], DACL[3][i])
            if DashFrameTimer != 0:
                ACL[1][1] = ACL[0][1].PlayAnimation(DashHitboxList[0][0] - 32, DashHitboxList[1][0] - 32, ACL[1][1] + 1, ACL[2][1], ACL[3][1])

        #Scrolling Backwards
        if PlayerX - XOffsetForScrolls <= 100 and XOffsetForScrolls >= 1:
            XOffsetForScrolls -= 4
            screen.fill(BgColor)
            screen.blit(HPpoint, (2*PlayerIframesAndHP[1] -89, 640))
            screen.blit(BottomGameBar, (0, 640))
            StaticObjManager.LoadStaticObjects(YList[0], YList[1], YList[2], YList[3], YList[4], YList[5], YList[6], YList[7], YList[8], YList[9], screen, BlockAppendix, XOffsetForScrolls)
            if DashFrameTimer != 0:
                ACL[1][1] = ACL[0][1].PlayAnimation(DashHitboxList[0][0] - 32, DashHitboxList[1][0] - 32, ACL[1][1] + 1, ACL[2][1], ACL[3][1])
        if PortalCalled:
            CurrentScene = 0
            CurrentGlobalLevel += 1
            PlayerX = 50
            PlayerY = 500
            PlayerSpawnPos = [PlayerX, PlayerY], [CurrentScene]
            MovObjectsList, BlockAppendix = MapLoader.LoadLevel(CurrentGlobalLevel)
            YList, BgColor = MapLoader.LoadScene(YList, CurrentScene, CurrentGlobalLevel, PlayerSpawnPos)
            BgReplace.fill(BgColor)
            screen.fill(BgColor)
            StaticObjManager.LoadStaticObjects(YList[0], YList[1], YList[2], YList[3], YList[4], YList[5], YList[6], YList[7], YList[8], YList[9], screen, BlockAppendix, XOffsetForScrolls)
            DOIS = StaticObjManager.LoadDynamicObjectsList(MovObjectsList, CurrentScene)
            PortalCalled = False
        #Player Iframe Animations (I think)
        if PlayerIframesAndHP[0] == 3:
            screen.blit(HPpoint, (2*PlayerIframesAndHP[1] -89, 640))
            screen.blit(BottomGameBar, (0, 640))
        if PlayerIframesAndHP[0] in [5*i for i in range(1, 200)] or PlayerIframesAndHP[0] in [5*i+1 for i in range(1, 200)] or PlayerIframesAndHP[0] in [5*i+2 for i in range(1, 200)]:
            ACL[0][0].ChangeOpacity(128)
        else:
            ACL[0][0].ChangeOpacity(256)

        for i in range(len(str(PlayerIframesAndHP[2]))):
            screen.blit(NumberSpriteList[int(str(PlayerIframesAndHP[2])[i])], (656 + 32*i, 656))

        #PlayerAnimation and Static Object Replacement
        ACL[1][0] = ACL[0][0].PlayAnimation(PlayerX, PlayerY, ACL[1][0] + 1, ACL[2][0], ACL[3][0])
        StaticObjManager.LoadSpecificStaticObjects(YList[0], YList[1], YList[2], YList[3], YList[4], YList[5], YList[6], YList[7], YList[8], YList[9], SpecificStaticObjects, screen, BlockAppendix, YList, XOffsetForScrolls, PlayerIframesAndHP, NumberSpriteList, HPpoint, BottomGameBar)
        
        #Loads in a new level if the player reacher the end!!
        if PlayerX >= 64*len(YList[0]) - 140:
            XOffsetForScrolls = 0
            PlayerX = 0
            CurrentScene = CurrentScene + 1
            DOIS = StaticObjManager.LoadDynamicObjectsList(MovObjectsList, CurrentScene)
            YList, BgColor = MapLoader.LoadScene(YList, CurrentScene, CurrentGlobalLevel, PlayerSpawnPos)
            screen.fill(BgColor)
            screen.blit(HPpoint, (2*PlayerIframesAndHP[1] -89, 640))
            screen.blit(BottomGameBar, (0, 640))
            BgReplace.fill(BgColor)
            StaticObjManager.LoadStaticObjects(YList[0], YList[1], YList[2], YList[3], YList[4], YList[5], YList[6], YList[7], YList[8], YList[9], screen, BlockAppendix, XOffsetForScrolls)
            DACL = [[], [], [], []]
            for i in range(len(DOIS[0])):
                DACL[0].append(NewAnimate(pygame.image.load(path.join(directory, DynamicAnimationsAppendix[int(DOIS[0][i])])), DynamicAnimationStringAppendix[int(DOIS[0][i])], DynamicAniimationScaleFactorYAppendix[int(DOIS[0][i])], DynamicAniimationScaleFactorXAppendix[int(DOIS[0][i])]))
                DACL[1].append(0)
                DACL[2].append(0)
                DACL[3].append(0)
                           
        pygame.display.update()

    pygame.mixer.music.stop()
#DEATH SCREEN
    deathscreentimer = 0
    pygame.mixer.Sound.play(pygame.mixer.Sound("SFX//YOUDIED.mp3"))
    while DeathRun:
        if deathscreentimer == 0:
            f = open("Save.txt", "r")
            print(CurrentGlobalLevel)
            print(PlayerSpawnPos)
            CurrentGlobalLevel = int(f.readline())
            PlayerIframesAndHP[2] = int(f.readline())
            f.close()
            PlayerIframesAndHP[2] -= 200
            if PlayerIframesAndHP[2] <= 0:
                PlayerIframesAndHP[2] = 0
            f = open("Save.txt", "w")
            f.write(str(CurrentGlobalLevel) + "\n" + str(PlayerIframesAndHP[2]) + "\n" + str(PlayerSpawnPos[0][0]) + "\n" + str(PlayerSpawnPos[0][1]) + "\n" + str(PlayerSpawnPos[1][0]))
            f.close()    
        if deathscreentimer < 255:
            deathscreentimer += 1
        screen.fill((0, 0, 0))
        youdiedblit.set_alpha(deathscreentimer)
        screen.blit(youdiedblit, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                DeathRun = False
                GlobalRun = False
            if event.type == pygame.KEYDOWN and deathscreentimer > 250:
                DeathRun = 0
                run = 1
                PlayerIframesAndHP[0] = 0
                PlayerIframesAndHP[1] = 100
                PlayerIframesAndHP[3] = 0
                PlayerIframesAndHP[4] = 0
                PlayerIframesAndHP[5] = 0

                XOffsetForScrolls = 0
                PlayerX = PlayerSpawnPos[0][0]
                PlayerY = PlayerSpawnPos[0][1]
                CurrentScene = PlayerSpawnPos[1][0]
                DOIS = StaticObjManager.LoadDynamicObjectsList(MovObjectsList, CurrentScene)
                YList, BgColor = MapLoader.LoadScene(YList, CurrentScene, CurrentGlobalLevel, PlayerSpawnPos)
                screen.fill(BgColor)
                screen.blit(HPpoint, (2*PlayerIframesAndHP[1] -89, 640))
                screen.blit(BottomGameBar, (0, 640))
                for i in range(len(str(PlayerIframesAndHP[2]))):
                    screen.blit(NumberSpriteList[int(str(PlayerIframesAndHP[2])[i])], (656 + 32*i, 656))
                BgReplace.fill(BgColor)
                StaticObjManager.LoadStaticObjects(YList[0], YList[1], YList[2], YList[3], YList[4], YList[5], YList[6], YList[7], YList[8], YList[9], screen, BlockAppendix, XOffsetForScrolls)
                DACL = [[], [], [], []]
                for i in range(len(DOIS[0])):
                    DACL[0].append(NewAnimate(pygame.image.load(DynamicAnimationsAppendix[int(DOIS[0][i])]), DynamicAnimationStringAppendix[int(DOIS[0][i])], DynamicAniimationScaleFactorYAppendix[int(DOIS[0][i])], DynamicAniimationScaleFactorXAppendix[int(DOIS[0][i])]))
                    DACL[1].append(0)
                    DACL[2].append(0)
                    DACL[3].append(0)
pygame.quit()
print("Hi Elisa")