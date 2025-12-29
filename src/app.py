# Importando biblioteca para criar servidor web local
from http.server import HTTPServer, SimpleHTTPRequestHandler
# Importando biblioteca para manipular caminhos de arquivos
import os
# Importando biblioteca para trabalhar com JSON (formato de dados)
import json
# Importando biblioteca para manipular datas
from datetime import datetime

# Classe para gerenciar requisições HTTP do servidor
class CustomHandler(SimpleHTTPRequestHandler):
    # Método que processa requisições GET (carregamento de páginas)
    def do_GET(self):
        # Verificando se a requisição é para a página principal
        if self.path == '/' or self.path == '/index.html':
            # Definindo o caminho do arquivo HTML principal
            self.path = '/index.html'
        # Chamando o método da classe pai para processar a requisição
        return super().do_GET()
    
    # Método para desabilitar logs automáticos do servidor
    def log_message(self, format, *args):
        # Retornando vazio para não exibir logs no console
        return

# Função para carregar notícias do arquivo JSON
def carregar_noticias():
    # Verificando se o arquivo de notícias existe
    if os.path.exists('noticias.json'):
        # Abrindo o arquivo JSON em modo leitura
        with open('noticias.json', 'r', encoding='utf-8') as f:
            # Carregando e retornando os dados do arquivo JSON
            return json.load(f)
    # Retornando lista vazia se o arquivo não existir
    return []

# Função para salvar notícias no arquivo JSON
def salvar_noticias(noticias):
    # Abrindo o arquivo JSON em modo escrita
    with open('noticias.json', 'w', encoding='utf-8') as f:
        # Salvando as notícias no arquivo com formatação indentada
        json.dump(noticias, f, ensure_ascii=False, indent=2)

# Função para adicionar uma nova notícia ao blog
def adicionar_noticia(titulo, conteudo, autor="TECNOFANJOS"):
    # Carregando notícias existentes
    noticias = carregar_noticias()
    # Criando um dicionário com os dados da nova notícia
    nova_noticia = {
        # ID único baseado no número de notícias existentes
        "id": len(noticias) + 1,
        # Título da notícia
        "titulo": titulo,
        # Conteúdo da notícia
        "conteudo": conteudo,
        # Autor da notícia (padrão: TECNOFANJOS)
        "autor": autor,
        # Data e hora atual da criação
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        # Contador de cliques inicializado em zero
        "cliques": 0
    }
    # Adicionando a nova notícia à lista
    noticias.append(nova_noticia)
    # Salvando todas as notícias no arquivo
    salvar_noticias(noticias)
    # Retornando mensagem de sucesso
    return f"Notícia '{titulo}' adicionada com sucesso!"

# Função para incrementar contador de cliques de uma notícia
def incrementar_cliques(noticia_id):
    # Carregando todas as notícias
    noticias = carregar_noticias()
    # Procurando a notícia pelo ID
    for noticia in noticias:
        # Verificando se o ID corresponde
        if noticia["id"] == noticia_id:
            # Incrementando o contador de cliques
            noticia["cliques"] += 1
            # Salvando as alterações
            salvar_noticias(noticias)
            # Retornando True indicando sucesso
            return True
    # Retornando False se a notícia não foi encontrada
    return False

# Função para obter as notícias mais clicadas
def obter_noticias_mais_clicadas(limite=5):
    # Carregando todas as notícias
    noticias = carregar_noticias()
    # Ordenando as notícias por número de cliques (maior para menor)
    noticias_ordenadas = sorted(noticias, key=lambda x: x["cliques"], reverse=True)
    # Retornando apenas as primeiras N notícias (padrão: 5)
    return noticias_ordenadas[:limite]

# Função principal para iniciar o servidor web
def iniciar_servidor():
    # Definindo a porta do servidor (8080)
    porta = 8080
    # Criando instância do servidor HTTP
    servidor = HTTPServer(('localhost', porta), CustomHandler)
    # Exibindo mensagem informando que o servidor está rodando
    print(f"Servidor iniciado em http://localhost:{porta}")
    print("Pressione Ctrl+C para parar o servidor")
    # Iniciando o servidor e mantendo-o em execução
    servidor.serve_forever()

# Verificando se o script está sendo executado diretamente (não importado)
if __name__ == "__main__":
    # Iniciando o servidor web
    iniciar_servidor()

