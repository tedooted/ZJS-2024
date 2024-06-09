from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.antylopa import Antylopa
from Organisms.rys import Rys
import os

def add_new_organism(world):
    organism_map = {
        'G': Grass,
        'S': Sheep,
        'R': Rys,
        'A': Antylopa
    }
    print("Wybierz ktory organism chciałbys dodac (G - Grass, S - Sheep, R - Rys, A - Antylopa): ")
    org_type = input().upper()
    if org_type in organism_map:
        print("Podaj pozycje gdzie chciałbyc wstawic organizm (x, y): ")
        x, y = map(int, input().split())
        position = Position(xPosition=x, yPosition=y)
        if world.is_position_free(position):
            new_org = organism_map[org_type](position=position, world=world)
            world.addOrganism(new_org)
        else:
            print("W tym miejscu jest już organizm.")
    else:
        print("Podaj poprawna literke.")

if __name__ == '__main__':
    pyWorld = World(10, 10)

    newOrg = Grass(position=Position(xPosition=9, yPosition=9), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Grass(position=Position(xPosition=1, yPosition=1), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Sheep(position=Position(xPosition=2, yPosition=2), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Antylopa(position=Position(xPosition=3, yPosition=4), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Rys(position=Position(xPosition=4, yPosition=5), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    print(pyWorld)
    for _ in range(50):
        command = input('Nacisnij Enter aby przejsc dalej albo napisz Plaga aby uruchomić trybplagi albo napisz Dodaj aby dodac organizm: ')
        if command.lower() == 'plaga':
            pyWorld.activate_plague_mode()
        elif command.lower() == 'dodaj':
            add_new_organism(pyWorld)
        os.system('cls')
        pyWorld.makeTurn()
        print(pyWorld)
