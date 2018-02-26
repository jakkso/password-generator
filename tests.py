from os import listdir, path, remove
import unittest

import classes
import functions

PASSWORD_LENGTH = 2
TEST_DICT = 'test_dict'


class BaseUnitTest(unittest.TestCase):

    def assertTypeEqual(self, obj1, obj2, msg=None):
        self.assertEqual(type(obj1), type(obj2), msg)


class TestPasswordGen(BaseUnitTest):

    def setUp(self):
        pass

    def tearDown(self):
        if TEST_DICT in listdir(path.dirname(path.abspath(__file__))):
            remove(TEST_DICT)

    def test_pickle_dict(self):
        functions.create_dict('test_dict')
        files = listdir(path.dirname(path.abspath(__file__)))
        self.assertIn('test_dict', files)

    def test_load_words(self):
        pw = classes.Password(PASSWORD_LENGTH)
        words = pw.get_words()
        word1, word2, word3 = 'aa', 'aegilops', 'endostracal'
        self.assertEqual(word1, words[1])
        self.assertEqual(word2, words[4808])
        self.assertEqual(word3, words[99999])

    def test_magic_methods(self):
        pw = classes.Password(PASSWORD_LENGTH)
        self.assertEqual(pw.__str__(), 'Password object created with 2 words')
        self.assertEqual(pw.__len__(), PASSWORD_LENGTH)
        self.assertEqual(pw.__repr__(), 'Password(2)')
        
    def test_getter_setter(self):
        pw = classes.Password(PASSWORD_LENGTH)
        self.assertEqual(pw.get_num_words(), PASSWORD_LENGTH)
        pw.set_num_words(3)
        self.assertEqual(pw.get_num_words(), 3)

    def test_password(self):
        pw = classes.Password(PASSWORD_LENGTH).password
        self.assertTypeEqual(pw, '')
        self.assertEqual(PASSWORD_LENGTH, len(pw.split(' ')))


if __name__ == '__main__':
    unittest.main()
