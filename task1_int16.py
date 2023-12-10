from typing import List
import unittest


def title(string_: str) -> str:
    char_array: List[str] = list(string_)
    
    is_first_char: bool = False
    
    ind: int = 0
    
    while(ind < len(char_array)):
        if char_array[ind].isalpha() and is_first_char == False:
            
            char_array[ind] = char_array[ind].upper()
            is_first_char = True

        elif not(char_array[ind].isalpha()):
            is_first_char = False
        
        ind += 1

    return ''.join(char_array)

class TestTitleFunction(unittest.TestCase):
    
    def test_single_word(self):
        self.assertEqual(title("hello"), "Hello")

    def test_multiple_words(self):
        self.assertEqual(title("this is a test"), "This Is A Test")

    def test_empty_string(self):
        self.assertEqual(title(""), "")

    def test_all_uppercase(self):
        self.assertEqual(title("ALL CAPS"), "All Caps")

    def test_mixed_cases(self):
        self.assertEqual(title("tHIs iS A MiXed cASe sTrIng"), "This Is A Mixed Case String")

    def test_special_characters(self):
        self.assertEqual(title("@test #123"), "@Test #123")

if __name__ == '__main__':
    unittest.main()
