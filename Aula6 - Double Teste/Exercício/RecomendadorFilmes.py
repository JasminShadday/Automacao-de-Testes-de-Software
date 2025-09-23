# --- Código principal ---
class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class ServicoRecomendacao:
    def recomendar(self, usuario, genero):
        raise NotImplementedError("Não deve chamar API real durante teste!")


class RecomendadorFilmes:
    def __init__(self, servico):
        self.servico = servico

    def recomendar_para_usuario(self, usuario, genero):
        return self.servico.recomendar(usuario, genero)


# --- Double 1: Dummy ---
class UsuarioDummy:
    """Um Dummy é usado apenas como objeto de preenchimento"""
    def __init__(self):
        self.nome = "Dummy"
        self.idade = 0


# --- Double 2: Mock ---
class ServicoRecomendacaoMock:
    """Mock registra chamadas feitas durante o teste"""
    def __init__(self):
        self.chamadas = []

    def recomendar(self, usuario, genero):
        self.chamadas.append((usuario, genero))
        return ["Filme de Teste"]

    def foi_chamado_com(self, genero):
        return any(g == genero for _, g in self.chamadas)


# --- Execução dos testes ---
def testar_dummy():
    print("===== Teste com Dummy =====")
    servico_mock = ServicoRecomendacaoMock()
    recomendador = RecomendadorFilmes(servico_mock)

    usuario_dummy = UsuarioDummy()  # Não importa os dados desse objeto
    resultado = recomendador.recomendar_para_usuario(usuario_dummy, "ação")

    print("Recomendação recebida:", resultado)  # Esperado: ["Filme de Teste"]


def testar_mock():
    print("\n===== Teste com Mock =====")
    servico_mock = ServicoRecomendacaoMock()
    recomendador = RecomendadorFilmes(servico_mock)

    usuario_dummy = UsuarioDummy()
    recomendador.recomendar_para_usuario(usuario_dummy, "ficção")

    print("Foi chamado com 'ficção'? ->", servico_mock.foi_chamado_com("ficção"))
    print("Foi chamado com 'ação'? ->", servico_mock.foi_chamado_com("ação"))


# --- Rodar testes ---
if __name__ == "__main__":
    testar_dummy()
    testar_mock()
