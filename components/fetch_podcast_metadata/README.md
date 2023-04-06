
# FetchPodcastMetadata

A component that takes InputPodcastUrl as input and retrieves the podcast's metadata, such as episode title and description, using the Listen Notes API. Outputs a metadata object (dict) containing the information.

## Initial generation prompt
description: A component that takes InputPodcastUrl as input and retrieves the podcast's
  metadata, such as episode title and description, using the Listen Notes API. Outputs
  a metadata object (dict) containing the information.
name: FetchPodcastMetadata


## Transformer breakdown
- Parse the InputPodcastUrl to extract the podcast ID
- Construct the API request to the Listen Notes API with the podcast ID and the provided API key
- Send the API request and wait for the response
- Parse the response JSON to extract the podcast metadata
- Create a dictionary containing the extracted metadata
- Output the metadata dictionary

## Parameters
[{'name': 'api_key', 'default_value': 'your_listen_notes_api_key', 'description': 'The API key for the Listen Notes API.', 'type': 'str'}]

        