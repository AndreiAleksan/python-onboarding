from src.word_counter import wlc_counter

def test_wlc_counter_full():
    total_lines, total_characters, total_words = wlc_counter("full.txt")
    assert total_lines == 4 and total_characters == 48 and total_words == 10

def test_wlc_counter_empty():
    total_lines, total_characters, total_words = wlc_counter("empty.txt")
    assert total_lines == 0 and total_characters == 0 and total_words == 0