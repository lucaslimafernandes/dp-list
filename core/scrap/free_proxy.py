# https://proxyscrape.com/free-proxy-list
# url = 'https://www.freeproxy.world/?speed=144'


import requests
from bs4 import BeautifulSoup

def get_free_proxy():

    data = []
    try:

        url = "https://www.freeproxy.world/?speed=144"

        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"'
        }


        r = requests.get(url, headers=headers)

        if r.status_code != 200:
            raise Exception()
        
        print("Conexão bem-sucedida:")


        soup = BeautifulSoup(r.text, 'html.parser')

        table = soup.table
        headers = [header.text for header in table.find_all('th')]

        print(table)

        for row in table.find_all('tr')[1:]:
            # Extraia as células da linha
            cells = row.find_all('td')
            # Crie um dicionário com os dados da linha
            row_data = {}
            for i, cell in enumerate(cells):
                # Use os cabeçalhos como chaves do dicionário
                header = headers[i]
                # Armazene o texto da célula no dicionário
                row_data[header] = cell.text.strip()
            # Adicione o dicionário à lista de dados
            if len(row_data) > 0:
                data.append(row_data) 
    
    except Exception as e:
        print(f"Erro ao se conectar ao site: {str(e)}")

    
    # ip_address = models.CharField(max_length=39)
    # port = models.IntegerField()
    # protocol = models.CharField(max_length=20) 
    # country = models.CharField(max_length=30)
    # latency = models.CharField(max_length=10)
    # request = models.IntegerField()
    # status_ok = models.IntegerField()

    response_list = []
    for i in data:
        try:

            if i['IP adress'] == '0.0.0.0':
                raise Exception()
            if i['Port'] == '':
                raise Exception()

            response = {
                'ip_address': i['IP adress'] ,
                'port': i['Port'] ,
                'protocol': i['Type'] ,
                'country': i['Country'] ,
                'latency': i['Speed'] ,
            }
            response_list.append(response)
        except (KeyError, Exception):
            pass

    return response_list

# print(data)


# def get_proxies():

#     # Fazer a requisição HTTP usando o proxy
#     try:
#         # response = requests.get(url)
#         data = []
#         for item in url:
#             response = requests.get(item)

#             # Verificar se a solicitação foi bem-sucedida
#             if response.status_code == 200:
#                 print("Conexão bem-sucedida:")
#                 # print(response.text)

#                 soup = BeautifulSoup(response.text, 'html.parser')

#                 print(soup.title)
#                 # print(soup.table)
#                 # print(soup.find_all('table'))

#                 table = soup.table
#                 headers = [header.text for header in table.find_all('th')]


#                 for row in table.find_all('tr')[1:]:
#                     # Extraia as células da linha
#                     cells = row.find_all('td')
#                     # Crie um dicionário com os dados da linha
#                     row_data = {}
#                     for i, cell in enumerate(cells):
#                         # Use os cabeçalhos como chaves do dicionário
#                         header = headers[i]
#                         # Armazene o texto da célula no dicionário
#                         row_data[header] = cell.text.strip()
#                     # Adicione o dicionário à lista de dados
#                     if len(row_data) > 0:
#                         data.append(row_data) 
            
#                 # Agora, 'data' contém os dados da tabela em forma de lista de dicionários
#                 # for row in data:
#                 #     print(row)
            
#                 save_js(data)
    
#             else:
#                 print(f"Falha na conexão. Código de status: {response.status_code}")
#     except Exception as e:
#         print(f"Erro ao se conectar ao site: {str(e)}")


