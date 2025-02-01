import pygame
from os import path
directory = path.dirname(path.abspath(__file__))

def LoadStaticObjects(GameRow0, GameRow1, GameRow2, GameRow3, GameRow4, GameRow5, GameRow6, GameRow7, GameRow8, GameRow9, screen, BlockAppendix, XOffsetForScrolls):
    for i in range(0, len(GameRow0)):
        if(GameRow0[i] != 0):
            screen.blit(BlockAppendix[0][GameRow0[i]], ((64 * i - XOffsetForScrolls) , 0))
        if(GameRow1[i] != 0):
            screen.blit(BlockAppendix[0][GameRow1[i]], ((64 * i - XOffsetForScrolls) , 64))
        if(GameRow2[i] != 0):
            screen.blit(BlockAppendix[0][GameRow2[i]], ((64 * i - XOffsetForScrolls) , 128))
        if(GameRow3[i] != 0):
            screen.blit(BlockAppendix[0][GameRow3[i]], ((64 * i - XOffsetForScrolls) , 192))
        if(GameRow4[i] != 0):
            screen.blit(BlockAppendix[0][GameRow4[i]], ((64 * i - XOffsetForScrolls) , 256))
        if(GameRow5[i] != 0):
            screen.blit(BlockAppendix[0][GameRow5[i]], ((64 * i - XOffsetForScrolls) , 320))
        if(GameRow6[i] != 0):
            screen.blit(BlockAppendix[0][GameRow6[i]], ((64 * i - XOffsetForScrolls) , 384))
        if(GameRow7[i] != 0):
            screen.blit(BlockAppendix[0][GameRow7[i]], ((64 * i - XOffsetForScrolls) , 448))
        if(GameRow8[i] != 0):
            screen.blit(BlockAppendix[0][GameRow8[i]], ((64 * i - XOffsetForScrolls) , 512))
        if(GameRow9[i] != 0):
            screen.blit(BlockAppendix[0][GameRow9[i]], ((64 * i - XOffsetForScrolls) , 576))

def LoadSpecificStaticObjects(GameRow0, GameRow1, GameRow2, GameRow3, GameRow4, GameRow5, GameRow6, GameRow7, GameRow8, GameRow9, SpecificStaticObjects, screen, BlockAppendix, YList, XOffsetForScrolls, PlayerIframesAndHP, NumberSpriteList, HPpoint, BottomGameBar):
    a = 0
    BarReplace = pygame.image.load(path.join(directory, "Sprites//AnimationReplacements//BGREPLACE.png"))
    BarReplace.fill((0, 0, 0))
    while a <= len(SpecificStaticObjects[0]) - 1:
        i = 0
        while i <= len(SpecificStaticObjects[0]) - 1:
            if i != a:
                if SpecificStaticObjects[0][i] == SpecificStaticObjects[0][a] and SpecificStaticObjects[1][i] == SpecificStaticObjects[1][a]:
                    SpecificStaticObjects[0].pop(i)
                    SpecificStaticObjects[1].pop(i)
                else:
                    i += 1
            else:
                i += 1
        a = a + 1
    for i in range(len(SpecificStaticObjects[0])):
        if SpecificStaticObjects[1][i] < 10 and abs(SpecificStaticObjects[0][i]) <= len(YList[0]):
            if SpecificStaticObjects[0][i] <= len(YList[SpecificStaticObjects[1][i]]) - 1:
                screen.blit(BlockAppendix[0][(YList[SpecificStaticObjects[1][i]])[SpecificStaticObjects[0][i]]], (64*SpecificStaticObjects[0][i] - XOffsetForScrolls, 64*SpecificStaticObjects[1][i]))
        elif SpecificStaticObjects[1][i] == 10:
            screen.blit(BarReplace, (64*SpecificStaticObjects[0][i], 640))
        #if SpecificStaticObjects[1][i] == 10 and  9 < SpecificStaticObjects[0][i] - XOffsetForScrolls/64 < 14:
        #    for i in range(len(str(PlayerIframesAndHP[2]))):
        #        screen.blit(NumberSpriteList[int(str(PlayerIframesAndHP[2])[i])], (656 + 32*i, 656))
        #    print("HP")
        #elif SpecificStaticObjects[1][i] == 10 and 0 < SpecificStaticObjects[0][i] - XOffsetForScrolls/64 < 5:
        #    print("Blit")
        #    screen.blit(HPpoint, (2*PlayerIframesAndHP[1] -89, 640))
        #    screen.blit(BottomGameBar, (0, 640))

def LoadDynamicObjectsList(MovObjectsList, CurrentScene):
    DOIS = [], [], [], [], [], [], [], [], [], [], [], []
    for i in range(len(MovObjectsList[CurrentScene])):
        PlaceHolderList = MovObjectsList[CurrentScene][i].split(", ")
        PlaceHolderList[1] = float(PlaceHolderList[1]) *64
        PlaceHolderList[2] = float(PlaceHolderList[2]) *64
        for i in range(len(PlaceHolderList)):
            DOIS[i].append(float(PlaceHolderList[i]))
        for i in range(len(PlaceHolderList), len(DOIS)):
            DOIS[i].append("")
    return(DOIS)