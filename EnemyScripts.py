
from StaticObjColliders import PlayerColFloor, PlayerColRight, PlayerColLeft, FindRow, CollisionsWithPlayer
from StaticObjManager import LoadStaticObjects, LoadDynamicObjectsList
import MapLoader
import math
import random
DOISGLOBALLIST = [0, 9, 12, 6, 22, 25, 19, 18]
def DynamicObjectScripts(DynamicTag, DOIS, DACL, PlayerX, PlayerY, PlayerIframesAndHP, SpawnList, DashHitboxList, YList, Debug, screen, ColVisualFloor, XOffsetForScrolls, PlayerSpawnPos, CurrentScene, BlockAppendix, HPpoint, BottomGameBar, BgColor, CurrentGlobalLevel, MovObjectsList, BgReplace):
    DOIS_ScaleFactor = DACL[0][DynamicTag].GetScaleFactors()
    NoRepeatingDeleteAnim = 0
    PortalCalled = False
    Damage = CollisionsWithPlayer(DOIS[1][DynamicTag], DOIS[2][DynamicTag], DOIS_ScaleFactor, DashHitboxList, PlayerX, PlayerY, screen, XOffsetForScrolls, PlayerIframesAndHP)
    if abs(DOIS[1][DynamicTag] - PlayerX) <= 1000 or DOIS[0][DynamicTag] in DOISGLOBALLIST:
        if PlayerIframesAndHP[0] == 0:
            PlayerIframesAndHP[5] = 0
            PlayerIframesAndHP[3] = 0
        if DOIS[0][DynamicTag] == 0:
            if DACL[1][DynamicTag] >= 240:
                DOIS[0][DynamicTag] = 1000
            NoRepeatingDeleteAnim = 1

        if DOIS[0][DynamicTag] == 1:
            if Damage == - 1 and DACL[2][DynamicTag] == 0:
                DACL[2][DynamicTag] = 1
                DACL[1][DynamicTag] = 0
                PlayerSpawnPos[0][0] = DOIS[1][DynamicTag]
                PlayerSpawnPos[0][1] = DOIS[2][DynamicTag] + 126
                PlayerSpawnPos[1][0] = CurrentScene
            if Damage == - 1 and DOIS[3][DynamicTag] == 0:
                PlayerIframesAndHP[4] = -50
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 0
                #Changes the savefile:
                f = open("Save.txt", "w")
                f.write(str(CurrentGlobalLevel) + "\n" + str(PlayerIframesAndHP[2]) + "\n" + str(PlayerSpawnPos[0][0]) + "\n" + str(PlayerSpawnPos[0][1]) + "\n" + str(PlayerSpawnPos[1][0]))
                f.close() 
            if DACL[2][DynamicTag] == 1:
                if DACL[1][DynamicTag] >= 120:
                    DACL[2][DynamicTag] = 2
                    DACL[1][DynamicTag] = 0
                DOIS[3][DynamicTag] = 1

        if DOIS[0][DynamicTag] == 2:
            if Damage > 0:
                DOIS[0][DynamicTag] = 1000
                PlayerIframesAndHP[2] += 150
            DOIS[3][DynamicTag] = DOIS[3][DynamicTag] + 2
            DOIS[1][DynamicTag] = DOIS[1][DynamicTag] + DOIS[4][DynamicTag]*math.cos(DOIS[3][DynamicTag]/500)
            DOIS[2][DynamicTag] = DOIS[2][DynamicTag] + DOIS[5][DynamicTag]*math.cos(DOIS[3][DynamicTag]/500)
            if DOIS[6][DynamicTag] <= 799:
                DOIS[6][DynamicTag] = DOIS[6][DynamicTag] + 2
            if (-128 <= PlayerY - DOIS[2][DynamicTag] <= 128 and -400 <= PlayerX - DOIS[1][DynamicTag] <= 400 and (DOIS[6][DynamicTag] == 800)) and DOIS[0][DynamicTag] != 1000:
                SpawnList.append("11, " + str(DOIS[1][DynamicTag]) + ", " + str(DOIS[2][DynamicTag]) + ", 0, 0")
                DACL[2][DynamicTag] = 1
                DACL[1][DynamicTag] = 0
                DOIS[6][DynamicTag] = 0
            if DACL[2][DynamicTag] == 1 and DACL[1][DynamicTag] >= 74:
                DACL[2][DynamicTag] = 0
            
            elif Damage == -1:
                PlayerIframesAndHP[4] = 4
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 8*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])

        if DOIS[0][DynamicTag] == 3:
            if FindRow(DOIS[2][DynamicTag], YList)[round(DOIS[1][DynamicTag]/64)] != 6:
                FindRow(DOIS[2][DynamicTag], YList)[round(DOIS[1][DynamicTag]/64)] = 6
            if Damage > 0:
                DOIS[0][DynamicTag] = 1001
                FindRow(DOIS[2][DynamicTag], YList)[round(DOIS[1][DynamicTag]/64)] = 0
                screen.fill((BgColor))
                LoadStaticObjects(YList[0], YList[1], YList[2], YList[3], YList[4], YList[5], YList[6], YList[7], YList[8], YList[9], screen, BlockAppendix, XOffsetForScrolls)
                screen.blit(HPpoint, (2*PlayerIframesAndHP[1] -89, 640))
                screen.blit(BottomGameBar, (0, 640))

        #REVIEW
        if DOIS[0][DynamicTag] == 4:
            if abs(PlayerX - DOIS[1][DynamicTag]) <= 120 and DOIS[3][DynamicTag] == 0:
                DOIS[3][DynamicTag] = 1
            if DOIS[3][DynamicTag] == 1 and DOIS[2][DynamicTag] > 64*DOIS[4][DynamicTag]:
                DOIS[2][DynamicTag] -= 8
            elif DOIS[3][DynamicTag] != 0 and DOIS[2][DynamicTag] <= 64*DOIS[4][DynamicTag] and DOIS[3][DynamicTag] < 250:
                DOIS[2][DynamicTag] = 64*DOIS[4][DynamicTag]
                DOIS[3][DynamicTag] += 1
            elif DOIS[3][DynamicTag] == 250 and DOIS[2][DynamicTag] < 64*DOIS[5][DynamicTag]:
                DOIS[2][DynamicTag] += 1
            elif DOIS[3][DynamicTag] == 250 and DOIS[2][DynamicTag] >= 64*DOIS[5][DynamicTag]:
                DOIS[2][DynamicTag] = 64*DOIS[5][DynamicTag]
                DOIS[3][DynamicTag] += 1
            elif 251 <= DOIS[3][DynamicTag] <= 700:
                DOIS[3][DynamicTag] += 1
            else:
                DOIS[3][DynamicTag] = 0
            if Damage == -1:
                    PlayerIframesAndHP[4] = 10
                    PlayerIframesAndHP[0] = 1
                    PlayerIframesAndHP[3] = 8*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])

        #REVIEW
        if DOIS[0][DynamicTag] == 5:
            if DOIS[3][DynamicTag] >= 1:
                DOIS[3][DynamicTag] = DOIS[3][DynamicTag] + 1
            if random.randint(1, 200) == 10 and DOIS[3][DynamicTag] == 0:
                DOIS[3][DynamicTag] = 1
                DOIS[4 + random.randint(0, 1)][DynamicTag] = random.randint(-20, 20)/10
            if DOIS[3][DynamicTag] >= 100:
                DOIS[3][DynamicTag] = 0
                DOIS[4][DynamicTag] = 0
                DOIS[5][DynamicTag] = 0
            DOIS[1][DynamicTag] = DOIS[1][DynamicTag] + DOIS[4][DynamicTag]
            DOIS[2][DynamicTag] = DOIS[2][DynamicTag] + DOIS[5][DynamicTag]
            if math.sqrt((DashHitboxList[0][0] - DOIS[1][DynamicTag])**2 + (DashHitboxList[1][0] - DOIS[2][DynamicTag])**2) <= 90:
                DOIS[0][DynamicTag] = 1000
            if Damage == -1:
                PlayerIframesAndHP[4] = 12
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 8*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])


        if DOIS[0][DynamicTag] == 6:
            DACL[2][DynamicTag] = 0
            if DOIS[5][DynamicTag] == 0:
                DOIS[5][DynamicTag] = random.randint(1, 2)
            DOIS[3][DynamicTag] = PlayerColFloor(DOIS[1][DynamicTag], DOIS[2][DynamicTag], YList, Debug, screen, ColVisualFloor, XOffsetForScrolls, BlockAppendix)
            if DOIS[3][DynamicTag] == 0:
                DOIS[4][DynamicTag] += 0.05
            else:
                DOIS[4][DynamicTag] = 0
            if DOIS[1][DynamicTag] - PlayerX <= 400 or DOIS[6][DynamicTag] == 1:
                DOIS[1][DynamicTag] -= 1.6
                DACL[2][DynamicTag] = 2
            if DOIS[3][DynamicTag] == 0:
                DACL[2][DynamicTag] = 1
            if DOIS[1][DynamicTag] - PlayerX <= 200 and DOIS[5][DynamicTag] == 2 and DOIS[3][DynamicTag] != 0:
                DOIS[4][DynamicTag] = -3.8
                DOIS[5][DynamicTag] = 1
            DOIS[2][DynamicTag] = DOIS[2][DynamicTag] + DOIS[4][DynamicTag]
            if Damage == -1:
                PlayerIframesAndHP[4] = 8
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 8*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])
            if DOIS[1][DynamicTag] <= -64:
                DOIS[0][DynamicTag] = 1000
            if Damage > 0:
                if DOIS[7][DynamicTag] != 0:
                    PlayerIframesAndHP[2] += 100
                DOIS[0][DynamicTag] = 1000

        #REVIEW
        if DOIS[0][DynamicTag] == 7:
            if DOIS[6][DynamicTag] > 0:
                DOIS[1][DynamicTag] += DOIS[3][DynamicTag]
                if random.randint(1, 200) == 200 and abs(DOIS[1][DynamicTag] - 64*DOIS[4][DynamicTag]) < 64*DOIS[5][DynamicTag] - 50:
                    DOIS[3][DynamicTag] *= -1
                elif abs(DOIS[1][DynamicTag] - 64*DOIS[4][DynamicTag]) > 64*DOIS[5][DynamicTag]:
                    DOIS[3][DynamicTag] *= -1
                    DOIS[1][DynamicTag] += 2*DOIS[3][DynamicTag]
                    DACL[2][DynamicTag] = int((1 + DOIS[3][DynamicTag]/abs(DOIS[3][DynamicTag]))/2)
                if abs(DOIS[1][DynamicTag] - PlayerX) < 200:
                    DOIS[6][DynamicTag] = random.randint(0, 350)
            elif DOIS[6][DynamicTag] == 0:
                DACL[2][DynamicTag] = 2
                DACL[1][DynamicTag] = 0
                DOIS[6][DynamicTag] = -1
            elif DOIS[6][DynamicTag] == -1 and Damage > 0 and DACL[1][DynamicTag] >= 195:
                DOIS[0][DynamicTag] = 1000
                PlayerIframesAndHP[2] += 1000
            if DOIS[6][DynamicTag] == -1 and DACL[1][DynamicTag] == 195:
                SpawnList.append("8, " + str(DOIS[1][DynamicTag]) + ", " + str(DOIS[2][DynamicTag] + 32) + ", 0, " + str((PlayerX - DOIS[1][DynamicTag])/abs(PlayerX - DOIS[1][DynamicTag])))
            if DOIS[6][DynamicTag] == -1 and DACL[1][DynamicTag] == 350:
                DOIS[6][DynamicTag] = 100
                DACL[1][DynamicTag] = 0
                DACL[2][DynamicTag] = int((1 + DOIS[3][DynamicTag]/abs(DOIS[3][DynamicTag]))/2)
            if Damage == -1:
                PlayerIframesAndHP[4] = 15
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 10*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])
            DACL[3][DynamicTag] = (PlayerX - DOIS[1][DynamicTag])/abs(PlayerX - DOIS[1][DynamicTag])
        #REVIEW
        if DOIS[0][DynamicTag] == 8:
            DACL[3][DynamicTag] = DOIS[4][DynamicTag]
            DOIS[1][DynamicTag] += -6*-DOIS[4][DynamicTag]
            DOIS[3][DynamicTag] += 2
            if DOIS[3][DynamicTag] >= 140:
                DOIS[0][DynamicTag] = 1000
            if Damage == -1:
                PlayerIframesAndHP[4] = 24
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 8*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])
                DOIS[0][DynamicTag] = 1000
        
        if DOIS[0][DynamicTag] == 9:
            if DACL[1][DynamicTag] == 0 and random.randint(0, 3) == 0:
                DACL[2][DynamicTag] = 1
                DACL[1][DynamicTag] = 1
            if DACL[2][DynamicTag] == 1 and DACL[1][DynamicTag] == 0:
                DACL[2][DynamicTag] = 0
            if DACL[1][DynamicTag] == 180 and DACL[2][DynamicTag] == 1:
                SpawnList.append("6, " + str(DOIS[1][DynamicTag]) + ", " + str(DOIS[2][DynamicTag] + 32) + ", 2, -3, 0, 1, 0")
            if Damage > 2:
                DOIS[0][DynamicTag] = 1000
                PlayerIframesAndHP[2] += 500
            elif Damage == -1:
                PlayerIframesAndHP[4] = 4
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 16*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])

        if DOIS[0][DynamicTag] == 10 and Damage == -1:
            PlayerIframesAndHP[4] = -DOIS[3][DynamicTag]
            PlayerIframesAndHP[0] = 1
            PlayerIframesAndHP[3] = 0
            DOIS[0][DynamicTag] = 1000

        if DOIS[0][DynamicTag] == 11:
            DOIS[1][DynamicTag] = DOIS[1][DynamicTag] + 2*int(DOIS[4][DynamicTag])
            if DOIS[4][DynamicTag] == 0:
                DOIS[4][DynamicTag] = 1*(PlayerX - DOIS[1][DynamicTag])/math.sqrt((PlayerX - DOIS[1][DynamicTag])**2)
            DOIS[3][DynamicTag] = DOIS[3][DynamicTag] + 1
            if Damage == -1:
                PlayerIframesAndHP[4] = 12
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 8*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])
                DOIS[0][DynamicTag] = 1000
            if abs(PlayerX - DOIS[1][DynamicTag]) >= 400:
                DOIS[0][DynamicTag] = 1000

        if DOIS[0][DynamicTag] == 12:
            DACL[0][DynamicTag].ChangeOpacity(DOIS[3][DynamicTag])
            if math.sqrt((DOIS[2][DynamicTag] - PlayerY)**2 + (DOIS[1][DynamicTag] - PlayerX)**2) < 500:
                DOIS[2][DynamicTag] -= (DOIS[2][DynamicTag] - PlayerY)/500
                DOIS[1][DynamicTag] -= (DOIS[1][DynamicTag] - PlayerX + 120*(DOIS[1][DynamicTag] - PlayerX)/abs(DOIS[1][DynamicTag] - PlayerX))/1000
                DOIS[3][DynamicTag] = 255 - math.sqrt((DOIS[2][DynamicTag] - PlayerY)**2 + (DOIS[1][DynamicTag] - PlayerX)**2)
                if DOIS[3][DynamicTag] <= 0:
                    DOIS[3][DynamicTag] = 0
                elif DOIS[3][DynamicTag] >= 200:
                    DOIS[3][DynamicTag] = 200
                if Damage == -1:
                    PlayerIframesAndHP[4] = 12
                    PlayerIframesAndHP[0] = 1
                    PlayerIframesAndHP[3] = 8*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])
                elif Damage > 0:
                    DOIS[0][DynamicTag] = 1000
                    PlayerIframesAndHP[2] += 140
            
                    

        if DOIS[0][DynamicTag] == 13:
            if DOIS[5][DynamicTag] == 0:
                DACL[3][DynamicTag] = (PlayerX - DOIS[1][DynamicTag])/abs(PlayerX - DOIS[1][DynamicTag])
            if (abs(DOIS[1][DynamicTag] - PlayerX) <= 350 or DACL[2][DynamicTag] != 0) and DOIS[4][DynamicTag] > 1:
                DOIS[2][DynamicTag] -= abs((DOIS[2][DynamicTag] - 40))/100
                DOIS[1][DynamicTag] += (PlayerX - DOIS[1][DynamicTag])/100 + 2*math.sin(math.radians(DOIS[3][DynamicTag]))
                DACL[2][DynamicTag] = 1
                if DOIS[3][DynamicTag] >= 500:
                    DOIS[4][DynamicTag] = random.randint(0, 1000)
                DOIS[3][DynamicTag] += 1
            elif DOIS[4][DynamicTag] == 0:
                if abs(DOIS[2][DynamicTag] - PlayerY) < 40 and DOIS[5][DynamicTag] == 0:
                    DACL[2][DynamicTag] = 2
                    DOIS[5][DynamicTag] = 5*(PlayerX - DOIS[1][DynamicTag])/abs(PlayerX - DOIS[1][DynamicTag])
                elif DOIS[5][DynamicTag] != 0:
                    DOIS[1][DynamicTag] += DOIS[5][DynamicTag]
                else:
                    DOIS[2][DynamicTag] += (PlayerY - DOIS[2][DynamicTag])/200
                    DOIS[1][DynamicTag] += (PlayerX - DOIS[1][DynamicTag])/100 - 4*(PlayerX - DOIS[1][DynamicTag])/abs(PlayerX - DOIS[1][DynamicTag])
            elif DOIS[4][DynamicTag] == 1:
                DOIS[2][DynamicTag] += 4
            else:
                DACL[2][DynamicTag] = 0
            if Damage == -1:
                    PlayerIframesAndHP[4] = 20
                    PlayerIframesAndHP[0] = 1
                    PlayerIframesAndHP[3] = 8*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])
            elif Damage > 0:
                DOIS[0][DynamicTag] = 1000
                if PlayerSpawnPos[1] != 7:
                    PlayerIframesAndHP[2] += 200
            if DOIS[2][DynamicTag] > 600:
                DOIS[0][DynamicTag] = 1000

        if DOIS[0][DynamicTag] == 15 and DOIS[4][DynamicTag] != 1:
            DOIS[1][DynamicTag] += 2*DOIS[3][DynamicTag]
            DOIS[2][DynamicTag] -= (DOIS[2][DynamicTag] - PlayerY)/200
            DACL[3][DynamicTag] = DOIS[3][DynamicTag]
            if (DOIS[1][DynamicTag] - PlayerX < -200 and DOIS[3][DynamicTag] == -1) or (DOIS[1][DynamicTag] - PlayerX > 200 and DOIS[3][DynamicTag] == 1):
                DOIS[0][DynamicTag] = 1000
            if Damage > 0:
                PlayerIframesAndHP[2] += 5
                DOIS[0][DynamicTag] = 1000
            elif Damage == -1:
                PlayerIframesAndHP[4] = 10
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 20*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])
        elif DOIS[0][DynamicTag] == 15 and DOIS[4][DynamicTag] == 1:
            DACL[2][DynamicTag] = 1
            DACL[3][DynamicTag] = DOIS[3][DynamicTag]
            DOIS[1][DynamicTag] += 2*DOIS[3][DynamicTag]
            if DOIS[1][DynamicTag] - PlayerX < -200:
                DOIS[0][DynamicTag] = 1000
            elif Damage == -1:
                PlayerIframesAndHP[4] = 0
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 25
                DOIS[0][DynamicTag] = 1000


        if DOIS[0][DynamicTag] == 14 and DOIS[4][DynamicTag] == 0:
            DACL[3][DynamicTag] = DOIS[3][DynamicTag]
            if DACL[1][DynamicTag] == 500:
                SpawnList.append("15, " + str(DOIS[1][DynamicTag] + 32) + ", " + str(DOIS[2][DynamicTag]) + ", " + str(DOIS[3][DynamicTag]))
        elif DOIS[0][DynamicTag] == 14 and DOIS[4][DynamicTag] == 1:
            DACL[2][DynamicTag] = 1
            if DACL[1][DynamicTag] == 50:
                SpawnList.append("15, " + str(DOIS[1][DynamicTag] + 32) + ", " + str(DOIS[2][DynamicTag]) + ", " + str(DOIS[3][DynamicTag]) + ", 1")

        if DOIS[0][DynamicTag] == 16:
            if DOIS[6][DynamicTag] <= 0:
                screen.fill((BgColor))
                DOIS[0][DynamicTag] = 1000
                PlayerIframesAndHP[2] += 10000
                YList[7][14] = 0
                YList[6][14] = 0
                YList[5][14] = 0
                LoadStaticObjects(YList[0], YList[1], YList[2], YList[3], YList[4], YList[5], YList[6], YList[7], YList[8], YList[9], screen, BlockAppendix, XOffsetForScrolls)
                screen.blit(HPpoint, (2*PlayerIframesAndHP[1] -89, 640))
                screen.blit(BottomGameBar, (0, 640))
            if DOIS[3][DynamicTag] == 0:
                DACL[3][DynamicTag] = (-DOIS[1][DynamicTag] + PlayerX)/abs(DOIS[1][DynamicTag] - PlayerX)
                DOIS[4][DynamicTag] += 0.3
                DOIS[1][DynamicTag] = 380 + 304*math.sin(math.radians(DOIS[4][DynamicTag]))
                DOIS[2][DynamicTag] = 60
                DACL[2][0] = 0
                if DACL[1][0] == 0:
                    if math.cos(math.radians(DOIS[5][DynamicTag])) == 1:
                        SpawnList.append("18, " + str(DOIS[1][DynamicTag] + 96 + 46*DACL[3][DynamicTag]) + ", " + str(DOIS[2][DynamicTag] + 64) + ", 0")
                    else:
                        SpawnList.append("17, " + str(DOIS[1][DynamicTag] + 96 + 46*DACL[3][DynamicTag]) + ", " + str(DOIS[2][DynamicTag] + 64) + ", 0")
                    DOIS[5][DynamicTag] += 45
                if abs(math.sin(math.radians(DOIS[4][DynamicTag]))) > 0.95 and random.randint(0, 300) == 0 and 13 not in DOIS[0] and DOIS[3][DynamicTag] == 0:
                    SpawnList.append("13, 400, 100, 0, 100, 0")
                    SpawnList.append("13, 400, 100, 100, 100, 0")
                elif abs(math.sin(math.radians(DOIS[4][DynamicTag]))) > 0.95 and random.randint(0, 300) == 0:
                    DOIS[8][DynamicTag] = -math.sin(math.radians(DOIS[4][DynamicTag]))
                    DOIS[3][DynamicTag] = 1
                    DOIS[4][DynamicTag] = -400
                elif abs(math.sin(math.radians(DOIS[4][DynamicTag]))) > 0.95 and random.randint(0, 400) == 0:
                    DOIS[8][DynamicTag] = -math.sin(math.radians(DOIS[4][DynamicTag]))
                    DOIS[3][DynamicTag] = 2
                    DOIS[4][DynamicTag] = 0
                    DOIS[5][DynamicTag] = 90
            if (DOIS[9][DynamicTag] == 800 or PlayerX > 128) and YList[9][0] != 0:
                screen.fill((BgColor))
                YList[9][0] = 0
                YList[9][1] = 0
                YList[9][2] = 0
                LoadStaticObjects(YList[0], YList[1], YList[2], YList[3], YList[4], YList[5], YList[6], YList[7], YList[8], YList[9], screen, BlockAppendix, XOffsetForScrolls)
                screen.blit(HPpoint, (2*PlayerIframesAndHP[1] -89, 640))
                screen.blit(BottomGameBar, (0, 640))
            if 0 <= DOIS[9][DynamicTag] < 800:
                DOIS[9][DynamicTag] += 1
            if DOIS[3][DynamicTag] == 1:
                DOIS[4][DynamicTag] += 1
                if 0 < DOIS[4][DynamicTag] < 360:
                    DACL[2][DynamicTag] = 1
                    DOIS[2][DynamicTag] += 3.4*math.cos(math.radians(DOIS[4][DynamicTag]/2))
                    DOIS[1][DynamicTag] += 1.66*DOIS[8][DynamicTag]
                elif DOIS[4][DynamicTag] > 359:
                    DOIS[3][DynamicTag] = 0
                    DOIS[4][DynamicTag] = 90*DOIS[8][DynamicTag]
            if DOIS[3][DynamicTag] == 2:
                if DOIS[4][DynamicTag] < 720:
                    DOIS[4][DynamicTag] += 1
                    DACL[2][DynamicTag] = 1
                    DOIS[2][DynamicTag] += 1.7*math.cos(math.radians(DOIS[4][DynamicTag]/4))
                else:
                    DOIS[3][DynamicTag] = 0
                    DOIS[4][DynamicTag] = -90*DOIS[8][DynamicTag]
                if DACL[1][DynamicTag] == 0:
                    DOIS[5][DynamicTag] += 90
                    if math.cos(math.radians(DOIS[5][DynamicTag])) == 1:
                        SpawnList.append("18, " + str(DOIS[1][DynamicTag] + 96 + 46*DACL[3][DynamicTag]) + ", " + str(DOIS[2][DynamicTag] + 64) + ", " + str(DOIS[8][DynamicTag]))
                    else:
                        SpawnList.append("17, " + str(DOIS[1][DynamicTag] + 96 + 46*DACL[3][DynamicTag]) + ", " + str(DOIS[2][DynamicTag] + 64) + ", " + str(DOIS[8][DynamicTag]))
            if Damage == -1:
                PlayerIframesAndHP[4] = 10
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 12*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])
            if Damage > 0 and DOIS[7][DynamicTag] == 0:
                DOIS[6][DynamicTag] -= Damage
                DOIS[7][DynamicTag] = 1
            if 1 <= DOIS[7][DynamicTag] <= 299:
                DOIS[7][DynamicTag] += 1
                DACL[0][DynamicTag].ChangeOpacity(45 + DOIS[7][DynamicTag]*0.7)
            else:
                DOIS[7][DynamicTag] = 0
        #Tag, X, Y, BattleSetting, Counter, TornadoCounter, HP, Iframes, DirectionVarForAttacks, DespawnBlocks

        if DOIS[0][DynamicTag] == 17:
            if DOIS[3][DynamicTag] != 0:
                DACL[0][DynamicTag].ChangeAngle(90*DOIS[3][DynamicTag])
                DOIS[2 - abs(DOIS[3][DynamicTag])][DynamicTag] += 3*DOIS[3][DynamicTag]
            else:
                DOIS[2][DynamicTag] += 4
            if DOIS[2][DynamicTag] > 500:
                DOIS[0][DynamicTag] = 1000
            if Damage == -1:
                PlayerIframesAndHP[4] = 10
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 16*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])
                DOIS[0][DynamicTag] = 1000
            if 0 > DOIS[1][DynamicTag] > 960:
                DOIS[0][DynamicTag] = 1000

        if DOIS[0][DynamicTag] == 18:
            if DOIS[3][DynamicTag] != 0:
                DOIS[2 - abs(DOIS[3][DynamicTag])][DynamicTag] += 3*DOIS[3][DynamicTag]
            else:
                DOIS[2][DynamicTag] += 1
            if DOIS[2][DynamicTag] > 560:
                DOIS[0][DynamicTag] = 1000
            if Damage == -1:
                PlayerY -= 10
                PlayerIframesAndHP[4] = 0
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[5] = -5
                DOIS[0][DynamicTag] = 1000
            if 0 > DOIS[1][DynamicTag] > 960:
                DOIS[0][DynamicTag] = 1000
            
        if DOIS[0][DynamicTag] == 19:
            if DACL[1][DynamicTag] == 0 and DOIS[3][DynamicTag] != 1:
                SpawnList.append("18, " + str(DOIS[1][DynamicTag] + 96 + 46*DACL[3][DynamicTag]) + ", 1, 0")
            elif DACL[1][DynamicTag] == 0 and DOIS[3][DynamicTag] == 1:
                SpawnList.append("17, " + str(DOIS[1][DynamicTag] + 96 + 46*DACL[3][DynamicTag]) + ", 1, 0")


        if DOIS[0][DynamicTag] == 20 and Damage == -1:
            DOIS[0][DynamicTag] = 1000
            PlayerIframesAndHP[2] += 1

        if DOIS[0][DynamicTag] == 22:
            if DOIS[4][DynamicTag] > 0:
                if DOIS[4][DynamicTag] != 3:
                    DOIS[3][DynamicTag] += 1
                    DOIS[5][DynamicTag] = 896 + 800*math.sin(math.radians(DOIS[3][DynamicTag]/6))
                    DOIS[6][DynamicTag] = 280 + 150*math.cos(math.radians(DOIS[3][DynamicTag] + 90))
                    DOIS[1][DynamicTag] += 0.007*(DOIS[5][DynamicTag] - DOIS[1][DynamicTag])
                    DOIS[2][DynamicTag] += 0.007*(DOIS[6][DynamicTag] - DOIS[2][DynamicTag])
                    if random.randint(0, 350) == 0 and (DOIS[4][DynamicTag] != 3 or DOIS[4][DynamicTag] != 4) and len(DOIS[0]) < 10:
                        SpawnList.append("24, " + str(DOIS[1][DynamicTag] + 32) + ", " + str(DOIS[2][DynamicTag] + 32))
                if DOIS[4][DynamicTag] == 1 and random.randint(0, 1000) == 0:
                    DOIS[4][DynamicTag] = 2
                elif DOIS[4][DynamicTag] == 1 and random.randint(0, 2000) == 0:
                    DOIS[4][DynamicTag] = 3
                    DACL[1][DynamicTag] = 1
                elif DOIS[4][DynamicTag] == 1 and random.randint(0, 3000) == 0:
                    DOIS[4][DynamicTag] = -1
                    #DOIS[3][DynamicTag] = 6*math.asin((DOIS[5][DynamicTag] - 896)/800)
                #Attacks
                if DOIS[4][DynamicTag] == 2:
                    DACL[2][DynamicTag] = 1
                    DOIS[7][DynamicTag] += 1
                    if DOIS[7][DynamicTag] > 600:
                        DOIS[7][DynamicTag] = 0
                        DOIS[4][DynamicTag] = 1
                    if random.randint(1, 100) == 100 and len(DOIS[0]) < 20:
                        SpawnList.append("23, " + str(PlayerX + random.randint(-600, 600)) + ", " + str(PlayerY + random.randint(-300, 300)) + ", 0, 0, " + str(random.randint(-1, 1)))
                #Attack modes 3 and 4 are for teleport
                if DOIS[4][DynamicTag] == 3:
                    DACL[2][DynamicTag] = 2
                    if DACL[1][DynamicTag] >= 50:
                        DOIS[4][DynamicTag] = 4
                if DOIS[4][DynamicTag] == 4:
                    if DACL[1][DynamicTag] == 0:
                        DACL[2][DynamicTag] = 0
                    if DACL[2][DynamicTag] == 0:
                        DOIS[7][DynamicTag] += 1
                        DACL[0][DynamicTag].ChangeOpacity(DOIS[7][DynamicTag])
                        if DOIS[7][DynamicTag] >= 255:
                            DOIS[7][DynamicTag] = 0
                            DOIS[4][DynamicTag] = 1
                    else:
                        DOIS[3][DynamicTag] += random.randint(3, 5)
            #ORANGE ATTACKS
            if DOIS[4][DynamicTag] < 0:
                DACL[2][DynamicTag] = 3
                DOIS[3][DynamicTag] += 1
                if DOIS[4][DynamicTag] == -1 or DOIS[4][DynamicTag] == -2:
                    DOIS[5][DynamicTag] = 896 + 950*math.sin(math.radians(DOIS[3][DynamicTag]/2))
                    DOIS[6][DynamicTag] = 280 + 100*math.cos(math.radians(DOIS[3][DynamicTag] + 90))
                DOIS[1][DynamicTag] += 0.014*(DOIS[5][DynamicTag] - DOIS[1][DynamicTag])
                DOIS[2][DynamicTag] += 0.014*(DOIS[6][DynamicTag] - DOIS[2][DynamicTag])
                if random.randint(0, 125) == 0 and (DOIS[4][DynamicTag] != 3 or DOIS[4][DynamicTag] != 4) and len(DOIS[0]) < 10 and DOIS[4][DynamicTag] != -2:
                        SpawnList.append("27, " + str(PlayerX + random.randint(-300, 300)) + ", 1, " + str(random.randint(-20, 20)))
                if random.randint(0, 1000) == 0 and DOIS[4][DynamicTag] == -1:
                    DOIS[4][DynamicTag] = -2
                    DACL[1][DynamicTag] = 0
                elif random.randint(0, 1200) == 0 and DOIS[4][DynamicTag] == -1:
                    DOIS[3][DynamicTag] = 0
                    DOIS[4][DynamicTag] = 1
                    DACL[2][DynamicTag] = 0
                if DOIS[4][DynamicTag] == -2:
                    DACL[2][DynamicTag] = 4
                    if DACL[1][DynamicTag] == 150:
                        SpawnList.append("28, " + str(DOIS[1][DynamicTag]) + ", " + str(DOIS[2][DynamicTag]))
                    if DACL[1][DynamicTag] == 799:
                        DOIS[4][DynamicTag] = -1
                        DACL[2][DynamicTag] = 3
                if Damage == -1:
                    PlayerIframesAndHP[4] = 10
                    PlayerIframesAndHP[0] = 1
                    PlayerIframesAndHP[3] = 0
            if Damage > 0 and DOIS[9][DynamicTag] == 0:
                DOIS[9][DynamicTag] = 1
                if DOIS[4][DynamicTag] < 0:
                    DOIS[8][DynamicTag] -= 2*Damage
                else:
                    DOIS[8][DynamicTag] -= Damage
                print("HIT! HP REMAINING: " + str(DOIS[8][DynamicTag]))
            if 0 < DOIS[9][DynamicTag] < 150:
                DOIS[9][DynamicTag] += 1
                DACL[0][DynamicTag].ChangeOpacity(55 + 4*DOIS[9][DynamicTag])
            else:
                DOIS[9][DynamicTag] = 0
            
            if DOIS[8][DynamicTag] <= 0:
                DOIS[0][DynamicTag] = 1000
                DOIS[0][DynamicTag + 1] = 1000
                PlayerIframesAndHP[2] += 20000
                screen.fill((0, 0, 0))
                YList[8][29] = 0
                YList[7][29] = 0
                YList[6][29] = 0
                LoadStaticObjects(YList[0], YList[1], YList[2], YList[3], YList[4], YList[5], YList[6], YList[7], YList[8], YList[9], screen, BlockAppendix, XOffsetForScrolls)
                screen.blit(HPpoint, (2*PlayerIframesAndHP[1] -89, 640))
                screen.blit(BottomGameBar, (0, 640))




            
        #Tag, X, Y, Timer, Mode, PathX, PathY, AttackTimer

        if DOIS[0][DynamicTag] == 23:
            DOIS[3][DynamicTag] += 0.1*(200-DOIS[3][DynamicTag])/200
            if math.sqrt((PlayerX - DOIS[1][DynamicTag])**2 + (PlayerY - DOIS[2][DynamicTag])**2) < 100 and DOIS[4][DynamicTag] == 0:
                DOIS[1][DynamicTag] += 20*(PlayerX - DOIS[1][DynamicTag])
                DOIS[4][DynamicTag] = 1
            DOIS[4][DynamicTag] = 1
            DOIS[1][DynamicTag] -= (DOIS[1][DynamicTag] - PlayerX)*0.003 + DOIS[5][DynamicTag]*math.cos(math.radians(DOIS[3][DynamicTag]))
            DOIS[2][DynamicTag] -= (DOIS[2][DynamicTag] - PlayerY)*0.003 + DOIS[5][DynamicTag]*0.5*math.cos(math.radians(DOIS[3][DynamicTag]))
            if Damage == -1:
                PlayerIframesAndHP[4] = 15
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 0
                DOIS[0][DynamicTag] = 1000
            elif Damage > 0:
                DOIS[0][DynamicTag] = 1000

        if DOIS[0][DynamicTag] == 24:
            if Damage == -1:
                PlayerIframesAndHP[4] = 10
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 10
            elif Damage > 0:
                DOIS[0][DynamicTag] = 1000
            DOIS[1][DynamicTag] -= (DOIS[1][DynamicTag] - PlayerX)*0.00015
            DOIS[2][DynamicTag] -= (DOIS[2][DynamicTag] - PlayerY)*0.0003

        if DOIS[0][DynamicTag] == 25:
            DACL[2][DynamicTag] = 0
            if (DOIS[4][0] == 3 or DOIS[4][0] < 0) and DOIS[4][DynamicTag] == 0:
                DOIS[3][DynamicTag] = random.randint(1, 2)
                DOIS[4][DynamicTag] = 1
            if DOIS[3][DynamicTag] == 1:
                if 0 < DOIS[4][DynamicTag] < 500:
                    DOIS[4][DynamicTag] += 1
                    DOIS[1][DynamicTag] += 0.021*(PlayerX - 32 - DOIS[1][DynamicTag])
                    DOIS[2][DynamicTag] += 0.021*(64 - DOIS[2][DynamicTag])
                elif DOIS[4][DynamicTag] == 500:
                    DACL[1][DynamicTag] = 1
                    DOIS[4][DynamicTag] += 1
                elif DACL[1][DynamicTag] > 0 and DOIS[4][DynamicTag] != 0:
                    DACL[2][DynamicTag] = 2
                    if DACL[1][DynamicTag] >= 65 and DOIS[2][DynamicTag] < 500:
                        DOIS[2][DynamicTag] += 16
                        if Damage == -1:
                            PlayerIframesAndHP[4] = 18
                            PlayerIframesAndHP[0] = 1
                            PlayerIframesAndHP[3] = 16*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])
                else:
                    DOIS[4][DynamicTag] = 0
                    DOIS[3][DynamicTag] = 0
            if DOIS[3][DynamicTag] == 2:
                DOIS[4][DynamicTag] += 1
                DACL[2][DynamicTag] = 1
                DOIS[1][DynamicTag] += 0.021*(960 + 900*math.cos(math.radians(DOIS[4][DynamicTag])) - DOIS[1][DynamicTag])
                DOIS[2][DynamicTag] += 0.021*(64 - DOIS[2][DynamicTag])
                if DACL[1][DynamicTag] == 145:
                    SpawnList.append("26, " + str(DOIS[1][DynamicTag] + 32) + ", " + str(DOIS[2][DynamicTag] + 32))
                if DOIS[4][DynamicTag] > 1400:
                    DOIS[3][DynamicTag] = 0
                    DOIS[4][DynamicTag] = 0

            if DOIS[4][DynamicTag] == 0:
                DOIS[3][DynamicTag] = 0
                DOIS[1][DynamicTag] += 0.007*(DOIS[5][0] - DOIS[1][DynamicTag])
                DOIS[2][DynamicTag] += 0.007*(DOIS[6][0] + 64 - DOIS[2][DynamicTag])

        if DOIS[0][DynamicTag] == 26:
            DOIS[2][DynamicTag] += 2
            if Damage == -1:
                PlayerIframesAndHP[4] = 10
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 16*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])
                DOIS[0][DynamicTag] = 1000
            elif Damage > 0:
                DOIS[0][DynamicTag] = 1000

        if DOIS[0][DynamicTag] == 27:
            DOIS[2][DynamicTag] += 2
            DOIS[1][DynamicTag] += DOIS[3][DynamicTag]/20
            if Damage == -1:
                PlayerIframesAndHP[4] = 10
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 16*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])
                DOIS[0][DynamicTag] = 1000

        if DOIS[0][DynamicTag] == 28:
            DOIS[1][DynamicTag] = DOIS[1][0] + 32
            DOIS[2][DynamicTag] = DOIS[2][0] + 125
            if Damage == -1:
                PlayerIframesAndHP[4] = 20
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 16*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])
            if DACL[1][DynamicTag] >= 799:
                DOIS[0][DynamicTag] = 1000
            if DOIS[4][0] != -2:
                DOIS[2][DynamicTag] += 1000

        if DOIS[0][DynamicTag] == 21:
            if Damage == -1:
                PlayerIframesAndHP[4] = 10
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 0
                #Changes the savefile:
                f = open("Save.txt", "w")
                f.write(str(CurrentGlobalLevel + 1) + "\n" +  str(PlayerIframesAndHP[2]) + "\n50\n500\n0")
                f.close()
                
                PortalCalled = True
    if PlayerIframesAndHP[2] == 44444 and CurrentGlobalLevel == 2 and CurrentScene == 16 and len(DOIS[0]) == 1:
        SpawnList.append("21, 1824, 320, 0")


    if DOIS[2][DynamicTag] > 575 and DOIS[0][DynamicTag] != 0:
        DOIS[0][DynamicTag] = 1000
    if DOIS[0][DynamicTag] == 1000 and NoRepeatingDeleteAnim == 0:
        SpawnList.append("0, " + str(DOIS[1][DynamicTag] + 32*DACL[0][DynamicTag].GetScaleFactors()[0]) + ", " + str(DOIS[2][DynamicTag] + 32*DACL[0][DynamicTag].GetScaleFactors()[1]) + ", 0, 0")
    if DOIS[0][DynamicTag] == 1001:
        DOIS[0][DynamicTag] = 1000
    
    DACL[1][DynamicTag] = DACL[0][DynamicTag].PlayAnimation(DOIS[1][DynamicTag] + 1, DOIS[2][DynamicTag] + 1, DACL[1][DynamicTag] + 1, DACL[2][DynamicTag], DACL[3][DynamicTag])

    return(DOIS, SpawnList, PlayerSpawnPos, PlayerY, PlayerX, MovObjectsList, BlockAppendix, BgColor, BgReplace, PortalCalled)
def DOIS_Delete(DOIS, DACL):
    while 1000 in DOIS[0]:
        DeleteDynamicObjects = DOIS[0].index(1000)
        for i in range(len(DOIS)):
            DOIS[i].pop(DeleteDynamicObjects)
        for i in range(0, len(DACL)):
                DACL[i].pop(DeleteDynamicObjects)
    return(DOIS, DACL)


