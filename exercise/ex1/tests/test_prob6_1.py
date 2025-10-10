import pytest

from prob6_1 import min_operations


def test_prob6_1_0():
	init = []
	target = []
	expt = None
	assert min_operations(init, target) == expt


def test_prob6_1_1():
	init = [3,2,1,4,5,6]
	target = [5,6,3,2,1,4]
	expt = 2
	assert min_operations(init, target) == expt


def test_prob6_1_2():
	init = [1,2,3,4]
	target = [3,4,2,1]
	expt = None
	assert min_operations(init, target) == expt


def test_prob6_1_3():
	init = [1]
	target = []
	expt = None
	assert min_operations(init, target) == expt


def test_prob6_1_4():
	init = 0
	target = []
	expt = None
	assert min_operations(init, target) == expt


def test_prob6_1_5():
	init = [1,2,3,4,5]
	target = [1,2,3,4,5]
	expt = None
	assert min_operations(init, target) == expt


def test_prob6_1_6():
	init = [1,2]
	target = [1,2]
	expt = None
	assert min_operations(init, target) == expt


def test_prob6_1_7():
	init = [3,2,1,4,5,6]
	target = [5,7,3,2,1,4]
	expt = None
	assert min_operations(init, target) == expt


def test_prob6_1_8():
	init = [3,2,1,4,5,6]
	target = [5,3,6,2,4,1]
	expt = -1
	assert min_operations(init, target) == expt



