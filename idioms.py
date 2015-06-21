import unittest
import random

class Mean:
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        return self

    def __exit__(self, a, b, c):
        print("exit a=" + str(a) + ", b=" + str(b) + ", c=" + str(c) )
        self.message = None

    def getString(self):
        if(random.random() > 0.5):
            return self.message
        else:
            raise ArithmeticError("Mean error")


def piDigits():
    str = "3.14159265359"[2:]
    for char in str:
        yield char

class Contacts():

    names = ["Alan", "Benjamin", "Charlotte"]

    def __init__(self):
        print("init")

    def __iter__(self):
        return ContactsIterator()

class ContactsIterator():

    def __init__(self):
        self.i = 0;

    def __next__(self):

        if(self.i == len(Contacts.names)):
            raise StopIteration

        name = Contacts.names[self.i]
        self.i = self.i+1
        return name


class TestIdioms( unittest.TestCase ):

    def test_tuples(self):
        ita = tuple( ["Italy", 60E6, "+39", "EU"] )
        fra = tuple( ["France", 70E6, "+34", "EU"] )
        txs = tuple( ["Texas", 8E6, "+1", "US"] )
        self.assertEqual( ita[3], "EU" )
        self.assertEqual( ita[3], fra[3] )

    def test_mean_object(self):
        try:
            with Mean("I'm mean") as mean:
                print(mean.getString())
        except:
            pass


    def test_pi_generator(self):
        digits = []
        for d in piDigits():
            digits.append( d )

        self.assertEqual( '1', digits[0] )
        self.assertEqual( '4', digits[1] )
        self.assertEqual( '1', digits[2] )
        self.assertEqual( '5', digits[3] )


    def test_is(self):

        numberA = 5
        numberB = 5

        self.assertIs(numberA, numberB)
        self.assertEqual(numberA, numberB)

        stringA = "hello"
        stringB = "hello"

        self.assertIs(stringA, stringB)
        self.assertEqual(stringA, stringB)

        listA = [stringA, numberA]
        listB = [stringB, numberB]

        self.assertIsNot(listA, listB)
        self.assertEqual(listA, listB)

    def test_contacts_as_iterable(self):
        contacts = Contacts();

        expected = []
        for contact in contacts:
            expected.append(contact)

        self.assertEqual( "Alan", expected[0] )
        self.assertEqual( "Benjamin", expected[1] )
        self.assertEqual( "Charlotte", expected[2] )

if __name__ == '__main__':
    unittest.main()
