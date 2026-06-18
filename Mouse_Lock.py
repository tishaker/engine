import tkinter as tk
import time

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
        self.position.x += self.velocity.x * delta_time
        self.position.y += self.velocity.y * delta_time

class Engine:

    """The core engine pipeline handling windows, inputs, loops, and rendering."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Pure Python Engine")

        self.canvas_width = 800
        self.canvas_height = 600
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()

        self.keys = {}
        self.root.bind("<KeyPress>", lambda e: self.keys.__setitem__(e.keysym, True))
        self.root.bind("<KeyRelease>", lambda e: self.keys.__setitem__(e.keysym, False))

        self.player = GameObject(400, 300, 10, 10, "lime")
        
        self.painted_blocks = []
        
        self.last_time = time.time()

        self.canvas.bind("<Motion>", self.on_mouse_move)
        self.canvas.bind("<Button-1>", self.on_mouse_click)

    def on_mouse_move(self, event):
        self.player.position.x = event.x
        self.player.position.y = event.y
        
    def on_mouse_click(self, event):
        new_block = GameObject(event.x, event.y, 10, 10, "white")
        self.painted_blocks.append(new_block)

    def render(self):
        # Completely clear the canvas for the new frame
        self.canvas.delete("all")
        
        for block in self.painted_blocks:
            x1 = block.position.x - (block.width / 2)
            y1 = block.position.y - (block.height / 2)
            x2 = block.position.x + (block.width / 2)
            y2 = block.position.y + (block.height / 2)
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=block.color, outline="")
        
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
        
        self.player.update(delta_time)
        self.render()

        # Request the engine to run this loop again in ~16 milliseconds (~60 FPS)
        self.root.after(8, self.run_loop)

    def start(self):
        self.run_loop()
        self.root.mainloop()

if __name__ == "__main__":
    engine = Engine()
    engine.start()
