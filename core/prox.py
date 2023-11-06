## Teste proxy

import json
import requests



def ler_json():
    # with open('prox/list_proxies.json', 'r') as fl:
    with open('list_proxies.json', 'r') as fl:
        proxie_list = json.loads(fl.read())


    # for i in proxie_list:
    #     if i['IP adress'] != '':
    #         print(i['IP adress'])
    
    
    # for i in proxie_list:
    #     d = {k:v for k, v in i if i['IP adress'] != ''}

    # return [
    #     {k:v for k, v in i if i['IP adress'] != ''} for i in proxie_list
    # ]

    return proxie_list


# print(ler_json())



# Configurar o endereço do proxy
# proxy = {
#     # 'http': 'http://162.214.165.203:80',
#     'http': 'http://35.236.207.242:33333'
#     # 'https': 'https://seu_proxy_aqui'
# }


def reqq(url):

    pp = ler_json()

    for proxy in pp:

        try:
            # p = f"{proxy['Type']}://{proxy['IP adress']}:{proxy['Port']}"
            # p = {proxy['Type']: f"{proxy['Type']}://{proxy['IP adress']}:{proxy['Port']}"}
            p = {'https': f"{proxy['Type']}s://{proxy['IP adress']}:{proxy['Port']}"}
            response = requests.get(url, proxies=p, timeout=(5,5))
                
            if response.status_code == 200:
                return response
            else:
                print(f"Erro na solicitação HTTP para {url} usando o proxy {p}. Status code: {response.status_code}")

        except Exception as e:
            print(f"Erro ao acessar {url} usando o proxy {p}: {str(e)}")
            continue
    
    return None
        
        # print("Todos os proxies falharam. Não foi possível acessar a página.")
        # return None


if __name__ == '__main__': 

    url = 'https://icanhazip.com/'

    
    
    res = reqq(url)
    if res:
        print(res.text)


# # URL do site que você deseja acessar
# url = 'http://icanhazip.com/'

# # Fazer a requisição HTTP usando o proxy
# try:
#     response = requests.get(url, proxies=proxy,timeout=(15,15))

#     # Verificar se a solicitação foi bem-sucedida
#     if response.status_code == 200:
#         print("Conexão bem-sucedida:")
#         print(response.text)
#     else:
#         print(f"Falha na conexão. Código de status: {response.status_code}")
# except Exception as e:
#     print(f"Erro ao se conectar ao site: {str(e)}")











###########################################
###########################################
###########################################

# Crawler

import json
import requests
from bs4 import BeautifulSoup



# URL do site que você deseja acessar
url = 'https://www.freeproxy.world/?speed=144'
url_s = 'https://www.freeproxy.world/?type=https'

l_url = ['https://www.freeproxy.world/?speed=144', 'https://www.freeproxy.world/?type=https']


def save_js(data):
    print('aqui')
    
    with open('list_proxies.json', 'w+') as fl:
        json.dump(data, fl, indent="\t")


def reqq(url):
    return requests.get(url)



def get_proxies():

    # Fazer a requisição HTTP usando o proxy
    try:
        # response = requests.get(url)
        data = []
        for item in l_url:
            response = requests.get(item)

            # Verificar se a solicitação foi bem-sucedida
            if response.status_code == 200:
                print("Conexão bem-sucedida:")
                # print(response.text)

                soup = BeautifulSoup(response.text, 'html.parser')

                print(soup.title)
                # print(soup.table)
                # print(soup.find_all('table'))

                table = soup.table
                headers = [header.text for header in table.find_all('th')]


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
            
                # Agora, 'data' contém os dados da tabela em forma de lista de dicionários
                # for row in data:
                #     print(row)
            
            save_js(data)


        else:
            print(f"Falha na conexão. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Erro ao se conectar ao site: {str(e)}")
    

    
if __name__ == '__main__':

    get_proxies()


