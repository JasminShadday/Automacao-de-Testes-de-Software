import pytest 
from tests.LivroRepositorioMock import LivroRepositorioMock 
from tests.LivroRepositorioMock import ExcecaoLivroNaoEncontrado
from src.livro import Livro

def test_busca_livro_por_id():
    #Preparação
    livroRepositorio = LivroRepositorioMock()
    #acão
    livro = livroRepositorio.obter_livro('111')
    #verificação
    assert livro.id == '111'
    assert livro.titulo == 'Python para iniciantes'
    assert livroRepositorio.numero_de_chamadas() == 1
