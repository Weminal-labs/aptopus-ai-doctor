class AptopusAIInteractor:
  def __init__(self, socket) -> None:
    self.socket = socket
    pass

  def get_anwser(self):
    can_break = False
    data = {
      "type": "handle_answer",
      "data": ""
    }
    self.socket.send(data)

    count = 0
    previous_chunk = ""
    text = ""

    while not can_break:
      data = self.socket.receive()
      text += data["data"]

      if data["data"]== "" and previous_chunk == "" and count != 0:
        can_break = True

      previous_chunk = data["data"]
      count = count + 1

    return text