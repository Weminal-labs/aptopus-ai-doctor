class CommandNotFoundException(Exception):

  def __init__(self, command: str, message="") -> None:
    self.command = command

    if message == "":
      message = f"The command '{command}' isn't found"

    self.message = message
    super().__init__(message)

class CommandInvalidException(Exception):

  def __init__(self, command: str, message="") -> None:
    self.command = command

    if message == "":
      message = f"The command '{command}' isn't valid"

    self.message = message
    super().__init__(message)