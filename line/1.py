#!/etc/bin/python
#coding=utf-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator


def get_data(fname):
	fd = open(fname, "r");
	line = fd.readline()
	y = [ [] for i in range(8)]
	flag = -1;
	while(line):
		if(line[0] == '#' and line[1] == '#'):
			break;
		if(line[0] == ' ' or line[0] == '\n'):
			line = fd.readline()
			continue;
		if(line[0] == '$'):
			flag += 1
			line = fd.readline()
			continue
		num = float(line)
		y[flag].append(num)
		line = fd.readline()
	return y



if __name__ == '__main__':
	x_lb = []
	xs = []
	for i in range(40):
		xs.append(i)
		x_lb.append((i + 1)/40)


	y = get_data("tmp.dat.txt");
	y_lb = ['leveldb', 'hash_db-1', 'hash_db-8', 'hash_db-16', 'hash_db-32',
	 'hash_db-64', 'hash_db-128', 'hash_db-256']

	def format_fn(tick_val, tick_pos):
	    if int(tick_val) in xs:
	        return x_lb[int(tick_val)]
	    else:
	        return ''

	fig = plt.figure()
	ax = fig.add_subplot(111)

	# ax.xaxis.set_major_formatter(FuncFormatter(format_fn))
	# ax.xaxis.set_major_locator(MaxNLocator(integer=True))

	l_type = ['+-', 'o-', 'x-', '*-', '>-', '<-', '^-', 'v-']

	for i in range(len(y)):
		if(i == 0):
			ax.plot(x_lb, y[i], 'b+-', linewidth = 1.5,label = y_lb[i])
		else:
			ax.plot(x_lb, y[i], '-', linewidth = 1.5,label = y_lb[i])
		# ax.plot(x_lb, y[i], l_type[i], linewidth = 1.5,label = y_lb[i])

	plt.grid(True)
	plt.legend(loc = 0) #图例位置自动
	plt.axis('tight')
	plt.xlim((0, 1))
	plt.xlabel('get percentage')
	plt.ylabel('time (second)')
	# plt.title('random read 992,063 key-value pairs from 992,06 pairs\nwhich value size is 1000 Bytes')
	plt.title('random get 7,352,941 key-value pairs which value size is 128 Bytes')
	plt.show()