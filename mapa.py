from pygame import image, Color

moveimage = image.load("mapa.jpg) 

def check_move_point(gracz):
    move_x, move_y = 0, 0
    if gracz.keys_active["right"]:
        move_x = 1
    if gracz.keys_active["up"]:
        move_y = -1
    if gracz.keys_active["left"]:
        move_x = -1
    if gracz.keys_active["down"]:
        move_x = 1

    if moveimage.get_at((int(gracz.x+move_x), int(gracz.y+move_y - 80)))  != Color("black"):
        return False
    return True

def get_possible_directions(enemy):
    black_width = 18 #umowna, bo są różne, lepiej żeby była mniejsza
    directions = [0, 0, 0, 0] #right, up, left, down
    
    move_x, move_y = enemy.decide_point
    dpx = enemy.x + move_x
    dpy = enemy.y + move_y                   
    
    if moveimage.get_at((int(dpx + black_width), int(dpy - 80))) == Color("black):
        directions[0] = 1
    if moveimage.get_at((int(dpx), int(dpy - 80 - black_width))) == Color("black"):
        directions[1] = 1
    if moveimage.get_at((int(dpx - black_width), int(dpy - 80))) == Color("black"):
        directions[2] = 1
    if moveimage.get_at((int(dpx), int(dpy - 80 + 18))) == Color("black"):
        directions[3] = 1
    return directions
