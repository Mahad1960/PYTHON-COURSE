import argparse
parser=argparse.ArgumentParser(description="Greet The User.")
parser.add_argument("name",help="Name Of The User.")
parser.add_argument("--greeting",default="Hello",help="Greeting Message")
args=parser.parse_args()
print(f"{args.greeting}, {args.name}!")
# Search this module futher from the sources.