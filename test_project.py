import json
from project import load_paper, manage_glossary, manage_notes

def test_load_paper(tmp_path): #used tmp_path to create a temporary file for testing
    file_path = tmp_path / "sample.txt"
    file_path.write_text("It was fun doing CS50P!", encoding="utf-8")
    result = load_paper(file_path)
    assert result == "It was fun doing CS50P!"

def test_load_paper_missing_file(tmp_path):
    file_path = tmp_path / "missing.txt"
    result = load_paper(file_path)
    assert result is None

def test_load_paper_with_unicode(tmp_path): #this test checks if the function can handle unicode characters correctly or not
    file_path = tmp_path / "symbol.txt"
    expected = """Attention Is All You Need
α + β = γ
Self-attention allows parallel processing."""
    file_path.write_text(expected, encoding="utf-8")
    result = load_paper(file_path)
    assert result == expected

def test_manage_glossary(monkeypatch, tmp_path): #used monkeypatch to simulate user input and again tmp_path to create a temp file for testing
    monkeypatch.chdir(tmp_path)
    answers = iter([
        "1",
        "CS50",
        "Introduction to Python",
        "3",
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(answers)) #here we are using monkeypatch to replace the built-in input function with a lambda function 
                                                                   #that returns the next value from the answers iterator. This simulates user input for the test.
    manage_glossary()
    with open("glossary.json", "r") as file:
        glossary = json.load(file)
    assert glossary["CS50"] == "Introduction to Python"

def test_manage_glossary_duplicate(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    with open("glossary.json", "w") as file:
        json.dump({"CS50": "Introduction to computer science"}, file)
    answers = iter([
        "1",
        "CS50",
        "3",
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    manage_glossary()
    with open("glossary.json", "r") as file:
        glossary = json.load(file)
    assert glossary["CS50"] == "Introduction to computer science"

def test_manage_notes(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    answers = iter([
        "1",
        "Understand self-attention",
        "3",
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    manage_notes("hello.txt")
    with open("notes.json", "r") as file:
        notes = json.load(file)
    assert notes["hello.txt"] == ["Understand self-attention"]