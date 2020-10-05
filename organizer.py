import os, shutil
from datetime import datetime


# função para pegar datas do arquivo
def get_file_date(file):
    date = datetime.fromtimestamp(os.path.getmtime(file))
    return date

# formatando datas
def file_date_format(file):
    date = get_file_date(file)
    return date.strftime('%d-%m-%Y') 

# pega extensões dos arquivos
def get_extension(file):
    file_name, ext = os.path.splitext(file)
    return ext

# nomeia a pasta conforme a extensao
def name_dir(file):
    ext = get_extension(file)
    directory = '.'

    if ext == '.pdf':
        directory = 'PDFs/'+file_date_format(file)
    
    elif ext == '.png' or ext == '.jpg' or ext == '.jpeg' or ext == '.gif':
        directory = 'Imagens/'+file_date_format(file)
    
    elif ext == '.zip':
        directory = 'Zip/'+file_date_format(file)
    
    elif ext == '.exe':
        directory = 'Instaladores/'+file_date_format(file)
    
    elif ext == '.doc' or ext == '.docx':
        directory = 'Documentos/'+file_date_format(file)
    
    elif ext == '.mp3' or ext == '.wav':
        directory = 'Músicas/'+file_date_format(file)

    elif ext == '.py':
        directory = 'Python Files/'+file_date_format(file)
    
    elif ext == '.mp4' or ext == '.mov' or ext == 'wmv':
        directory = 'Vídeos/'+file_date_format(file)

    return directory   

# move o arquivo
def move_photo(file):
    folder = name_dir(file)

    if not os.path.exists(folder):
        os.makedirs(folder)
    
    shutil.move(file, folder + '/' + file)

# organiza todos os arquivos do diretório atual
def organizer():
    files = os.listdir('.')

    for filename in files:
        move_photo(filename)

