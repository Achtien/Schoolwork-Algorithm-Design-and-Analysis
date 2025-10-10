import pytest

from prob3 import TotalCombatPower

def test_prob3_0():
	ls = []
	expt_mem = []
	expt_tcp = 0
	inst = TotalCombatPower(ls)
	assert inst.members == expt_mem
	assert inst.max_tcp == expt_tcp


def test_prob3_1():
	ls = [1.2, 1.1, 1, 1.9, 1.8]
	expt_mem = sorted(ls, reverse=True)
	expt_tcp = sum(ls)
	inst = TotalCombatPower(ls)
	assert inst.members == expt_mem
	assert inst.max_tcp == expt_tcp


def test_prob3_2():
	ls = [1.2, 1.1, 1, 1.9, 1.8, 90]
	expt_mem = [1.9, 1.8, 1.2, 1.1, 1] 
	expt_tcp = sum(ls) - 90
	inst = TotalCombatPower(ls)
	assert inst.members == expt_mem
	assert inst.max_tcp == expt_tcp


def test_prob3_3():
	ls = [1, 2, 1.5]
	expt_mem = [2, 1.5, 1]
	expt_tcp = 4.5
	inst = TotalCombatPower(ls)
	assert inst.members == expt_mem
	assert inst.max_tcp == expt_tcp


