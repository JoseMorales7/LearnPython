from nose.tools import *
from ex48and49.parser import * 
from ex48and49.parser import ParserError

def test_subject():
    x = parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(x.subject, 'player')
    
    y = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert_equal(y.subject, 'bear')
    
    z = parse_sentence([('noun', 'eat'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert_raises(ParseError("doesnt"), "doesnt"  )
    
def test_verb():
    x = parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(x.verb, 'run')

    y = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert_equal(y.verb, 'eat')
    
def test_object():
    x = parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(x.object, 'north')
    
    y = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert_equal(y.object, 'honey')