import matplotlib.pyplot as plt
import math
import time

def draw_line():
    x_number_list = list();
    y_number_list = list();

    for i in range(0,315):
      t = i * 0.02;
      x = math.cos(t * 3)
      y = math.sin(t * 2)
      x_number_list.append(x)
      y_number_list.append(y)
      if abs(x - x_number_list[0]) + abs(y - y_number_list[0]) < 0.01 and i > 1:
        print("iterated " + str(i) + " points")
        break

    plt.plot(1, 1, linewidth=3)
    plt.title("Lissajous Curve", fontsize=19)
    plt.plot(y_number_list, x_number_list, linewidth = 1, c="orange")
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    # Display the plot in the matplotlib's viewer.
    plt.show()    
    plt.savefig('lissajous.png', bbox_inches='tight')


if __name__ == '__main__':
    draw_line()