import math
import pygame
def PlayerDash(DashFrameTimer, DashHitboxList, PlayerX, PlayerY, PlayerSpeed, IsPlayerTouchingFloor, PlayerStaticBool, PlayerIframesAndHP):
    if PlayerIframesAndHP[0] == 2:
        DashFrameTimer = 0
        DashHitboxList[0][0] = -100
        DashHitboxList[1][0] = -100
    if DashFrameTimer != 0:
        DashFrameTimer = DashFrameTimer + 2

        if DashFrameTimer == 41:
            PlayerSpeed[0] = PlayerSpeed[0] * 10
            PlayerSpeed[1] = -0.1
        elif DashFrameTimer == 51:
            PlayerSpeed[0] = PlayerSpeed[0]/4
        if 24 <= DashFrameTimer <= 181 and PlayerSpeed[0] != 0:
            DashHitboxList[0][0] = PlayerX + 32 + 64 * ((PlayerSpeed[0])/math.sqrt((PlayerSpeed[0])**2))
            DashHitboxList[1][0] = PlayerY + 32
        if DashFrameTimer >= 171 or IsPlayerTouchingFloor:
            PlayerStaticBool = False
            DashHitboxList[0][0] = -100
            DashHitboxList[1][0] = -100
            DashFrameTimer = 0 
    else:
        DashFrameTimer = 0
        DashHitboxList[0][0] = -100
        DashHitboxList[1][0] = -100
    return(DashHitboxList, PlayerStaticBool, PlayerSpeed, DashFrameTimer)

def PlayerSmash(PlayerChargeTimer, PlayerCharge, ACL, WhichCharge, PlayerSpeed, DashHitboxList, PlayerX, PlayerY, PlayerStaticBool):
    if PlayerChargeTimer == 1:
        ACL[1][2] = 0
        ACL[1][3] = 0
    if 1 <= PlayerCharge <= 249:
        ACL[2][0] = 4
        WhichCharge = 1
    elif 250 <= PlayerCharge:
        ACL[2][0] = 5
        WhichCharge = 2
    if PlayerChargeTimer != 0:
        PlayerChargeTimer = PlayerChargeTimer + 2
        PlayerStaticBool = True
        PlayerSpeed[0] = 0
        ACL[2][0] = 0
        if  PlayerChargeTimer >= 150*WhichCharge:
            PlayerChargeTimer = 0
            for i in range(0, len(DashHitboxList[0])):
                DashHitboxList[0][i] = -100
                DashHitboxList[1][i] = -100 
            WhichCharge = 0
        if WhichCharge >= 1 and 0 <= PlayerChargeTimer <= 400:
            if ACL[3][0] == 0:
                DashHitboxList[0][6] = PlayerX + 96
            if ACL[3][0] == 1:
                DashHitboxList[0][6] = PlayerX - 32
            DashHitboxList[1][6] = PlayerY + 32
            ACL[1][2] = ACL[0][2].PlayAnimation(DashHitboxList[0][6] - 32, DashHitboxList[1][6] - 32, ACL[1][2] + 1, ACL[2][2], ACL[3][2])
        if WhichCharge >= 2 and PlayerChargeTimer >= 100:
            if ACL[3][0] == 0:
                DashHitboxList[0][1] = PlayerX + 160
                DashHitboxList[0][2] = PlayerX + 160
            if ACL[3][0] == 1:
                DashHitboxList[0][1] = PlayerX - 96
                DashHitboxList[0][2] = PlayerX - 96
            DashHitboxList[1][1] = PlayerY + 32
            DashHitboxList[1][2] = PlayerY - 32
            ACL[1][3] = ACL[0][3].PlayAnimation(DashHitboxList[0][2] - 32, DashHitboxList[1][2] - 40, ACL[1][3] + 1, ACL[2][3], ACL[3][3])
        #if WhichCharge >= 3 and PlayerChargeTimer >= 220:
        #    if ACL[3][0] == 0:
        #        DashHitboxList[0][3] = PlayerX + 224
        #        DashHitboxList[0][4] = PlayerX + 224
        #        DashHitboxList[0][5] = PlayerX + 224
        #    if ACL[3][0] == 1:
        #        DashHitboxList[0][3] = PlayerX - 160
        #        DashHitboxList[0][4] = PlayerX - 160
        #        DashHitboxList[0][5] = PlayerX - 160
        #    DashHitboxList[1][3] = PlayerY + 32
        #    DashHitboxList[1][4] = PlayerY - 32
        #    DashHitboxList[1][5] = PlayerY -96
    return(WhichCharge, ACL, DashHitboxList, PlayerSpeed, PlayerStaticBool, PlayerChargeTimer)