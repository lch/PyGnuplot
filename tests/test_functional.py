import unittest
import numpy as np
from PyGnuplot import gp


class FunctionalTest(unittest.TestCase):
	def test_draw(self):
		f1 = gp()
		x = np.linspace(0, 20, 1001)
		yn = np.random.randn(1001) / 10
		y = np.sin(x)
		data = [x, y + yn]
		func = 'y(x) = a + b*cos(x + c)'
		(a, b, c), report = f1.fit(data, func, via='a,b,c', limit=1e-9)
		f1.save(data, 'tmp.dat')
		f1.a('plot "tmp.dat" w lp')
		f1.a('replot y(x)')
		dat_s = f1.m_str([x, y], delimiter='\t')
		print()
		print('fitting function is: ' + func)
		print('fit report:')
		for line in report:
			print(line)


if __name__ == '__main__':
	unittest.main()
