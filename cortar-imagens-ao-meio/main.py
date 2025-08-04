import os
from PIL import Image

input_folder = "pre-recortadas"
output_folder = "pos-recortadas"

# Cria a pasta de saída se não existir
os.makedirs(output_folder, exist_ok=True)

# Extensões válidas para imagem
valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.webp']

# Percorre todos os arquivos da pasta
for filename in os.listdir(input_folder):
    name, ext = os.path.splitext(filename)

    if ext.lower() in valid_extensions:
        # Caminho completo da imagem
        img_path = os.path.join(input_folder, filename)

        # Abre a imagem
        img = Image.open(img_path)
        width, height = img.size

        # Define as duas metades (esquerda e direita)
        esquerda_crop = img.crop((0, 0, width // 2, height))
        direita_crop = img.crop((width // 2, 0, width, height))

        # Caminhos de saída
        esquerda_path = os.path.join(output_folder, f"{name}_esquerda.jpg")
        direita_path = os.path.join(output_folder, f"{name}_direita.jpg")

        # Salva as imagens recortadas
        esquerda_crop.save(esquerda_path, format="JPEG")
        direita_crop.save(direita_path, format="JPEG")

        print(f"Salvo: {esquerda_path}, {direita_path}")