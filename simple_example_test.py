import pytest
from simple_example import Calculator


class TestExample(object):
	def test__add_number__2_2__returns_4(self):
		calculator = Calculator()

		result = calculator.add(2,2)

		assert result == 4
	
	def test__divide__0__raises(self):
		calculator = Calculator()
		with pytest.raises(ZeroDivisionError):
			calculator.divide(2,0)


	def test__divide__0__raises(self, calculator):

		with pytest.raises(ZeroDivisionError):
			calculator.divide(2,0)

		
