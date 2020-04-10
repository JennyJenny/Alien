import pygame


class Audio():

    def __init__(self):
        self.play_flag = 1
        self.bg_audio = pygame.mixer.music.load("audio/FarAwayFromHome.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

    def add_shot_sound(self):
        self.shot_sound = pygame.mixer.Sound("audio/shot.wav")
        self.shot_sound.set_volume(0.5)
        self.shot_sound.play()

    def add_crash_sound(self):
        self.crash_sound = pygame.mixer.Sound("audio/crashed.wav")
        self.crash_sound.set_volume(0.5)
        self.crash_sound.play()

    def unpause_pause_music(self):
        # 播放/暂停背景音乐
        if self.play_flag:
            pygame.mixer.music.pause()
            self.play_flag = 0
        else:
            pygame.mixer.music.unpause()
            self.play_flag = 1


