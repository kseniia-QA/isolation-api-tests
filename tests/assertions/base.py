from typing import Any

import allure

from tests.tools.logger import get_test_logger

# Единый логгер для всех базовых проверок.
# Это позволяет в логах быстро отследить, что падение произошло
# именно на уровне ассертов, а не в клиенте или сценарии.
logger = get_test_logger("BASE_ASSERTIONS")


@allure.step("Check that {name} equals to {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    logger.info(f'Check that "{name}" equals to {expected}')

    assert actual == expected, (
        f'Incorrect value: "{name}". ' 
        f'Expected value: {expected}. '
        f'Actual value: {actual}'
    )
