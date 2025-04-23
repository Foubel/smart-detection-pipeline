"""Script to download a dataset from Picsellia and convert to YOLO format."""

import os

from dotenv import load_dotenv
from picsellia import Client

load_dotenv()


def main():
    """Authenticate with Picsellia and download dataset in COCO and YOLO formats."""
    client = Client(api_token=os.getenv("PICSELLIA_TOKEN"))
    datasets = client.list_datasets()
    print(f"✅ Connexion Picsellia OK — {len(datasets)} dataset(s) dispo")


if __name__ == "__main__":
    main()
