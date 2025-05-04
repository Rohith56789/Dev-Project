## If you want to create some complex CLI you can use this
import argparse

parser = argparse.ArgumentParser(description='Sample Example for command-Line Argument.')
parser.add_argument('name', type=str, help='Name of the user')
parser.add_argument('age', type=int, help='Age of the user')
parser.add_argument('--city', type=str, help='City of the user', default='Unknown')

args = parser.parse_args()

print(f"Hello {args.name}, you are {args.age} years old and live in {args.city}.")
## To run this script, save it as `04.argparse.py` and run it from the command line:
## python 04.argparse.py John 30 --city NewYork
## py filename.py ( you can see validation error)
## py filename.py -h ( you can see description of arguments)
## py filename.py "rohith " 24 ( pass name and age then see the result)
## py filename.py "rohith " 24 --city Hyderabad ( pass name, age and city then see the result)
## py filename.py --city Hyderabad "rohith " 24 ( pass name, age and city then see the result)
