from PIL import Image
import pygame
from os import path
directory = path.dirname(path.abspath(__file__))

OldTrack = 0
GlobalLevelsList = [r"Levels//Level 0.png", r"Levels//Level 1.png", r"Levels//Castle.png", r"Levels//4444.png"]
TutorialBlockList = []
GoblinsBlockList = [(0, 0, 0, 0), (255, 249, 189, 255), (77, 109, 243, 255), (240, 231, 149, 255), (50, 75, 173, 255), (180, 180, 180, 255), (0, 0, 1, 255), (255, 242, 0, 255), (204, 193, 43, 255)]
CastleBlockList = [(0, 0, 0, 0), (130, 134, 184, 255), (80, 75, 110, 255), (60, 56, 82, 255), (186, 132, 146, 255), (112, 76, 84, 255), (56, 38, 41, 255), (34, 212, 84, 255), (34, 177, 76, 255), (24, 133, 55, 255), (0, 183, 239, 255), (255, 126, 0, 255), (130, 134, 184, 255), (205, 95, 227, 255), (180, 59, 204, 255), (108, 10, 128, 255), (235, 115, 203, 255), (214, 32, 163, 255), (153, 17, 117, 255), (212, 245, 154, 255), (206, 224, 175, 255)]
FOURCOLORS = [(0, 0, 0, 0), (0, 183, 239, 255), (47, 54, 153, 255)]
BlockColorLists = [TutorialBlockList, GoblinsBlockList, CastleBlockList, FOURCOLORS]

