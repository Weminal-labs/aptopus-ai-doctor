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
from typing import Literal

# Import from prompt_toolkit
from prompt_toolkit import HTML, prompt, print_formatted_text as print
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.shortcuts import clear

# Import from rich
from rich.console import Console
from rich.markdown import Markdown

AptopusColors = Literal["red", "green", "blue", "yellow", "white", "gray", "purple", "pink"]
AptopusFontStyles = Literal["default", "italic", "bold", "italic_bold"]
console = Console()

class AptopusIO:
  def __init__(self, args_parser) -> None:
    self.args_parser = args_parser
    self.style = Style.from_dict({
      "red": "red",
      "green": "green",
      "blue": "dodgerblue",
      "yellow": "yellow",
      "white": "white",
      "gray": "dimgray",
      "purple": "purple",
      "pink": "pink"
    })
    pass

  def _is_color_support(self, color):
    if color == "red": return True
    if color == "green": return True
    if color == "blue": return True
    if color == "yellow": return True
    if color == "white": return True
    if color == "gray": return True
    if color == "purple": return True
    if color == "pink": return True
    return False

  def get_html(sefl, content: str):
    return HTML(content)

  def attach_font_style(
    self,
    content: str,
    style: AptopusFontStyles | None = None,
    is_html_result = False
  ):
    """Get content with font style (italic, bold or italic and bold).

    Args:
        content (str): content that you want to attach font style to.
        style (AptopusFontStyles | None, optional): supported font styles.
        is_html_result (bool, optional): if you want this method return HTML, set to `True`.

    Returns:
        HTML | str: _description_
    """
    if style == None or style == "default": return content
    content_wrapper = ""

    if style == "bold": content_wrapper = f"<strong>{content}</strong>"
    if style == "italic": content_wrapper = f"<i>{content}</i>"
    if style == "italic_bold": content_wrapper = f"<strong><i>{content}</i></strong>"

    if is_html_result:
      return HTML(content_wrapper)
    return content_wrapper

  def paint_text(
    self,
    content: str,
    text_color: AptopusColors | None = None,
    bg_color: AptopusColors | None = None,
    is_html_result = True
  ):
    """Get colored text with colored background (or not) in the supported range of colors

    Args:
        content (str): the content you want to paint.
        text_color (AptopusColors | None, optional): the color of text.
        bg_color (AptopusColors | None, optional): the background color of text.
        is_html_result (bool, optional): if you want this method return HTML, set to `True`.

    Returns:
        HTML | str: the output can be a literal string or instance of prompt_toolkit.HTML 
    """
    if text_color == None and bg_color == None:
      return content

    # If the text color isn't support, set to default color.
    if not self._is_color_support(text_color):
      text_color = "white"

    # If the background color isn't support, set to none.
    if not self._is_color_support(bg_color):
      bg_color = None

    output = ""

    # Setup output
    if bg_color == None:
      output = f"<{text_color}>{content}</{text_color}>"
    else:
      output = f"<{text_color} bg=\"{bg_color}\">{content}</{text_color}>"

    if is_html_result:
      return HTML(output)
    return output

  def output(
    self,
    output: HTML | str | None = None,
    is_markdown = True,
    is_inline = False
  ):
    """Print output to terminal console. Format of output can be `markdown`, `formatted_text`,
    `str` or `None`.

    Args:
        output (HTML | str | None, optional): the output.
        is_markdown (bool, optional): if the output is in markdown format, set to `True`
        is_inline (bool, optional): if you want to put the output in the same line with previous output, set to `True`
    """
    if output == None: print()
    if isinstance(output, HTML):
      is_markdown = False

    _print = print

    if is_markdown:
      output = Markdown(output)
      _print = console.print

    if is_inline:
      _print(output, style=(None if is_markdown else self.style), end=" ")
    else:
      _print(output, style=(None if is_markdown else self.style))

  def get_input(
    self,
    content: HTML | str,
    placeholder: str | None = None
  ):
    # kb = KeyBindings()

    if placeholder != None:
      placeholder = self.attach_font_style(placeholder, style="italic")
      placeholder = self.paint_text(placeholder, text_color="gray")
      content = prompt(content, placeholder=placeholder, style=self.style)
    else:
      content = prompt(content, style=self.style)

    return content
  
  def clear_screen(self):
    clear()