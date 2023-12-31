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

def test_exam_initialization():
    # Setup
    name = 'Yoel'
    total_points = 85
    total_possible_points = 100

    # Invoke
    result = practice13_2.Exam(name, total_points, total_possible_points)

    # Analysis
    assert result.get_name() == name
    assert result.get_total_points() == total_points
    assert result.get_total_possible_points() == total_possible_points

def test_exam_add_points():
    # Setup
    exam = practice13_2.Exam('Yoel', 85, 100)

    # Invoke
    exam.add_total_points(15)
    exam.add_total_possible_points(50)

    # Analysis
    assert exam.get_total_points() == 100
    assert exam.get_total_possible_points() == 150

def test_exam_ratio():
    # Setup
    exam = practice13_2.Exam('Yoel', 500, 1000)

    # Invoke
    result = exam.get_ratio()

    # Analysis
    assert result == 50

def test_exam_repr():
    # Setup
    exam = practice13_2.Exam('Yoel', 500, 1000)

    # Invoke
    result = str(exam)

    # Analysis
    assert result == "Yoel (50.0)"

def test_eq_comparison():
    # Setup
    exam_1 = practice13_2.Exam('Yoel', 200, 100)
    exam_2 = practice13_2.Exam('Yoel', 300, 400)
    exam_3 = practice13_2.Exam('Bruce', 200, 400)

    # Invoke
    result_1 = exam_1 == exam_2
    result_2 = exam_3 == exam_1

    # Analysis
    assert result_1 == True
    assert result_2 == False

def test_hash_exam():
    # Setup
    exam_1 = practice13_2.Exam('Yoel', 50, 100)
    exam_2 = practice13_2.Exam('Yoel', 50, 100)

    # Invoke
    result_1 = hash(exam_1)
    result_2 = hash(exam_2)


    # Analysis
    assert result_1 != result_2

def test_lt_comparator():
    # Setup
    exam_1 = practice13_2.Exam('B', 50, 100)
    exam_2 = practice13_2.Exam('A', 50, 100)
    exam_3 = practice13_2.Exam('C', 85, 100)

    # Result
    some_list = [exam_1, exam_2, exam_3]
    some_list.sort()

    # Analysis
    assert some_list[0] == exam_2
    assert some_list[1] == exam_1
    assert some_list[2] == exam_3





