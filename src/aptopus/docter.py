"""AptopusDocter is a composer of Aptopus Core. Program will create an instance
from AptopusDocter to mamage and use all of modules in program to give Users
good experience.

Program's modules are:
  - Input / Output module.
  - AI (Interactor) module.
  - Functions module.
  - Utils module.
"""
import os
import sys

#
from .ai import AptopusAIInteractor
from .socket_client import SocketClient

class AptopusDocter:
  def __init__(self, io) -> None:
    self.io = io

    # Create SocketClient instance
    self.socket = SocketClient()
    self.socket.connect()

    # Create AptopusAIClient
    self.ai_interactor = AptopusAIInteractor(self.socket)
    pass

  def handle_input(self, input):
    data = {
      "type": "receive_question",
      "data": input
    }

    self.socket.send(data)

    # Wait for response from server
    data = self.socket.receive()
    
    if data["type"] == "answer_available":
      return self.ai_interactor.get_anwser()

  def run(self):
    while True:
      try:
        # Get input from user
        input = self.io.get_input("You > ")

        # Handle input from user
        message = self.handle_input(input)

        # Print message
        self.io.output(f"Aptopus > {message}")
        self.io.output()
        
      except KeyboardInterrupt:
        # Do something if user presses ctrl-c
        self.io.output("Exit")
        raise SystemExit
      
      except Exception as e:
        print(f"There is an error: {e}")