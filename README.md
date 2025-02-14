# Code Challenge - SDK

This project is a simple Python application that uses the JSONPlaceholder API to fetch, create, update, and delete posts. It demonstrates a layered architecture with a service layer, an SDK client layer, and an in-memory storage implementation.

## Project Structure

- **main.py** - Entry point for the application.
- **requirements.txt** - Lists the project dependencies.
- **sdk/**
  - **jsonplaceholder_client.py** - Contains the [`JSONPlaceholderClient`](sdk/jsonplaceholder_client.py) class for interacting with the API.
- **service/**
  - **post_service.py** - Implements the [`PostService`](service/post_service.py) class that encapsulates business logic.
- **storage/**
  - **in_memory_storage.py** - Implements an in-memory storage solution via the [`InMemoryStorage`](storage/in_memory_storage.py) class.
- **setup.cfg** - Configuration for linting and type-checking tools.
- **README.md** - This file.

## Installation

1. Clone the repository.
2. Install the dependencies by running:

   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

Run the main application with:

```sh
python main.py
```

This will execute the `PostApp` class in main.py which performs the following actions:

- Fetches and stores posts from JSONPlaceholder.
- Creates and stores a new post.
- Retrieves, updates, and deletes a stored post.
- Lists all stored posts.

## Configuration

- The JSONPlaceholder API URL is defined in `jsonplaceholder_client.py` as `BASE_URL`.
- The application logs messages to the console using Python's `logging` module.
