import socket
import sys


def main():
    # Tenta efetuar uma conexão tcp
    try:
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou !")
        print("Erro: {}".format(e))
        sys.exit()

    print("Socket criado com sucesso !")


    # definir o host a ser conectado
    Host = input("Digite o Host ou Ip a ser conectado: ")
    Port = input("Digite a porta a set conectada: ")

    try:
        con.connect((Host, int(Port)))
        print("Cliente TCP conectado com sucesso no host: " + Host + " e na porta: " + Port )
        con.shutdown(2)
    except socket.error as e:
        print("A conexão com o host: " + Host + " na porta: "+ Port +" falhou ")
        print("Error: {}".format(e))
        sys.exit()    



if __name__ == '__main__':
    main()
