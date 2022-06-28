class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = {}

    def assign_player(self, player):
        if player.name in self.list_of_players:
            return f"Player {player.name} is already in the guild."
        elif not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.list_of_players[player.name] = player
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player):
        if player not in self.list_of_players:
            return f"Player {player} is not in the guild."

        self.list_of_players[player].guild = "Unaffiliated"
        self.list_of_players.pop(player)
        return f"Player {player} has been removed from the guild."

    def guild_info(self):
        guild_information = f"Guild: {self.name}\n"
        if self.list_of_players:
            player_info = "".join(f"{el.player_info()}" for el in self.list_of_players.values())
            return guild_information + player_info
        else:
            return guild_information
