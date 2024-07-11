from PIL import Image
import numpy as np

def image_to_ascii(image_path, width=50):
    # Carregar a imagem
    image = Image.open(image_path)
    
    # Redimensionar a imagem, mantendo a proporção
    aspect_ratio = image.height / image.width
    height = int(aspect_ratio * width * 0.55)
    image = image.resize((width, height))
    
    # Converter a imagem para escala de cinza
    image = image.convert('L')
    
    # Mapear pixels para caracteres ASCII
    pixels = np.array(image)
    chars = np.array([' ', '.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', '@'])
    ascii_image = chars[(pixels / 255 * (chars.size - 1)).astype(int)]
    
    # Montar a string do ASCII art
    ascii_str = "\n".join("".join(row) for row in ascii_image)
    
    return ascii_str

if __name__ == "__main__":
    image_path = "./assets/foto.jpeg"
    ascii_art = image_to_ascii(image_path)
    print(ascii_art)
