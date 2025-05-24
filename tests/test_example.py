import pytest


def test_simple():
    """A simple test to verify pytest is working."""
    assert True


class TestBasicFunctionality:
    """Group of tests for basic functionality."""

    def test_addition(self):
        """Test simple addition."""
        assert 1 + 1 == 2

    def test_string_operations(self):
        """Test string operations."""
        text = "Generate CV"
        assert "CV" in text
        assert "CV".lower() == "cv"


@pytest.fixture
def sample_data():
    """Fixture providing sample data for testing."""
    return {
        "personal_info": {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "+1234567890",
        },
        "education": [
            {
                "institution": "University of Testing",
                "degree": "Bachelor of Science",
                "field": "Computer Science",
                "graduation_year": 2020,
            }
        ],
        "experience": [
            {
                "company": "Tech Corp",
                "position": "Software Developer",
                "start_date": "2020-01",
                "end_date": "2022-12",
                "description": "Developed various applications",
            }
        ],
    }


def test_with_fixture(sample_data):
    """Test using the sample data fixture."""
    assert "name" in sample_data["personal_info"]
    assert len(sample_data["education"]) == 1
    assert sample_data["experience"][0]["company"] == "Tech Corp"


@pytest.mark.parametrize(
    "input_value,expected",
    [
        (1, 1),
        ("test", "test"),
        ([1, 2, 3], [1, 2, 3]),
    ],
)
def test_parametrized(input_value, expected):
    """Demonstrate parameterized testing."""
    assert input_value == expected


def test_temporary_file(tmp_path):
    """Test using pytest's tmp_path fixture."""
    temp_file = tmp_path / "test.txt"
    temp_file.write_text("Test content")

    assert temp_file.exists()
    assert temp_file.read_text() == "Test content"
