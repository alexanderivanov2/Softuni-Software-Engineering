import json


class School:
    def __init__(self, name, students):
        self.students = students
        self.name = name

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def from_string(cls, school_string):
        index = school_string.index(":")
        name = school_string[:index]
        students = school_string[index + 1:].split(", ")
        return cls(name, students)

    @classmethod
    def from_json(cls, school_json):
        attrs = json.loads(school_json)
        return cls(attrs['name'], attrs['students'])

print(School("Softuni", ['Sofi', 'Mari', 'Gosho']))
the_input = 'students: Sofi, Mari, Gosho'
print(School.from_string(the_input))
print(School.from_json('''
{
    "name": "Softuni",
    "students": [
    "Sofi",
    "Marta",
    "Gosho"
    ]
}    
'''))
