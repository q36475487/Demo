import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('保卫媳妇小牛牛之哒哒哒打击大蛇蛇')

    # 生出一只小AA
    small_aa = Ship(ai_settings,screen)

    # 开始游戏主循环
    while True:
        gf.check_events(small_aa)
        small_aa.update()
        gf.update_screen(ai_settings,screen,small_aa)
run_game()