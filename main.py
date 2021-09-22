# Princípio da Substituição de Liskov

from mangas import Mangas
from quadrinhos import Quadrinhos
from webtoon import Webtoon

naruto = Quadrinhos()
manga = Mangas()
naruto.ler(manga)
