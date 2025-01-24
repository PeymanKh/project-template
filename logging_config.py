import logging.config
import yaml

# Load YAML file
with open("logging_config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Apply logging configuration
logging.config.dictConfig(config)

# Example log messages
logging.debug("This is a debug message")  # Won't appear (root level is INFO)
logging.info("This is an info message")   # Will appear in Loki
logging.error("This is an error message") # Will appear in Loki
