import requests, os, urllib.request, re


def mlb_menu():
    while True:
        print("-- Funcoes com MLB --")
        print("--------------------")
        print("[0] Menu inicial")
        print("[1] ID das variacoes de um MLB")
        print("[2] Baixar imagens de um MLB")
        option = int(input("R: "))
        os.system('cls')
        if option == 0:
            break
        elif option == 1:
            get_variations_infos()
        elif option == 2:
            get_images()


def get_variations_infos():
    print("Exemplo: MLB123456789 | Ou 0 para voltar")
    while True:
        mlb = input("MLB: ")
        
        if mlb == "0":
            os.system('cls')
            break
        
        res = requests.get(f"https://api.mercadolibre.com/items/{mlb}")
        res = res.json()

        if res.get("variations"):
            print(f"[v] ID das variaçoes")
            print()
            for product in res.get('variations') or []:
                mlb_id = product['id']
                try:
                    name = product['attribute_combinations'][0]['name']
                    value = product['attribute_combinations'][0]['value_name']
                    name2 = product['attribute_combinations'][1]['name']
                    value2 = product['attribute_combinations'][1]['value_name']
                    print(f"[>] {mlb}|{mlb_id}|{name}:{value};{name2}:{value2}")

                except IndexError:
                    name = product['attribute_combinations'][0]['name']
                    value = product['attribute_combinations'][0]['value_name']
                    print(f"[>] {mlb}|{mlb_id}|{name}:{value}")

        else:
            print(f"[+] Produto simples")
            
            
def create_folder(folder_name):
    os.mkdir(folder_name)    
        

def download_images(url, folder_path):
    picture_id = url.split("/")[-1].split("-")[0]
    image_path = os.path.join(folder_path, f"{picture_id}.jpg")
    urllib.request.urlretrieve(url, image_path)


def get_images():
    while True:
        print("Exemplo: MLB123456789 | Ou 0 para voltar")
        mlb = input("MLB: ")
        
        if mlb == "0":
            os.system('cls')
            break
        
        url = f"https://api.mercadolibre.com/items/{mlb}"

        response = requests.get(url)
        response_data = response.json()
        variations = response_data.get("variations", [])
        pictures = response_data.get("pictures", [])

        if variations:
            for variation in variations:
                variation_name_parts = [
                    f"{attribute['name']}-{attribute['value_name']}"
                    for attribute in variation.get("attribute_combinations", [])
                ]
                variation_name = "-".join(variation_name_parts)
                variation_name = re.sub(r'[^a-zA-Z-]', '', variation_name)
                folder_name = f"result/{mlb}-{variation_name}-{variation['id']}"
                create_folder(folder_name)

                for picture_id in variation.get("picture_ids", []):
                    url = f"https://http2.mlstatic.com/D_{picture_id}-F.jpg"
                    download_images(url, folder_name)

        elif pictures:
            folder_name = f"result/{mlb}"
            create_folder(folder_name)

            for picture in pictures:
                url = f"https://http2.mlstatic.com/D_{picture['id']}-F.jpg"
                download_images(url, folder_name)
