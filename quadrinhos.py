import abc
from typing import Type
from comics import Comics
from mangas import Mangas

class Quadrinhos(Comics):
    def ler(self, comic: Type[Mangas]):
        comic.ler()
