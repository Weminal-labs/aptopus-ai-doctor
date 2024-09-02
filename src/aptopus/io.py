import io

class AptopusIO:
  def __init__(self) -> None:
    pass

  def get_input(self, message="Prompt here:"):
    try:
      content = input(message)
      return content
    except:
      print("There is an error")