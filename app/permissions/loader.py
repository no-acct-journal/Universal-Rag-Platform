"""Permission checker loader.

Dynamically loads a permission checker instance from configuration.
"""
from __future__ import annotations

import importlib
import logging
from typing import Any

from app.core.config import get_settings

logger = logging.getLogger(__name__)

# Global singleton.
_checker_instance: Any = None


def load_permission_checker() -> Any:
    """Load the permission checker instance.
    
    Loads the checker based on PERMISSION_MODE:
    - none: uses NoOpPermissionChecker with no permission checks
    - plugin: uses the configured plugin class
    
    Returns:
        Permission checker instance.
    """
    global _checker_instance
    
    if _checker_instance is not None:
        return _checker_instance
    
    settings = get_settings()
    
    if settings.permission_mode == "none":
        from app.permissions.noop import NoOpPermissionChecker
        _checker_instance = NoOpPermissionChecker()
        logger.info("Loaded NoOpPermissionChecker (permission_mode=none)")
    elif settings.permission_mode == "plugin":
        plugin_path = settings.permission_plugin
        try:
            module_path, class_name = plugin_path.rsplit(".", 1)
            module = importlib.import_module(module_path)
            checker_class = getattr(module, class_name)
            _checker_instance = checker_class()
            logger.info(f"Loaded permission checker: {plugin_path}")
        except Exception as e:
            logger.error(f"Failed to load permission checker {plugin_path}: {e}")
            raise ValueError(f"Failed to load permission checker: {plugin_path}") from e
    else:
        raise ValueError(f"Unknown permission_mode: {settings.permission_mode}")
    
    return _checker_instance


def reset_permission_checker() -> None:
    """Reset the permission checker instance.
    
    Used by tests or when reloading configuration.
    """
    global _checker_instance
    _checker_instance = None
