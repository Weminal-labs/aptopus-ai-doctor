# Create a new function from this file
# A function contains these files by default
def describe(can_print: bool = False):
  """Describe what function can does

  Args:
    can_print (bool, optional): can print function's description to console?. Defaults to False.

  Returns:
     str: a description string
  """
  content = "Your function description"
  if can_print:
    print(content)
  return content

def get_help():
  """Describe what function can does and its options
  """
  print("Use of your function")