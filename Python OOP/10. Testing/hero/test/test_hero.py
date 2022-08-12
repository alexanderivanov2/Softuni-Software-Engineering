import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("A", 1, 10, 10)
        self.enemy = Hero("B", 1, 5, 5)

    def test_construct(self):
        self.assertEqual(1, self.hero.level)
        self.assertTrue(isinstance(self.hero.level, int))
        self.assertEqual("A", self.hero.username)
        self.assertEqual(10, self.hero.health)
        self.assertTrue(isinstance(self.hero.health, int))
        self.assertEqual(10, self.hero.damage)
        self.assertTrue(isinstance(self.hero.damage, int))

    def test_battle_you_against_you(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_is_zero_or_less(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as val_er:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(val_er.exception))

    def test_enemy_hero_health_is_zero_or_less(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as val_er:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(val_er.exception))

    def test_battle_draw(self):
        enemy = Hero("B", 1, 10, 10)
        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)

    def test_battle_won(self):
        self.hero.damage = 100
        result = self.hero.battle(self.enemy)
        self.assertEqual(result, "You win")
        self.assertEqual(2, self.hero.level)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual(10, self.hero.health)

    def test_battle_lost(self):
        self.enemy.damage = 100
        self.enemy.health = 100
        result = self.hero.battle(self.enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(105, self.enemy.damage)
        self.assertEqual(95, self.enemy.health)
        self.assertEqual(2, self.enemy.level)

    def test_str(self):
        result = f"Hero A: 1 lvl\nHealth: 10\nDamage: 10\n"
        self.assertEqual(result, self.hero.__str__())


if __name__ == "__main__":
    unittest.main()
