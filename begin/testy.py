import unittest
from World import World
from Position import Position
from Organisms.Sheep import Sheep
from Organisms.rys import Rys
from Organisms.antylopa import Antylopa

class TestWorld(unittest.TestCase):
    def setUp(self):
        self.world = World(10, 10)

    def test_plague_mode(self):
        for i in range(3):
            self.world.addOrganism(Sheep(position=Position(i, 0), world=self.world))
            self.world.addOrganism(Antylopa(position=Position(i, 1), world=self.world))
            self.world.addOrganism(Rys(position=Position(i, 2), world=self.world))
        
        self.world.togglePlagueMode()
        self.world.makeTurn()

        for organism in self.world._World__organisms:
            self.assertEqual(organism.liveLength, organism.initialLiveLength // 2)

    def test_plague_turns(self):
        for i in range(3):
            self.world.addOrganism(Sheep(position=Position(i, 0), world=self.world))
            self.world.addOrganism(Antylopa(position=Position(i, 1), world=self.world))
            self.world.addOrganism(Rys(position=Position(i, 2), world=self.world))

        self.world.togglePlagueMode()
        self.world.makeTurn()
        self.assertTrue(self.world._World__plague_mode)

        self.world.makeTurn()
        self.assertTrue(self.world._World__plague_mode)

        self.world.makeTurn()
        self.assertFalse(self.world._World__plague_mode)

    def test_conservation_rules(self):
        for i in range(15):
            self.world.addOrganism(Sheep(position=self.world.find_free_position(), world=self.world))

        self.world.makeTurn()

        sheep_count = sum(1 for o in self.world._World__organisms if isinstance(o, Sheep))
        self.assertEqual(sheep_count, 10)

    def test_add_organism(self):
        self.world.makeTurn()
        new_sheep = Sheep(position=Position(0, 0), world=self.world)
        self.world.addOrganism(new_sheep)
        self.assertIn(new_sheep, self.world._World__organisms)

    def test_turn_progression(self):
        initial_turn = self.world._World__turn
        self.world.makeTurn()
        self.assertEqual(self.world._World__turn, initial_turn + 1)

if __name__ == '__main__':
    unittest.main()
