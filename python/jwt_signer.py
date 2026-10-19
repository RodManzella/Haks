# separar e decodificar o token JWT
import time
import jwt
import base64
import json
import cryptography
from colorama import Fore, Back, Style, init

init(autoreset=True)
escape_while = False

symmetric_allowed_digital_signature_algorithms = ['HS256','HS286', 'HS512']



def main():
    jwt_token = input("Coloque o JWT aqui: ")
    print("=======================\n\n")
    header_bytes, payload_bytes = split_jwt(jwt_token)

    header_object, payload_object = get_jwt_py_objects(header_bytes, payload_bytes)
    print_jwt_structure(header_object, payload_object)

    print(Style.BRIGHT+Fore.YELLOW+"Altere itens do payload (aperte 0 para sair)\n")

   
    do_jwt_payload_modification_loop(payload_object, escape_while)
      

    token = create_symmetric_signed_jwt_token(payload_object, "123", "HS256")

    print(token)



def create_symmetric_signed_jwt_token(payload, secret="", algorithms=['HS256','HS286', 'HS512']):
     token = jwt.encode(payload, secret, algorithms)
     return token
     
def do_jwt_payload_modification_loop(payload, will_escape_loop=False):
    while will_escape_loop == False:
        print("Valor atual")
        print_jwt_payload_structure(payload)
        jwt_value = ""
        jwt_field = input("Digite o campo jwt que quer alterar: \n")
        
        if (jwt_field in payload.keys()):
            jwt_value = input(f"Digite o novo valor de {jwt_field}: ")
            payload[jwt_field] = jwt_value
        
            escape_input = input("Aperte 0 para sair, qualquer outro para continuar\n\n")
        
            if escape_input == "0":
                will_escape_loop = True
    
        return will_escape_loop
    return
    


def split_jwt(token):
    split_token = token.split('.')
    header_bytes = base64.b64decode(split_token[0] + '==')
    payload_bytes = base64.b64decode(split_token[1] + '==')

    return header_bytes, payload_bytes

def get_jwt_py_objects(header, payload):
    header_decoded = header.decode('utf-8')
    header_object = json.loads(header_decoded)
        
    payload_decoded = payload.decode('utf-8')
    payload_object = json.loads(payload_decoded)

    return header_object, payload_object

def print_jwt_structure(header_object, payload_object):
    print(Style.BRIGHT+Fore.YELLOW+f"Estrutura do JWT:")
    print(Style.BRIGHT+Fore.WHITE+f"Header:")
    print(Style.BRIGHT+Fore.YELLOW+f"{header_object} \n")
    print(Style.BRIGHT+Fore.WHITE+f"Payload:")
    print(Style.BRIGHT+Fore.YELLOW+f"{payload_object} \n\n\n")
    return


def print_jwt_payload_structure(payload_object):
        print(Style.BRIGHT+Fore.WHITE+f"Payload:")
        print(Style.BRIGHT+Fore.YELLOW+f"{payload_object} \n")




if __name__ == "__main__":
    main()