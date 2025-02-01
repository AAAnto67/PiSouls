import pygame
pygame.mixer.init()
MusicTracksList = ["MUSIC//GOBLINS.mp3", "MUSIC//CASTLEOUTSIDE.mp3", "MUSIC//CASTLEINSIDE.mp3", "MUSIC//BOSSFIGHT1", "MUSIC//BOSSFIGHT2"]
def ChangeTracks(OldTrack, NewTrack):
    if OldTrack != NewTrack:
        print("MUSIC SWAP")