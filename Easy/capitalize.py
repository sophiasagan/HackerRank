#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return " ".join([x.capitalize() for x in (s.split(' '))])
