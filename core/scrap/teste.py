import requests

# Configurar o endereço do proxy
proxy = {
    'http': 'http://162.214.165.203:80',
    # 'https': 'https://seu_proxy_aqui'
}

# URL do site que você deseja acessar
url = 'http://icanhazip.com/'

# Fazer a requisição HTTP usando o proxy
try:
    response = requests.get(url, proxies=proxy)

    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        print("Conexão bem-sucedida:")
        print(response.text)
    else:
        print(f"Falha na conexão. Código de status: {response.status_code}")
except Exception as e:
    print(f"Erro ao se conectar ao site: {str(e)}")
