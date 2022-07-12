class Trainer:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.id
        Trainer.id += 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @classmethod
    def get_next_id(cls):
        return Trainer.id