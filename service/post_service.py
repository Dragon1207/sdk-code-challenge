from typing import Any, Dict, List, Optional, Union
from sdk.jsonplaceholder_client import JSONPlaceholderClient
from storage.in_memory_storage import InMemoryStorage

Post = Dict[str, Any]
Posts = List[Post]
APIResponse = Union[Post, Posts]


class PostService:
    """Service layer for managing posts."""

    def __init__(
        self,
        client: Optional[JSONPlaceholderClient] = None,
        storage: Optional[InMemoryStorage] = None,
    ) -> None:
        self.client = client or JSONPlaceholderClient()
        self.storage = storage or InMemoryStorage()

    def fetch_and_store(self, post_id: Optional[int] = None) -> APIResponse:
        """
        Fetch post(s) from the API and store them.
        When post_id is None, fetches all posts; otherwise fetches a single post.
        """
        if post_id is None:
            posts = self.client.get_posts()
            for post_item in posts:
                self.storage.create(post_item["id"], post_item)
            return posts
        else:
            single_post = self.client.get_post(post_id)
            self.storage.create(single_post["id"], single_post)
            return single_post

    def create_and_store_post(self, post_data: Dict[str, Any]) -> Post:
        """Create a new post via API and store the result."""
        created_post = self.client.create_post(post_data)
        self.storage.create(created_post["id"], created_post)
        return created_post

    def get_stored_post(self, post_id: int) -> Post:
        """Retrieve a post from storage."""
        post = self.storage.read(post_id)
        if not post:
            raise ValueError(f"Post with ID {post_id} not found in storage.")
        return post

    def update_stored_post(self, post_id: int, update_data: Dict[str, Any]) -> bool:
        """Update a stored post."""
        return self.storage.update(post_id, update_data)

    def delete_stored_post(self, post_id: int) -> bool:
        """Delete a stored post."""
        return self.storage.delete(post_id)

    def list_stored_posts(self) -> List[Post]:
        """List all stored posts."""
        return list(self.storage.list_all().values())
