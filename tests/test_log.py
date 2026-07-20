from src.log_analyzer import tokenize,top_words

def test_tokenize_spiles_words()->None:
    result= tokenize("Hello World! Hello 123")
    assert result == ['hello', 'world', 'hello']
def test_top_words()->None:
    text = "a b b c c c d d d d"
    result= top_words(text,2)
    assert result == [("d",4),("c",3)]
def test_top_words_empty()->None:
    assert top_words("")==[]