import random

def get_input(prompt):
  """Gets an input from the user."""
  return input(prompt)

def generate_mad_lib():
  """Generates a Mad Lib."""
  noun = get_input("Enter a noun: ")
  verb = get_input("Enter a verb: ")
  adjective = get_input("Enter an adjective: ")
  adverb = get_input("Enter an adverb: ")

  mad_lib = """
  The {noun} {verb}ed the {adjective} {adverb}.
  """.format(noun=noun, verb=verb, adjective=adjective, adverb=adverb)

  return mad_lib

def main():
  """The main function of the Mad Libs game."""
  mad_lib = generate_mad_lib()
  print(mad_lib)

if __name__ == "__main__":
  main()
