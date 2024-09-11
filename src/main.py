import os
import re
import sys
import threading

# Import modules
from aptopus.doctor import AptopusDoctor
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
  doctor = AptopusDoctor(io=io)

  # Otherwise, Aptopus will start a new conversation
  # by default
  io.clear_screen()

  while True:
    try:
      doctor.run()
      return None
    except Exception as e:
      # The strange exception is threw
      # Terminate program
      print(e)
      sys.exit(0)

if __name__ == "__main__":
  main()
  sys.exit(0)