from ursina import *
import random

# made by Téo JAUFFRET

def update():
    global velocity, dev_mod, activate, paused, game_over
    if paused:
        if not game_over:
            game_over = Text("GAME OVER", color=color.white, scale=(5, 5, 5), position=(-0.35,0.07,0))
            music_loop.stop()
            game_over = True
        return

    if abs(player.y) < 2.3:
        player.y = player.y - velocity

    score.text = str(int(score.text) + 1)

    if abs(enemy.x) > 8:
        size = random.randint(-1,1)
        if size < 0:
            if enemy.scale_y < 3:
                enemy.scale_y = enemy.scale_y + 1
            else:
                enemy.scale_y = enemy.scale_y - 1
        if size == 0:
            pass
        if size > 0:
            if enemy.scale_x < 3:
                enemy.scale_x = enemy.scale_x + 0.2
            else:
                enemy.scale_x = enemy.scale_x - 0.2

        enemy.x = 8
    
    enemy.x = enemy.x - velocity

    collider = player.intersects(enemy)
    if collider.hit:
        paused = True

    if dev_mod:
        if activate:
            activate.text = f"devmod activate!\nCamera position = {editor_camera.position}"

        if held_keys['d']:
            camera.position = (camera.x+0.05, camera.y, camera.z)
        
        if held_keys['s']:
            camera.position = (camera.x, camera.y, camera.z-0.05)
        
        if held_keys['w']:
            camera.position = (camera.x, camera.y, camera.z+0.05)

        if held_keys['a']:
            camera.position = (camera.x-0.05, camera.y, camera.z)

def jump_step(i=0):
    if i < 20:
        player.y += 0.15
        player.rotation_z += 4.5
        invoke(jump_step, i+1, delay=0.02)

def input(key):
    global velocity, dev_mod, activate, paused
    if key == "space" and not paused:
        jump_step()
        jump_sound.play()

    if key == "!":
        if not dev_mod:
            dev_mod = True
            activate = Text(text=f"devmod activate!\nCamera position = {editor_camera.position}", color=color.red)
        else:
            dev_mod = False
            destroy(activate)

app = Ursina()

plate = Entity(model="cube", color=color.white, scale=(16, 0.5, 1), texture="white_cube", position=(0,-3,0))
player = Entity(model="cube", scale=(0.75,0.75,0.75), texture="player.png", collider="box")

enemy = Entity(model="cube", scale=(0.5,1,0.75), color=color.red, collider="box", position=(8, -2.2, 0))
score = Text("0", position=(0,0.4,0), scale=(2,2,2))

jump_sound = Audio("jump.ogg", autoplay=False)
music_loop = Audio("loop.ogg", autoplay=True, loop=True)

velocity = 0.05
dev_mod = False
activate = None
paused = False
game_over = False
camera.position = (0,0,-20)
editor_camera = EditorCamera()
app.run()
