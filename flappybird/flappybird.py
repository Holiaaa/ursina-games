from ursina import *
import random

# made by Téo JAUFFRET

def update():
    global velocity, paused, score_incremented, text_display
    if paused:
        if not text_display:
            Text("GAME OVER", color=color.white, scale=(5, 5, 5), position=(-0.35,0.07,0))
            gameover_sound.play()
            text_display = True
        return
    player.y = player.y - velocity

    for pipe_ in pipes:
        pipe_.x = pipe_.x - time.dt*5
        invisible.x = pipe_.x

        if abs(pipe_.x) > 10:
            if abs(pipe_.y) > 10:
                num = random.randint(-2,0)
            else:
                num = random.randint(-4,4)

            pipe.y = pipe.y - num
            pipe2.y = pipe2.y - num

            pipe_.x = 10
            invisible.x = 10
    
    hit_info = player.intersects(pipe) or player.intersects(pipe2)
    if hit_info.hit:
        paused = True

    score_info = player.intersects(invisible)
    if score_info.hit and not score_incremented:
        score_incremented = True
        score.text = str(int(score.text)+1)
    
    if not score_info.hit:
        score_incremented = False
                
def input(key):
    global paused

    if paused:
        return
    if key == "space":
        player.y = player.y + 2
        jump_sound.play()

app = Ursina()
player = Entity(model="cube", scale=(2, 2, 2), color=color.red, collider="box")
pipes = []
pipe = Entity(model="cube", scale=(2, 16, 2), position=(10,-18,0), color=color.green, collider="box", texture="brick")
pipe2 = duplicate(pipe)
pipe2.position = (10, 5, 0)

jump_sound = Audio('jump.ogg', autoplay=False)
gameover_sound = Audio('gameover.ogg', autoplay=False)

score = Text("0", position=(0,0.4,0), scale=(2,2,2))
text_display = False
paused = False
score_incremented = False

pipes.append(pipe)
pipes.append(pipe2)

invisible = Entity(model="cube", color=color.clear, position=(10,pipe.y+pipe2.y*2, 0), scale=(1, 80, 1), collider="box")

camera.position = (0, 0, -60)
velocity = 0.1
app.run()