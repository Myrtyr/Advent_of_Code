x_s = 201
x_e = 230
y_s = -99
y_e = -65

def calc_highest():
    diff = 0-y_s
    max_velocity = diff - 1
    top = 0
    for i in range(1, max_velocity+1):
        top += i
    return top

print(calc_highest())


def check_in_box(x_vel, y_vel):
    x = 0
    y = 0
    while x < x_e and y > y_s:
        x += x_vel
        y += y_vel
        if x > x_e or y < y_s:
            x -= x_vel
            y -= y_vel
            break
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        y_vel -= 1
    return (y_s <= y <= y_e) and (x_s <= x <= x_e)


total = 0
for x_try in range(0,x_e+1):
    for y_try in range(-abs(y_s), abs(y_s)+1):
        if check_in_box(x_try, y_try):
            total += check_in_box(x_try, y_try)
print(total)
