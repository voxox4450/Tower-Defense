#library
import pygame, time, random, os
#other class
from button import Button, Text, ButtonPP
from interface import Hud
from map import Map
#slimes map 1
from MAP_1.slime_1 import Slime_1
from MAP_1.slime_2 import Slime_2
from MAP_1.slime_3 import Slime_3
from MAP_1.slime_4 import Slime_4
from MAP_1.slime_5 import Slime_5
from MAP_1.slime_6 import Slime_6
#slimes map 2
from MAP_2.slime_1_map2 import Slime_1_map_2
from MAP_2.slime_2_map2 import Slime_2_map_2
from MAP_2.slime_3_map2 import Slime_3_map_2
from MAP_2.slime_4_map2 import Slime_4_map_2
from MAP_2.slime_5_map2 import Slime_5_map_2
from MAP_2.slime_6_map2 import Slime_6_map_2
#slimes map 3
from MAP_3.slime_1_map3 import Slime_1_map_3
from MAP_3.slime_2_map3 import Slime_2_map_3
from MAP_3.slime_3_map3 import Slime_3_map_3
from MAP_3.slime_4_map3 import Slime_4_map_3
from MAP_3.slime_5_map3 import Slime_5_map_3
from MAP_3.slime_6_map3 import Slime_6_map_3
#import towers
from Tower_1 import Tower1Long
from Tower_2 import Tower2Short
from Tower_3 import Tower3Medium
from Tower_4 import Tower4Slow
from Tower_5 import Tower5Money
from support_Tower1 import Support_Range_Tower
from support_Tower2 import Support_DMG_Tower

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_mode((1300, 900))
screen = pygame.display.set_mode((1300, 900))
pygame.display.set_caption("Tower Defense")

LIGHTPINK = pygame.color.THECOLORS['lightpink']
BLACK = pygame.color.THECOLORS['black']
RED = pygame.color.THECOLORS['red']
GREEN = pygame.color.THECOLORS['green']
YELLOW = pygame.color.THECOLORS['yellow']
BLUE = pygame.color.THECOLORS['blue']
VIOLET = pygame.color.THECOLORS['violet']

#Loading images
new_game_img = pygame.image.load("jpg/MENU/button_new_game.png").convert_alpha()
options_img = pygame.image.load("jpg/MENU/button_options.png").convert_alpha()
quit_img = pygame.image.load("jpg/MENU/button_quit.png").convert_alpha()
audio_imgplus = pygame.image.load('jpg/interface/TD_menu_plus.png').convert_alpha()
audio_imgminus = pygame.image.load('jpg/interface/TD_menu_minus.png').convert_alpha()
back_img = pygame.image.load('jpg/MENU/button_back.png').convert_alpha()
continue_img = pygame.image.load('jpg/MENU/button_resume.png').convert_alpha()

new_game_button_button = Button(55, 700, new_game_img, 0.75)
options_button = Button(470, 700, options_img, 0.75)
quit_button = Button(885, 700, quit_img, 0.75)
plus = Button(450, 250, audio_imgplus, 0.5)
minus = Button(450, 250, audio_imgminus, 0.5)
back_button = Button(570, 600, back_img, 0.5)

#MENU IN GAME
resume_img = pygame.image.load("jpg/MENU/button_resume_game.png").convert_alpha()
options_img = pygame.image.load("jpg/MENU/button_options_game.png").convert_alpha()
quit_img = pygame.image.load("jpg/MENU/button_back_to_menu.png").convert_alpha()
back_img = pygame.image.load('jpg/MENU/button_back.png').convert_alpha()
back_img2 = pygame.image.load('jpg/MENU/button_back_to_menu.png').convert_alpha()

resume_button2 = Button(410, 220, resume_img, 0.75)
options_button2 = Button(410, 370, options_img, 0.75)
quit_button2 = Button(410, 520, quit_img, 0.75)
audio_button2plus = Button(810, 250, audio_imgplus, 1)
audio_button2minus = Button(310, 250, audio_imgminus, 1)
back_button2 = Button(490, 640, back_img, 1)
quit_button3 = Button(490, 800, back_img2, 0.5)

BG_LOGO = pygame.image.load("jpg/bg/TD_logo3.png").convert_alpha()
BG_LOGO = Button(106, 0, BG_LOGO, 0.40)
BG_LOGO_2 = pygame.image.load("jpg/bg/TD_logo.png").convert_alpha()
BG_LOGO_2 = Button(106, 0, BG_LOGO_2, 0.40)

