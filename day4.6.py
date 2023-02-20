from math import pi
class Shapes:
    def __init__(self, *args):
        self.args = args
        if len(args) == 1:
            print('Cir')
            print('area:', pi * args[0] * args[0])
            print('perimeter:', 2 * pi * args[0])

        else:
            print('Quad')
            print('area:', args[0] * args[1])
            print('perimeter:', args[0] + args[1] + args[0] + args[1])
s1 = Shapes(10)
s2 = Shapes(10, 20)
