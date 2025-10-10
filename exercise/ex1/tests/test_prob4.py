import pytest

from prob4 import max_rev


def test_prob4_0():
	k = 0
	profit1 = []
	profit2 = []
	expt = 0
	assert max_rev(k, profit1, profit2) == expt


def test_prob4_1():
	k = 2
	profit1 = [2, 3, 5, 0, 30, 20]
	profit2 = [4, 1, 1, 2, 100, 100]
	expt = 214
	assert max_rev(k, profit1, profit2) == expt


def test_prob4_2():
	k = 2
	profit1 = []
	profit2 = []
	expt = 0
	assert max_rev(k, profit1, profit2) == expt


def test_prob4_3():
	k = 0
	profit1 = [2, 4]
	profit2 = []
	expt = 0
	assert max_rev(k, profit1, profit2) == expt


def test_prob4_4():
	k = 5
	profit1 = [1, 2]
	profit2 = [3, 4]
	expt = 3
	assert max_rev(k, profit1, profit2) == expt


def test_prob4_5():
	k = -19
	profit1 = [1, 2]
	profit2 = [3, 5]
	expt = 8
	assert max_rev(k, profit1, profit2) == expt



