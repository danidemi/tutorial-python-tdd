import unittest
import sys
import warnings
import inspect

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Executed once before all tests
        pass

    def setUp(self):
        # Executed once before each test
        self.names = ["Paolo", "Simona", "Roberta"]

    def tearDown(self):
        # Executed once after each test
        self.names = None

    @classmethod
    def tearDownClass(cls):
        # Executed once after all tests
        pass

    def test_skipped(self):
        if( sys.platform == "win32" ):
            self.skipTest("Not supposed to run on win32")
        self.assertEqual("a", "a")

    def test_asserts(self):

        self.assertEqual([1,2,3], [1,2,3])
        self.assertNotEqual("a", "b")

        self.assertIs(3, 3)
        self.assertIsNot([], [])

        self.assertTrue( 3<9 )
        self.assertFalse( not True )

        self.assertIsNone( None )
        self.assertIsNotNone( [] )

        self.assertIn( 4, [1,2,3,4] )
        self.assertIn( 512, [2**i for i in range(1,10)] )
        self.assertNotIn( 4, [1,2,3] )
        self.assertNotIn( 513, [2**i for i in range(1,10)] )

        #self.assertIsInstance( File(), File )

    def test_file(self):

        with self.assertRaises(FileNotFoundError):
            file = open("does-not-exist", "r")
            file.read(100)

        with self.assertRaises(FileNotFoundError) as cm:
            file = open("does-not-exist", "r")
            file.read(100)
        self.assertEqual(str(cm.exception), "[Errno 2] No such file or directory: 'does-not-exist'")

        with self.assertRaisesRegex(FileNotFoundError, ".+No such file or directory:.+"):
            file = open("does-not-exist", "r")
            file.read(100)

    def test_warns(self):

        with self.assertWarns(Warning):
            MyClass().methodThatRaiseAWarning()

        with self.assertWarns(Warning) as ctx:
            MyClass().methodThatRaiseAWarning()
        self.assertRegex( str(ctx.warning), ".+warning.+MyClass" )

    def test_other_asserts(self):

        self.assertAlmostEqual( 10.0/3.0, 3.33, delta=0.1)
        self.assertGreater(4, 3)
        self.assertLess(3, 4)
        self.assertCountEqual( range(3,6), [3, 4, 5] )


class MyClass():
    def methodThatRaiseAWarning(self):
        warnings.warn( "A warning from MyClass", Warning )

if __name__ == '__main__':
    unittest.main()
