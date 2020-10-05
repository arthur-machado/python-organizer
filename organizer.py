import os, shutil
from datetime import datetime

class PythonOrganizer():

# função para pegar datas do arquivo
    def get_file_date(self, file):
        date = datetime.fromtimestamp(os.path.getmtime(file))
        return date

    # formatando datas
    def file_date_format(self, file):
        date = self.get_file_date(file)
        return date.strftime('%d-%m-%Y') 

    # pega extensões dos arquivos
    def get_extension(self, file):
        file_name, ext = os.path.splitext(file)
        return ext

    # nomeia a pasta conforme a extensao
    def name_dir(self, file):
        ext = self.get_extension(file)
        directory = '.'

        if ext == '.pdf':
            directory = 'PDFs/'+ self.file_date_format(file)
        
        elif ext == '.png' or ext == '.jpg' or ext == '.jpeg' or ext == '.gif':
            directory = 'Imagens/'+ self.file_date_format(file)
        
        elif ext == '.zip':
            directory = 'Zip/'+ self.file_date_format(file)
        
        elif ext == '.exe':
            directory = 'Instaladores/'+ self.file_date_format(file)
        
        elif ext == '.doc' or ext == '.docx':
            directory = 'Documentos/'+ self.file_date_format(file)
        
        elif ext == '.mp3' or ext == '.wav':
            directory = 'Músicas/'+ self.file_date_format(file)

        elif ext == '.py':
            directory = 'Python Files/'+ self.file_date_format(file)
        
        elif ext == '.mp4' or ext == '.mov' or ext == 'wmv':
            directory = 'Vídeos/'+ self.file_date_format(file)

        return directory   

    # move o arquivo
    def move_photo(self, file):
        folder = self.name_dir(file)

        if not os.path.exists(folder):
            os.makedirs(folder)
        
        shutil.move(file, folder + '/' + file)

    # organiza todos os arquivos do diretório atual
    def organizer(self):
        files = os.listdir('.')

        for filename in files:
            self.move_photo(filename)


ORG = PythonOrganizer()
ORG.organizer()