#The lists containing the positions of all dynamic objects for the different levels are stored here!
TutorialMovList = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
GoblinsMovList = ["6, 9, 6, 0, 0, 1"], ["2, 9, 5, 0, 0, 0.2, 0", "6, 14, 6, 0, 0, 2"], [ "6, 9, 4, 0, 0, 0", "2, 13, 4, 0, 0, 0.5, 0"], ["6, 12, 7, 0, 0, 1", "6, 14, 3, 0, 0, 0", "2, 8, 4, 0, 0, 0.2, 0", "2, 17.5, 4, 0, 0, 0.5, 0", "6, 25, 4, 0, 0, 0", "10, 24, 3, 10"], ["6, 8, 6, 0, 0, 1", "2, 10.5, 3.5, 0, 0, 0.3, 0", "6, 16, 3, 0, 0, 0", "6, 23, 8, 0, 0, 1", "6, 28, 4, 0, 0, 1"], ["6, 12, 1, 0, 0, 1", "2, 14.5, 5, 0, 0, 0.2, 0", "6, 20, 3, 0, 0, 1", "10, 20, 0.5, 10"], ["6, 14, 7, 0, 0, 1", "2, 6, 1, 0, 0, 0.2, 0"], ["6, 8, 8, 0, 0, 0", "2, 9, 5, 0, 0, 0.4, 0", "2, 15, 3, 0, 0, 0.3, 0", "6, 13, 8, 0, 0, 1", "6, 19, 6, 0, 0, 1", "6, 22, 4, 0, 0, 0", "6, 19, 4, 0, 0, 0", "2, 21, 2, 0, 0, 0.2, 0", "6, 28, 4, 0, 0, 1", "20, 28.5, 1.5", "9, 28, 1"], ["1, 7, 2, 0"], ["3, 5, 7", "3, 6, 7", "3, 6, 6", "3, 7, 6", "3, 9, 5", "3, 9, 4", "3, 8, 5", "3, 8, 4", "3, 9, 3", "3, 10, 3"], ["4, 7.1, 6.05, 0, 4.05, 6.05", "4, 12.1, 8.05, 0, 6.05, 12.1", "3, 10, 1", "3, 10, 2", "3, 11, 1", "3, 11, 2", "3, 12, 1", "3, 12, 2", "3, 13, 1", "3, 13, 2", "3, 14, 1", "3, 14, 2", "3, 5, 4"], ["10, 5, 1, 20", "2, 8, 3, 0, 0, 0.6, 0", "4, 7.1, 6.9, 0, 5.9, 6.9", "4, 14.1, 6.05, 0, 4.05, 6.05", "4, 18.1, 4.05, 0, 2, 4.05", "4, 23.1, 6.95, 0, 0, 6.95", "4, 24.1, 6.95, 0, 0, 6.95", "3, 3, 3", "3, 18, 3", "3, 18, 2", "6, 9, 7, 0, 0, 1", "2, 13, 3, 0, 0, 0.2, 0"], ["2, 12.5, 5, 0, 0, 0.4, 0", "4, 10.1, 6.8, 0, 5.05, 6.8", "3, 5, 4", "3, 5, 5", "3, 5, 6"], ["2, 3.5, 2, 0, 0, 0.2, 0", "4, 5.1, 6.7, 0, 4.7, 6.7", "3, 11, 3", "2, 9, 3, 0, 0, 0.7, 0", "2, 14, 6, 0, 0, 0.4, 0"], ["10, 2.5, 0.5, 10", "6, 22.5, 2, 0, 0, 0", "6, 12.6, 2, 0, 0, 0", "6, 25.4, 2, 0, 0, 0", "4, 6.1, 7.05, 0, 5.05, 7.05", "4, 9.1, 5.05, 0, 3.05, 5.05", "4, 12.1, 3.05, 0, 1.05, 3.05", "4, 19.1, 6.7, 0, 4.7, 6.7", "4, 25.1, 3.2, 0, 0.7, 3.2", "3, 23, 3", "2, 28, 2, 0, 0, 0.7, 0", "4, 32.1, 3.2, 0, 0.7, 3.2", "3, 29, 7", "3, 29, 8", "3, 28, 7", "3, 28, 8", "20, 28.5, 7.5", "10, 35, 4.5, 15"], ["4, 16.1, 6.7, 0, 4.7, 6.7", "4, 20.1, 4.7, 0, 2.7, 4.7", "4, 10.1, 6, 0, 4, 6", "2, 18, 4, 0, 0, 0.7, 0", "2, 13, 6, 0, 0, 0.3, 0", "9, 27, 1"], ["21, 7, 4, 0"]
CastleMovList = [], ["12, 1, 0, 0, 0", "12, 15, 3, 0, 0", "13, 16, 7, 0, 100, 0", "12, 17, 0, 0, 0", "12, 20, 3, 0, 0", "12, 32, 2, 0, 0", "12, 30, 6, 0, 0", "12, 35, 3, 0, 0", "12, 40, 5, 0, 0", "13, 40, 5, 0, 100, 0", "13, 23, 4, 0, 100, 0", "15, 24, 6, -1", "15, 27, 6, -1", "15, 40, 6, -1"], ["7, 7, 5, 0.1, 7, 2, 100", "13, 12, 7, 0, 100, 0"], ["13, 12, 2, 0, 100, 0", "14, 7, 5, -1, 0", "14, 13, 2, -1, 0"], ["14, 4, 1.5, -1, 1", "14, 4, 0.5, -1, 1", "14, 16, 6.5, -1, 0", "19, 12, 1"], ["14, 4, 7.5, 1, 0", "14, 4, 5.5, 1, 0", "14, 12, 2.5, -1, 1", "20, 11.5, 1.5"], [], ["16, 3, 4, 0, 0, 135, 10, 0, 0, 0"], ["1, 13.8, 3, 0"], [], ["4, 7.1, 6.55, 0, 0.05, 6.55", "2, 13, 2.5, 0, 0, 0.3, 0", "7, 3, 3, 0.1, 3, 2, 100", "7, 13, 3, 0.1, 13, 2, 100", "6, 13, 3, 0, 0, 1"], ["19, 7, 1", "19, 19, 1", "19, 28, 1", "19, 34, 1", "19, 1, 1, 1", "19, 13, 1, 1"], ["12, 2, 7, 0, 0", "12, 1, 11, 0, 0", "13, 16, 5, 0, 100, 0", "13, 11, 4, 0, 100, 0", "13, 8, 4, 0, 100, 0", "7, 9, 3, 0.1, 9, 2, 100", "7, 14, 4, 0.1, 14, 2, 100", "14, 17, 4, -1, 0", "9, 19, 0", "14, 26, 8, -1, 1", "7, 29, 6, 0.1, 29, 2, 20", "7, 33, 7, 0.1, 33, 2, 20", "7, 40, 6, 0.1, 38, 2, 20", "2, 41.5, 6, 0, 0, 0.4, 0"], ["10, 19, 1, 50", "7, 13, 1, 0.1, 14, 2, 20", "7, 20, 1, 0.1, 19, 2, 30", "6, 19, 2, 0, 0, 1", "2, 16, 3, 0, 0, 0.4, 0", "4, 22.1, 5.55, 0, 3.05, 5.55", "2, 33, 7.6, 0, 0, 0.2, 0", "19, 2.5, 1, 1", "19, 8.5, 1, 1", "2, 9.5, 3, 0, 0, 0.4, 0", "19, 25, 1, 0", "7, 37, 1, 0.1, 37, 2, 30", "13, 35, 5, 0, 100, 0", "14, 34, 3, -1, 0", "14, 22, 2, -1, 0", "20, 42.5, 1", "4, 30.6, 3.55, 0, 1.05, 3.55", "14, 31, 6, -1, 0"], ["1, 7, 6, 0"], ["22, 14, 4, 0, 1, 896, 256, 0, 40, 0, 0, 0", "25, 14, 4, 0, 0, 896, 256"], ["6, 9, 6, 0, 0, 1"]
FOURMOVEMENTLISTS = ["9, 8, 5"], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
MovListList = [TutorialMovList, GoblinsMovList, CastleMovList, FOURMOVEMENTLISTS]
#"14, 3, 3, 1", 

