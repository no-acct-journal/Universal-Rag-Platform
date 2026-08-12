"""No-op permission checker implementation.

This implementation does not perform permission checks and allows all access.
Suitable for:
- Development environments
- Trusted internal environments
- Enterprise deployments that enforce permissions at the gateway layer
"""
from __future__ import annotations

from typing import Any


class NoOpPermissionChecker:
    """No-op permission checker that allows all access.
    
    This is the default permission checker. It does not evaluate permissions,
    so all documents are accessible to all users.
    """
    
    def can_access_document(
        self,
        document: dict[str, Any],
        user_context: dict[str, Any] | None,
    ) -> bool:
        """Always return True to allow access to every document."""
        return True
    
    def filter_documents(
        self,
        documents: list[dict[str, Any]],
        user_context: dict[str, Any] | None,
    ) -> list[dict[str, Any]]:
        """Return all documents without filtering."""
        return documents
