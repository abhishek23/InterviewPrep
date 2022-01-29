import random

ladders_arr = [(32,62), (44,66), (22,58), (34,60), (2,90)]
snakes_arr = [(85,7), (63,31), (87,13), (75,11), (89,33), (57,5), (71,15), (55,25)]

def roll_dice():
	face_prob_arr = [0.39,0.05,0.14,0.05,0.12,0.25]
	return random.choices([1, 2, 3, 4, 5, 6], face_prob_arr)[0]


def check_snake_or_ladder(curr_pos):
	ladder = dict(ladders_arr)
	snakes = dict(snakes_arr)

	while curr_pos in (list(snakes.keys()) + list(ladder.keys())):
		if curr_pos in snakes.keys():
			curr_pos = snakes[curr_pos]
		if curr_pos in ladder.keys():
			curr_pos = ladder[curr_pos]

	return curr_pos


def main():
	curr_pos = 0
	moves = 0

	while curr_pos != 100:
		dice_val = roll_dice()
		moves += 1

		if (curr_pos+dice_val) > 100:
			continue

		curr_pos += dice_val

		if curr_pos == 100:
			break;

		curr_pos = check_snake_or_ladder(curr_pos)

	return moves


if __name__ == '__main__':

	avg_moves = []
	for k in range(0, 10):

		moves = []
		for i in range(0, 2000):
			print(f"Simulation No: {i}")
			moves.append(main())

		avg_moves.append(sum(moves)/len(moves))

	print(f"Avg Moves: {avg_moves}")