#, "25, 14, 4, 0, 0, 896, 256"

#The lists containing the positions of all static blocks in each level!
GoblinsAppendix = [pygame.image.load(path.join(directory, "Sprites//NoneList//None.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_L1//Tile_Grass1.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_L1//Tile_Ground.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_L1//Tile_Grass2.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_L1//Tile_Goblin_Cave_Left.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_L1//Tile_Brick1.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_L1//Tile_Brick_Destructible.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_L1//Tile_DrillBlock.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_L1//Tile_DrillBlock_Double.png"))], ["", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static"]
CastleBlockAppendix = [pygame.image.load(path.join(directory, "Sprites//NoneList//None.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Castle_TopTile_Left.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Castle_TopTile_Center.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Castle_TopTile_Right.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Castle_BottomTile_Left.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Castle_BottomTile_Center.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Castle_BottomTile_Right.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Castle_GrassTile_Left.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Castle_GrassTile_Center.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Castle_GrassTile_Right.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Castle_Window.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Castle_OrangePumpDoor.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Castle_PurplePumpDoor.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Inner_TopTile_Left.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Inner_TopTile_Center.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Inner_TopTile_Right.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Inner_BottomTile_Left.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Inner_BottomTile_Center.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Inner_BottomTile_Right.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Interior_PillarC.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_Castle//Tiles_Interior_PillarS.png"))], ["", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "Static", "", "", ""]
TutorialBlockAppendix = []
FOURBLOCKS = [pygame.image.load(path.join(directory, "Sprites//NoneList//None.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_L1//Tile_DarkGrass1.png")), pygame.image.load(path.join(directory, "Sprites//Tiles_L1//Tile_DarkGrass2.png"))], ["", "Static", "Static"]
BlockAppendixList = [TutorialBlockAppendix, GoblinsAppendix, CastleBlockAppendix, FOURBLOCKS]

GoblinsBG = [(165, 191, 230), (165, 191, 230), (165, 191, 230), (165, 191, 230), (165, 191, 230), (165, 191, 230), (165, 191, 230), (165, 191, 230), (165, 191, 230), (176, 176, 176), (176, 176, 176), (176, 176, 176), (176, 176, 176), (176, 176, 176), (176, 176, 176), (176, 176, 176), (176, 176, 176), (176, 176, 176), (176, 176, 176), (176, 176, 176)]
CastleBG = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (7, 9, 38), (7, 9, 38), (7, 9, 38), (0, 0, 0), (7, 9, 38), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
TutorialBG = []
FOURBG = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (7, 9, 38), (7, 9, 38), (7, 9, 38), (0, 0, 0), (7, 9, 38), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
BGList = [TutorialBG, GoblinsBG, CastleBG, FOURBG]

TutorialMusic = []
GoblinsMusic = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
CastleMusic = [2, 2, 2, 2, 2, 2, 2, 3, 2, 4, 4, 4, 2, 4, 4, 5, 4]
FOURmmusic = []
MusicList = [TutorialMusic, GoblinsMusic, CastleMusic, FOURmmusic]

#C:\Users\Apr15\OneDrive\Escritorio\Pyth0n\PyGame\Sprites\NoneList
#C:\Users\Apr15\AppData\Local\Temp\_MEI269962\Sprites//NoneList//None.png'



def LoadScene(YList, CurrentScene, CurrentGlobalLevel, PlayerSpawnPos):
    ChangeTracks(MusicList[CurrentGlobalLevel][CurrentScene], CurrentScene, CurrentGlobalLevel, PlayerSpawnPos)
    BgColor = BGList[CurrentGlobalLevel][CurrentScene]
    for i in range(0, len(YList)):
        YList[i] = []
    OffsetX = 0
    BlockColorAppendix = BlockColorLists[CurrentGlobalLevel]
    f = Image.open(GlobalLevelsList[CurrentGlobalLevel])
    LenLevel = 0
    while CurrentScene != 0:
        OffsetX += 1
        if f.getpixel((OffsetX,0)) == (255, 0, 0, 255):
            CurrentScene -= 1
    if OffsetX != 0:
        SecondOffsetX = 1
    else:
        SecondOffsetX = 0
    for i in range(0, 1000):
        if f.getpixel((i + OffsetX + SecondOffsetX,0)) == (255, 0, 0, 255):
            LenLevel = i
            break
    for a in range(0, 10):
        for i in range(0, LenLevel):
            YList[a].append(BlockColorAppendix.index(f.getpixel((i + OffsetX + SecondOffsetX,a))))
        YList[a].append(1)
    print("SIIIII")

    return(YList, BgColor)

def LoadLevel(CurrentGlobalLevel):
    MovObjectsList = MovListList[CurrentGlobalLevel]
    BlockAppendix = BlockAppendixList[CurrentGlobalLevel]
    return(MovObjectsList, BlockAppendix)

pygame.mixer.init()
MusicTracksList = [0, "MUSIC//GOBLINS.mp3", "MUSIC//CASTLEOUTSIDE.mp3", "MUSIC//BOSSFIGHT1.mp3", "MUSIC//CASTLEINSIDE.mp3", "MUSIC//BOSSFIGHT2.mp3"], [0, 0.25, 0.7, 0.7, 0.7, 0.7]

def ChangeTracks(NewTrack, CurrentScene, CurrentGlobalLevel, PlayerSpawnPos):
    if CurrentScene == PlayerSpawnPos[1][0]:
        OldTrack = 0
    else:
        OldTrack = MusicList[CurrentGlobalLevel][CurrentScene - 1]
    if OldTrack != NewTrack:
        pygame.mixer.music.load(MusicTracksList[0][NewTrack])
        pygame.mixer.music.set_volume(MusicTracksList[1][NewTrack])
        pygame.mixer.music.play(-1)
    