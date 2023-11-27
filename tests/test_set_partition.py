from ecgenpy.set_bipart import set_bipart, stirling2nd2
from ecgenpy.set_partition import set_partition, stirling2nd


def test_set_partition_odd_odd():
    cnt = 1
    for _ in set_partition(11, 5):
        cnt += 1
    assert cnt == stirling2nd(11, 5)


def test_set_partition_even_odd():
    cnt = 1
    for _ in set_partition(10, 5):
        cnt += 1
    assert cnt == stirling2nd(10, 5)


def test_set_partition_odd_even():
    cnt = 1
    for _ in set_partition(11, 6):
        cnt += 1
    assert cnt == stirling2nd(11, 6)


def test_set_partition_even_even():
    cnt = 1
    for _ in set_partition(10, 6):
        cnt += 1
    assert cnt == stirling2nd(10, 6)


def test_set_partition_special():
    cnt = 1
    for _ in set_partition(6, 6):
        cnt += 1
    assert cnt == 1
    for _ in set_partition(5, 5):
        cnt += 1
    assert cnt == 1


def test_set_bipart_odd():
    cnt = 1
    for _ in set_bipart(11):
        cnt += 1
    assert cnt == stirling2nd2(11)


def test_set_bipart_even():
    cnt = 1
    for _ in set_bipart(10):
        cnt += 1
    assert cnt == stirling2nd2(10)


def test_set_bipart_two():
    cnt = 1
    for _ in set_bipart(2):
        cnt += 1
    assert cnt == stirling2nd2(2)
