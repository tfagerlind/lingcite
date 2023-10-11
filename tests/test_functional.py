import lingcite.gramcite

def test_answer():
    result = lingcite.gramcite.bibtex("Hahn, Ferdinand. (1901) A Primer of the Asur Dukmā, A dialect of the Kolarian Language.  Journal of the Asiatic Society of Bengal 69(1). 149-172.")
    expected_result= """@article{00,
    author = {Hahn, Ferdinand},
    title = {A Primer of the Asur Dukmā},
    journal = {A dialect of the Kolarian Language. Journal of the Asiatic Society of Bengal},
    volume = {69},
    number = {1},
    pages = {149-172},
    year = {1901}
}
"""

    assert result == expected_result


