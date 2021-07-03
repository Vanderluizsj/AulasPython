import socket
import json

def main():
    print("Starting UDP client...")
    dest_ip = "127.0.0.1"
    dest_port = 50000
    comando = 'get'
    valor = "off"
    local = ["luz_sala_reuniões", "luz_guarita", "ar_guarita", "luz_estacionamento"]
    #-----------------------------------------------------------------
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        msg = str(input("Type a message: "))
        dados_json= json.dumps(msg)
        print("\tSending message to {}:{:d} with payload: {}".format(dest_ip, dest_port, dados_json))
        sock.sendto(bytes(dados_json, 'utf-8'), (dest_ip, dest_port))





        if msg.lower() == "<exit>":
            print("\tClosing...")
            sock.close()
            break

if __name__ == "__main__":
    main()
