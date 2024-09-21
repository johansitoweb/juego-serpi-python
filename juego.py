import tkinter as tk  
import random  
from tkinter import messagebox  

class SnakeGame:  
    def __init__(self, master):  
        self.master = master  
        self.master.title("Juego de la Serpiente")  

        self.width = 600  
        self.height = 400  
        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg='black')  
        self.canvas.pack()  

        self.snake = [(5, 5)]  # Posición inicial de la serpiente  
        self.direction = (1, 0)  # Dirección inicial (hacia la derecha)  
        self.food = self.place_food()  # Colocar la primera comida  
        self.score = 0  # Inicializar el puntaje  
        self.game_running = True  

        # Etiqueta para mostrar el puntaje  
        self.label = tk.Label(master, text=f"Comida: {self.score}", font=("Arial", 14))  
        self.label.pack()  

        self.master.bind("<KeyPress>", self.change_direction)  # Cambiar dirección con las teclas  
        self.update()  # Iniciar el bucle de actualización  

    def place_food(self):  
        """Colocar comida en un lugar aleatorio que no esté ocupado por la serpiente."""  
        while True:  
            x = random.randint(0, (self.width // 20) - 1) * 20  
            y = random.randint(0, (self.height // 20) - 1) * 20  
            if (x, y) not in self.snake:  
                return (x, y)  

    def change_direction(self, event):  
        """Cambiar la dirección de la serpiente según la tecla presionada."""  
        if event.keysym == 'Up' and self.direction != (0, 1):  
            self.direction = (0, -1)  
        elif event.keysym == 'Down' and self.direction != (0, -1):  
            self.direction = (0, 1)  
        elif event.keysym == 'Left' and self.direction != (1, 0):  
            self.direction = (-1, 0)  
        elif event.keysym == 'Right' and self.direction != (-1, 0):  
            self.direction = (1, 0)  

    def update(self):  
        """Actualizar el juego: mover la serpiente, dibujar y verificar colisiones."""  
        if self.game_running:  
            self.move()  
            self.draw()  
            self.master.after(200, self.update)  # Velocidad reducida  

    def move(self):  
        """Mover la serpiente y verificar si ha comido o si ha perdido."""  
        head_x, head_y = self.snake[0]  
        new_head = (head_x + self.direction[0] * 20, head_y + self.direction[1] * 20)  

        # Comprobación de colisiones (con paredes y consigo misma)  
        if (new_head in self.snake or  
                new_head[0] < 0 or new_head[0] >= self.width or  
                new_head[1] < 0 or new_head[1] >= self.height):  
            self.game_running = False  
            messagebox.showinfo("Juego Terminado", f"¡Perdiste! Has comido {self.score} unidades. Juega de nuevo!")  
            return  

        self.snake.insert(0, new_head)  # Agregar nueva cabeza a la serpiente  

        # Verificar si ha comido la comida  
        if new_head == self.food:  
            self.food = self.place_food()  # Colocar nueva comida  
            self.score += 1  # Aumentar el puntaje  
            self.label.config(text=f"Comida: {self.score}")  # Actualizar el texto del puntaje  
        else:  
            self.snake.pop()  # Mover la serpiente quitando el último segmento  

    def draw(self):  
        """Dibujar la serpiente y la comida en el canvas."""  
        self.canvas.delete(tk.ALL)  # Limpiar el canvas  
        for segment in self.snake:  
            x, y = segment  
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill='green')  # Dibujar la serpiente  

        # Dibujar la comida como una pelota pequeña roja  
        food_x, food_y = self.food  
        self.canvas.create_oval(food_x, food_y, food_x + 10, food_y + 10, fill='red')  # Comida más pequeña  

if __name__ == "__main__":  
    root = tk.Tk()  
    game = SnakeGame(root)  
    root.mainloop()