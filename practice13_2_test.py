import practice13_2

def test_street_initialization():
    # Setup
    expected_name = 'ABC'
    expected_type = 'TYPE'
    expected_direction = 'DIRECTION'

    # Invoke
    result = practice13_2.Street(expected_name, expected_direction, expected_type)

    # Analysis
    assert expected_name == result.get_name()
    assert expected_type in result.get_types()
    assert expected_direction == result.get_direction()

def test_street_types():
    # Setup
    first_type = 'FIRST'
    second_type = 'SECOND'
    street = practice13_2.Street('ABC', 'DIRECTION', first_type)

    # Invoke
    street.add_type(second_type)

    assert len(street.get_types()) == 2
    assert first_type in street.get_types()
    assert second_type in street.get_types()

def test_street_inquiry():
    # Setup
    street_1 = practice13_2.Street('ABC', 'DIRECTION', 'DR')
    street_2 = practice13_2.Street('DFG', 'DIRECTION_2', 'LN')

    # Invoke
    streets = practice13_2.Streets()
    streets.add_street(street_1)
    streets.add_street(street_2)
    result = streets.inquire_street('ABC', 'DR')
    fail_result = streets.inquire_street('DFG', 'CT')


    # Analysis
    assert result == True
    assert fail_result == False


def test_streets_street_types():
    # Setup
    street_1 = practice13_2.Street('ABC', 'DIRECTION', 'DR')
    street_2 = practice13_2.Street('DFG', 'DIRECTION_2', 'LN')
    street_1.add_type('CT')

    # Invoke
    streets = practice13_2.Streets()
    streets.add_street(street_1)
    streets.add_street(street_2)

    # Analysis
    assert len(streets.get_street_types('ABC')) == 2
    assert len(streets.get_street_types('DFG')) == 1