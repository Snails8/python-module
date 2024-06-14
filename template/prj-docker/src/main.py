import math
import sys

from domain import init

def main():
  val = float(sys.argv[1])
  print(math.radians(val))

if __name__ == "__main__":
  main()

init("sample")