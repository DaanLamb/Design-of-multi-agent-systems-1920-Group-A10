# Iterative prisoner's dilemma with emotions
This program is an alpha version of a multi-agent system containing agents with emotions that play the iterative prisoner's dilemma. This system will be used for research on the influence of particular emotions on the welfare of the world.

## Dependencies 
The code is written in Python 3 and can be used with Windows, Linux and Mac. Python 3 should be available on most computers, but if this is not the case it can be installed using the following link https://www.python.org/downloads/.
A number of packages are required to run the system. These can be installed using pip, which can be found here https://docs.python.org/3/installing/index.html.

The required packages are:
- [Numpy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

The packages can be installing using the command: 
```bash
$ pip install <package-name>
```

## Usage
The main program can be run by using the following command:
```bash
$ python3 world.py
```
The visualization of the grid (for now a random grid) can be shown by using the following command:
```bash
$ python3 plotting.py
```

## Output
The (for now terminal) output shows a number of features of the system. In an agent types grid, the following numbers are used:
- 0 Cooperator agent
- 1 Defector agent
- 2 Emotional agent
