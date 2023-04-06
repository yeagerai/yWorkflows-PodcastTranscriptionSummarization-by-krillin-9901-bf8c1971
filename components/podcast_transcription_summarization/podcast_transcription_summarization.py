
import typing
from typing import Any
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from core.workflows.abstract_workflow import AbstractWorkflow

class InputPodcastUrl(BaseModel):
    url: str

class OutputTranscriptSummaryAudio(BaseModel):
    transcript: str
    summary: str
    audio_file_path: str

class PodcastTranscriptionSummarization(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: InputPodcastUrl, callbacks: typing.Any
    ) -> OutputTranscriptSummaryAudio:
        results_dict = await super().transform(args=args, callbacks=callbacks)

        transcript = results_dict[2].transcript
        summary = results_dict[3].summary
        audio_file_path = results_dict[4].audio_file_path

        out = OutputTranscriptSummaryAudio(
            transcript=transcript,
            summary=summary,
            audio_file_path=audio_file_path,
        )
        return out

load_dotenv()
podcast_transcription_summarization_app = FastAPI()

@podcast_transcription_summarization_app.post("/transform/")
async def transform(
    args: InputPodcastUrl,
) -> OutputTranscriptSummaryAudio:
    podcast_transcription_summarization = PodcastTranscriptionSummarization()
    return await podcast_transcription_summarization.transform(args, callbacks=None)
