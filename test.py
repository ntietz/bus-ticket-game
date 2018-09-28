import unittest

from interpreter import evaluate, interpret, parse, tokenize
from interpreter import add, sub, mul, div
from interpreter import to_string
from solve import fast_is_solvable, is_solvable, all_sequences
from solve import all_sequences

class TestEvaluator(unittest.TestCase):
    def testEvaluatingSingleOperand(self):
        symbols = [1]
        result = evaluate(symbols)
        self.assertEqual(result, 1)

    def testEvaluatingSimpleAddition(self):
        symbols = [add, 1, 2]
        result = evaluate(symbols)
        self.assertEqual(result, 3)

    def testEvaluateCompoundAddition(self):
        symbols = [add, 1, add, 2, 3]
        result = evaluate(symbols)
        self.assertEqual(result, 6)

    def testEvaluateCompoundAddition2(self):
        symbols = [add, add, 1, 2, 3]
        result = evaluate(symbols)
        self.assertEqual(result, 6)

    def testEvaluateCompoundOperations(self):
        symbols = [add, 1, mul, 2, 3]
        result = evaluate(symbols)
        self.assertEqual(result, 7)

    def testEvaluateCompoundAddition2(self):
        symbols = [add, mul, 1, 2, 3]
        result = evaluate(symbols)
        self.assertEqual(result, 5)


class TestParser(unittest.TestCase):
    def testParsingSimpleAddition(self):
        result = parse(['+', '1', '2'])
        expected = [add, 1, 2]
        self.assertEqual(result, expected)

    def testParsingComplexAddition(self):
        result = parse('+ 1 + + 2 3 4'.split())
        expected = [add, 1, add, add, 2, 3, 4]
        self.assertEqual(result, expected)


class TestInterpreter(unittest.TestCase):
    def testInterpret(self):
        result = interpret('+ 1 + 2 + 3 4')
        self.assertEqual(result, 10)


class TestSolver(unittest.TestCase):
    def testSolve(self):
        ticket = '665711'
        self.assertEqual(fast_is_solvable(ticket), True)

    def testUnsolvable(self):
        ticket = '611111'
        self.assertEqual(fast_is_solvable(ticket), False)

    def testGeneratesSequences(self):
        sequences = [
            '+ 1 2', '- 1 2', 
            '* 1 2', '/ 1 2', 
            '+ 2 1', '- 2 1',
            '* 2 1', '/ 2 1'
        ]
        self.assertEqual(list(all_sequences('12')), sequences)

    def testGeneratesSequences2(self):
        self.assertEqual(len(list(all_sequences('123'))), 6*4*4)


if __name__ == '__main__':
    unittest.main()
