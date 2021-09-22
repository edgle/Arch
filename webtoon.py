from mangas import Mangas

class Webtoon(Mangas):
    def __init__(self) -> None:
        super().__init__()

    def ler_scroll(self):
        print("Você esta lendo de cima pra baixo")