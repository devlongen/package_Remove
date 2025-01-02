from rembg import remove
import time
from PIL import Image
import psutil
from flask import Flask, request, jsonify

"""
# Validação da memória inicial
print(f"Uso inicial da CPU: {psutil.cpu_percent(interval=0.1)}%")
print(f"Uso inicial da memória: {psutil.virtual_memory().percent}%")
start = time.time()
"""
app = Flask(__name__)

@app.route('/remove_imageBG', methods=['POST'])
def remove_imageBG():
    try:
        # Verifica se um arquivo foi enviado
        if 'image' not in request.files:
            return jsonify({"error": "Nenhum arquivo enviado. Envie um arquivo de imagem com o campo 'image'."}), 400
        
        # Obtém o arquivo enviado
        file = request.files['image']
        
        # Verifica se o arquivo é válido
        if file.filename == '':
            return jsonify({"error": "Nenhum arquivo selecionado."}), 400
        
        # Processa a imagem
        input_image = Image.open(file).convert("RGB")
        output_image = remove(input_image)
        
        # Salva a imagem processada
        output_path = 'output.png'
        output_image.save(output_path)
        
        # Retorna a resposta ao cliente
        return jsonify({"message": "Background removido com sucesso!", "output_path": output_path}), 200
    
    except Exception as e:
        return jsonify({"error": f"Erro no processamento da imagem: {str(e)}"}), 500
"""
end = time.time()
"""
if __name__ == '__main__':
    app.run(debug=True)


"""
# Validação da memória e do tempo de duração do programa
print(f"Tempo total: {end - start:,.2f} segundos\n")
print("=====================")
mem_info = psutil.virtual_memory()._asdict()
print("\nInformações da memória RAM:")
for key, value in mem_info.items():
    if key in ["total", "available", "used", "free"]:
        print(f"{key.capitalize()}: {value / (1024**3):,.2f} GB")
    else:
        print(f"{key.capitalize()}: {value} %")
print("\nUso médio da CPU durante a execução: ", psutil.cpu_percent(interval=1), "%")

"""
