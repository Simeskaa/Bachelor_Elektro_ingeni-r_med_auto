import numpy as np
import scipy as sci

def cordinate(x, y):  # bære navn trengs
    x_center = x + 350
    y_center = -y + 350
    print(x_center)
    return y_center, x_center
    # if y > 0:
    #     y = -y + 350
    #
    # else:
    #     y =




def main():
    pass


if __name__ == '__main__':
    """
    y_cord = 10
    x_cord = 10
    x_cord, y_cord = cordinate(x_cord, y_cord)
    #cor_x = cordinate.x_center
    main()
    print(f'x = {x_cord}, y = {y_cord}')"""
    y = 300*np.sin(np.pi)
    print(y)
