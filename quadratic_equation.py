from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2


if __name__ == '__main__':
    print('Hi! I can solve quadratic equations!')
    while True:
        try:
            a = int(input('Input first coefficent (a): '))
            b = int(input('Input second coefficent (b): '))
            c = int(input('Input last coefficent (c): '))
        except ValueError:
            print('\nCoefficent must be number only!\n')
            continue
        root1, root2 = get_roots(a, b, c)
        print('Roots of your equation are {0} and {1}'.format(root1, root2))
        break
