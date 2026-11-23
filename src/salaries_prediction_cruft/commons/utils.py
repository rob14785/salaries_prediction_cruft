def normalize_project_name(name: str) -> str:
    """Return a project name suitable for use as a Python package name."""
    return name.strip().lower().replace("-", "_").replace(" ", "_")