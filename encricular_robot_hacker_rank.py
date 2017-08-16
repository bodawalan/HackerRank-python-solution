import sys
import os
def  doesCircleExist(commands):
    """  https://gist.github.com/rainiera/d4fcff8fe1e12d6117998b6d0e9f05ee   """

    def doesCircleExists(commands):
        results = []
        for command in commands:
            robot = Robot()
            for c in command:
                if c == 'L':
                    robot.l()
                if c == 'R':
                    robot.r()
                if c == 'G':
                    robot.g()
            if robot.dir == Dir.N and robot.x ** 2 + robot.y ** 2 > 0:
                results.append("NO")
            else:
                results.append("YES")
        return results

    class Dir:
        N = 0
        S = 1
        W = 2
        E = 3

    class Robot:

        def __init__(self):
            self.ldict = {Dir.N: Dir.W,
                          Dir.S: Dir.E,
                          Dir.W: Dir.S,
                          Dir.E: Dir.N}
            self.rdict = {Dir.N: Dir.E,
                          Dir.S: Dir.W,
                          Dir.W: Dir.N,
                          Dir.E: Dir.S}
            self.dir = Dir.N
            self.x = 0
            self.y = 0

        def l(self):
            self.dir = self.ldict[self.dir]

        def r(self):
            self.dir = self.rdict[self.dir]

        def g(self):
            if self.dir == Dir.N:
                self.y += 1
            if self.dir == Dir.S:
                self.y -= 1
            if self.dir == Dir.W:
                self.x -= 1
            if self.dir == Dir.E:
                self.x += 1

    ### end of my code ###

    f = open(os.environ['OUTPUT_PATH'], 'w')

    _commands_cnt = 0
    _commands_cnt = int(raw_input())
    _commands_i = 0
    _commands = []
    while _commands_i < _commands_cnt:
        _commands_item = raw_input()
        _commands.append(_commands_item)
        _commands_i += 1

    res = doesCircleExists(_commands);
    for res_cur in res:
        f.write(str(res_cur) + "\n")

    f.close()

