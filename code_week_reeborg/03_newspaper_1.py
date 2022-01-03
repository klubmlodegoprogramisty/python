from library import *

take()
print(carries_object())
for _ in range(3):
    set_north()
    next_level()
while object_here():
    take()
print(carries_object())
put("gwiazda")
print(carries_object())
back()
for _ in range(3):
    prev_level()

# kod biblioteki
def set_north():
    while True:
        if is_facing_north():
            break
        turn_left()
        
def turn_right():
    for _ in range(3):
        turn_left()
        
def next_level():
    move()
    turn_right()
    move()
    move()
    
def back():
    turn_left()
    turn_left()

def prev_level():    
    move()
    move()
    turn_left()
    move()
    turn_right()
    
