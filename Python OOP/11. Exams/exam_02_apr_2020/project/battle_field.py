from project.player.beginner import Beginner


class BattleField:
    # def fight(self, attacker, enemy):
    #     if attacker.is_dead or enemy.is_dead:
    #         raise ValueError("Player is dead!")
    #     if isinstance(attacker, Beginner):
    #         attacker.health += 40
    #         for card in attacker.card_repository:
    #             card.damage_points += 30
    #     if isinstance(enemy, Beginner):
    #         enemy.health += 40
    #         for card in enemy.card_repository:
    #             card.damage_points += 30
    #     add_health_attacker = 0
    #     add_health_enemy = 0
    #     for card in attacker.card_repository:
    #         add_health_attacker += card.health_points
    #     for card in enemy.card_repository:
    #         add_health_enemy += card.health_points
    #     attacker.health += add_health_attacker
    #     enemy.health += add_health_enemy
    #     for card in attacker.card_repository.cards:
    #         enemy.take_damage(card.damage_points)
    #     for card in enemy.card_repository.cards:
    #         attacker.take_damage(card.damage_points)
    def fight(self, attacker, enemy):
        self.validate_player_alive(attacker)
        self.validate_player_alive(enemy)
        self.check_for_beginner(attacker)
        self.check_for_beginner(enemy)
        self.get_bonus(attacker)
        self.get_bonus(enemy)
        self.attack(attacker, enemy)
        self.attack(enemy, attacker)

    @staticmethod
    def validate_player_alive(player):
        if player.is_dead:
            raise ValueError("Player is dead!")

    def check_for_beginner(self, player):
        if not isinstance(player, Beginner):
            return
        self.increase_health(player)
        self.increase_cards_damage(player)

    @staticmethod
    def increase_health(player):
        player.health += 40

    @staticmethod
    def increase_cards_damage(player):
        for card in player.card_repository.cards:
            card.damage_points += 30

    @staticmethod
    def get_bonus(player):
        player.health += sum([card.health_points for card in player.card_repository.cards])

    @staticmethod
    def attack(att, en):
        for card in att.card_repository.cards:
            en.take_damage(card.damage_points)