CMAP = pygame.image.load("jpg/MENU/TD_menu4_wybormap.png").convert_alpha()
CMAP_2 = pygame.image.load("jpg/MENU/TD_menu4_wybormap.png").convert_alpha()
CMAP_3 = pygame.image.load("jpg/MENU/TD_menu4_wybormap.png").convert_alpha()
CMAP = Button(100, 304, CMAP, 0.75)
CMAP_2 = Button(470, 304, CMAP_2, 0.75)
CMAP_3 = Button(840, 304, CMAP_3, 0.75)

GAME_1 = pygame.image.load("jpg/MAPS/TD_map_vanilla.png").convert()
GAME_1 = pygame.transform.scale(GAME_1, (241, 167))
GAME_1 = Button(145, 349, GAME_1, 1)

GAME_2 = pygame.image.load("jpg/MAPS/TD_map_winter.png").convert()
GAME_2 = pygame.transform.scale(GAME_2, (241, 167))
GAME_2 = Button(515, 349, GAME_2, 1)

GAME_3 = pygame.image.load("jpg/MAPS/TD_map_citl.png").convert()
GAME_3 = pygame.transform.scale(GAME_3, (241, 167))
GAME_3 = Button(885, 349, GAME_3, 1)

text_game_1 = Text("Village", BLACK, 270, 556, 50, 'Berlin Sans FB Demi')
text_game_2 = Text("Winter", BLACK, 640, 556, 50, 'Berlin Sans FB Demi')
text_game_3 = Text("City", BLACK, 1010, 556, 50, 'Berlin Sans FB Demi')
finish_text = Text("YOU LOSE", BLACK, *screen.get_rect().center, 248, "Impact")
win_text = Text("YOU WIN", BLACK, *screen.get_rect().center, 248, "Impact")

#lives
lives_image = pygame.image.load("jpg/SLIMES/LIVES/TD_menu3_zycie.png").convert_alpha()
lives_image = pygame.transform.scale(lives_image, (64, 64))
money_image = pygame.image.load("jpg/SLIMES/LIVES/TD_menu3_waluta.png").convert_alpha()
money_image = pygame.transform.scale(money_image, (64, 64))

#sidebar
tower_1_img = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu3_Tower_1.png")), (60, 60))
tower_2_img = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu3_Tower_2.png")), (60, 60))
tower_3_img = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu3_Tower_3.png")), (60, 60))
tower_4_img = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu3_Tower_4.png")), (60, 60))
tower_5_img = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu3_Tower_5.png")), (60, 60))
support_1_img = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu_BUFF1.png")), (60, 60))
support_2_img = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu_BUFF2.png")), (60, 60))

#play off game/music
play_on = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu_play.png")), (60, 60))
play_off = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu_stop.png")), (60, 60))
play_music_on = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu_soundON.png")), (60, 60))
play_music_off = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu_soundOFF.png")), (60, 60))

sidebar_wave = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu_sidebar.png")), (100, 300)),270)

