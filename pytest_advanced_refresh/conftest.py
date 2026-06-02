import os
import pytest
from app import SimpleDb

@pytest.fixture(scope="function")
def temp_db():
    # Setup: przygotowanie zasobów przed testem
    db_path = "test_database.txt"
    db = SimpleDb(db_path)
    
    yield db  # Przekazanie zasobów do testu

    # Teardown: sprzątanie zasobów po teście
    if os.path.exists(db_path):
        os.remove(db_path)