#!/usr/bin/python3

class pets:
    def __init__(self, animal, likes):
        self.animal = animal
        self.likes = likes

mypets = [pets("Dog", "bone"), pets("cat", "catnip"), pets("rabbit", "carrots")]
print((mypets[1].animal), end="=> ")
print(mypets[1].likes)
