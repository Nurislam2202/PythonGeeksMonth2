class Books:

    prise=350

    def __init__(self, title, author):
        self.title=title
        self.author=author

    def __str__(self):
        return f'{self.title} \nавтор:{self.author}\n'

    def prise_book(self):
        ...


# дочерний класс
class Manga(Books):

    prise = 600

    def __init__(self, title, author,image='default.jpg'):
        Books.__init__(self,title,author)
        super().__init__(title,author)
        self.image=image

    def reverse(self):
        print('читай с права на лево')

    def __str__(self):
        return f'{super().__str__()}\n{self.image}\nцена:{self.prise}'


# DRY
class Anime(Manga):
    def __init__(self, title, author,drive_image):
        Books.__init__(self,title, author)
        self.drive_image=drive_image

    def prise_book(self):
        print('120 за серию')

    def __len__(self):
        return self.prise

    def __str__(self):
        return f"\nprint(anime)\n{Books.__str__(self)}drive image = {self.drive_image}"


class Remanga:
    def __init(self, manga):
        self.manga = manga

    def manga_upp(self):
        print(self.manga, "улучшена рисовка")


# class Newmanga(Books, Manga, Remanga):    # Будет ошибка
class Newmanga(Manga, Remanga):
    pass
# MRO - порядок выполнения методов
mymanga = Newmanga("ванпис", "ода", "image+320")
print(Newmanga.mro())
