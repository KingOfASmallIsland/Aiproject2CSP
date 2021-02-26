from typing import Generic, TypeVar

arg1 = TypeVar("arg1")
arg2 = TypeVar("arg2")


class MapColoringConstraint(Generic[arg1, arg2]):
    def __init__(self, place1, place2):
        self.vertices = vertices
        self.place1 = place1
        self.place2 = place2

    def ifassigned(self, assigned):
        if self.place1 not in assigned or self.place2 not in assigned:
            return True
        if assigned[self.place1] != assigned[self.place2]:
            return True
        return False


class Constraint(Generic[arg1, arg2]):
    def __init__(self, vertices):
        self.vertices = vertices

    def ifassigned(self, assigned):
        pass


class CSP(Generic[arg1, arg2]):
    def __init__(self, vertices, colors):
        self.vertices = vertices
        self.colors = colors
        self.constraints = {}
        for k in self.vertices:
            self.constraints[k] = []

    def constraint(self, constraint):
        for variable in constraint.vertices:
            if variable in self.vertices:
                self.constraints[variable].append(constraint)

    def ac3(self, uncolored, colored):
        for constraint in self.constraints[uncolored]:
            if not constraint.ifassigned(colored):
                return False
        return True

    def recursivesearch(self, assigned={}):
        if len(self.vertices) - len(assigned) == 0:
            return assigned

        unassigned = []
        for k in self.vertices:
            if k not in assigned:
                unassigned.append(k)

        for coloring in self.colors[unassigned[0]]:
            assigned2 = assigned.copy()
            assigned2[unassigned[0]] = coloring
            if self.ac3(unassigned[0], assigned2):
                result = self.recursivesearch(assigned2)
                if result is not False:
                    return result
        return False


for j in range(1, 6):
    print("result for", j, "txt file")
    f = open(str.__add__(str(j), ".txt"))
    inputdatalist = []
    vertices = []
    for data in f.readlines():
        data = data.strip("\n")
        data2 = data.split(',')

        if data2[0].__contains__('#'):
            continue
        if data2[0].__contains__('colors'):
            data3 = data.split(' ')
            color = data3[2]
            continue
        if int(data2[0]) not in vertices:
            vertices.append(int(data2[0]))
        if int(data2[1]) not in vertices:
            vertices.append(int(data2[1]))
        inputdatalist.append(data2)

    colors = []
    for i in range(0, int(color)):
        colors.append(i)
    colors2 = {}
    for i in range(len(vertices) + 1):
        colors2[i] = colors
    csp = CSP(vertices, colors2)
    for i in range(len(inputdatalist)):
        csp.constraint(MapColoringConstraint(int(inputdatalist[i][0]), int(inputdatalist[i][1])))

    print(csp.recursivesearch())