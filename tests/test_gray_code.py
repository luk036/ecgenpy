from math import comb

from ecgenpy.combin import EMK_gen
from ecgenpy.gray_code import BRGC_gen


def test_Gray_code_odd():
    cnt = 1
    for _ in BRGC_gen(5):
        cnt += 1
    assert cnt == 2 ** 5


def test_Gray_code_even():
    cnt = 1
    for _ in BRGC_gen(6):
        cnt += 1
    assert cnt == 2 ** 6


def test_combinations():
    cnt = 1
    for _ in EMK_gen(5, 3):
        cnt += 1
    assert cnt == comb(5, 3)
