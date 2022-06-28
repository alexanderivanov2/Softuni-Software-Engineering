class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        return f"{game} is not in library"

    def buy_game(self, game):
        if game in self.games:
            return f"{game} is already in your library"
        self.games.append(game)
        return f"{self.username} bought {game}"

    def stats(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.stats())

import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        user = SteamUser("Me", ["CSGO", "Like A Dragon"])
        self.assertEqual(user.username, "Me")
        self.assertEqual(user.games, ["CSGO", "Like A Dragon"])
        self.assertEqual(user.played_hours, 0)

    def test_play_successful(self):
        user = SteamUser("Me", ["CSGO", "Like A Dragon"])
        res = user.play("CSGO", 3)
        self.assertEqual(res, "Me is playing CSGO")
        self.assertEqual(user.played_hours, 3)

    def test_play_unsuccessful(self):
        user = SteamUser("Me", ["CSGO", "Like A Dragon"])
        res = user.play("Overwatch", 2)
        self.assertEqual(res, "Overwatch is not in library")
        self.assertEqual(user.played_hours, 0)

    def test_add_game_successful(self):
        user = SteamUser("Me", ["CSGO", "Like A Dragon"])
        res = user.buy_game("Risk of Rain 2")
        self.assertEqual(res, "Me bought Risk of Rain 2")
        self.assertEqual(user.games, ["CSGO", "Like A Dragon", "Risk of Rain 2"])

    def test_add_game_unsuccessful(self):
        user = SteamUser("Me", ["CSGO", "Like A Dragon"])
        res = user.buy_game("CSGO")
        self.assertEqual(res, "CSGO is already in your library")
        self.assertEqual(user.games, ["CSGO", "Like A Dragon"])

    def test_stats(self):
        user = SteamUser("Me", ["CSGO", "Like A Dragon"])
        res = user.stats()
        self.assertEqual(res, "Me has 2 games. Total play time: 0")


if __name__ == "__main__":
    unittest.main()