import math


def format_to_currency(input_no):
	input_no_str = str(input_no)
	output_str = ''

	if input_no < 1000:
		return input_no
	else:
		output_str = input_no_str[-3:]

		temp = input_no_str[:-3][::-1]
		total_iters = math.ceil(len(temp) / 2)

		i = 0
		for _ in range(0, total_iters):
			output_str = temp[i:i+2][::-1] + ',' + output_str
			i += 2

		return output_str


if __name__ == '__main__':
	input_no = 1000000
	print(input_no)
	print(format_to_currency(input_no))