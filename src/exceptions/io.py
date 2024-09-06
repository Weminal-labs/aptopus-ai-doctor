class InvalidOutputException(Exception):

  def __init__(self, output: str, message="") -> None:
    self.output = output

    if message == "":
      message = f"'{output}' isn't a valid output"

    self.message = message
    super().__init__(message)