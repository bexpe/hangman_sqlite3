import unittest
from player_class import Player


class PlayerTest(unittest.TestCase):
    def setUp(self):
        name = "Beata"
        score = 20
        lives = 2
        self.player = Player(
            score=score,
            name=name,
            lives=lives)

    def test_is_name_correct(self):
        expected_name = "Beata"
        msg = "Name is not set correctly"
        self.assertEqual(expected_name, self.player.get_name(), msg)

    def test_is_score_correct(self):
        expected_score = 20
        msg = "Score is not set correctly"
        self.assertEqual(expected_score, self.player.get_score(), msg)

    def test_is_arg_lives_correct(self):
        expected_lives = 2
        msg = "Lives are not set correctly"
        self.assertEqual(expected_lives, self.player.get_lives(), msg)


if __name__ == '__main__':
    unittest.main()
