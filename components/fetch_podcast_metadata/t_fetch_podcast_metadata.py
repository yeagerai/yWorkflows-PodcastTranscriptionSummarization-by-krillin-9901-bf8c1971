
import pytest
from pydantic import ValidationError
from typing import Dict
from fetch_podcast_metadata import FetchPodcastMetadata, InputPodcastUrl, MetadataOutputDict

# Test cases with mocked input and expected output data
test_cases = [
    (
        "https://www.example.com/podcasts/12345",
        {"title": "Test Podcast", "description": "A test podcast for unit testing"},
    ),
    (
        "https://www.example.com/podcasts/67890",
        {"title": "Another Test Podcast", "description": "Another test podcast for unit testing"},
    ),
]

# Test cases for invalid inputs
invalid_inputs = [
    "https://www.example.com/podcasts/",
    "https://www.example.com/podcasts",
    "https://www.example.com/posts/12345",
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_url, expected_output", test_cases)
def test_fetch_podcast_metadata(input_url: str, expected_output: Dict[str, str], monkeypatch):
    # Mocking requests.get
    def mock_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        json_response = {
            "title": expected_output["title"],
            "description": expected_output["description"],
        }

        return MockResponse(json_response, 200)

    monkeypatch.setattr("requests.get", mock_requests_get)

    component_input = InputPodcastUrl(url=input_url)
    fetch_podcast_metadata = FetchPodcastMetadata()
    output = fetch_podcast_metadata.transform(component_input)

    assert output.metadata == expected_output

@pytest.mark.parametrize("invalid_input", invalid_inputs)
def test_invalid_input(invalid_input: str):
    with pytest.raises(ValidationError):
        InputPodcastUrl(url=invalid_input)
