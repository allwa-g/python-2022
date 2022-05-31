# -*- coding: utf-8 -*-

# Podrobný popis je dostupný na: https://github.com/ianmagyar/introduction-to-python/blob/master/assignments/homeworks/homework9.md


from math import sqrt
import random
import matplotlib.pyplot as plt


class Location:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def move(self, dx, dy):
        return Location(self.x + float(dx), self.y + float(dy))

    def getCoords(self):
        return self.x, self.y

    def getDistance(self, other):
        o_x, o_y = other.getCoords()
        xDist = self.x - o_x
        yDist = self.y - o_y
        return sqrt(xDist ** 2 + yDist ** 2)


class Direction:
    possibles = ['N', 'E', 'S', 'W']

    def __init__(self, direction):
        if direction in self.possibles:
            self.direction = direction
        else:
            raise ValueError(
                "Unknown direction {} in Direction.__init__".format(direction))

    def move(self, dist):
        if self.direction == 'N':
            return (0, dist)
        elif self.direction == 'E':
            return (dist, 0)
        elif self.direction == 'S':
            return (0, -dist)
        elif self.direction == 'W':
            return (-dist, 0)
        else:
            raise ValueError("Unexpected direction in Direction.move")


class Field:
    def __init__(self, drunk, loc):
        self.drunk = drunk
        self.loc = loc

    def move(self, direction, dist):
        oldLoc = self.loc
        dx, dy = direction.move(dist)
        self.loc = oldLoc.move(dx, dy)

    def getLoc(self):
        return self.loc

    def getDrunk(self):
        return self.drunk


class Drunk:
    def __init__(self, name):
        self.name = name

    def move(self, field, direction, steps=1):
        if field.getDrunk() != self:
            raise ValueError(
                "Drunk.move called when drunk was not added to a field")
        for i in range(steps):
            field.move(direction, 1)


class UsualDrunk(Drunk):
    def move(self, field, steps=1):
        direction = Direction(random.choice(Direction.possibles))
        Drunk.move(self, field, direction, steps)


class BiasedDrunk(Drunk):
    def move(self, field, steps=1):
        # https://github.com/ianmagyar/introduction-to-python/blob/master/assignments/homeworks/homework9.md
        # the drunk should move with probabilities:
        # N - 15%, E - 15%, S - 10%, W - 60%
        # step size to west should be 2

        sides = ['N', 'N', 'N', 'E', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
        direction = Direction(random.choice(sides))
        # Drunk.move(self, field, direction, steps)
        if (direction == 'W'):
            Drunk.move(self, field, direction, 2 * steps)
        else:
            Drunk.move(self, field, direction, steps)


class UnsureDrunk(Drunk):
    def move(self, field, steps=1):
        # https://github.com/ianmagyar/introduction-to-python/blob/master/assignments/homeworks/homework9.md
        # the drunk should not make the same step twice in row

        sides = ['W', 'S', 'N', 'E']
        direction = Direction(random.choice(sides))
        if (direction == 'W'):
            sides = ['S', 'S', 'E', 'E', 'E', 'N', 'N', 'N']
            direction = Direction(random.choice(sides))
            Drunk.move(self, field, direction, steps)
        elif (direction == 'S'):
            sides = ['N', 'N', 'N', 'E', 'E', 'E', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
            direction = Direction(random.choice(sides))
            Drunk.move(self, field, direction, steps)
        elif (direction == 'E'):
            sides = ['N', 'N', 'N', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
            direction = Direction(random.choice(sides))
            Drunk.move(self, field, direction, steps)
        elif (direction == 'N'):
            sides = ['E', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
            direction = Direction(random.choice(sides))
            Drunk.move(self, field, direction, steps * 2)


def performTrial(steps, field):
    start = field.getLoc()
    distances = [0.0]
    for t in range(1, steps + 1):
        field.getDrunk().move(field)
        newLoc = field.getLoc()
        distance = newLoc.getDistance(start)
        distances.append(distance)
    return distances, newLoc.getCoords()


def performSim(steps, numTrials, drunkType):
    distLists = []
    endPoints = []
    for trial in range(numTrials):
        d = drunkType("Drunk" + str(trial))
        f = Field(d, Location(0, 0))
        distances, endPoint = performTrial(steps, f)
        distLists.append(distances)
        endPoints.append(endPoint)
    return distLists, endPoints


def ansQuest(steps, numTrials):
    plt.figure()

    drunkType = UsualDrunk
    means = []
    distLists, endPoints = performSim(steps, numTrials, drunkType)
    for t in range(steps + 1):
        total = 0.0
        for distL in distLists:
            total += distL[t]
        means.append(total / len(distLists))
    # plt.legend(['Usual drunk'])
    plt.plot(means, label='Usual drunk')

    drunkType = BiasedDrunk
    means = []
    distLists, endPoints = performSim(steps, numTrials, drunkType)
    for t in range(steps + 1):
        total = 0.0
        for distL in distLists:
            total += distL[t]
        means.append(total / len(distLists))
    # plt.legend(['Biased drunk'])
    plt.plot(means, label='Biased drunk')

    drunkType = UnsureDrunk
    means = []
    distLists, endPoints = performSim(steps, numTrials, drunkType)
    for t in range(steps + 1):
        total = 0.0
        for distL in distLists:
            total += distL[t]
        means.append(total / len(distLists))
    # plt.legend(['Unsure drunk'])
    plt.plot(means, label='Unsure drunk')

    plt.ylabel('distance')
    plt.xlabel('time')
    plt.title('Average distance vs. Time')

    plt.legend()


ansQuest(500, 300)
plt.show()
