import json
import logging

logger = logging.getLogger(__name__)


def logger_init(response):
    print("\n" + "=" * 60)

    try:
        data = response.json()
    except Exception:
        logger.error(f"{response.status_code} -> Non-JSON response:\n{response.text}")
        print("=" * 60 + "\n")
        return

    if isinstance(data, list):
        preview = data[:3]
    else:
        preview = data

    pretty = json.dumps(preview, indent=2)

    if response.status_code >= 400:
        logger.error(f"STATUS: {response.status_code}\nBODY:\n{pretty}")
    else:
        logger.info(f"STATUS: {response.status_code}\nBODY:\n{pretty}")

    print("=" * 60 + "\n")
