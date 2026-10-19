import pytest

from collector import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()

    return collector