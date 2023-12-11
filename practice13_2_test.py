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