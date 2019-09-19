# test function
from SM1 import *

def test_is_word_guessed():
	assert is_word_guessed("person", "person") == True
	assert is_word_guessed("circle", "square") == False
	assert is_word_guessed("positive", "positive") == True
	assert is_word_guessed("two", "two") == True

def test_get_guessed_word():
	assert get_guessed_word("dog", ["d","g"]) == ["d","_","g"], "works!"
	assert get_guessed_word("frog", ["f","r","g"]) == ["f","r","_","g"], "works!"
	assert get_guessed_word("pear", ["p","e","a"]) == ["p","e","a","_"], "works!"
	assert get_guessed_word("stop", ["s","o","p"]) == ["s","_","o","p"], "works!"

def test_letter_in_word():
	assert letter_in_word("r", "rendition") == True
	assert letter_in_word("g", "geography") == True
	assert letter_in_word("p", "river") == False
	assert letter_in_word("n", "banana") == True
