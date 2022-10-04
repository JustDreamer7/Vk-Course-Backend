import unittest

from tictactoe import TicTacGame


class ValidateInputTest(unittest.TestCase):
    def setUp(self):
        self.inputs_right = ["0", "0 "]
        self.labels_right = 0
        self.inputs_wrong = ["3 1", "-1.5", "a", "b b", "", "3", "15", "²", "9"]
        self.inputs_1 = ["3 1", "-1.5", "a", "b b", "", "15"]
        self.labels_1 = "Должно быть в вводе одно целое число от одного до восьми"
        self.inputs_2 = "3"
        self.labels_2 = "Эта клетка занята"
        self.inputs_3 = "9"
        self.labels_3 = "Должно быть число от одного до восьми"
        self.inputs_4 = "²"
        self.labels_4 = "Не балуйтесь со степенями, введите полноразмерное целое число от одного до восьми"
        self.game = TicTacGame()
        self.game.board = [" "] * 9
        self.game.board[3] = "X"

    def test_result(self):
        for inputs in self.inputs_right:
            self.assertEqual(self.labels_right, self.game.validate_input(inputs))
        for inputs in self.inputs_1:
            try:
                self.game.validate_input(inputs)
            except ValueError as error:
                self.assertEqual(self.labels_1, str(error))
        for inputs, labels in zip([self.inputs_2, self.inputs_3, self.inputs_4],
                                  [self.labels_2, self.labels_3, self.labels_4]):
            try:
                self.game.validate_input(inputs)
            except ValueError as error:
                self.assertEqual(labels, str(error))


class ValidatePriority(unittest.TestCase):
    def setUp(self):
        self.inputs_right = ["n", "y", "y "]
        self.labels_right = ["n", "y", "y"]
        self.inputs_wrong = ["ds", "", "12"]
        self.labels_wrong = "Должно быть либо y, либо n:"
        self.game = TicTacGame()
        self.game.board = [" "] * 9

    def test_result(self):
        for inputs in self.inputs_wrong:
            try:
                self.game.validate_priority(inputs)
            except ValueError as error:
                self.assertEqual(self.labels_wrong, str(error))
        for inputs, labels in zip(self.inputs_right, self.labels_right):
            self.assertEqual(labels, self.game.validate_priority(inputs))


class ValidateWinner(unittest.TestCase):
    def setUp(self):
        self.inputs_draw = 0
        self.inputs_comp = "X"
        self.inputs_human = "O"
        self.game = TicTacGame()
        self.game.board = [" "] * 9

    def test_result(self):
        self.assertEqual(self.game.game_result(self.inputs_draw, self.inputs_comp), "Ничья\n")
        self.assertEqual(self.game.game_result(self.inputs_comp, self.inputs_comp), "Победил компьютер!")
        self.assertEqual(self.game.game_result(self.inputs_human, self.inputs_comp), "Вы победили!")


class ValidateTurn(unittest.TestCase):
    def setUp(self):
        self.turn = "X"
        self.turn_2 = "O"
        self.turn_3 = " "
        self.game = TicTacGame()
        self.game.board = [" "] * 9

    def test_result(self):
        self.assertEqual(self.game.next_turn(self.turn), self.turn_2)
        self.assertEqual(self.game.next_turn(self.turn_2), self.turn)
        self.assertEqual(self.game.next_turn(self.turn_3), self.turn)


class ValidateCheckWinner(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame()
        self.game.board = [" "] * 9
        self.game_2 = TicTacGame()
        self.game_2.board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]

    def test_result(self):
        self.assertEqual(self.game.check_winner(), None)
        self.assertEqual(self.game_2.check_winner(), 0)
        win_ways = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for way_of_win in win_ways:
            self.game = TicTacGame()
            self.game.board = [" "] * 9
            for i in way_of_win:
                self.game.board[i] = "X"
            self.assertEqual(self.game.check_winner(), "X")
        for way_of_win in win_ways:
            self.game = TicTacGame()
            self.game.board = [" "] * 9
            for i in way_of_win:
                self.game.board[i] = "O"
            self.assertEqual(self.game.check_winner(), "O")


class ValidateComputerMove(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame()
        self.game.board = [" "] * 9

    def test_result(self):
        self.assertIn(self.game.computer_move(computer="X", dermal_bag="O"), [i for i in range(9)])


if __name__ == "__main__":
    unittest.main()
