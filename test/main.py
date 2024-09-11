# Import from std
import sys
import signal

# Import from prompt_toolkit
from prompt_toolkit import prompt, print_formatted_text as print
from prompt_toolkit.formatted_text import FormattedText, HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import print_container
from prompt_toolkit.widgets import Frame, TextArea
from prompt_toolkit.key_binding import KeyBindings

def main():
  questions = [
    "Target'name",
    "Target's living place",
    "Target's age"
  ]
  result_titles = [
    "Name",
    "Living at",
    "Age"
  ]
  answers = []

  style = Style.from_dict({
    "success": "LightGreen",
    "warn": "Yellow",
    "error": "Red",
    "info": "LightBlue"
  })

  kb = KeyBindings()

  @kb.add("c-c", eager=True)
  def _(event):
    print(HTML("\n<strong><warn>Stop collect information</warn></strong>"), style=style)
    raise KeyboardInterrupt()

  try:
    print(HTML("\n<strong><info>Information Collector Program</info></strong>"), style=style)
    print(HTML("<info bg='green'>Press [ctrl-c] to exit the program</info>"), style=style)
    print("Please answer these question below\n")

    times = 0
    while True:
      input = prompt(f"{questions[times % len(questions)]} - ", key_bindings=kb)
      answers.append((result_titles[times % len(result_titles)], input))
      times += 1
  except SystemExit:
    print(HTML("\n<strong><success>Information collected!</success></strong>"), style=style)

    result = ""
    times = 0

    for answer in answers:
      result += f"{answer[0]}: {answer[1]}\n"

      print(f"({times}; {len(questions)})")

      if ((times + 1) % len(questions)) == 0 and times != 0 and times != (len(answers) - 1):
        result += "\n"

      times += 1

    print_container(
      Frame(
        TextArea(text=result),
        title="Result",
      )
    )
    print(HTML("<strong><warn>Exit program</warn></strong>"), style=style)


if __name__ == "__main__":
  main()