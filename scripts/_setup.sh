#!/bin/bash

. utils.sh

# Our entire program will be set up in this script, within following steps:
# Download release package from origin
# Unpack and install the requirement
# Move to **/bin
# Alias main.py = aptopus
# Add to bash profile