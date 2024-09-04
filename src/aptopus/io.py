"""IO stands for Input / Output, it exports a class is used to create
an instance to manage the `input` and `output` of program as well as
history of `input`.

### Input
First, we'll talk about `input`: input is a data that the program can
consume or use for other processes, input can come from:
  - User prompts to program (*).
  - User presses keys that are binded and used in prompt (*).
  - A response from AI.
  - A text, string from a File.
  - A reuslt of a function.

An input can have a `context`, because some inputs ins't cleared,
so the program (or AI) can ask user to gain more understanding
of the input.

### Output
The output of program isn't only printed in Terminal console, but also
they are can be:
  - Writed to a file(s) (logging, ledger, ...).
  - Inserted to a collection(s) / table(s) of a database(s).
  - Writed to memory for other use cases (contextual conversation, auto-completion, ...).
"""
import os
import sys

# Import from prompt_toolkit
from prompt_toolkit import prompt, print_formatted_text as print
from prompt_toolkit.styles import Style
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.shortcuts import clear

class AptopusIO:
  def __init__(self, args_parser) -> None:
    self.args_parser = args_parser
    self.style = Style.from_dict({})
    pass

  def output(self, output=None):
    try:
      print(output)
    except:
      # There is an error
      print()

  def get_input(self, message="Enter your question: "):
    kb = KeyBindings()

    content = prompt(message, key_bindings=kb)
    return content
  
  def clear_screan(self):
    clear()