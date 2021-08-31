import random


class Panthera:

    """
    a hybrid panthera with a random gender
    """

    def __init__(self, male, female, generation):
        self.male = male
        self.female = female
        self.generation = generation

    def cross(self, panthera):
        p1 = random.choice([self.male, self.female])
        if p1 == self.male:
            p2 = panthera.female 
        else:
            p2 = panthera.male
        return F"{p1} + {p2} ="

    def __lt__(self, panthera):
        return self.generation < panthera.generation

    def __repr__(self):
        return self.male


class Tiger(Panthera):
    pass

class Lion(Panthera):
    pass

class Leopard(Panthera):
    pass

class Jaguar(Panthera):
    pass

class Tigon(Panthera):
    pass

class Jagupard(Panthera):
    pass

class Jaglion(Panthera):
    pass

class Jagger(Panthera):
    pass

class Lipard(Panthera):
    pass

class Tigard(Panthera):
    pass


tiger = Tiger("Tiger", "Tigress", 1)
lion = Lion("Lion", "Lioness", 1)
leopard = Leopard("Leopard", "Leopardess", 1)
jaguar = Jaguar("Jaguar", "Jaguaress", 1)
tigon = Tigon("Tigon", "Tigoness", 2)
jagupard = Jagupard("Jagupard", "Jagupardess", 2)
tigard = Tigard("Tigard", "Tigardess", 2)
lipard = Lipard("Lipard", "Lipardess", 2)
jagger = Jagger("Jagger", "Jaggress", 2)
jaglion = Jaglion("Jaglion", "Jaglioness", 2)

panthera_list = [tiger, jaglion, lion, leopard, jaguar, tigon, jagupard, tigard, lipard, jagger]


a1 = eval(input("p1: ")) #input panthera
a2 = eval(input("p2: "))

if (a1 == tiger and a2 == lion) or (a2 == tiger and a1 == lion):
    hybrid = random.choice([tigon.male, tigon.female])
elif (a1 == leopard and a2 == jaguar) or (a2 == leopard and a1 == jaguar):
    hybrid = random.choice([jagupard.male, jagupard.female])
elif (a1 == leopard and a2 == leopard):
    hybrid = random.choice([leopard.male, leopard.female])
elif (a1 == jaguar and a2 == jaguar):
    hybrid = random.choice([jaguar.male, jaguar.female])
elif (a1 == tiger and a2 == tiger):
    hybrid = random.choice([tiger.male, tiger.female])
elif (a1 == lion and a2 == lion):
    hybrid = random.choice([lion.male, lion.female])
elif (a1 == leopard and a2 == tiger) or (a2 == leopard and a1 == tiger):
    hybrid = random.choice([tigard.male, tigard.female])
elif (a1 == leopard and a2 == lion) or (a2 == leopard and a1 == lion):
    hybrid = random.choice([lipard.male, lipard.female])
elif (a1 == jaguar and a2 == tiger) or (a2 == jaguar and a1 == tiger):
    hybrid = random.choice([jagger.male, jagger.female])
elif (a1 == jaguar and a2 == lion) or (a2 == jaguar and a1 == lion):
    hybrid = random.choice([jaglion.male, jaglion.female])
else:
    hybrid = "none"


parents = a1.cross(a2) #cross function, random parent gender


print(parents, hybrid)
panthera_list.sort()
print(panthera_list)