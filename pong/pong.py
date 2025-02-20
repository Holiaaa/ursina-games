from ursina import *

# made by Téo JAUFFRET

def update():
    global speed_x, speed_y
    ball.x += speed_x * time.dt*10
    ball.y += speed_y * time.dt*11

    if abs(ball.x) > 6.3:
        score_sound.play()

        if ball.x > 0:
            score_player2.text = str(int(score_player2.text) + 1)
        else:
            score_player1.text = str(int(score_player1.text) + 1)

        ball.position = (0,0,0)
        speed_x = 0.2

    if abs(ball.y) > 3.3:
        collision_sound.play()
        speed_y = -speed_y

    if ball.intersects(player).hit or ball.intersects(player2).hit:
        if speed_x < 0:
            speed_x -= 0.05
        else:
            speed_x += 0.05
        collision_sound.play()
        speed_x = -speed_x
    
    if held_keys['w']:
        if not abs(player2.y) > 2.8:
            player2.y += .1
        else:
            player2.y = player2.y-0.05
    if held_keys['s']:
        if not abs(player2.y) > 2.8:
            player2.y -= .1
        else:
            player2.y = player2.y+0.05
    
    if held_keys['up arrow']:
        if not abs(player.y) > 2.8:
            player.y += .1
        else:
            player.y = player.y-0.05
    if held_keys['down arrow']:
        if not abs(player.y) > 2.8:
            player.y -= .1
        else:
            player.y = player.y+0.05

app = Ursina()
window.color = color.brown

collision_sound = Audio('touch.ogg', autoplay=False)
score_sound = Audio('score.ogg', autoplay=False)

board = Entity(model="cube", scale=(13.5,7,0), color=color.black)
player = Entity(model="cube", z=-1, scale=(0.2, 2, 0), position=(6,0,0), collider="box")
player2 = Entity(model="cube", z=-1, scale=(0.2, 2, 0), position=(-6,0,0), collider="box")

players = []
players.append(player)
players.append(player2)

ball = Entity(model="sphere", z=-1, scale=(0.2,0.2,0.2), position=(0,0,0),collider="box")

score_player1 = Text("0", scale=(3.5, 3.7, 0), z=-1, position=(0.75, 0.05, 0))
score_player2 = Text("0", scale=(3.5, 3.7, 0), z=-1, position=(-0.8, 0.05, 0))

speed_x = speed_y = 0.2

camera.position = (0,0,-25)

app.run()
