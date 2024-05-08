#!/usr/bin/env python3

from person import Person
import matplotlib.pyplot as plotter
from numba import njit
import time

def fib_py(n):
	if n<= 1:
		return n
	return (fib_py(n-1) + fib_py(n-2))

@njit
def fib_numba(n: int):
	if n<= 1:
		return n
	return (fib_numba(n-1) + fib_numba(n-2))

def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(30)
	print(f.getAge())
	print(f.getDecades())
	print(f"C++: {f.fib()}")
	print(f"Python w/ numba: {fib_numba(30)}")
	print(f"Vanilla python: {fib_py(30)}")

	# Specify interval to try across functions
	fromN = 20
	toN = 35
	# Wrapper function for matching function calls with fib_numba and fib_py
	def cppfoo(n):
		f.setAge(n)
		return f.fib()
	
	# Establish the data structures to be accessed by pyplot
	cpp = {"call": cppfoo, "x": [], "y": [], "marker": "ro--", "id": "C++"}
	numba = {"call": fib_numba, "x": [], "y": [], "marker": "bo--", "id": "Python w/ Numba"}
	vanilla = {"call": fib_py, "x": [], "y": [], "marker": "go--", "id": "Python (Vanilla)"}
	
	# Call the functions sequentially and populate their respective dataset
	for dataset in [cpp, numba, vanilla]:
		for n in range(fromN, toN+1):
			dataset["x"].append(n)
			t0 = time.perf_counter()
			dataset["call"](n)
			dataset["y"].append(time.perf_counter() - t0)
	
		plotter.plot(dataset["x"], dataset["y"], dataset["marker"], label=dataset["id"])
		print(f'=== {dataset["id"]} ===\nx-values: {dataset["x"]}\ny-values: {dataset["y"]}')

	# Graph vanity setup
	plotter.xlabel("n=", fontweight="semibold", fontsize="13")
	plotter.ylabel("Time (seconds)", fontweight="semibold", fontsize="13")
	plotter.xticks(range(fromN, toN+1))
	plotter.xlim(right=toN+0.5)
	plotter.grid(True)
	plotter.legend(title="Functions:")
	plotter.savefig(f"{fromN}-{toN}_results.png")
	plotter.show()

	# Commented out to save time during runtime
	#print(f"Fib(47) with Numba: {fib_numba(47)}")
	#f.setAge(47)
	#print(f"Fib(47) with C++: {f.fib()}")
	'''
	Example output:
	Fib(47) with Numba: 2971215073
	Fib(47) with C++: 2971215073
	'''

if __name__ == '__main__':
	main()
