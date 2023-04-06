
import pytest
from fastapi.testclient import TestClient
from .main import (
    podcast_transcription_summarization_app,
    InputPodcastUrl,
    OutputTranscriptSummaryAudio
)
