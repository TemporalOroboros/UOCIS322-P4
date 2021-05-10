import nose
import arrow
import ../src.acp_times as acp_times


ZERO_TIME = arrow.utcnow().floor('minutes') # Limited to minutes so it's compatible with the rounding donw in acp_times
BASE_ARROW = arrow.get(ZERO_TIME)

def test_open_times():
	"""Tests the open time offsets produced by several input values.
	"""
	base_time = arrow.get(ZERO_TIME)
	assert acp_times.open_time(0, 1000, BASE_ARROW) == BASE_ARROW
	assert acp_times.open_time(60, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=1, minutes=46)
	assert acp_times.open_time(200, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=5, minutes=53)
	assert acp_times.open_time(400, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=12, minutes=8)
	assert acp_times.open_time(600, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=18, minutes=48)
	assert acp_times.open_time(1000, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=33, minutes=5)

def test_open_brevet_size():
	"""Tests that open times are properly limited by brevet size.
	"""
	assert acp_times.open_time(1200, 200, BASE_ARROW) == BASE_ARROW.shift(hours=5, minutes=53)
	assert acp_times.open_time(1200, 400, BASE_ARROW) == BASE_ARROW.shift(hours=12, minutes=8)
	assert acp_times.open_time(1200, 600, BASE_ARROW) == BASE_ARROW.shift(hours=18, minutes=48)
	assert acp_times.open_time(1200, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=33, minutes=5)

def test_close_times():
	"""Tests the close times produced by several input calues
	"""
	assert acp_times.close_time(0, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=1)
	assert acp_times.close_time(20, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=2)
	assert acp_times.close_time(60, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=4)
	assert acp_times.close_time(75, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=5)
	assert acp_times.close_time(200, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=13, minutes=20)
	assert acp_times.close_time(400, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=26, minutes=40)
	assert acp_times.close_time(600, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=40)
	assert acp_times.close_time(1000, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=61, minutes=20)

def test_close_brevet_size():
	"""Tests that close times are properly limited by brevet size.
	"""
	assert acp_times.close_time(1200, 200, BASE_ARROW) == BASE_ARROW.shift(hours=13, minutes=20)
	assert acp_times.close_time(1200, 400, BASE_ARROW) == BASE_ARROW.shift(hours=26, minutes=40)
	assert acp_times.close_time(1200, 600, BASE_ARROW) == BASE_ARROW.shift(hours=40)
	assert acp_times.close_time(1200, 1000, BASE_ARROW) == BASE_ARROW.shift(hours=61, minutes=20)


