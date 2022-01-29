denoms = [1,2,5,10]


def main(amount):

	sorted_denom = sorted(denoms, reverse=True)
	final_denoms = []

	for max_denom in sorted_denom:
		max_denom_count = amount // max_denom
		if max_denom_count > 0:
			amount -= (max_denom_count * max_denom)

		final_denoms.append((max_denom, max_denom_count))

	return final_denoms


if __name__ == '__main__':

	amount = 0.5
	min_denoms = main(amount)

	print(min_denoms)