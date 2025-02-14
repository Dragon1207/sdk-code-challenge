import logging
from service.post_service import PostService

logging.basicConfig(level=logging.INFO, format="%(message)s")


class PostApp:
    def __init__(self) -> None:
        self.service = PostService()
        self.post_id = 1

    def run(self) -> None:
        # Fetch and store all posts, then fetch a single post by ID.
        self.fetch_and_store()
        self.fetch_and_store(self.post_id)
        self.create_and_store_new_post()
        self.retrieve_stored_post()
        self.update_and_delete_stored_post()
        self.list_all_stored_posts()

    def fetch_and_store(self, post_id: int = None) -> None:
        if post_id is None:
            logging.info("Fetching and storing all posts...")
            posts = self.service.fetch_and_store()
            logging.info("Stored {} posts.\n".format(len(posts)))
        else:
            logging.info("Fetching and storing post with ID {}...".format(post_id))
            post = self.service.fetch_and_store(post_id)
            logging.info("Stored post: {}\n".format(post))

    def create_and_store_new_post(self) -> None:
        logging.info("Creating and storing a new post...")
        new_post = self.service.create_and_store_post(
            {"title": "Foo", "body": "Bar", "userId": 1}
        )
        logging.info("Created post: {}\n".format(new_post))

    def retrieve_stored_post(self) -> None:
        logging.info("Retrieving stored post with ID {}...".format(self.post_id))
        post = self.service.get_stored_post(self.post_id)
        logging.info("Retrieved post: {}\n".format(post))

    def update_and_delete_stored_post(self) -> None:
        logging.info("Updating stored post with ID {}...".format(self.post_id))
        if self.service.update_stored_post(self.post_id, {"title": "Updated Title"}):
            post = self.service.get_stored_post(self.post_id)
            logging.info("Updated post: {}\n".format(post))
        else:
            logging.info("Update failed.\n")
        logging.info("Deleting stored post with ID {}...".format(self.post_id))
        if self.service.delete_stored_post(self.post_id):
            logging.info("Post deleted successfully.\n")
        else:
            logging.info("Delete failed.\n")

    def list_all_stored_posts(self) -> None:
        stored_posts = self.service.list_stored_posts()
        logging.info("Listing all stored posts...")
        logging.info("Total stored posts: {}".format(len(stored_posts)))


def main() -> None:
    app = PostApp()
    app.run()


if __name__ == "__main__":
    main()
