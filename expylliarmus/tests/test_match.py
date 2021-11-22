from expylliarmus.match import SPELL_MATCHER

def test_SPELL_MATCHER_Pascal_Case_spell():
    assert 'Expylliarmus!' == SPELL_MATCHER.match('Expylliarmus!').group(0)
    assert 'Youpi!' == SPELL_MATCHER.match('Youpi!').group(0)
    assert 'Mischief managed!' == SPELL_MATCHER.match('Mischief managed!').group(0)
    assert 'Wingardium Leviosa!' == SPELL_MATCHER.match('Wingardium Leviosa!').group(0)

def test_SPELL_MATCHER_UPPER_CASE_spell():
    assert 'EXPELLIARMUS!' == SPELL_MATCHER.match('EXPELLIARMUS!').group(0)
    assert 'WINGARDIUM LEVIOSA!' == SPELL_MATCHER.match('WINGARDIUM LEVIOSA!').group(0)

def test_SPELL_MATCHER_do_not_match():
    assert SPELL_MATCHER.match('hello!') is None
    assert SPELL_MATCHER.match('expelliarmus') is None

# def test_SPELL_MATCHER():
#     for match in SPELL_MATCHER.finditer('“Wingardium Leviosa!” he shouted, PETRIFICUS TOTALUS!” she cried'):
#         print(match.group(1))
#     assert False
