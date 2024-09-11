#!/usr/bin/env python
"""
Example of adding a custom key binding to a prompt.
"""

import asyncio

from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.key_binding import KeyBindings

def main():
  kb = KeyBindings()

  question = FormattedText([("Pink", "Will you marry me? [press y for 'yes' and n for 'no']: ")])

  @kb.add("y")
  def _(event):
    event.app.current_buffer.insert_text("yes")

  @kb.add("n")
  def _(event):
    event.app.current_buffer.insert_text("no")

  text = prompt(question, key_bindings=kb)
  print(f"You said {text}")

if __name__ == "__main__":
  main()