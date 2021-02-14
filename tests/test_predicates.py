from lib.predicates import is_even


class TestPredicates(object):
	def test_should_return_true_when_number_is_even(self):
		assert is_even(2)

	def test_should_return_false_when_number_is_odd(self):
		assert not is_even(3)