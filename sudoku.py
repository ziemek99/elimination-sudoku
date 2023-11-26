import numpy as np
from copy import deepcopy

board = np.array([set(range(1, 10)) for _ in range(81)]).reshape(9, 9)


def generate_html():
	html = (
		'<!DOCTYPE html><html lang=""><head><meta charset="utf-8">'
		+ '<link rel="stylesheet" href="style.css"><title>Elimination Sudoku'
		+ '</title><script type="text/javascript">setInterval("window.location.reload()"'
		+ ', 1000);</script></head><body><table class="main">'
	)

	for i in range(0, 9, 3):
		html += '<tr>'
		for j in range(0, 9, 3):
			html += '<td><table class="square">'
			square = board[i : i+3, j : j+3]
			for k in range(0, 3):
				html += '<tr>'
				for l in range(0, 3):
					possible_numbers = deepcopy(square[k, l])
					if len(possible_numbers) == 1:
						html += f'<td class="complete">{next(iter(possible_numbers))}</td>'
					else:
						html += '<td><table class="hint">'
						for m in range(0, 3):
							html += '<tr>'
							for n in range(1, 4):
								html += '<td>'
								number = 3*m + n
								if number in possible_numbers:
									html += str(number)
									possible_numbers.remove(number)
								html += '</td>'
							html += '</tr>'
						html += '</table></td>'
				html += '</tr>'
			html += '</table></td>'
		html += '</tr>'
	html += '</table></body></html>'

	with open('sudoku.html', 'w') as file:
		file.write(html)


def modify_board():
	y, x, number = [int(value) for value in input().split()]
	y, x = y-1, x-1
	if number not in board[y, x]:
		print('Error: wrong number, valid numbers are:', board[y, x])
		return
	for i in range(9):
		if number in board[y, i]:
			board[y, i].remove(number)
	for i in range(9):
		if number in board[i, x]:
			board[i, x].remove(number)
	for possible_numbers in board[y//3*3 : y//3*3+3, x//3*3 : x//3*3+3].reshape(9):
		if number in possible_numbers:
			possible_numbers.remove(number)
	board[y, x] = {number}


def main():
	print('Enter the values in format: y x number')
	while True:
		generate_html()
		modify_board()


if __name__ == '__main__':
	main()
