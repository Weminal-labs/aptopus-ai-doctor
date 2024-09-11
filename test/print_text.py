#!/usr/bin/env python
"""
Demonstration of all the ANSI colors.
"""

from prompt_toolkit import HTML, print_formatted_text as print
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style

def main():
  style = Style.from_dict({
    "red": "Red",
    "green": "Green"
  })

  html = "\n<strong><green>Welcome to Aptopus!!!</green></strong>"
  html += "\nYou can interact with <strong>Aptopus</strong> in your terminal directly."
  html += "\n=============================="
  html += "\nEnter your question:"
  html += "\n"
  
  print(HTML(html), style=style)

if __name__ == "__main__":
  main()