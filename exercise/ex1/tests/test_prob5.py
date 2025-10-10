import pytest

from prob5 import select_books


def test_prob5_0():
	d = []
	a = 0
	m = 0
	expt = []
	assert select_books(d, a, m) == expt


def test_prob5_1():
	d = [18,11,17,4,8,6,10,13,10]
	a = 10
	m = 3
	expt = [1, 6, 8]
	assert select_books(d, a, m) == expt


def test_prob5_2():
	d = []
	a = 0
	m = 1
	expt = []
	assert select_books(d, a, m) == expt

	
def test_prob5_3():
	d = [1]
	a = 0
	m = 0
	expt = []
	assert select_books(d, a, m) == expt


def test_prob5_4():
	d = []
	a = 0
	m = 10
	expt = []
	assert select_books(d, a, m) == expt


def test_prob5_5():
	d = [7,7,7,7,7,8,8,8,8,100]
	a = 8
	m = 5
	expt = [0,5,6,7,8]
	assert select_books(d, a, m) == expt



