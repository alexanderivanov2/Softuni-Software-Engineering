class NextVersion:
    def __init__(self, version):
        self.version = version

    def get_next_version(self):
        n1, n2, n3 = self.version.split('.')
        n3 = int(n3)
        n2 = int(n2)
        n1 = int(n1)
        if n3 + 1 == 10 and n2 + 1 == 10:
            n1 += 1
            n2 = 0
            n3 = 0
            return f"{n1}.{n2}.{n3}"
        elif n3 + 1 == 10 and n2 + 1 != 10:
            n2 += 1
            n3 = 0
            return f"{n1}.{n2}.{n3}"
        n3 += 1
        return f"{n1}.{n2}.{n3}"


version = NextVersion(input())
print(version.get_next_version())
