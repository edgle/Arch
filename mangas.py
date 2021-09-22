from comics import Comics

class Mangas(Comics):
    def __init__(self) -> None:
        super().__init__()

    def ler_contrario(self):
        print("Você esta lendo de tras pra frente")