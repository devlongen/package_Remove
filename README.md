Ficha Técnica:

  Python -v : Python 3.11.0rc2
  Bibliotecas: rembg,onnxruntime,psutil,time e flask

Arquivo "newMachine.py" será uma ferramenta para fazer instalação de forma automática sobre as bibliotecas que é necessário para o programa rodar, apenas executar o .py.

Arquivo "removeBg.py" é um removedor de fundo via API, apenas executar ele e realizar uma requisição via POST para API, a api irá rodar localmente, não está instalando em nenhum VPS/ServerHost.
OBS: O input é recomendavél utilizar JPEG (outros tipos pode ocorrer instabilidade), ele irá converter para RGB para melhor leitura da máquina e após isto remover irá converter em PNG.
