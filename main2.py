from basics.output.simple_message import run as simple_message
from basics.output.multiline_message import run as multiline_message
from basics.output.escape_characters import run as escape
from basics.repetitions.for_loop.characters import run as characters
from basics.repetitions.for_loop.count_down import run as count_down
from basics.repetitions.for_loop.range import run as range
from basics.repetitions.for_loop.reverse import run as reverse
from basics.repetitions.nested_loop.nested import run as nested
from basics.repetitions.nested_loop.nesting import run as nesting
from basics.repetitions.while_loop.ascii import run as ascii
from basics.repetitions.while_loop.count import run as count
from basics.repetitions.while_loop.factorial import run as factorial
from basics.repetitions.while_loop.len import run as len
from basics.repetitions.while_loop.simple import run as simple
from basics.repetitions.while_loop.sum_100 import run as sum_100
from basics.repetitions.while_loop.sum_user_numbers import run as sum_user_numbers
from basics.functions.multiple_functions import run as multiple_functions
from basics.functions.ascii_character import run as ascii_character
from basics.functions.ascii_code import run as ascii_code
from basics.functions.function_calls import run as function_calls
from basics.functions.function_with_loop import run as function_with_loop
from basics.functions.function_with_nesting import run as function_with_nesting
from basics.functions.function_with_parameter import run as function_with_parameter
from basics.functions.function_with_parameters import run as function_with_parameters
from basics.functions.return_values import run as return_values
from basics.functions.simple_function import run as simple_function

functions = ["simple_message", "multiline_messasum_100ge", "escape", "characters", "count_down", "range", "reverse", "simple", "nested", "nesting", "ascii", "count", "factorial", "len", "simple", "sum_100", "sum_user_numbers", "multiple_functions", "ascii_character", "ascii_code", "function_calls", "function_with_loop", "function_with_nesting", "function_with_parameter", "function_with_parameters", "return_values", "simple_function"]

def run_block_a():
  print("Which program in 'Block A: Basics' do you wish to run?")
  response = input()
  if response in functions:
    globals()[response]()

def run():
  is_running = True
  while(is_running):
    print("What would you like to do?")
    print("[a] Run 'Block A: Basics' programs")
    print("[q] Quit")
    response = input()
    if (response == "a"):
      run_block_a()
    elif (response == "q"):
      break
    else:
      print("Invalid option! Please try again.")
run()