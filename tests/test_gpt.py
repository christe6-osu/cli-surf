"""
QA tests for gpt.py
Make sure pytest is installed: pip install pytest
Run pytest: pytest
"""

from unittest.mock import Mock

from src import gpt


def test_simple_gpt(mocker):
    """
    Testing the simple_gpt function
    Calls the simple gpt and asks it to output
    the days of the week. If the output does not contain
    any day of the week, we assume the gpt is non-fucntional
    """

    mock_response = Mock(
        return_value="here are the days of the week in english:\n\n"
        "- monday\n- tuesday\n- wednesday\n- thursday\n"
        "- friday\n - saturday\n- sunday\n\n"
        "as an ai, i don't have personal preferences, but many people"
        "enjoy saturday or sunday because they are typically days off "
        "from work or school! what's your favorite day?"
    )

    mock_request = mocker.patch(
        "client.chat.completions.create",
        return_value=mock_response.return_value,
    )

    surf_summary = ""
    gpt_prompt = """Please output the days of the week in English. What day
        is your favorite?"""

    gpt_response = gpt.simple_gpt(surf_summary, gpt_prompt).lower()
    expected_response = set([
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday" "saturday",
        "sunday",
        "一",
        "二",
        "三",
        "四",
        "五",
    ])

    # Can case the "gpt_response" string into a list, and
    # check for set intersection with the expected response set
    gpt_response_set = set(gpt_response.split())

    assert gpt_response_set.intersection(
        expected_response
    ), f"Expected '{expected_response}', but got: {gpt_response}"

    mock_request.assert_called_once()
