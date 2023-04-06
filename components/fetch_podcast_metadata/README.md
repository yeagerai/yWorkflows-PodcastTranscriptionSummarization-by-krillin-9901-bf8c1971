markdown
# Component Name

FetchPodcastMetadata

# Description

The `FetchPodcastMetadata` component is a building block in a Yeager Workflow, designed to fetch metadata of a podcast from the Listen Notes API based on a podcast URL. It inherits from the `AbstractComponent` base class.

# Input and Output Models

- **Input Model: `InputPodcastUrl`**: The input model contains a single attribute, `url` (a `str`), which represents the URL of the podcast.

- **Output Model: `MetadataOutputDict`**: The output model contains a single attribute, `metadata` (a dictionary containing str keys and values), which represents the fetched metadata for the podcast.

## Parameters

- **configuration_path (str)**: The path to the configuration file.
- **api_key (str, optional)**: The API key required to access the Listen Notes API. Obtained from the environment variable specified in the configuration file.

# Transform Function

The `transform()` method of the `FetchPodcastMetadata` component performs the following steps:

1. Parse the input podcast URL.
2. Extract the podcast ID from the parsed URL.
3. Construct the API URL using the podcast ID.
4. Set the API headers, including the API key.
5. Make an API call to fetch podcast metadata.
6. Check for status code 200, and raise an exception otherwise.
7. Parse the API response into a metadata dictionary.
8. Return the metadata dictionary as an instance of `MetadataOutputDict`.

# External Dependencies

- **requests**: Used to make API calls to fetch podcast metadata.
- **yaml**: Used to load the component configuration from the YAML file.
- **os**, **dotenv**: Used to load and access environment variables.
- **FastAPI**, **pydantic**: Used to define input and output models as well as create an API endpoint to execute the component.
- **urllib.parse**: Used to parse the podcast URL and extract the podcast ID.

# API Calls

An API call is made to the Listen Notes API using the API URL, which includes the podcast ID, and the API headers, which include the API key.

API Endpoint: `https://listen-api.listennotes.com/api/v2/podcasts/{podcast_id}`

Purpose: To fetch the metadata of a podcast.

# Error Handling

The component checks for status code 200 in the API response. If the status code isn't 200, it raises an exception with an error message indicating that the API call failed.

# Examples

To use the `FetchPodcastMetadata` component within a Yeager Workflow, first define an environment variable containing the Listen Notes API key, and make sure it is specified in the component's YAML configuration file.

Example configuration file:

