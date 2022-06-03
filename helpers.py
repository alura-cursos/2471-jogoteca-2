import os
from jogoteca import app

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}.jpg' == nome_arquivo:
            return nome_arquivo

    return 'capa_padrao.jpg'