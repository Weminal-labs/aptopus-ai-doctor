# Import argparse
import argparse

from aptopus import __version__

class AptopusArgsParser:
  def __init__(self) -> None:
    self._parser = argparse.ArgumentParser(
      prog="aptopus",
      description="Aptopus is AI pair programming being used in your Aptos project with Terminal.",
    )

    # Add some global flag
    self._parser.add_argument(
      "--version",
      action="version",
      version=f"%(prog)s {__version__}",
      help="Show the version number"
    )

    # Add some arguments
    group = self._parser.add_argument_group("Main")
    group.add_argument(
      "-q", "--question",
      help="Get answer from your question immediately",
    )
    pass

  def get_args(self):
    return self._parser.parse_args()