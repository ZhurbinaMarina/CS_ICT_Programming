import unittest
from src.lab3.sudoku import group, get_row, get_col, get_block, find_empty_positions, find_possible_values, \
    check_solution, generate_sudoku, solve


class SudokuTestCase(unittest.TestCase):

    def test_group(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_get_row(self):
        self.assertEqual(get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '2', '.'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0)), ['4', '.', '6'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0)), ['.', '8', '9'])

    def test_get_col(self):
        self.assertEqual(get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '4', '7'])
        self.assertEqual(get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1)), ['2', '.', '8'])
        self.assertEqual(get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2)), ['3', '6', '9'])

    def test_get_block(self):
        grid = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
                ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
                ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
        self.assertEqual(get_block(grid, (0, 1)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
        self.assertEqual(get_block(grid, (4, 7)), ['.', '.', '3', '.', '.', '1', '.', '.', '6'])
        self.assertEqual(get_block(grid, (8, 8)), ['2', '8', '.', '.', '.', '5', '.', '7', '9'])

    def test_find_empty_positions(self):
        self.assertEqual(find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]), (0, 2))
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]), (1, 1))
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]), (2, 0))

    def test_find_possible_values(self):
        grid = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
                ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
                ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
        self.assertEqual(find_possible_values(grid, (0, 2)), {'1', '2', '4'})
        self.assertEqual(find_possible_values(grid, (4, 7)), {'2', '5', '9'})

    def test_check_solution(self):
        grid = [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
                ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
                ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
                ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
                ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
        self.assertEqual(check_solution(grid), True)

        grid = [['8', '3', '5', '4', '1', '6', '9', '2', '7'], ['2', '9', '6', '8', '5', '7', '4', '3', '1'],
                ['4', '1', '7', '2', '9', '9', '6', '5', '8'], ['5', '6', '9', '1', '3', '4', '7', '8', '2'],
                ['1', '2', '3', '6', '7', '8', '5', '4', '9'], ['7', '8', '8', '5', '2', '9', '1', '6', '3'],
                ['6', '5', '2', '7', '8', '1', '3', '9', '4'], ['9', '8', '1', '3', '4', '5', '2', '7', '6'],
                ['3', '7', '4', '9', '6', '2', '3', '1', '5']]
        self.assertEqual(check_solution(grid), False)

    def test_generate_sudoku(self):
        matrix = generate_sudoku(40)
        self.assertEqual(sum(1 for row in matrix for elem in row if elem == '.'), 41)
        self.assertEqual(check_solution(solve(matrix)), True)

        matrix = generate_sudoku(60)
        self.assertEqual(sum(1 for row in matrix for elem in row if elem == '.'), 21)
        self.assertEqual(check_solution(solve(matrix)), True)

        matrix = generate_sudoku(75)
        self.assertEqual(sum(1 for row in matrix for elem in row if elem == '.'), 6)
        self.assertEqual(check_solution(solve(matrix)), True)
