# helloworld
This is a package to say hello and run a couple of simple functions.

## Installation
Clone the repo, cd into it, and use pip to install it.
```
git clone https://github.com/izrubin/helloworld.git
cd helloworld/
pip install .
```

## CLI Usage
To use the executable helloworld command line program (CLI):
```
$ helloworld -h
usage: helloworld [-h] [-n NAME] [--nextm] [--roll]

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  optional name to say hello to
  --nextm               print the number of days until the next millenium
  --roll                print two numbers as if you rolled two 6-sided dice
```

## API Usage
To use the helloworld Python API, import helloworld and then use any one or more of the three options:
```
import helloworld
helloworld.helloworld(name="Ilana", nextm=True, roll=True)
```

```
Hello, Ilana.
There are 358611 days until the new millenium.
You rolled a 6 and a 5.
```