import os
import yaml


class PathConfig:
    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        self.paths = self.config.get("paths", {})

    def get_path(self, key):
        """Get path by key"""
        return self.paths.get(key, "")

    def ensure_directories(self):
        """Create all required directories"""
        for key, path in self.paths.items():
            os.makedirs(path, exist_ok=True)


# Global instance
path_config = PathConfig()


# Shortcut variables (optional)
RAW_DATA_PATH = path_config.get_path("raw_data")
PROCESSED_DATA_PATH = path_config.get_path("processed_data")
EXTRACTED_DATA_PATH = path_config.get_path("extracted_data")
LOG_PATH = path_config.get_path("logs")


if __name__ == "__main__":
    path_config.ensure_directories()
    print("Directories created successfully ✅")