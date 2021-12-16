put()
while True:
    if not front_is_clear():
        turn_left()
    move()
    if object_here():
        break
