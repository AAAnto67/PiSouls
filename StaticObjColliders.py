def PlayerColRight(WallX, RowBeingUsed, Debug, screen, BlockAppendix, ColVisualRight, XOffsetForScrolls, PlayerY):
    WallX = WallX
    ColPlayerX = round(WallX + 34)
    WallX = round((ColPlayerX-32)/64)
    HasWallBeenFound = False
    while(HasWallBeenFound == False):
        WallX = WallX + 1
        if BlockAppendix[1][RowBeingUsed[WallX]] == "Static":
            HasWallBeenFound = True
    WallX = WallX*64 
    if Debug:
        screen.blit(ColVisualRight, (WallX - XOffsetForScrolls, PlayerY - 32))
    if(WallX - ColPlayerX <= 32):
        return(True)
    else:
        return(False)

def PlayerColLeft(WallX, RowBeingUsed, BlockAppendix, Debug, screen, ColVisualLeft, XOffsetForScrolls, PlayerY):
    ColPlayerX = round(WallX + 32)
    WallX = round((ColPlayerX-32)/64)
    HasWallBeenFound = False
    while(HasWallBeenFound == False):
        WallX = WallX - 1
        if BlockAppendix[1][RowBeingUsed[WallX]] == "Static":
            HasWallBeenFound = True
    WallX = WallX*64
    if Debug:
        screen.blit(ColVisualLeft, (WallX - XOffsetForScrolls, PlayerY - 32))
    WallX = WallX + 65
    if(ColPlayerX - WallX <= 32):
        return(True)
    else:
        return(False)

def PlayerColFloor(PlayerX, PlayerY, YList, Debug, screen, ColVisualFloor, XOffsetForScrolls, BlockAppendix): 
    GridPositionX = round((PlayerX)/64)
    GridPositionY = round(PlayerY/64)
    TruePlayerY = PlayerY + 32
    PlaceHolderList = YList[GridPositionY]
    while(BlockAppendix[1][PlaceHolderList[GridPositionX]] == ""):
        if GridPositionY > 9:
            GridPositionY = 11
            break
        PlaceHolderList = YList[GridPositionY]
        GridPositionY = GridPositionY + 1
    GridPositionY = GridPositionY - 1
    FloorHeight = 64*GridPositionY
    if Debug:
        screen.blit(ColVisualFloor, (PlayerX - XOffsetForScrolls, FloorHeight))
    if FloorHeight - TruePlayerY <= 32:
        return(True)
    else:
        return(False)

def PlayerColRoof(PlayerX, PlayerY, YList, ColVisualRoof, Debug, screen, XOffsetForScrolls, BlockAppendix):
    GridPositionX = round((PlayerX)/64)
    GridPositionY = round(PlayerY/64)
    TruePlayerY = PlayerY + 32
    PlaceHolderList = YList[GridPositionY]
    while(BlockAppendix[1][PlaceHolderList[GridPositionX]] == ""):
        if GridPositionY < -10:
            GridPositionY = -11
            break
        PlaceHolderList = YList[GridPositionY]
        GridPositionY = GridPositionY - 1
    GridPositionY = GridPositionY + 1
    RoofHeight = (GridPositionY + 1)*64
    if Debug:
        screen.blit(ColVisualRoof, (PlayerX - XOffsetForScrolls, RoofHeight - 64))
    if round(TruePlayerY)- RoofHeight <= 32:
        return(True)
    else:
        return(False)
    
def FindRow(PlayerY, YList):
    if PlayerY >= 576:
        return(YList[9])
    else:
        PlayerY = round(PlayerY/64)
        return(YList[PlayerY])

