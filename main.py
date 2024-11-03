#import libarys
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

#create an instance of the ursina app
app = Ursina()

#create player
player = FirstPersonController(
    mouse_sensitivity=Vec2(100, 100)
)

#create the ground
ground = Entity(
    model="plane",
    scale=(100, 1, 100),
    Texture="grass",
    texture_scale=(10, 10),
    Collider="true"
)

#run the app
app.run()