import pygame 
import random

# Inicializa o pygame
pygame.init()

# Definir constantes
LARGURA_TELA = 500
ALTURA_TELA = 500
TAMANHO_CELULA = 40
LINHAS = COLUNAS = 10
FONTE = pygame.font.SysFont('Arial', 24)

# Cores
COR_FUNDO = (255, 255, 255)
COR_TEXTOS = (0, 0, 0)
COR_CELULAS = (200, 200, 255)
COR_SELECIONADA = (255, 255, 0)

# Função para gerar equações e seus resultados
def gerar_equacoes():
    equacoes = [
        ("5 + 3", 5 + 3),
        ("10 - 4", 10 - 4),
        ("6 * 2", 6 * 2),
        ("9 / 3", 9 / 3),
        ("7 + 2", 7 + 2),
        ("12 - 5", 12 - 5),
        ("8 * 3", 8 * 3),
        ("16 / 4", 16 / 4)
    ]
    random.shuffle(equacoes)  # Embaralha para dar variedade nas equações
    return equacoes

# Função para gerar o grid de caça-palavras
def gerar_caca_palavras(results):
    size = 10  # Tamanho do grid
    grid = [[' ' for _ in range(size)] for _ in range(size)]  # Cria um grid vazio

    for result in results:
        num_str = str(result)
        placed = False

        while not placed:
            direction = random.choice(['horizontal', 'vertical'])  # Direção para colocar o número
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)

            if direction == 'horizontal' and col + len(num_str) <= size:
                # Verifica se a palavra cabe horizontalmente
                if all(grid[row][col + i] == ' ' for i in range(len(num_str))):
                    for i in range(len(num_str)):
                        grid[row][col + i] = num_str[i]
                    placed = True
            elif direction == 'vertical' and row + len(num_str) <= size:
                # Verifica se a palavra cabe verticalmente
                if all(grid[row + i][col] == ' ' for i in range(len(num_str))):
                    for i in range(len(num_str)):
                        grid[row + i][col] = num_str[i]
                    placed = True

    # Preenche as lacunas com números aleatórios
    for row in range(size):
        for col in range(size):
            if grid[row][col] == ' ':
                grid[row][col] = str(random.randint(1, 9))  # Preenche com números aleatórios entre 1 e 9

    return grid

# Função para desenhar o grid e os textos
def desenhar_tela(tela, grid, selecionado):
    tela.fill(COR_FUNDO)

    # Desenha o grid
    for row in range(LINHAS):
        for col in range(COLUNAS):
            rect = pygame.Rect(col * TAMANHO_CELULA, row * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
            cor_celula = COR_CELULAS if (row, col) != selecionado else COR_SELECIONADA
            pygame.draw.rect(tela, cor_celula, rect)

            # Desenha o número na célula
            texto = FONTE.render(grid[row][col], True, COR_TEXTOS)
            tela.blit(texto, (col * TAMANHO_CELULA + 10, row * TAMANHO_CELULA + 10))

    pygame.display.update()

# Função principal
def main():
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Caça-Palavras - Resultados das Equações")
    
    # Gerar equações e seus resultados
    equacoes = gerar_equacoes()
    
    # Imprimir as equações no console
    print("Equações:")
    for eq, res in equacoes:
        print(f"{eq} = {res}")

    # Gerar o grid de caça-palavras com os resultados
    results = [res for _, res in equacoes]
    grid = gerar_caca_palavras(results)

    selecionado = None  # Nenhuma célula selecionada inicialmente

    # Loop principal do jogo
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Detecta a célula clicada
                x, y = evento.pos
                col = x // TAMANHO_CELULA
                row = y // TAMANHO_CELULA
                selecionado = (row, col)

                # Verifica se o jogador clicou na célula correta
                if selecionado:
                    valor_celula = grid[row][col]
                    print(f"Célula selecionada: {valor_celula}")

        # Desenhar o grid
        desenhar_tela(tela, grid, selecionado)

    pygame.quit()

if __name__ == "__main__":
    main()
