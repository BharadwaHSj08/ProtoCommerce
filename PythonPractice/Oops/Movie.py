class Movie:

    def __init__(self,title,hero,heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print(f"Movie name is {self.title}, Hero is {self.hero}, Heroine is {self.heroine}")

list_of_movies = []

while True:
    title = input("Enter Movie name:")
    hero = input("Enter Hero name:")
    heroine = input("Enter Heroine name:")

    m = Movie(title,hero,heroine)
    list_of_movies.append(m)

    option = input("Do you want to add New Movie? Yes/No:")
    if option.lower() == 'no':
        break

for movie in list_of_movies:
    movie.info()
    print()
