import tkinter as tk
import time

class Vectorf2D:
    """Custom math class to handle object positions and physics."""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class GameObject:
    """The base blueprint for any visual item inside your engine."""
    def __init__(self, x, y, vx=0.0, vy=0.0, width=40, height=40, color="white", gravity=500, on_ground=False):
        self.position = Vectorf2D(x, y)
        self.velocity = Vectorf2D(vx, vy)
        self.width = width
        self.height = height
        self.color = color
        self.gravity = gravity
        self.on_ground = on_ground


    def update(self, delta_time):
        if not self.on_ground:
            self.velocity.y += self.gravity * delta_time

        self.position.x += self.velocity.x * delta_time
        self.position.y += self.velocity.y * delta_time

        if self.position.y >= 300:
            self.position.y = 300
            self.velocity.y = 0
            self.on_ground = True

class Engine:
    """The core engine pipeline handling windows, inputs, loops, and rendering."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Pure Python Engine")
        
        # Create a raw visual canvas
        self.canvas_width = 800
        self.canvas_height = 600
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()

        # Input Tracker State
        self.keys = {}
        self.root.bind_all("<KeyPress>", lambda e: self.keys.__setitem__(e.keysym, True))
        self.root.bind_all("<KeyRelease>", lambda e: self.keys.__setitem__(e.keysym, False))

        # Scene Data
        self.player = GameObject(400, 300, 10, 10, 40, 40, "orange", gravity=500, on_ground=False)
        self.last_time = time.time()

    def process_input(self):
        
        speed = 250 
        self.player.velocity.x = 0
        
        if self.keys.get("Left") or self.keys.get("a"):
            self.player.velocity.x = -speed
        if self.keys.get("Right") or self.keys.get("d"):
            self.player.velocity.x = speed

        jump_pressed = self.keys.get("Up") or self.keys.get("w")
        if jump_pressed and self.player.on_ground:
            self.player.velocity.y = -300
            self.player.on_ground = False

        if self.keys.get("Down") or self.keys.get("s"):
            self.player.velocity.y = speed

    def render(self):
        
        self.canvas.delete("all")
        
        # Render the game object based on its custom spatial coordinates
        x1 = self.player.position.x - (self.player.width / 2)
        y1 = self.player.position.y - (self.player.height / 2)
        x2 = self.player.position.x + (self.player.width / 2)
        y2 = self.player.position.y + (self.player.height / 2)
        
        
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.player.color, outline="")

    def run_loop(self):
        
        current_time = time.time()
        delta_time = current_time - self.last_time
        self.last_time = current_time

        self.process_input()
        self.player.update(delta_time)
        self.render()
        self.root.after(16, self.run_loop)

    def start(self):
        self.run_loop()
        self.root.mainloop()

if __name__ == "__main__":
    engine = Engine()
    engine.start()