all_attack_names = ["long", "short", "medium", "slow", "money"]
all_support_names = ['support1', "support2"]
waves = [
    [ 15,   5,   5,   1,   0,   0],
    [ 20,  10,   6,   5,   0,   0],#2
    [ 50,   0,  20,   0,   0,   0],
    [ 50,  20,  40,  22,   0,   0],#4
    [150,  50,   0,  25,  10,   0],
    [  0, 100,  50,   0,  20,   5],#6
    [100, 100,  75,  25,  15,   6],
    [105, 100, 100,  50,  50,  15],#8
    [100, 100, 100,  75,  75,  50],
    [100, 100, 100, 100, 100, 100],#10
    [200, 150, 125, 100, 100, 100],
    [300, 200, 150, 125, 100, 100],#12
    [400, 250, 175, 150, 125, 100],
    [500, 300, 200, 200, 150, 125],#14
    [600, 350, 250, 225, 200, 150]#15
]
waves_map2 = [
    [40,  5,  5,  1,  0,   0],
    [20, 10,  5,  1,  1,   0],#2
    [25, 15, 10,  3,  2,   0],
    [30, 20, 15,  5,  2,   1],#4
    [35, 25, 20, 10,  3,   1],
    [40, 30, 25, 15,  4,   1],#6
    [45, 35, 30, 20,  5,   1],
    [50, 40, 35, 25,  7,   3],#8
    [55, 45, 40, 30, 10,   5],
    [60, 50, 45, 35, 14,   5],#10
    [65, 55, 50, 40, 18,   7],
    [70, 60, 55, 45, 22,  10],#12
    [75, 65, 60, 50, 25,  13],
    [80, 70, 65, 55, 30,  15],#14
    [85, 75, 70, 60, 35,  20] #15
]
waves_map3 = [
    [40,  5,  5,  1,  0,   0],
    [50, 10,  5,  1,  1,   0],#2
    [51, 25, 10,  3,  1,   0],
    [52, 30, 12,  5,  1,   0],#4
    [53, 35, 14, 10,  2,   0],
    [54, 40, 16, 15,  2,   1],#6
    [55, 45, 20, 20,  2,   2],
    [56, 50, 22, 25,  3,   3],#8
    [57, 51, 25, 30,  5,   4],
    [58, 52, 30, 35,  5,   5],#10
    [59, 55, 35, 40,  5,   6],
    [60, 60, 40, 45,  7,   7],#12
    [60, 65, 60, 50, 10,   8],
    [60, 70, 65, 55, 15,   9],#14
    [65, 75, 70, 60, 20,  10] #15
]

