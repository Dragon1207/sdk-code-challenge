import requests
from typing import Any, Dict, List

BASE_URL = "https://jsonplaceholder.typicode.com"  # moved to module level


class JSONPlaceholderClient:
    """Client for interacting with JSONPlaceholder API."""

    def get_posts(self) -> List[Dict[str, Any]]:
        """Fetch all posts."""
        response = requests.get(f"{BASE_URL}/posts")
        response.raise_for_status()
        return response.json()

    def get_post(self, post_id: int) -> Dict[str, Any]:
        """Fetch a single post by ID."""
        response = requests.get(f"{BASE_URL}/posts/{post_id}")
        response.raise_for_status()
        return response.json()

    def create_post(self, post_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new post."""
        response = requests.post(f"{BASE_URL}/posts", json=post_data)
        response.raise_for_status()
        return response.json()
