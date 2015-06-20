import unittest

class Contacts():

    def __init__(self):
        print("init")

    def __iter__(self):
        return ContactsIterator()

class ContactsIterator():

    names = ["Alan", "Benjamin", "Charlotte"]

    def __init__(self):
        self.i = 0;

    def __next__(self):

        if(self.i == len(ContactsIterator.names)):
            raise StopIteration

        name = ContactsIterator.names[self.i]
        self.i = self.i+1
        return name


class TestIdioms( unittest.TestCase ):

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
