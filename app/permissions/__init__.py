"""Permissions package.

This package provides permission checking support with plugin-based extension.

Usage:
1. Default mode (no permission checks):
   - Set PERMISSION_MODE=none
   - The system uses NoOpPermissionChecker and skips permission checks

2. Plugin mode (custom enterprise permissions):
   - Set PERMISSION_MODE=plugin
   - Set PERMISSION_PLUGIN=your.module.YourChecker
   - Implement the PermissionChecker interface

Interfaces:
- PermissionChecker: permission checker interface defined in app.core.permission
- NoOpPermissionChecker: no-op permission checker implementation
- load_permission_checker: loads a permission checker instance
"""

from app.core.permission import PermissionChecker
from app.permissions.noop import NoOpPermissionChecker
from app.permissions.loader import load_permission_checker, reset_permission_checker

__all__ = [
    "PermissionChecker",
    "NoOpPermissionChecker",
    "load_permission_checker",
    "reset_permission_checker",
]
