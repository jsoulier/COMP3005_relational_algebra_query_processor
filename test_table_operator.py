import unittest

from table_operator import TableOperator

class TestTableOperator(unittest.TestCase):

    def test_eq(self):
        self.assertEqual(TableOperator.SELECTION2, 'select')
        self.assertEqual(TableOperator.PROJECTION2, 'pi')
        self.assertNotEqual(TableOperator.SELECTION2, 'select2')
        self.assertNotEqual(TableOperator.PROJECTION2, '2pi')
        self.assertEqual(TableOperator.SELECTION, TableOperator.SELECTION)
        self.assertNotEqual(TableOperator.SELECTION, TableOperator.PROJECTION)
        self.assertEqual(TableOperator.SELECTION, TableOperator.SELECTION)
        self.assertEqual(TableOperator.SELECTION, TableOperator.SELECTION1)
        self.assertEqual(TableOperator.SELECTION, TableOperator.SELECTION2)
        self.assertNotEqual(TableOperator.SELECTION, TableOperator.PROJECTION)
        self.assertNotEqual(TableOperator.SELECTION, TableOperator.NONE)
        self.assertEqual(TableOperator.SELECTION1, TableOperator.SELECTION2)
        self.assertEqual(TableOperator.PROJECTION1, TableOperator.PROJECTION2)
        self.assertEqual(TableOperator.CROSS_JOIN1, TableOperator.CROSS_JOIN2)
        self.assertEqual(TableOperator.UNION1, TableOperator.UNION2)
        self.assertEqual(TableOperator.INTERSECTION1, TableOperator.INTERSECTION2)
        self.assertEqual(TableOperator.MINUS1, TableOperator.MINUS2)
        self.assertEqual(TableOperator.DIVISION1, TableOperator.DIVISION2)

    def test_bool(self):
        self.assertFalse(TableOperator.NONE)
        self.assertTrue(TableOperator.SELECTION)
        self.assertTrue(TableOperator.PROJECTION)
        self.assertTrue(TableOperator.CROSS_JOIN)
        self.assertTrue(TableOperator.NATURAL_JOIN)
        self.assertTrue(TableOperator.LEFT_OUTER_JOIN)
        self.assertTrue(TableOperator.RIGHT_OUTER_JOIN)
        self.assertTrue(TableOperator.FULL_OUTER_JOIN)
        self.assertTrue(TableOperator.UNION)
        self.assertTrue(TableOperator.INTERSECTION)
        self.assertTrue(TableOperator.MINUS)
        self.assertTrue(TableOperator.DIVISION)

    def test_bool(self):
        self.assertEqual(len(TableOperator.NONE), 0)
        self.assertEqual(len(TableOperator.SELECTION1), 1)
        self.assertEqual(len(TableOperator.SELECTION2), 6)
        self.assertEqual(len(TableOperator.PROJECTION1), 1)
        self.assertEqual(len(TableOperator.PROJECTION2), 2)
        self.assertEqual(len(TableOperator.CROSS_JOIN), 1)
        self.assertEqual(len(TableOperator.NATURAL_JOIN), 1)
        self.assertEqual(len(TableOperator.LEFT_OUTER_JOIN), 1)
        self.assertEqual(len(TableOperator.RIGHT_OUTER_JOIN), 1)
        self.assertEqual(len(TableOperator.FULL_OUTER_JOIN), 1)
        self.assertEqual(len(TableOperator.UNION), 1)
        self.assertEqual(len(TableOperator.INTERSECTION), 1)
        self.assertEqual(len(TableOperator.MINUS1), 1)
        self.assertEqual(len(TableOperator.MINUS1), 1)
        self.assertEqual(len(TableOperator.DIVISION1), 1)
        self.assertEqual(len(TableOperator.DIVISION2), 1)

    def test_left(self):
        self.assertFalse(TableOperator.NATURAL_JOIN.left())
        self.assertTrue(TableOperator.LEFT_OUTER_JOIN.left())
        self.assertFalse(TableOperator.RIGHT_OUTER_JOIN.left())
        self.assertTrue(TableOperator.FULL_OUTER_JOIN.left())

    def test_right(self):
        self.assertFalse(TableOperator.NATURAL_JOIN.right())
        self.assertFalse(TableOperator.LEFT_OUTER_JOIN.right())
        self.assertTrue(TableOperator.RIGHT_OUTER_JOIN.right())
        self.assertTrue(TableOperator.FULL_OUTER_JOIN.right())

    def test_parametrize(self):
        self.assertTrue(TableOperator.NONE.parametrize(0))
        self.assertFalse(TableOperator.NONE.parametrize(1))
        self.assertFalse(TableOperator.SELECTION.parametrize(0))
        self.assertFalse(TableOperator.SELECTION.parametrize(0))
        self.assertTrue(TableOperator.SELECTION.parametrize(2))
        self.assertFalse(TableOperator.PROJECTION.parametrize(0))
        self.assertTrue(TableOperator.PROJECTION.parametrize(1))
        self.assertTrue(TableOperator.PROJECTION.parametrize(2))
        self.assertTrue(TableOperator.CROSS_JOIN.parametrize(0))
        self.assertFalse(TableOperator.CROSS_JOIN.parametrize(1))
        self.assertFalse(TableOperator.CROSS_JOIN.parametrize(2))
        self.assertTrue(TableOperator.NATURAL_JOIN.parametrize(0))
        self.assertFalse(TableOperator.NATURAL_JOIN.parametrize(1))
        self.assertTrue(TableOperator.NATURAL_JOIN.parametrize(2))
        self.assertTrue(TableOperator.LEFT_OUTER_JOIN.parametrize(0))
        self.assertFalse(TableOperator.LEFT_OUTER_JOIN.parametrize(1))
        self.assertTrue(TableOperator.LEFT_OUTER_JOIN.parametrize(2))
        self.assertTrue(TableOperator.RIGHT_OUTER_JOIN.parametrize(0))
        self.assertFalse(TableOperator.RIGHT_OUTER_JOIN.parametrize(1))
        self.assertTrue(TableOperator.RIGHT_OUTER_JOIN.parametrize(2))
        self.assertTrue(TableOperator.FULL_OUTER_JOIN.parametrize(0))
        self.assertFalse(TableOperator.FULL_OUTER_JOIN.parametrize(1))
        self.assertTrue(TableOperator.FULL_OUTER_JOIN.parametrize(2))
        self.assertTrue(TableOperator.UNION.parametrize(0))
        self.assertFalse(TableOperator.UNION.parametrize(1))
        self.assertFalse(TableOperator.UNION.parametrize(2))
        self.assertTrue(TableOperator.INTERSECTION.parametrize(0))
        self.assertFalse(TableOperator.INTERSECTION.parametrize(1))
        self.assertFalse(TableOperator.INTERSECTION.parametrize(2))
        self.assertTrue(TableOperator.MINUS.parametrize(0))
        self.assertFalse(TableOperator.MINUS.parametrize(1))
        self.assertFalse(TableOperator.MINUS.parametrize(2))
        self.assertTrue(TableOperator.DIVISION.parametrize(0))
        self.assertFalse(TableOperator.DIVISION.parametrize(1))
        self.assertFalse(TableOperator.DIVISION.parametrize(2))