class Game:
    def __init__(self):
        self.width = 1300
        self.height = 900
        self.screen = pygame.display.set_mode((1300, 900))

        #Variables
        self.menu_state = "main_menu"
        self.MAIN_MENU = False
        self.GAME_ACTIVE = False
        self.game_paused = False
        self.selected_tower = 0
        self.object = None
        self.pause = True
        self.music = False
        self.new_volume = 0.1

        #enemies
        self.enemies = []
        self.enemies_map_2 = []
        self.enemies_map_3 = []

        #towers
        self.attack_towers = []
        self.attack_towers_map_2 = []
        self.attack_towers_map_3 = []
        self.support_towers = []
        self.support_towers_map_2 = []
        self.support_towers_map_3 = []

        #GAME
        self.lives = 3
        self.money = 5000
        self.money_map2 = 6000
        self.money_map3 = 7333
        self.lives_init = self.lives
        self.list_money = [self.money, self.money_map2, self.money_map3]
        self.timer = time.time()
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.current_wave_map2 = waves_map2[self.wave][:]
        self.current_wave_map3 = waves_map3[self.wave][:]
        self.ButtonPP = ButtonPP(self.width-135, self.height-65, play_on, play_off)
        self.ButtonPPmusic = ButtonPP(self.width-70, self.height-65, play_music_on, play_music_off)

        #fonts
        self.font_lives = pygame.font.SysFont("Berlin Sans FB Demi", 64)
        self.font_wave = pygame.font.SysFont("Brush Script", 94)

        #backbrounds
        self.BG_MENU = pygame.image.load("jpg/bg/TD_background.png").convert()
        self.BG_MENU = pygame.transform.scale(self.BG_MENU, (1300, 900))

        self.BG_MENU_2 = self.BG_MENU

        #map 1
        self.BG_GAME_1 = pygame.image.load("jpg/MAPS/TD_map_vanilla.png").convert()
        self.BG_GAME_1 = pygame.transform.scale(self.BG_GAME_1, (1300, 900))
        self.hud = Hud(self.width-80, 200)
        self.hud.add_button(tower_1_img, -15, 0, 'tower_1_img', 500)
        self.hud.add_button(tower_2_img, -15, -70, 'tower_2_img', 650)
        self.hud.add_button(tower_3_img, -15, -140, 'tower_3_img', 750)
        self.hud.add_button(tower_4_img, -15, -210, 'tower_4_img', 1000)
        self.hud.add_button(tower_5_img, -15, -280, 'tower_5_img', 1200)
        self.hud.add_button(support_1_img, -15, -350, 'support_1_img', 200)
        self.hud.add_button(support_2_img, -15, -420, 'support_2_img', 200)

        #map 2
        self.BG_GAME_2 = pygame.image.load("jpg/MAPS/TD_map_winter.png").convert()
        self.BG_GAME_2 = pygame.transform.scale(self.BG_GAME_2, (1300, 900))

        #map 3
        self.BG_GAME_3 = pygame.image.load("jpg/MAPS/TD_map_citl.png").convert()
        self.BG_GAME_3 = pygame.transform.scale(self.BG_GAME_3, (1300, 900))
        self.hud_map3 = Hud(410, 5)
        self.hud_map3.add_button(tower_1_img, 0, -5, 'tower_1_img', 500)
        self.hud_map3.add_button(tower_2_img, -70, -5, 'tower_2_img', 650)
        self.hud_map3.add_button(tower_3_img, -140, -5, 'tower_3_img', 750)
        self.hud_map3.add_button(tower_4_img, -210, -5, 'tower_4_img', 1000)
        self.hud_map3.add_button(tower_5_img, -280, -5, 'tower_5_img', 1200)
        self.hud_map3.add_button(support_1_img, -350, -5, 'support_1_img', 200)
        self.hud_map3.add_button(support_2_img, -420, -5, 'support_2_img', 200)

        #list of scenes
        self.bg_list = [self.BG_MENU, self.BG_MENU_2, self.BG_GAME_1, self.BG_GAME_2, self.BG_GAME_3]

        #music
        self.playlist = [
            "music/17 - Space Shuttle (156bpm) - YP BEATS.mp3",
            "music/49 - L2R2 (130bpm) - YP BEATS.mp3",
            "music/24 - Ballistic Missle (170bpm) - YP BEATS.mp3"
        ]
        self.current_song_index = random.randint(0, 2)
        pygame.mixer.music.load(self.playlist[self.current_song_index])
        pygame.mixer.music.set_volume(self.new_volume)
        pygame.mixer.music.play()

    def run(self):
        pygame.mixer.music.load(self.playlist[self.current_song_index])
        pygame.mixer.music.play()
        self.run = True
        clock = pygame.time.Clock()
        while self.run:
            clock.tick(60)
            pos = pygame.mouse.get_pos()

            self.handle_events(pos)

            if self.MAIN_MENU:
                self.draw(1)
                BG_LOGO_2.draw(self.screen)
                game_list = [GAME_1, GAME_2, GAME_3]
                text_list = [text_game_1, text_game_2, text_game_3]
                CMAP_list = [CMAP,CMAP_2,CMAP_3]
                for game, text, choose in zip(game_list, text_list, CMAP_list):
                    if game.rect.collidepoint(pygame.mouse.get_pos()):
                        text.text_color = LIGHTPINK
                    else:
                        text.text_color = BLACK
                    choose.draw(self.screen)
                    text.draw(self.screen)

                if self.menu_state == 'Menu_2':
                    if quit_button3.draw(self.screen):
                        pygame.time.delay(200)
                        self.menu_state = "main_menu"
                        self.MAIN_MENU = False
                    if GAME_1.draw(self.screen):
                        pygame.time.delay(200)
                        self.menu_state = 'GAME1'
                        self.GAME_ACTIVE = '1'
                        self.MAIN_MENU = False
                    else:
                        text_game_1.text_color = BLACK
                    if GAME_2.draw(self.screen):
                        pygame.time.delay(200)
                        self.menu_state = 'GAME2'
                        self.GAME_ACTIVE = '2'
                        self.MAIN_MENU = False
                    if GAME_3.draw(self.screen):
                        pygame.time.delay(200)
                        self.menu_state = 'GAME3'
                        self.GAME_ACTIVE = '3'
                        self.MAIN_MENU = False
                    # MAP 1
            elif self.GAME_ACTIVE == '1':
                self.draw(2)
                if self.game_paused:
                    if self.menu_state == "GAME1":
                        # draw pause screen buttons
                        if resume_button2.draw(self.screen):
                            self.game_paused = False
                        if options_button2.draw(self.screen):
                            self.menu_state = "options"
                        if quit_button2.draw(self.screen):
                            self.menu_state = "main_menu"
                            self.game_paused = False
                            self.MAIN_MENU = False
                            self.GAME_ACTIVE = False
                            self.enemies.clear()
                            self.current_wave.clear()
                            self.support_towers.clear()
                            self.attack_towers.clear()
                            self.lives = self.lives_init
                            self.money = self.list_money[0]
                            self.wave = 0
                            self.current_wave = waves[self.wave][:]
                    if self.menu_state == "options":
                        if audio_button2plus.draw(self.screen):
                            current_volume = pygame.mixer.music.get_volume()
                            self.new_volume = min(current_volume + 0.1, 1.0)
                            pygame.mixer.music.set_volume(self.new_volume)
                            if pygame.mixer.music.get_volume() == 0:
                                self.music = False
                                self.ButtonPPmusic.paused = self.music
                            else:
                                self.music = True
                                self.ButtonPPmusic.paused = self.music

                        if audio_button2minus.draw(self.screen):
                            current_volume = pygame.mixer.music.get_volume()
                            self.new_volume = max(current_volume - 0.1, 0.0)
                            pygame.mixer.music.set_volume(self.new_volume)
                            if pygame.mixer.music.get_volume() == 0:
                                self.music = False
                                self.ButtonPPmusic.paused = self.music
                            else:
                                self.music = True
                                self.ButtonPPmusic.paused = self.music

                        if back_button2.draw(self.screen):
                            self.menu_state = "GAME1"
                else:
                    self.draw_hud(self.hud)
                    map1 = Map(self, self.attack_towers, self.support_towers, self.enemies, self.hud, 1, self.money, self.current_wave)
                    map1.game()
                    if self.lives <= 0:
                        self._reset_game(finish_text, RED)
            # MAP 2
            elif self.GAME_ACTIVE == '2':
                self.draw(3)
                if self.game_paused:
                    if self.menu_state == "GAME2":
                        # draw pause screen buttons
                        if resume_button2.draw(self.screen):
                            self.game_paused = False
                        if options_button2.draw(self.screen):
                            self.menu_state = "options"
                        if quit_button2.draw(self.screen):
                            self.menu_state = "main_menu"
                            self.game_paused = False
                            self.MAIN_MENU = False
                            self.GAME_ACTIVE = False
                            self.enemies_map_2.clear()
                            self.current_wave_map2.clear()
                            self.support_towers_map_2.clear()
                            self.attack_towers_map_2.clear()
                            self.lives = self.lives_init
                            self.money_map2 = self.list_money[1]
                            self.current_wave_map2 = 0
                            self.wave = 0
                            self.current_wave_map2 = waves_map2[self.wave][:]
                    if self.menu_state == "options":
                        if audio_button2plus.draw(self.screen):
                            current_volume = pygame.mixer.music.get_volume()
                            self.new_volume = min(current_volume + 0.1, 1.0)
                            pygame.mixer.music.set_volume(self.new_volume)
                            if pygame.mixer.music.get_volume() == 0:
                                self.music = False
                                self.ButtonPPmusic.paused = self.music
                            else:
                                self.music = True
                                self.ButtonPPmusic.paused = self.music

                        if audio_button2minus.draw(self.screen):
                            current_volume = pygame.mixer.music.get_volume()
                            self.new_volume = max(current_volume - 0.1, 0.0)
                            pygame.mixer.music.set_volume(self.new_volume)
                            if pygame.mixer.music.get_volume() == 0:
                                self.music = False
                                self.ButtonPPmusic.paused = self.music
                            else:
                                self.music = True
                                self.ButtonPPmusic.paused = self.music
                        if back_button2.draw(self.screen):
                            self.menu_state = "GAME2"
                else:
                    self.draw_hud(self.hud)
                    map2 = Map(self, self.attack_towers_map_2, self.support_towers_map_2, self.enemies_map_2, self.hud, 2, self.money_map2, self.current_wave_map2)
                    map2.game()
                    if self.lives <= 0:
                        self._reset_game(finish_text, BLUE)
            # MAP 3
            elif self.GAME_ACTIVE == '3':
                self.draw(4)
                if self.game_paused:
                    if self.menu_state == "GAME3":
                        # draw pause screen buttons
                        if resume_button2.draw(self.screen):
                            self.game_paused = False
                        if options_button2.draw(self.screen):
                            self.menu_state = "options"
                        if quit_button2.draw(self.screen):
                            self.menu_state = "main_menu"
                            self.game_paused = False
                            self.MAIN_MENU = False
                            self.GAME_ACTIVE = False
                            self.enemies_map_3.clear()
                            self.current_wave_map3.clear()
                            self.support_towers_map_3.clear()
                            self.attack_towers_map_3.clear()
                            self.lives = self.lives_init
                            self.money_map3 = self.list_money[2]
                            self.wave = 0
                            self.current_wave_map3 = waves_map3[self.wave][:]
                    if self.menu_state == "options":
                        if audio_button2plus.draw(self.screen):
                            current_volume = pygame.mixer.music.get_volume()
                            self.new_volume  = min(current_volume + 0.1, 1.0)
                            pygame.mixer.music.set_volume(self.new_volume)
                            if pygame.mixer.music.get_volume() == 0:
                                self.music = False
                                self.ButtonPPmusic.paused = self.music
                            else:
                                self.music = True
                                self.ButtonPPmusic.paused = self.music

                        if audio_button2minus.draw(self.screen):
                            current_volume = pygame.mixer.music.get_volume()
                            self.new_volume  = max(current_volume - 0.1, 0.0)
                            pygame.mixer.music.set_volume(self.new_volume)
                            if pygame.mixer.music.get_volume() == 0:
                                self.music = False
                                self.ButtonPPmusic.paused = self.music
                            else:
                                self.music = True
                                self.ButtonPPmusic.paused = self.music

                        if back_button2.draw(self.screen):
                            self.menu_state = "GAME3"
                else:
                    self.draw_hud(self.hud_map3)
                    map3 = Map(self, self.attack_towers_map_3, self.support_towers_map_3, self.enemies_map_3, self.hud_map3, int(self.GAME_ACTIVE), self.money_map3, self.current_wave_map3)
                    map3.game()
                    if self.lives <= 0:
                        self._reset_game(finish_text, VIOLET)

            else:
                self.draw(0)
                BG_LOGO.draw(self.screen)
                if self.menu_state == "main_menu":
                    if new_game_button_button.draw(self.screen):
                        self.MAIN_MENU = True
                        self.menu_state = "Menu_2"
                    if options_button.draw(self.screen):
                        self.menu_state = "options_menu"
                    if quit_button.draw(self.screen):
                        self.run = False
                if self.menu_state == "options_menu":
                    if audio_button2plus.draw(self.screen):
                        current_volume = pygame.mixer.music.get_volume()
                        self.new_volume = min(current_volume + 0.1, 1.0)
                        pygame.mixer.music.set_volume(self.new_volume)
                        if pygame.mixer.music.get_volume() == 0:
                            self.music = False
                            self.ButtonPPmusic.paused = self.music
                        else:
                            self.music = True
                            self.ButtonPPmusic.paused = self.music

                    if audio_button2minus.draw(self.screen):
                        current_volume = pygame.mixer.music.get_volume()
                        self.new_volume = max(current_volume - 0.1, 0.0)
                        pygame.mixer.music.set_volume(self.new_volume)
                        if pygame.mixer.music.get_volume() == 0:
                            self.music = False
                            self.ButtonPPmusic.paused = self.music
                        else:
                            self.music = True
                            self.ButtonPPmusic.paused = self.music

                    if back_button.draw(self.screen):
                        self.menu_state = "main_menu"
        pygame.quit()

    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["tower_1_img", "tower_2_img", "tower_3_img", "tower_4_img", "tower_5_img","support_1_img", "support_2_img"]
        object_list = [Tower1Long(x, y), Tower2Short(x, y), Tower3Medium(x, y), Tower4Slow(x, y), Tower5Money(x,y), Support_Range_Tower(x,y), Support_DMG_Tower(x,y)]
        obj = object_list[name_list.index(name)]
        self.object = obj
        obj.moving = True

    def gen(self, enemies, map_number, wave_map):
        if sum(wave_map) == 0:
            if len(enemies) == 0:
                self.wave += 1
                self.pause = False
                self.ButtonPP.paused = self.pause
                self.lives += 1
                try:
                    if map_number == 1:
                        self.current_wave = waves[self.wave]
                    elif map_number == 2:
                        self.current_wave_map2 = waves_map2[self.wave]
                    elif map_number == 3:
                        self.current_wave_map3 = waves_map3[self.wave]
                except IndexError:
                    self._reset_game(win_text, GREEN)

        else:
            wave_enemies = [
                Slime_1(), Slime_2(), Slime_3(),
                Slime_4(), Slime_5(), Slime_6()
            ]
            wave_enemies_map2 = [
                Slime_1_map_2(), Slime_2_map_2(), Slime_3_map_2(),
                Slime_4_map_2(), Slime_5_map_2(), Slime_6_map_2()
            ]
            wave_enemies_map3 = [
                Slime_1_map_3(), Slime_2_map_3(), Slime_3_map_3(),
                Slime_4_map_3(), Slime_5_map_3(), Slime_6_map_3()
            ]

            wave_enemies_map = {
                1: wave_enemies,
                2: wave_enemies_map2,
                3: wave_enemies_map3
            }

            for x in range(len(wave_map)):
                if wave_map[x] != 0:
                    enemies.append(wave_enemies_map[map_number][x])
                    wave_map[x] -= 1
                    break

    def handle_events(self, pos):
        self.ButtonPPmusic.draw(self.screen)
        if not pygame.mixer.music.get_busy():
            self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
            pygame.mixer.music.load(self.playlist[self.current_song_index])
            pygame.mixer.music.play()
        # moving obj
        if self.object:
            self.object.move(pos[0], pos[1])

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if self.pause:
                    if event.key == pygame.K_ESCAPE and self.GAME_ACTIVE:
                        self.game_paused = True
                        self.pause = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.object:
                    if self.object.name in all_attack_names:
                        if self.GAME_ACTIVE == '1':
                            self.attack_towers.append(self.object)
                        elif self.GAME_ACTIVE == '2':
                            self.attack_towers_map_2.append(self.object)
                        elif self.GAME_ACTIVE == '3':
                            self.attack_towers_map_3.append(self.object)
                    if self.object.name in all_support_names:
                        if self.GAME_ACTIVE == '1':
                            self.support_towers.append(self.object)
                        elif self.GAME_ACTIVE == '2':
                            self.support_towers_map_2.append(self.object)
                        elif self.GAME_ACTIVE == '3':
                            self.support_towers_map_3.append(self.object)
                    self.object.moving = False
                    self.object = None

                else:
                    # Play/Pause
                    if self.ButtonPP.click(pos[0], pos[1]):
                        self.pause = not self.pause
                        self.ButtonPP.paused = self.pause
                    # play/pause music
                    if self.ButtonPPmusic.click(pos[0], pos[1]):
                        self.music = not self.music
                        self.ButtonPPmusic.paused = self.music
                        if self.music:
                            pygame.mixer.music.set_volume(self.new_volume)
                        else:
                            pygame.mixer.music.set_volume(0)

                    if self.GAME_ACTIVE == '1':
                        # sidebar
                        self.sidebar_cliced = self.hud.get_clicked(pos[0], pos[1])
                        if self.sidebar_cliced:
                            if self.money >= self.hud.get_item_cost(self.sidebar_cliced):
                                self.money -= self.hud.get_item_cost(self.sidebar_cliced)
                                self.add_tower(self.sidebar_cliced)

                    if self.GAME_ACTIVE == '2':
                        # sidebar
                        self.sidebar_cliced = self.hud.get_clicked(pos[0], pos[1])
                        if self.sidebar_cliced:
                            if self.money_map2 >= self.hud.get_item_cost(self.sidebar_cliced):
                                self.money_map2 -= self.hud.get_item_cost(self.sidebar_cliced)
                                self.add_tower(self.sidebar_cliced)

                    if self.GAME_ACTIVE == '3':
                        # sidebar
                        self.sidebar_cliced = self.hud_map3.get_clicked(pos[0], pos[1])
                        if self.sidebar_cliced:
                            if self.money_map3 >= self.hud_map3.get_item_cost(self.sidebar_cliced):
                                self.money_map3 -= self.hud_map3.get_item_cost(self.sidebar_cliced)
                                self.add_tower(self.sidebar_cliced)

                    # upgrade and sell towers
                    self.name_click = None
                    money = 0
                    if self.selected_tower:
                        if self.GAME_ACTIVE == '1':
                            money = self.money
                        elif self.GAME_ACTIVE == '2':
                            money = self.money_map2
                        elif self.GAME_ACTIVE == '3':
                            money = self.money_map3

                        self.name_click = self.selected_tower.interface.get_clicked(pos[0], pos[1])

                        if self.name_click == 'upgrade':
                            try:
                                if money >= self.selected_tower.interface.buying():
                                    money -= self.selected_tower.interface.buying()
                                    self.selected_tower.upgrade()
                                    self.name_click = None
                            except TypeError:
                                self.selected_tower.price[self.selected_tower.level-1] = 'MAX'

                        if self.name_click == 'sell':
                            money += self.selected_tower.interface.selling()
                            lists_of_towers = [
                                self.attack_towers, self.support_towers,
                                self.attack_towers_map_2, self.support_towers_map_2,
                                self.attack_towers_map_3, self.support_towers_map_3
                            ]

                            for tower_list in lists_of_towers:
                                if self.selected_tower in tower_list:
                                    for tower in (self.support_towers, self.support_towers_map_2, self.support_towers_map_3):
                                        if self.selected_tower in tower:
                                            for tower in self.selected_tower.effected:
                                                if isinstance(self.selected_tower, Support_Range_Tower):
                                                    tower.range = tower.original_range
                                                if isinstance(self.selected_tower, Support_DMG_Tower):
                                                    tower.damage = tower.original_damage
                                                self.name_click = None
                                    tower_list.remove(self.selected_tower)
                                    self.name_click = None

                        if self.GAME_ACTIVE == '1':
                            self.money = money
                        elif self.GAME_ACTIVE == '2':
                            self.money_map2 = money
                        elif self.GAME_ACTIVE == '3':
                            self.money_map3 = money

                    if not self.name_click:
                        all_attack_towers = self.attack_towers + self.attack_towers_map_2 + self.attack_towers_map_3
                        all_support_towers = self.support_towers + self.support_towers_map_2 + self.support_towers_map_3
                        for tower in all_attack_towers:
                            if tower.click(pos[0], pos[1]):
                                tower.selected = True
                                self.selected_tower = tower
                            else:
                                tower.selected = False
                        for tower in all_support_towers:
                            if tower.click(pos[0], pos[1]):
                                tower.selected = True
                                self.selected_tower = tower
                            else:
                                tower.selected = False

            elif event.type == pygame.QUIT:
                self.run = False

    def _reset_game(self, text, color,):
        self.menu_state = "main_menu"
        self.MAIN_MENU = False
        self.GAME_ACTIVE = False
        self.game_paused = False
        self.selected_tower = 0
        self.object = None
        self.pause = True
        self.lives = self.lives_init
        self.money = self.list_money[0]
        self.money_map2 = self.list_money[1]
        self.money_map3 = self.list_money[2]
        self.timer = time.time()
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.current_wave_map2 = waves_map2[self.wave][:]
        self.current_wave_map3 = waves_map3[self.wave][:]
        self.enemies = []
        self.enemies_map_2 = []
        self.enemies_map_3 = []
        self.attack_towers = []
        self.attack_towers_map_2 = []
        self.attack_towers_map_3 = []
        self.support_towers = []
        self.support_towers_map_2 = []
        self.support_towers_map_3 = []
        self.pause = True
        self.ButtonPP.paused = self.pause
        pygame.time.delay(500)
        self.screen.fill(color)
        text.draw(self.screen)
        pygame.display.flip()
        pygame.time.delay(2000)

    def draw(self, which):
        pygame.display.update()
        self.screen.blit(self.bg_list[which], (0, 0))

    def draw_lives(self):
        text = self.font_lives.render(str(self.lives), True, BLACK)
        live = lives_image
        start_x = self.width - live.get_width() - 10
        self.screen.blit(text, (start_x, 0))
        self.screen.blit(live, (start_x - live.get_width(), 10))

    def draw_currency(self, money_map):
        text_currency = self.font_lives.render(str(money_map), True, BLACK)
        money = money_image
        start_x = self.width - money.get_width() - 10
        if 0 <= money_map <= 99:
            self.screen.blit(text_currency, (start_x - 10, 80))
            self.screen.blit(money, (start_x - lives_image.get_width() - 10, 90))
        if 100 <= money_map <= 999:
            self.screen.blit(text_currency, (start_x - 45, 80))
            self.screen.blit(money, (start_x - lives_image.get_width() - 45, 90))
        if 1000 <= money_map <= 9999:
            self.screen.blit(text_currency, (start_x - 80, 80))
            self.screen.blit(money, (start_x - lives_image.get_width() - 80, 90))
        if 10000 <= money_map:
            self.screen.blit(text_currency, (start_x - 115, 80))
            self.screen.blit(money, (start_x - lives_image.get_width() - 115, 90))

    def draw_wave(self):
        text_wave = self.font_wave.render('Wave '+str(self.wave+1), False, (255, 255, 255))
        self.screen.blit(sidebar_wave, (5, 5))
        self.screen.blit(text_wave, (15, -5))

    def draw_hud(self, hud):
        hud.draw(self.screen, int(self.GAME_ACTIVE))
        self.ButtonPP.draw(self.screen)
