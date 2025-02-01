
from PIL import Image
im = Image.open("Levels//ExampleLevel.png")

DOIS[1][DynamicTag] += DOIS[4][DynamicTag]
            DOIS[3][DynamicTag] += 1
            if DACL[2][DynamicTag] != 2 and DOIS[6][DynamicTag] == 0:
                if 1000 >= DOIS[3][DynamicTag] >= DOIS[5][DynamicTag]:
                    DOIS[4][DynamicTag] = -DOIS[4][DynamicTag]
                    DOIS[3][DynamicTag] = 0
                    DOIS[5][DynamicTag] = random.randint(200, 700)
                if DOIS[4][DynamicTag] <= -0.0001:
                    DACL[2][DynamicTag] = 0
                elif DOIS[4][DynamicTag] >= 0.0001:
                    DACL[2][DynamicTag] = 1
            if 0 <= DOIS[1][DynamicTag] - PlayerX + 32 <= 500 and DOIS[6][DynamicTag] == 0 and random.randint(0, 1100) == 200:
                DACL[1][DynamicTag] = 0
                DOIS[6][DynamicTag] = 1
                DOIS[4][DynamicTag] = 0
                DOIS[3][DynamicTag] = 0
            if DOIS[6][DynamicTag] == 1:
                DACL[2][DynamicTag] = 2
                if DOIS[3][DynamicTag] == 310:
                    SpawnList.append("8, " + str(DOIS[1][DynamicTag]) + ", " + str(DOIS[2][DynamicTag] + 32) + ", 0, 0")
                if 1000 >= DOIS[3][DynamicTag] >= 700:
                    DOIS[6][DynamicTag] = 0
                    DOIS[4][DynamicTag] = -0.1
                    DOIS[3][DynamicTag] = 0
                    DACL[2][DynamicTag] = 1
            if math.sqrt((DOIS[7][DynamicTag] - DOIS[1][DynamicTag])**2) >= 150:
                DOIS[4][DynamicTag] = 0.1*(DOIS[7][DynamicTag] - DOIS[1][DynamicTag])/math.sqrt((DOIS[7][DynamicTag] - DOIS[1][DynamicTag])**2)
                DOIS[3][DynamicTag] = 1200
            if DOIS[3][DynamicTag] >= 1900:
                DOIS[3][DynamicTag] = 0
                DOIS[4][DynamicTag] = -DOIS[4][DynamicTag]
            if Damage > 0 and DACL[2][DynamicTag] == 2 and DACL[1][DynamicTag] >= 330 or Damage == 5:
                DOIS[0][DynamicTag] = 1000
                PlayerIframesAndHP[2] += 500
            elif Damage == -1:
                PlayerIframesAndHP[4] = 8
                PlayerIframesAndHP[0] = 1
                PlayerIframesAndHP[3] = 6*(PlayerX-DOIS[1][DynamicTag])/abs(PlayerX-DOIS[1][DynamicTag])