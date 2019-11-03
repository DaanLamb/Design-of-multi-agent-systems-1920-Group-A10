# Iterative prisoner's dilemma with emotions
This is a simulation of a multi-agent system containing agents with emotions that play the iterative prisoner's dilemma and earn points. The system is used for research on the influence of one-strategy agents (cooperators and defectors) on emotional agents. Results are generated that give information about the total amount of points, total amount of points per emotion and the average amount of points per emotion.

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
## Contents
The repository has three folders.
- main_experiments: This folder contains the files that were used to generate the results of the main experiments.
- param_sweep: This folder contains the files that were used to generate the results of the parameter sweep.
- other: This folder contains some files that do not belong in the other folders.

## Usage
The program for both the main experiments and the parameter sweep can be run by using the following command:
```bash
$ python3 world.py
```

## Results
Both the main_experiments and param_sweep folder have a folder named results. This holds the .csv files that the results were written to. 
For the parameter sweep the results can be found in the file sweep.csv. The headers give an indication of what the data means. The main experiment results are spread over a number of files. The file total_gain.csv is an example of the results for the total gain per emotion for the distribution 0/100/0 of the complete simulation. The files gain_per_type_*_*.csv have the average gain per emotion for the four distributions.