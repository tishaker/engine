import tkinter
import time

class PhysVector:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
class PhysObject:
    def __init__(self, x, y, width, height, color):
        self.position = PhysVector(x, y)
        self.velocity = PhysVector(0, 0)
        self.acceleration = PhysVector(0, 0)
        self.width = width
        self.height = height
        self.color = color

    def update(self, delta_time):
        # Update velocity based on acceleration
        self.velocity.x += self.acceleration.x * delta_time
        self.velocity.y += self.acceleration.y * delta_time
        
        # Update position based on velocity
        self.position.x += self.velocity.x * delta_time
        self.position.y += self.velocity.y * delta_time

class Engine:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Motion with Acceleration Example")
        
        self.canvas_width = 800
        self.canvas_height = 800
        self.canvas = tkinter.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()

        self.keys = {}
        self.root.bind("<KeyPress>", lambda e: self.keys.__setitem__(e.keysym, True))
        self.root.bind("<KeyRelease>", lambda e: self.keys.__setitem__(e.keysym, False))

        self.player = PhysObject(400, 400, 40, 40, "cyan")
        self.last_time = time.time()

    def start(self):
        self.update()
        self.root.mainloop()

    def update(self):
        current_time = time.time()
        delta_time = current_time - self.last_time
        self.last_time = current_time

        # Update player position based on key presses
        if self.keys.get("Left"):
            self.player.acceleration.x = -100
        elif self.keys.get("Right"):
            self.player.acceleration.x = 100
        else:
            self.player.acceleration.x = 0

        if self.keys.get("Up"):
            self.player.acceleration.y = -100
        elif self.keys.get("Down"):
            self.player.acceleration.y = 100
        else:
            self.player.acceleration.y = 0

        self.player.update(delta_time)

        # Clear the canvas and redraw the player
        self.canvas.delete("all")
        self.canvas.create_rectangle(
            self.player.position.x,
            self.player.position.y,
            self.player.position.x + self.player.width,
            self.player.position.y + self.player.height,
            fill=self.player.color
        )

        # Schedule the next update
        self.root.after(16, self.update)  # Approximately 60 FPS

if __name__ == "__main__":
    engine = Engine()
    engine.start()