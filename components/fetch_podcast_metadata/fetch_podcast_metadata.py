
import os
from typing import Dict, Optional

import requests
import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from urllib.parse import urlparse

from core.abstract_component import AbstractComponent


class InputPodcastUrl(BaseModel):
    url: str


class MetadataOutputDict(BaseModel):
    metadata: Dict[str, str]


class FetchPodcastMetadata(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.api_key: Optional[str] = os.environ.get(
            yaml_data["parameters"]["api_key"]
        )

    def transform(
        self, args: InputPodcastUrl
    ) -> MetadataOutputDict:
        print(f"Executing the transform of the {type(self).__name__} component...")

        parsed_url = urlparse(args.url)
        podcast_id = parsed_url.path.split('/')[-1]

        api_url = f"https://listen-api.listennotes.com/api/v2/podcasts/{podcast_id}"
        headers = {"X-ListenAPI-Key": self.api_key}

        response = requests.get(api_url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"API call failed with status code {response.status_code}")

        response_json = response.json()
        metadata = {
            "title": response_json["title"],
            "description": response_json["description"],
        }

        return MetadataOutputDict(metadata=metadata)


load_dotenv()
fetch_podcast_metadata_app = FastAPI()


@fetch_podcast_metadata_app.post("/transform/")
async def transform(
    args_input: InputPodcastUrl,
) -> MetadataOutputDict:
    fetch_podcast_metadata = FetchPodcastMetadata()
    return fetch_podcast_metadata.transform(args_input)

