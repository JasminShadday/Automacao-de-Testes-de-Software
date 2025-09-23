from abc import ABCMeta, abstractmethod
from src.livro import Livro

class LivroRepositorio(metaclass=ABCMeta):
   def inserir(self, livro: Livro):
       pass 
   def buscar_todos(self) -> list:
       pass
   def obter_tamanho(self) -> int:
       pass
   


