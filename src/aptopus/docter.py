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

class AptopusDocter:
  def __init__(self, io) -> None:
    self.io = io
    pass

  def handle_input(self, input):
    self.io.output(f"Your input: {input}")

  def run(self):
    while True:
      try:
        # Get input from user
        input = self.io.get_input()

        # Handle input from user
        self.handle_input(input)
        self.io.output()
        
      except KeyboardInterrupt:
        # Do something if user presses ctrl-c
        self.io.output("Exit")
        raise SystemExit