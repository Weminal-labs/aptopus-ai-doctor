import os
import re
import sys
import threading

# Import modules
from aptopus.docter import AptopusDocter
from aptopus.io import AptopusIO
from aptopus.args import AptopusArgsParser

# Import functions from function module
from aptopus.ai import AptopusAIInteractor

def main():
  args_parser = AptopusArgsParser()
  
  args = args_parser.get_args()

  # If the command is a one run command
  # process and return to user
  if args.question != None:
    print("Your fast question will be hanlded here")
    return

  io = AptopusIO(args_parser=args_parser)
  docter = AptopusDocter(io=io)

  # Otherwise, Aptopus will start a new conversation
  # by default
  io.clear_screen()

  while True:
    try:
      docter.run()
      return None
    except SystemExit:
      sys.exit(0)
    except Exception as e:
      # Process other use cases after the program
      # is stop
      print(e)

if __name__ == "__main__":
  main()
  sys.exit(0)