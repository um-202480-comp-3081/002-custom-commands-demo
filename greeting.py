#!/Users/kbrid/.asdf/shims/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="name of the person to greet")
parser.add_argument(
    "--time",
    choices=["morning", "afternoon", "evening"],
    help="time of day",
)
parser.add_argument(
    "-e", "--excited", action="store_true", help="specifies excitement level"
)


args = parser.parse_args()

time = "morning"
if args.time:
    time = args.time
name = args.name
excited = args.excited
punct = "!"
if excited:
    punct = "!!!"


print(f"Good {time}, {name}{punct}")
