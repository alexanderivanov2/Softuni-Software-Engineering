class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type):
        decorations = [x for x in self.decorations if x.DECORATION_TYPE == decoration_type]
        if decorations:
            return decorations[0]
        return "None"
