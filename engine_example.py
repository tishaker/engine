import tkinter as tk
import time
from engine_outputs import Engine_Output, Engine_fap

class Vector2:
    """Custom math class to handle object positions and physics."""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class GameObject:
    """The base blueprint for any visual item inside your engine."""
    def __init__(self, x, y, width, height, color):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.width = width
        self.height = height
        self.color = color

    def update(self, delta_time):
        # Manually calculate movement physics based on time passed
        self.position.x += self.velocity.x * delta_time
        self.position.y += self.velocity.y * delta_time

class Engine:
    """Buddy, this shit is actually genius, I just wanna goon on our new engine>)"""
    engine1 = Engine_Output("Engine1", 10, 5)
    engine1.engine_strength_output()
    engine_fap1 = Engine_fap("FapEngine", 8, 4, 100)
    engine_fap1.engine_strength_output()

    """The core engine pipeline handling windows, inputs, loops, and rendering."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Pure Python Engine")
        
        # Create a raw visual canvas
        self.canvas_width = 800
        self.canvas_height = 800
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()

        # Input Tracker State
        self.keys = {}
        self.root.bind("<KeyPress>", lambda e: self.keys.__setitem__(e.keysym, True))
        self.root.bind("<KeyRelease>", lambda e: self.keys.__setitem__(e.keysym, False))

        # Scene Data
        self.player = GameObject(400, 400, 40, 40, "lime")
        self.last_time = time.time()

    def process_input(self):
        # Core player movement logic mapped directly to raw keystrokes
        speed = 250 
        self.player.velocity.x = 0
        self.player.velocity.y = 0
        
        if self.keys.get("Left") or self.keys.get("a"):  self.player.velocity.x = -speed
        if self.keys.get("Right") or self.keys.get("d"): self.player.velocity.x = speed
        if self.keys.get("Up") or self.keys.get("w"):    self.player.velocity.y = -speed
        if self.keys.get("Down") or self.keys.get("s"):  self.player.velocity.y = speed

    def render(self):
        # Completely clear the canvas for the new frame
        self.canvas.delete("all")
        
        # Render the game object based on its custom spatial coordinates
        x1 = self.player.position.x - (self.player.width / 2)
        y1 = self.player.position.y - (self.player.height / 2)
        x2 = self.player.position.x + (self.player.width / 2)
        y2 = self.player.position.y + (self.player.height / 2)
        
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.player.color, outline="")

    def run_loop(self):
        # Strict delta time tracking to ensure consistent speeds
        current_time = time.time()
        delta_time = current_time - self.last_time
        self.last_time = current_time

        self.process_input()
        self.player.update(delta_time)
        self.render()

        # Request the engine to run this loop again in ~16 milliseconds (~60 FPS)
        self.root.after(16, self.run_loop)

    def start(self):
        self.run_loop()
        self.root.mainloop()

if __name__ == "__main__":
    engine = Engine()
    engine.start()
