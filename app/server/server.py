import socket

def tcp_server(callback):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Server started")
    s.bind(("localhost", 30001))
    print("Server binded")
    while True:
      s.listen()
      conn, addr = s.accept()
      with conn:
        print("Connection established!")
        while True:
          data = conn.recv(1024)
          if not data:
            break
          callback(data)
      conn.close()
