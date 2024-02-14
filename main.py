import keyboard
from time import sleep
import os
from game_manager import *
import sys

def begin(scene_code):
    scene = Scene(scene_code)
    scene.decode_scene()
    scene.draw_scene()
    return scene
def update(scene, refresh_rate):
    score = [0,0]
    if keyboard.is_pressed('p'):
        exit()
    if keyboard.is_pressed('d'):
        can_move = True
        if scene.char_1.pos_x + scene.char_1.width + scene.char_1.stride >= scene.length : can_move = False
        for obstacle in scene.obstacles_pos:
            if scene.char_1.pos_x + scene.char_1.width + scene.char_1.stride >= obstacle and scene.char_1.pos_x + scene.char_1.width + scene.char_1.stride < obstacle + 2:
                can_move = False
        if scene.char_1.pos_x + scene.char_1.width + scene.char_1.stride >= scene.char_2.pos_x: can_move = False
        if can_move : 
            scene.char_1.pos_x += scene.char_1.stride
            os.system('cls')
            scene.draw_scene()
    if keyboard.is_pressed('q'):
        can_move = True
        if scene.char_1.pos_x - scene.char_1.stride <= 0 : can_move = False
        for obstacle in scene.obstacles_pos:
            if scene.char_1.pos_x - scene.char_1.stride <= obstacle + 2 and scene.char_1.pos_x - scene.char_1.stride > obstacle :
                can_move = False
        if can_move : 
            scene.char_1.pos_x -= scene.char_1.stride
            os.system('cls')
            scene.draw_scene()
    if keyboard.is_pressed('left arrow'):
        can_move = True
        if scene.char_2.pos_x - scene.char_2.stride <= 0 : can_move = False
        for obstacle in scene.obstacles_pos:
            if scene.char_2.pos_x - scene.char_2.stride <= obstacle + 2 and scene.char_2.pos_x - scene.char_2.stride > obstacle:
                can_move = False
        if scene.char_2.pos_x - scene.char_2.stride <= scene.char_1.pos_x + scene.char_1.width : can_move = False
        if can_move : 
            scene.char_2.pos_x -= scene.char_2.stride
            os.system('cls')
            scene.draw_scene()
    
        
    if keyboard.is_pressed('right arrow'):
        can_move = True
        if scene.char_2.pos_x + scene.char_2.width + scene.char_2.stride >= scene.length : can_move = False
        for obstacle in scene.obstacles_pos:
            if scene.char_2.pos_x + scene.char_2.width + scene.char_2.stride >= obstacle and scene.char_2.pos_x + scene.char_2.width + scene.char_2.stride < obstacle + 2:
                can_move = False
        if can_move : 
            scene.char_2.pos_x += scene.char_2.stride
            os.system('cls')
            scene.draw_scene()

    if keyboard.is_pressed('l'):
        can_move = True
        scene.char_2.pos_y += scene.char_2.jump_height
        sleep(scene.char_2.movement_speed * refresh_rate)
        os.system('cls')
        scene.draw_scene()
        if scene.char_2.pos_x - scene.char_2.stride <= 0 : can_move = False
        if scene.char_2.pos_x - scene.char_2.stride <= scene.char_1.pos_x + scene.char_1.width : can_move = False
        if can_move : 
            scene.char_2.pos_x -= scene.char_2.stride
            sleep(scene.char_2.movement_speed * refresh_rate)
            os.system('cls')
            scene.draw_scene()
        scene.char_2.pos_y -= scene.char_2.jump_height
        sleep(scene.char_2.movement_speed * refresh_rate)
        os.system('cls')
        scene.draw_scene()

            
        
    if keyboard.is_pressed('m'):
        can_move = True
        scene.char_2.pos_y += scene.char_2.jump_height
        sleep(scene.char_2.movement_speed * refresh_rate)
        os.system('cls')
        scene.draw_scene()
        if scene.char_2.pos_x + scene.char_2.width + scene.char_2.stride >= scene.length : can_move = False
        if can_move : 
            scene.char_2.pos_x += scene.char_2.stride
            os.system('cls')
            scene.draw_scene()
        scene.char_2.pos_y -= scene.char_2.jump_height
        sleep(scene.char_2.movement_speed * refresh_rate)
        os.system('cls')
        scene.draw_scene()

    if keyboard.is_pressed('a'):
        can_move = True
        scene.char_1.pos_y += scene.char_1.jump_height
        sleep(scene.char_1.movement_speed * refresh_rate)
        os.system('cls')
        scene.draw_scene()
        if scene.char_1.pos_x - scene.char_1.stride <= 0 : can_move = False
        if scene.char_1.pos_x - scene.char_1.stride <= scene.char_2.pos_x: can_move = False
        if can_move : 
            scene.char_1.pos_x -= scene.char_1.stride
            os.system('cls')
            scene.draw_scene()
        scene.char_1.pos_y -= scene.char_1.jump_height
        sleep(scene.char_1.movement_speed * refresh_rate)
        os.system('cls')
        scene.draw_scene()
        
    if keyboard.is_pressed('e'):
        can_move = True
        scene.char_1.pos_y += scene.char_1.jump_height
        sleep(scene.char_1.movement_speed * refresh_rate)
        os.system('cls')
        scene.draw_scene()
        if scene.char_1.pos_x + scene.char_1.width + scene.char_1.stride >= scene.char_2.pos_x: can_move = False
        if can_move : 
            scene.char_1.pos_x += scene.char_1.stride
            os.system('cls')
            scene.draw_scene()
        scene.char_1.pos_y -= scene.char_1.jump_height
        sleep(scene.char_1.movement_speed * refresh_rate)
        os.system('cls')
        scene.draw_scene()
    
    if keyboard.is_pressed('o'):
        scene.char_2.state = 1
        os.system('cls')
        scene.draw_scene()
        sleep(scene.char_2.attack_speed * refresh_rate)
        if scene.char_1.state == 0 :
            if scene.char_2.pos_x - scene.char_2.attack_range <= scene.char_1.pos_x + scene.char_1.width:
                score[1] += 1
                #reset scene
                # scene = Scene(INITIAL_SCENE)
                # scene.decode_scene()
                os.system('cls')
                scene.draw_scene()
        if scene.char_1.state == 1 :
            if scene.char_2.pos_x - scene.char_2.attack_range <= scene.char_1.pos_x + scene.char_1.width:
                # scene = Scene(INITIAL_SCENE)
                # scene.decode_scene()
                scene.draw_scene()
                
    
    if keyboard.is_pressed('z'):
        scene.char_1.state = 1
        os.system('cls')
        scene.draw_scene()
        sleep(scene.char_1.attack_speed * refresh_rate)
        if scene.char_2.state == 0 :
            if scene.char_1.pos_x + scene.char_1.width + scene.char_1.stride +scene.char_1.attack_range >= scene.char_2.pos_x :
                score[0] += 1
                # scene = Scene(INITIAL_SCENE)
                # scene.decode_scene()
                os.system('cls')
                scene.draw_scene()
        if scene.char_2.state == 1 :
            if scene.char_1.pos_x + scene.char_1.width + scene.char_1.attack_range+ scene.char_1.stride  >= scene.char_2.pos_x - scene.char_2.attack_range :
                # scene = Scene(INITIAL_SCENE)
                # scene.decode_scene()
                os.system('cls')
                scene.draw_scene()
    sleep(refresh_rate)


if len(sys.argv) < 3 :
    print ("Not enough arguments passed. Please run with python main.py $frames_per_second $scene_file")
    exit(-1)

frames_per_second = int(sys.argv[1])
scene_file = sys.argv[2]

if not scene_file.endswith('.ffscene'):
    print(" Invalid file format")
    exit(-2)
with open(scene_file,'r') as f :
    scene_code = f.read()

scene = begin(scene_code)
refresh_rate = 1 / frames_per_second
while True:
    update(scene,refresh_rate)