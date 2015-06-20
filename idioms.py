import unittest

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
