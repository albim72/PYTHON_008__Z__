from abc import ABC, abstractmethod


class Film(ABC):
    def __init__(self, title: str, director: str, year: int, duration: int):
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration
        self.create_film()

    def create_film(self):
        print(f"utworzono nowy obiekt oparty na klasie {self.__class__.__name__}")

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def get_info(self) -> str:
        pass


class AwardWinning:
    def __init__(self):
        self.awards = []

    def add_award(self, award: str):
        self.awards.append(award)

    def get_awards(self) -> list:
        return self.awards


class SeriesPart:
    def __init__(self, series_name: str, part_number: int):
        self.series_name = series_name
        self.part_number = part_number

    def get_series_info(self) -> str:
        return f"Seria: {self.series_name}, Część: {self.part_number}"


class ActionFilm(Film, AwardWinning):
    def __init__(self, title: str, director: str, year: int, duration: int):
        Film.__init__(self, title, director, year, duration)
        AwardWinning.__init__(self)

    def play(self):
        print(f"Odtwarzanie filmu akcji: {self.title}")

    def get_info(self) -> str:
        info = f"{self.title} (reż. {self.director}, {self.year}) - {self.duration} min"
        if self.awards:
            info += f" | Nagrody: {', '.join(self.awards)}"
        return info


class ComedyFilm(Film, SeriesPart):
    def __init__(self, title: str, director: str, year: int, duration: int, series_name: str, part_number: int):
        Film.__init__(self, title, director, year, duration)
        SeriesPart.__init__(self, series_name, part_number)

    def play(self):
        print(f"Odtwarzanie komedii: {self.title}")

    def get_info(self) -> str:
        info = f"{self.title} (reż. {self.director}, {self.year}) - {self.duration} min"
        series_info = self.get_series_info()
        info += f" | {series_info}"
        return info


class DocumentaryFilm(Film):
    def play(self):
        print(f"Odtwarzanie filmu dokumentalnego: {self.title}")

    def get_info(self) -> str:
        return f"{self.title} (reż. {self.director}, {self.year}) - {self.duration} min"


class FilmCollection:
    def __init__(self):
        self.films = []

    def add_film(self, film: Film):
        self.films.append(film)

    def remove_film(self, film: Film):
        self.films.remove(film)

    def display_all_films(self):
        for film in self.films:
            print(film.get_info())



# film = Film("Gwiezdne Wojny","George Lucas",1979,125)
# Przykładowe użycie
collection = FilmCollection()
film1 = ActionFilm("Mad Max: Fury Road", "George Miller", 2015, 120)
film2 = ComedyFilm("The Grand Budapest Hotel", "Wes Anderson", 2014, 99, "Wes Anderson's Universe", 1)
film3 = DocumentaryFilm("The Social Dilemma", "Jeff Orlowski", 2020, 94)

film1.add_award("Oscar za najlepszy montaż")
film1.add_award("Oscar za najlepszy dźwięk")

collection.add_film(film1)
collection.add_film(film2)
collection.add_film(film3)

collection.display_all_films()

# Odtwarzanie filmu
film1.play()
film2.play()
