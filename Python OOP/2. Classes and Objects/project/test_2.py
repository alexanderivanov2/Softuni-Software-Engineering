from project.library import Library
from project.user import User

user = User(12, 'Valentina')
library = Library()
library.add_user(user)
library.add_user(User(13, 'Peter'))
print(library.user_records[0].__str__())