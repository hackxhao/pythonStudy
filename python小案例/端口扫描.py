import socket
import threading


def get_ip_status(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((ip, port))
        print('{0} port {1} is open'.format(ip, port))
    except Exception as err:
        print('{0} port {1} is not open'.format(ip, port))
    finally:
        server.close()


if __name__ == '__main__':
    host = '39.106.117.123'
    threads = []
    for port in range(20, 100):
        t = threading.Thread(target=get_ip_status, args=(host, port))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
