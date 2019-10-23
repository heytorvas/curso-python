import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '<{}, {}>'.format(self.x, self.y)

class Reward(Point):

    def __init__(self, x, y, name):
        super(Reward, self).__init__(x, y)
        self.name = name
    
    def __str__(self):
        return '<{}, {}>: {}'.format(self.x, self.y, self.name)

    def __repr__(self):
        return 'Reward {}'.format(str(self))

def check_reward(robot, rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print('RECOMPENSA ENCONTRADA')
            ok = True
    return ok

class Robot(Point):
    
    def move_up(self):
        if self.y < 10:
            self.y += 1
        else:
            print('MOVIMENTO INVALIDO')
    
    def move_down(self):
        if self.y > 0:
            self.y -= 1
        else:
            print('MOVIMENTO INVALIDO')
    
    def move_left(self):
        if self.x > 0:
            self.x -= 1
        else:
            print('MOVIMENTO INVALIDO')
    
    def move_right(self):
        if self.x < 10:
            self.x += 1
        else:
            print('MOVIMENTO INVALIDO')

r1 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r2 = Reward(random.randint(0, 10), random.randint(0, 10), 'gasolina')
r3 = Reward(random.randint(0, 10), random.randint(0, 10), 'arma')
r4 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r5 = Reward(random.randint(0, 10), random.randint(0, 10), 'gasolina')
r6 = Reward(random.randint(0, 10), random.randint(0, 10), 'arma')
r7 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r8 = Reward(random.randint(0, 10), random.randint(0, 10), 'gasolina')
r9 = Reward(random.randint(0, 10), random.randint(0, 10), 'arma')
rewards = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

robot = Robot(random.randint(0, 10), random.randint(0, 10))

for i in range(10):
    moviment = input('DIGITE UP, DOWN LEFT OU RIGHT PARA O MOVIMENTO: ').lower().strip()
    if moviment == 'up':
        robot.move_up()
    elif moviment == 'down':
        robot.move_down()
    elif moviment == 'left':
        robot.move_left()
    elif moviment == 'right':
        robot.move_right()
    else:
        print('MOVIMENTO INVALIDO')
        continue
    
    print(robot)
    check_reward(robot, rewards)
    if check_reward(robot, rewards) == True:
        break


# reward1 = Reward(1, 2, 'moeda')
# reward2 = Reward(1, 2, 'moeda')
# robot = Robot(2, 2)
# rewards = [reward1, reward2]
# check_reward(robot, rewards)
# robot.move_left()
# check_reward(robot, rewards)

# HERANCA
# class Robot3D(Robot):
#     def __init__(self, x, y, z):
#         super(Robot3D, self).__init__(x, y)
#         self.z = z

# robot1 = Robot(5, 10)
# robot2 = Robot3D(5, 6, 8)
# print(robot1.x)
# print(robot2.z)