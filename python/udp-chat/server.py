import socket


def main():
    host = "0.0.0.0"
    port = 9999

    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.bind((host, port))

    print(f"Listening on {host}:{port}...")
    while True:
        try:
            data = s.recvfrom(1024)
            s.sendto(data[0], data[1])

        except KeyboardInterrupt:
            print("\nDisconnected.")
            s.close()
            return


if __name__ == "__main__":
    main()
