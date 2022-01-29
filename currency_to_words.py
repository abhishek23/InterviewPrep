from format_currency import format_to_currency


fixed_number_mapping = {
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40:	'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety',
}


place_value_mapping = {	
	1: 'thousand',
	2: 'lakh',
	3: 'crore',
}


def get_place_value(i, n):
	if n == '1':
		return place_value_mapping[i]
	else:
		place_value = place_value_mapping.get(i)
		return (place_value + 's' if place_value else '').strip()


def process_two_digits(two_digit_no):
	two_digit_no = int(two_digit_no)
	if two_digit_no not in fixed_number_mapping:
		tens_place_number = (two_digit_no // 10) * 10
		ones_place_number = two_digit_no % 10
		return fixed_number_mapping[tens_place_number] + " " + fixed_number_mapping[ones_place_number]
	return (fixed_number_mapping[int(two_digit_no)]).strip()


def process_three_digits(three_digit_no):
	three_digit_no = int(three_digit_no)
	three_digit_no_str = str(three_digit_no)

	hundreds_place_number = int(three_digit_no_str[0])
	output_str = fixed_number_mapping[hundreds_place_number] + " hundred"
	output_str += 's' if int(three_digit_no_str[0]) > 1 else ''

	if (three_digit_no % 100) == 0:
		return output_str
	else:
		last_two_digits = three_digit_no % 100
		output_str += " and " + process_two_digits(last_two_digits)

	return output_str


def currency_to_words(input_no):
	input_no_str = format_to_currency(input_no)
	input_no_split = input_no_str.split(',')[::-1]

	output_list = []	
	for i, n in enumerate(input_no_split):
		output_str = ''

		if int(n) >= 100:
			output_str = process_three_digits(n)
		elif int(n) > 0:
			output_str = process_two_digits(n)

		if int(n) > 0:
			output_str += ' ' + get_place_value(i, n)
		output_list = [output_str] + output_list

	return input_no_str, (' '.join(output_list).title()).strip() + ' Rupees'


if __name__ == '__main__':
	input_no = 1000000
	print(f"input: {input_no}")
	formatted_amount, amount_in_words = currency_to_words(input_no)
	print(f"formatted_amount: {formatted_amount}")
	print(f"amount_in_words: {amount_in_words}")

