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

# Import from local
from .ai import AptopusAIInteractor
from .socket_client import SocketClient
from .io import AptopusIO

class AptopusDocter:
  def __init__(self, io: AptopusIO) -> None:
    self.io = io

    # Create SocketClient instance
    self.socket = SocketClient()
    self.socket.connect()

    # Create AptopusAIClient
    self.ai_interactor = AptopusAIInteractor(self.socket)

    self.user_indicator_output = self.io.attach_font_style("You > ", style="bold", is_html_result=True)
    self.bot_indicator_output = self.io.paint_text(self.io.attach_font_style("Aptopus >", style="bold"), text_color="green")
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
        input = self.io.get_input(self.user_indicator_output, placeholder="Enter your question here")
        self.io.output(self.bot_indicator_output, is_inline=True)
        self.io.output("Please wait, answer is be generated...", is_markdown=False, is_inline=True)
        
        # Handle input from user
        message = self.handle_input(input)

        # Print message
        self.io.output(message, is_markdown=True, is_inline=True)
        self.io.output()
        
      except KeyboardInterrupt:
        # Do something if user presses ctrl-c
        self.io.output("Exit")
        raise SystemExit
      
      except Exception as e:
        print(f"There is an error: {e}")
        raise SystemExit