import socket
from datetime import datetime


def main():
    host = "127.0.0.1"
    port = 9999
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    while True:
        try:
            message = input(f"{host}: ")
            msg_bytes = message.encode()

            s.sendto(msg_bytes, (host, port))
            data = s.recvfrom(1024)

            sender_address = data[1][0]
            received_msg = data[0].decode("utf-8")

            print(
                f"{datetime.now().strftime("%d %B %Y %H:%M:%S")} {sender_address}: {received_msg}"
            )

        except KeyboardInterrupt:
            print("\nDisconnected.")
            s.close()
            return


if __name__ == "__main__":
    main()
