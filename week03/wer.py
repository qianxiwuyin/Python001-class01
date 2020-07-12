import socket
import threading

#创建对象

class Client():
  def send_info(self,PORT):
        try:
          s.connect(('192.168.0.35',PORT))  #要连接的IP与端口
          s.settimeout(1)
          s.sendall('hi good')
          print("连接成功")
        except Exception as e:
          print("服务器连接失败",e)

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = Client()
    for i in range(1,5):
      PORT=i+100
      t = threading.Thread(target=client.send_info,args=(PORT,))
      t.start()
      t.join()
    s.close()













