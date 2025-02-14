from typing import Any, Dict, Optional


class InMemoryStorage:
    """In-memory storage for storing API results."""

    def __init__(self) -> None:
        self._store: Dict[int, Dict[str, Any]] = {}

    def create(self, key: int, entry: Dict[str, Any]) -> None:
        """Create a new entry in the storage."""
        self._store[key] = entry

    def read(self, key: int) -> Optional[Dict[str, Any]]:
        """Read an entry from the storage."""
        return self._store.get(key)

    def update(self, key: int, entry: Dict[str, Any]) -> bool:
        """Update an existing entry in the storage."""
        existing_entry = self._store.get(key)
        if existing_entry is not None:
            existing_entry.update(entry)
            return True
        return False

    def delete(self, key: int) -> bool:
        """Delete an entry from the storage."""
        if self._store.get(key) is not None:
            self._store.pop(key)
            return True
        return False

    def list_all(self) -> Dict[int, Dict[str, Any]]:
        """List all entries in the storage."""
        return self._store.copy()
