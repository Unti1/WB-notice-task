import pytest
from tools.parser import WBParser

# Обратите внимание на добавление квадратных скобок, чтобы создать список кортежей для parametrize
@pytest.mark.parametrize("arg1, arg2, expected", [
    (
        "arg1", "arg2", "expected",
        ),
    ]
)
async def test_salaries_aggregator(dt_from, dt_upto, group_type, expected):
    result = await (dt_from, dt_upto, group_type)
    assert result == expected
