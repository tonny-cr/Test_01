import matplotlib.pyplot as plt


class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return (f" Titulo: {self.titulo}\n"
                f" Autor: {self.autor}\n"
                f" Gênero: {self.genero}\n"
                f" Quantidade: {self.quantidade}\n")


# Lista para armazenar os livros
livros = []


def cadastrar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    genero = input("Gênero do livro: ")

    livro = {"titulo": titulo, "autor": autor, "genero": genero}
    livros.append(livro)
    print(f"Livro '{titulo}' cadastrado com sucesso!\n")


def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.\n")
        return

    print("📚 Lista de Livros:")
    for i, livro in enumerate(livros, start=1):
        print(f"{i}. {livro['titulo']} - {livro['autor']} ({livro['genero']})")
    print()


def buscar_por_titulo():
    titulo = input("Digite o título do livro que deseja buscar: ")
    encontrados = [livro for livro in livros if titulo.lower()
                   in livro["titulo"].lower()]

    if encontrados:
        print("🔎 Livros encontrados:")
        for livro in encontrados:
            print(f"{livro['titulo']} - {livro['autor']} ({livro['genero']})")
    else:
        print("Nenhum livro encontrado com esse título.\n")


def grafico_por_genero():
    if not livros:
        print("Nenhum livro cadastrado para gerar gráfico.\n")
        return

    generos = {}
    for livro in livros:
        genero = livro["genero"]
        generos[genero] = generos.get(genero, 0) + 1

    plt.bar(generos.keys(), generos.values())
    plt.title("Quantidade de Livros por Gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade")
    plt.show()


def menu():
    while True:
        print("=== Sistema de Biblioteca ===")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Buscar livro por título")
        print("4 - Gerar gráfico por gênero")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_por_titulo()
        elif opcao == "4":
            grafico_por_genero()
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida!\n")


# Executa o sistema
menu()
