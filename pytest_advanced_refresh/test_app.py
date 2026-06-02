import os
import pytest
from app import SimpleDb, get_weather_alert

# 1. Zaawansowany fixture z Yield (Teardown)
@pytest.fixture
def temp_db():
    # Setup: przygotowanie zasobów przed testem
    db_path = "test_database.txt"
    db =SimpleDb(db_path)
    
    yield db  # Przekazanie zasobów do testu

    # Teardown: sprzątanie zasobów po teście
    if os.path.exists(db_path):
        os.remove(db_path)

# 2. Parametryzacja testów
@pytest.mark.parametrize(
    "usernames, expected_count",
    [
        (["adam"], 1),
        (["adam", "ewa", "jan"], 3),
        ([], 0),
    ]
)
def test_adding_users(temp_db, usernames, expected_count):
    # Act: Dodajemy użytkowników z parametru
    for user in usernames:
        temp_db.add_user(user)
    
    # Assert: Sprawdzamy czy liczba się zgadza
    assert len(temp_db.get_users()) == expected_count

def test_weather_alert_hot(mocker):
    # Arrange: Mockowanie odpowiedzi z API
    mock_response = mocker.Mock()
    mock_response.json.return_code = 200
    mock_response.json.return_value = {"temp": 35}

    # MOCKOWANIE requests.get
    mocked_get = mocker.patch("app.requests.get", return_value=mock_response)

    # Act: Wywołanie funkcji
    result = get_weather_alert("Warszawa")

    # Assert: Sprawdzenie wyniku
    assert result == "Alarm - gorąco!"

    # Sprawdzenie czy requests.get zostało wywołane z odpowiednim URL
    mocked_get.assert_called_once_with("https://api.weather.com/v1/Warszawa")
