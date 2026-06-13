import random

WIDTH = 960
HEIGHT = 540

game_started = False
game_over = False

score = 0
lives = 3

player = Actor("player")
player.pos = (120, HEIGHT // 2)

crystal = Actor("crystal")
crystal.pos = (random.randint(250, 900), random.randint(80, 460))

meteor = Actor("meteor")
meteor.pos = (WIDTH + 100, random.randint(80, 460))

def draw():
    screen.clear()
    screen.blit("background", (0, 0))

    if not game_started:
        draw_start_screen()
    elif game_over:
        draw_game_over()
    else:
        player.draw()
        crystal.draw()
        meteor.draw()
        draw_ui()

def draw_start_screen():
    screen.draw.text(
        "NEON SPACE DASH",
        center=(WIDTH // 2, 170),
        fontsize=70,
        color="cyan"
    )
    screen.draw.text(
        "Press SPACE to Start",
        center=(WIDTH // 2, 260),
        fontsize=36,
        color="white"
    )
    player.draw()

def draw_ui():
    screen.draw.filled_rect(Rect((20, 20), (180, 45)), "#001B5E")
    screen.draw.text(
        "Score: " + str(score),
        topleft=(35, 28),
        fontsize=30,
        color="white"
    )

    screen.draw.filled_rect(Rect((760, 20), (160, 45)), "#001B5E")
    screen.draw.text(
        "Lives: " + str(lives),
        topleft=(780, 28),
        fontsize=30,
        color="white"
    )

def draw_game_over():
    screen.draw.text(
        "GAME OVER",
        center=(WIDTH // 2, 210),
        fontsize=80,
        color="red"
    )
    screen.draw.text(
        "Final Score: " + str(score),
        center=(WIDTH // 2, 300),
        fontsize=40,
        color="white"
    )
    screen.draw.text(
        "Press R to Restart",
        center=(WIDTH // 2, 360),
        fontsize=32,
        color="cyan"
    )

def update():
    global score, lives, game_over

    if not game_started or game_over:
        return

    move_player()
    move_meteor()

    if player.colliderect(crystal):
        score += 1
        crystal.pos = (random.randint(250, 900), random.randint(80, 460))

        try:
            sounds.collect.play()
        except:
            pass

    if player.colliderect(meteor):
        lives -= 1
        meteor.pos = (WIDTH + 100, random.randint(80, 460))

        try:
            sounds.hit.play()
        except:
            pass

        if lives <= 0:
            game_over = True

def move_player():
    speed = 5

    if keyboard.left and player.x > 40:
        player.x -= speed
    if keyboard.right and player.x < WIDTH - 40:
        player.x += speed
    if keyboard.up and player.y > 50:
        player.y -= speed
    if keyboard.down and player.y < HEIGHT - 50:
        player.y += speed

def move_meteor():
    meteor.x -= 5

    if meteor.x < -80:
        meteor.x = WIDTH + 100
        meteor.y = random.randint(80, 460)

def on_key_down(key):
    global game_started, game_over, score, lives

    if key == keys.SPACE:
        game_started = True

    if key == keys.R and game_over:
        score = 0
        lives = 3
        game_over = False
        player.pos = (120, HEIGHT // 2)
        meteor.pos = (WIDTH + 100, random.randint(80, 460))
        crystal.pos = (random.randint(250, 900), random.randint(80, 460)) 