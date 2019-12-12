import socket
import threading
import sys
import pickle


class Client():
    """docstring for Client"""

    def __init__(self, host="localhost", port=4000):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect(host, port)
        self.username = None

    def connect(self, host, port):
        try:
            self.sock.connect((str(host), int(port)))
            msg_recv = threading.Thread(target=self.msg_recv)
            msg_recv.daemon = True
            msg_recv.start()

        except:
            if KeyboardInterrupt:
                print("\n ** connection not established **")
            else:
                print("Connection not established")

    def closeCon(self):
        print("Closing client")
        self.sock.close()
        sys.exit()

    def getUsername(self):
        return self.username

    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    message = pickle.loads(data).split(",")
                    if (message[0] == "closeCon"):
                        print("There cannot be more clients connected to server")
                        self.sock.close()
                    elif (message[0] == "allowCon"):
                        self.username = message[1]
                        print("Connected! Welcome username: ", self.username)
                    else:
                        print(pickle.loads(data))
            except:
                pass

    def send_msg(self, msg):
        try:
            self.sock.send(pickle.dumps(msg))
        except:
            print("Could not send message. Retry again.")
