"""Aptopus (Client) will communicate with Aptopus Server
through WebSocket Protocol. Program will use this class to
create and instance of socket to handle the base of listener
and emitter of socket.
"""

import socket
import json

class SocketClient:
  def __init__(self) -> None:
    self.host = "ws://127.0.0.0/ws/12345"
    self.port = "8080"
    self._instance = socket.socket()
    self._listener = {}
    pass

  def send(self, data, data_transformer=None):
    """Send a message (string) to server.

    Args:
        data (Any): A message data object
    """
    try:
      if data_transformer != None:
        self._instance.send(json.dumps(data_transformer(data)))
      self._instance.send(json.dumps(data))
    except:
      print("Fail to send message to SocketServer")

  def receive(self, size=1024, data_transformer=None):
    """If program is running in a infinite loop, it use this
    method to receive message from server.

    Returns:
        Any: Depend on the type of response data.
    """
    date_str = self._instance.recv(size).decode()
    data = json.loads(date_str)

    if data_transformer != None:
      data = data_transformer(data)

    return data

  def listen():
    """If the program isn't running in a infinite loop, it will
    listen the message from server and handle these message with
    named listener.

    Before you use this method, you should add listener to the list.
    """
    while True:
      print()

  def add_listener(self, name, fn):
    def _(data):
      fn(data)

    self._listener[name] = _
  
  def remove_listener(self, name):
    self._listener.pop(name)

  def connect(self):
    self._instance.connect((self.host, self.port))

  def disconnect(self):
    self._instance.close()