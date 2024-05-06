import logging

import pytest

@pytest.mark.healthcheck
def test_healthcheck():
    logging.debug("Hello world!!!")
    assert True