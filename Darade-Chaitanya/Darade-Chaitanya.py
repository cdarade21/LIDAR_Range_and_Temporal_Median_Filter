import numpy as np

def range_filter(scans,minimum,maximum):
	"""	MINIMUM MAXIMUM FILTER-
	If values are less than Minimum , replace the values with the Minimum and same way for maximum"""
	return [[min(max(value, minimum), maximum) for value in scan] for scan in scans]

def temp_median_filter(scans, d):
	""" TEMPORAL MEDIAN FILTER-
	Median of the elements by comparing it to the previous d scans
	ERROR HANDLING: try catch used if varied number of values are entered in scan"""
	result = []
	for current in range(len(scans)):
		medians = []
		try:
			for previousIndex in range(len(scans[current])):
				medians.append(round(np.median([scan[previousIndex]
					for scan in scans[max(-1, current - d) + 1: current + 1]]),1))
		except IndexError as err:
			print(err)
			exit()  # comment this line if u still want the values with varied scans
		result.append(medians)
	return result

def main():
    
	"""EXECUTION-
	Set the values of min max
	Pass the values of scans and d
	Print the output"""

	minimum, maximum = 0.03, 50  # assign max and min values

	# inputs and filter size
	d, big = 3, [[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.], [10., 2., 4., 0., 0.]]
	filter1_value = range_filter(big, minimum, maximum)
	filter2_value = list(temp_median_filter(filter1_value, d+1))

	# print the values and error handling
	print("input", big, "\n""after_MixMax_filter", filter1_value, "\n""After_temp_median:", filter2_value)

if __name__ == '__main__':
	main()
