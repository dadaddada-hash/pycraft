import sys
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Create an instance of the ursina app
app = Ursina()

# Create player
player = FirstPersonController(
    mouse_sensitivity=Vec2(100, 100),
    position=(0, 10, 0)
)

# Load texture
block_textures = {
    "stone": load_texture("Assets\Textures\Stone01.png"),
    "dirt": load_texture("Assets\Textures\groundMud.png"),
    "bedrock": load_texture(""),
    "grass": load_texture("Assets/Textures/groundEarth.png")
}

# Create the ground
ground = Entity(
    model="plane",
    scale=(100, 1, 100),
    texture=block_textures["grass"],
    texture_scale=(100, 100),
    collider="box"
)

# Run the app
app.run()
