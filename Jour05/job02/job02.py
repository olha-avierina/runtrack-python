# 
def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height-1:
            print('-' * width)
        else:
            print('|' + ' ' * (width-2) + '|')

# Example:
draw_rectangle(12, 8)
