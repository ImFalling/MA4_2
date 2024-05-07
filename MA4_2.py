#!/usr/bin/env python3

from person import Person
import matplotlib.pyplot as plotter
from numba import njit
import time

def fib_py_mem(n: int, memory = None):
	"""Fibonacci function, uses memoization."""
	if n % 1 != 0 or n < 0:
		print(f"Function fib() cannot be called with {n}, only with positive whole integers.")
		return None
	if memory == None:
		memory = {0: 0, 1: 1}
	if n not in memory:
		memory[n] = fib_py_mem(n-1, memory) + fib_py_mem(n-2, memory)
	return memory[n]

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

	fromN = 20
	toN = 35
	def cppfoo(n):
		f.setAge(n)
		return f.fib()
	
	cpp = {"call": cppfoo, "x": [], "y": [], "marker": "ro--", "id": "C++"}
	numba = {"call": fib_numba, "x": [], "y": [], "marker": "bo--", "id": "Python w/ Numba"}
	vanilla = {"call": fib_py, "x": [], "y": [], "marker": "go--", "id": "Python (Vanilla)"}
	
	for dataset in [cpp, numba, vanilla]:
		for n in range(fromN, toN+1):
			dataset["x"].append(n)
			t0 = time.perf_counter()
			dataset["call"](n)
			dataset["y"].append(time.perf_counter() - t0)
	
		plotter.plot(dataset["x"], dataset["y"], dataset["marker"], label=dataset["id"])
		print(f'=== {dataset["id"]} ===\nx-values: {dataset["x"]}\ny-values: {dataset["y"]}')

	plotter.xlabel("n=", fontweight="semibold", fontsize="13")
	plotter.ylabel("Time (seconds)", fontweight="semibold", fontsize="13")
	#plotter.axis([fromN, toN, 0, vanilla["y"][-1] + vanilla["y"][-1]/10])
	plotter.xticks(range(fromN, toN+1))
	plotter.xlim(right=toN+0.5)
	plotter.grid(True)
	plotter.legend(title="Functions:")
	plotter.savefig(f"{fromN}-{toN}_results.png")
	plotter.show()

	#print(f"Fib(47) with Numba: {fib_numba(47)}")
	#f.setAge(47)
	#print(f"Fib(47) with C++: {f.fib()}")
	'''
	Fib(47) with Numba: 2971215073
	Fib(47) with C++: 2971215073
	'''

if __name__ == '__main__':
	main()
