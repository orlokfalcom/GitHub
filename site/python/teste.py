from PIL import Image, ImageDraw

# Criando uma imagem em branco com fundo branco
img = Image.new('RGB', (200, 200), color=(255, 255, 255))

# Inicializando o objeto de desenho
d = ImageDraw.Draw(img)

# Desenhando um simples galo (representado por formas geométricas)
# Corpo do galo
d.ellipse([50, 80, 150, 180], fill=(255, 0, 0), outline=(0, 0, 0))  # Corpo vermelho
# Cabeça do galo
d.ellipse([120, 50, 170, 100], fill=(255, 0, 0), outline=(0, 0, 0))  # Cabeça vermelha
# Bico do galo
d.polygon([(170, 75), (190, 70), (170, 65)], fill=(255, 165, 0))  # Bico amarelo
# Crista do galo
d.polygon([(140, 50), (130, 30), (120, 50), (110, 30)], fill=(255, 0, 0))  # Crista vermelha
# Cauda do galo
d.polygon([(50, 150), (10, 140), (30, 180), (50, 180)], fill=(255, 0, 0))  # Cauda vermelha
# Pés do galo
d.line([90, 180, 90, 190], fill=(255, 165, 0), width=3)  # Pé esquerdo
d.line([110, 180, 110, 190], fill=(255, 165, 0), width=3)  # Pé direito

# Exibindo a imagem
img.show()