def InitCollider(PlayerSpeed, PlayerY, XOffsetForScrolls, PlayerX, BlockAppendix, Debug, screen, ColVisualRight, ColVisualLeft, YList, ColVisualFloor, ColVisualRoof, HasPlayerDashed):


    PlayerRow0 = FindRow(PlayerY + 26, YList)
    PlayerRow1 = FindRow(PlayerY - 30, YList)
    IsPlayerTouchingRight1 = PlayerColRight(PlayerX, PlayerRow0, Debug, screen, BlockAppendix, ColVisualRight, XOffsetForScrolls, PlayerY)
    IsPlayerTouchingRight2 = PlayerColRight(PlayerX, PlayerRow1, Debug, screen, BlockAppendix, ColVisualRight, XOffsetForScrolls, PlayerY)
    IsPlayerTouchingLeft1 = PlayerColLeft(PlayerX, PlayerRow0, BlockAppendix, Debug, screen, ColVisualLeft, XOffsetForScrolls, PlayerY)
    IsPlayerTouchingLeft2 = PlayerColLeft(PlayerX, PlayerRow1, BlockAppendix, Debug, screen, ColVisualLeft, XOffsetForScrolls, PlayerY)
    IsPlayerTouchingFloor1 = PlayerColFloor(PlayerX - 27, PlayerY, YList, Debug, screen, ColVisualFloor, XOffsetForScrolls, BlockAppendix)
    IsPlayerTouchingFloor2 = PlayerColFloor(PlayerX + 27, PlayerY, YList, Debug, screen, ColVisualFloor, XOffsetForScrolls, BlockAppendix)
    IsPlayerTouchingRoof1 = PlayerColRoof(PlayerX - 27, PlayerY, YList, ColVisualRoof, Debug, screen, XOffsetForScrolls, BlockAppendix)
    IsPlayerTouchingRoof2 = PlayerColRoof(PlayerX + 27, PlayerY, YList, ColVisualRoof, Debug, screen, XOffsetForScrolls, BlockAppendix)

    if(IsPlayerTouchingRight1 == False and IsPlayerTouchingRight2 == False):
        IsPlayerTouchingRight = False
    else:
        IsPlayerTouchingRight = True
    if(IsPlayerTouchingLeft1 == False and IsPlayerTouchingLeft2 == False):
        IsPlayerTouchingLeft = False
    else:
        IsPlayerTouchingLeft = True
    if(IsPlayerTouchingFloor1 == False and IsPlayerTouchingFloor2 == False):
        IsPlayerTouchingFloor = False
    else:
        IsPlayerTouchingFloor = True
        HasPlayerDashed = False
    if(IsPlayerTouchingRoof1 == False and IsPlayerTouchingRoof2 == False):
        IsPlayerTouchingRoof = False
    else:
        IsPlayerTouchingRoof = True
    
    if IsPlayerTouchingRight and PlayerSpeed[0] >= 0.0001:
        PlayerSpeed[0] = 0
    if IsPlayerTouchingLeft and PlayerSpeed[0] <= -0.0001:
        PlayerSpeed[0] = 0
    if IsPlayerTouchingRoof:
        PlayerSpeed[1] = 0
        PlayerY = PlayerY + 1
        IsPlayerTouchingRoof = False

    return(PlayerSpeed, PlayerY, IsPlayerTouchingFloor, IsPlayerTouchingRoof, IsPlayerTouchingLeft, IsPlayerTouchingRight, HasPlayerDashed)

def CollisionsWithPlayer(X, Y, ScaleFactorList, DashHitboxList, PlayerX, PlayerY, screen, XOffsetForScrolls, PlayerIframesAndHP):
    HighestDamage = 0
    
    if (abs(PlayerY + 32 - (Y + 32*(1 + ScaleFactorList[1]))) <= 32*(2 + ScaleFactorList[1])*0.8) and (abs(PlayerX + 32 - (X + 32*(1 + ScaleFactorList[0]))) <= 32*(2 + ScaleFactorList[0])*0.8) and PlayerIframesAndHP[0] == 0:
        HighestDamage = -1

    for i in range(len(DashHitboxList[0])):
        if (abs(DashHitboxList[1][i] - (Y + 32*(1 + ScaleFactorList[1]))) <= 30*(2 + ScaleFactorList[1])) and (abs(DashHitboxList[0][i] - (X + 32*(1 + ScaleFactorList[0]))) <= 30*(2 + ScaleFactorList[0])) and DashHitboxList[2][i] > HighestDamage:
            HighestDamage = DashHitboxList[2][i]
    return(HighestDamage)
