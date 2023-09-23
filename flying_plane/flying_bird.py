from ursina import *

app = Ursina()

score = 0
player_health = 3

me = Animation(
    'assets/player',  # Use forward slashes or escape backslashes
    collider='box',
    scale=(4, 3),
    y=5
)

Sky()
camera.orthographic = True
camera.fov = 20

Entity(
    model='quad',
    texture="assets/BG",  # Use forward slashes or escape backslashes
    scale=36,
    z=1
)
score_text = Text(text=f"Score: {score}", position=(-0.8, 0.4), scale=2)

health_text = Text(text=f"Health: {player_health}", position=(-0.8, -0.4), scale=2)

game_over_text = Text(text="GAME OVER", scale=4, x=-0.3,y=0)
game_over_text.enabled = False

def input(key):
    if key == 'space':
        bullet = Entity(
            y=me.y,
            x=me.x + 2,
            model="cube",
            texture="assets/bullet.png",  # Use forward slashes or escape backslashes
            collider='box',
        )
        bullet.animate_x(
            30,
            duration=2,
            curve=curve.linear
        )
        invoke(destroy, bullet, delay=2)
        bullets.append(bullet)
fly = Entity(
    model='cube',
    texture="enemy.png",  # Use forward slashes or escape backslashes
    collider='box',
    scale=5,
    x=20,
    y=-10
)
bullets =[]
flies = []

def newfly():
    new = duplicate(
        fly,
        y=-5 + (5124 * time.dt) % 15
    )
    flies.append(new)
    invoke(newfly, delay=1.5)

newfly()

def restart_game():
    global player_health, score

    # Reset player's health and score
    player_health = 3
    score = 0

    # Enable the player
    me.enable()

    # Destroy any remaining flies
    for fly in flies:
        destroy(fly)
    flies.clear()

    # Reset the score and health text


def game_over():
    global high_score,score

    game_over_text.enabled = True
    score_text.text = f"Score: {score}"


    # Hide the player and any remaining flies
    me.disable()
    for fly in flies:
        fly.disable()
    
    if score>high_score:
        high_score = score 


def update():
    global score,player_health
    me.y += held_keys['w'] * 8 * time.dt
    me.x -= held_keys['a'] * 5 * time.dt
    me.y -= held_keys['s'] * 8 * time.dt
    me.x += held_keys['d'] * 5 * time.dt
    a = held_keys['w'] * -20
    b = held_keys['s'] * 20
    if a != 0:
        me.rotation_z = a
    else:
        me.rotation_z = b

    # Collision detection between bullets and flies
    for bullet in bullets:
        for fly in flies:
            if bullet.intersects(fly):  # Check if bullet touches a fly
                destroy(bullet)  # Destroy the bullet
                flies.remove(fly)  # Remove the fly from the list
                destroy(fly)  # Destroy the fly
                score += 1
                score_text.text = f"Score is {score}"

    for fly in flies:
        fly.x -= 4 * time.dt
    #      for fly in flies:
        if me.intersects(fly):  # Check if the player touches a fly
            player_health -= 1  # Decrement player's health
            health_text.text = f"Health: {player_health}"

            # Remove the fly
            flies.remove(fly)
            destroy(fly)

            if player_health <= 0: 
                 # Game over condition
                game_over()
# Initialize the high score (you can load it from a file if needed)
high_score = 0

# Update the high score when the player's score exceeds it
if score > high_score:
    high_score = score

# Display the high score on the game over screen
high_score_text = Text(text=f"High Score: {high_score}", scale=2, y=-0.4)
 

app.run()



# score , quit, Game over, high score