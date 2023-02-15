#Kardo-Tamm_IS22
 #Avage fail lugemiseks
#with open("sammud.txt", "r") as f:
    # Read the lines of the file into a list of integers
#    steps_data = [int(line.strip()) for line in f.readlines()]

 #Arvutab sammude koguarvu
#total_steps = sum(steps_data)
#print("Total number of steps for the week:", total_steps)

 #Arvutab keskmise sammude arvu päevas
#average_steps = total_steps / len(steps_data)
#print("Average number of steps per day:", average_steps)

 #Leidke kõige suurema ja väikseima sammuga päev
#max_steps = max(steps_data)
#min_steps = min(steps_data)
#max_day = steps_data.index(max_steps) + 1
#min_day = steps_data.index(min_steps) + 1

 #Kirjutab tulemused
#print("Day with the most steps:", max_day, "with", max_steps, "steps")
#print("Day with the least steps:", min_day, "with", min_steps, "steps")


import turtle

# Funktsioon failist käskude lugemiseks ja nende teisendamiseks kilpkonna liikumiseks sobivasse vormingusse
def read_commands(file_path):
    commands = []
    with open(file_path, 'r') as f:
        for line in f:
            tokens = line.strip().split(' ')
            commands.append(tokens)
    return commands

# Funktsioon kilpkonnaga kujundi joonistamiseks käskude abil
def draw_shape(commands, turtle):
    for cmd in commands:
        if cmd[0] == 'forward':
            turtle.forward(int(cmd[1]))
        elif cmd[0] == 'backward':
            turtle.backward(int(cmd[1]))
        elif cmd[0] == 'right':
            turtle.right(int(cmd[1]))
        elif cmd[0] == 'left':
            turtle.left(int(cmd[1]))
        elif cmd[0] == 'circle':
            turtle.circle(int(cmd[1]))
        elif cmd[0] == 'penup':
            turtle.penup()
        elif cmd[0] == 'pendown':
            turtle.pendown()
        elif cmd[0] == 'pencolor':
            turtle.pencolor(cmd[1])
        elif cmd[0] == 'fillcolor':
            turtle.fillcolor(cmd[1])
        elif cmd[0] == 'beginfill':
            turtle.begin_fill()
        elif cmd[0] == 'endfill':
            turtle.end_fill()

# Küsib kasutajalt, mitu korda kujundit joonistada
num_shapes = int(input("How many times to draw the shape? "))

# Loeb failist käske
commands = read_commands('kilpkonn.txt')

# Loob kilpkonn aja määrab akna taustavärvi
bg_color = input("Enter a background color (in English): ")
window = turtle.Screen()
window.bgcolor(bg_color)
t = turtle.Turtle()
t.speed(0)

# Joonistab kujundit mitu korda
for i in range(num_shapes):
    draw_shape(commands, t)

# Väljuge programmist, kui kasutaja klõpsab ekraanil või vajutab Ctrl+C
turtle.exitonclick()
