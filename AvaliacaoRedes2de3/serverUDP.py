import socket
import json

def main():
    print("Starting UDP server...")
    local_ip = "127.0.0.1"
    local_port=50000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((local_ip, local_port))
    while True:
        dados_json, client=sock.recvfrom(1024)
        msg = json.loads(dados_json)

        print("Mensage received from {}: {}".format(client, msg))
        if msg.lower() == "<exit>":
            print("\tClosing...")
            sock.close()
            break

if __name__ == "__main__":
        main()