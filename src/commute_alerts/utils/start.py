from dotenv import load_dotenv
import os
from pathlib import Path

def load_env():
    """Load environment variables from a .env file."""

    # Find .env relative to this script, up two levels to project root
    env_path = os.path.join(Path(__file__).parent.parent.parent.parent, '.env')
    load_dotenv(dotenv_path=str(env_path))
