import lingcite.gramcite
import pytest


@pytest.mark.parametrize('input,output', [
    # each element of this list will provide values for the
    # topics "value_A" and "value_B" of the test and will
    # generate a stand-alone test case.
    ('Hahn, Ferdinand. (1901) A Primer of the Asur Dukmā, A dialect of the Kolarian Language.  Journal of the Asiatic Society of Bengal 69(1). 149-172.',
     """@article{00,
    author = {Hahn, Ferdinand},
    title = {A Primer of the Asur Dukmā},
    journal = {A dialect of the Kolarian Language. Journal of the Asiatic Society of Bengal},
    volume = {69},
    number = {1},
    pages = {149-172},
    year = {1901}
}
"""),
    ("Hǎi, Feng. (2003) Zhōngyà Dōnggānyǔ yánjiū 中亚东干语言研究 [A study of Dungan]. Urumchi: Xīnjiāng dàxué.",
     """@book{00,
    author = {Hǎi, Feng},
    title = {Zhōngyà Dōnggānyǔ yánjiū 中亚东干语言研究},
    publisher = {Urumchi: Xīnjiāng dàxué},
    year = {2003},
    title_english = {A study of Dungan}
}
"""),
])


def test_functional(input, output):
    assert lingcite.gramcite.bibtex(input) == output
