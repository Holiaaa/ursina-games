from ursina import *

# made by Téo JAUFFRET

def update():
    global speed_x, speed_y, ai_error, dev_mode, activate, editor, ai2_error
    ball.x += speed_x * time.dt*10
    ball.y += speed_y * time.dt*11

    player2.y = ball.y * ai_error
    player.y = ball.y * ai2_error

    if dev_mode and activate:
        activate.text = f"devmod activate!\nai level : {ai_error}/1\nai2 level : {ai2_error}/1\nball speed : {abs(speed_x)}\neditor camera : {'activated' if editor.enabled else 'desactivated'}"

    if abs(ball.x) > 6.3:
        score_sound.play()
        ai_error = random.uniform(0.2, 1)
        ai2_error = random.uniform(0.2, 1)

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

def input(key):
    global activate, dev_mode, editor
    if key == "!":
        if dev_mode:
            dev_mode = False
            destroy(activate)
        else:
            dev_mode = True
            activate = Text(text=f"devmod activate!\nai level : {ai_error}/1\nai2 level : {ai2_error}/1\nball speed : {abs(speed_x)}\neditor camera : {'activated' if editor.enabled else 'desactivated'}", color=color.red)
    
    if dev_mode:
        if key == "c":
            editor.enabled = not editor.enabled

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
ai_error = 0.4
ai2_error = 0.3

ball = Entity(model="sphere", z=-1, scale=(0.2,0.2,0.2), position=(0,0,0),collider="box")

score_player1 = Text("0", scale=(3.5, 3.7, 0), z=-1, position=(0.75, 0.05, 0))
score_player2 = Text("0", scale=(3.5, 3.7, 0), z=-1, position=(-0.8, 0.05, 0))

editor = EditorCamera(enabled=False)

speed_x = speed_y = 0.2

camera.position = (0,0,-25)
dev_mode = False
activate = None

app.run()