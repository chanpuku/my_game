import json
import pygame
import draw_replay
import taku_replay
import controller_replay as controller
import sys
import os
import random




folder='paifu'


file_list=os.listdir(folder)
file_name=random.choice(file_list)


with open(f'{folder}/{file_name}') as file:
	data = json.load(file)
SCREEN_SIZE = (1400,750)  # 画面サイズ
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
taku=taku_replay.taku(data)
draw=draw_replay.draw(taku,screen)
controller=controller.controller(data,screen,taku,draw)
pygame.display.update()# 画面を更新
# ゲームループ
while True:
	# イベント処理
	for event in pygame.event.get():
		if event.type == pygame.QUIT:  # 終了イベント
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			update=controller.mouse_button_down(event.pos)
			if update:
				pygame.display.update()# 画面を更新
		if event.type == pygame.MOUSEBUTTONUP:
			update=controller.mouse_button_up()
			if update:
				pygame.display.update()# 画面を更新
