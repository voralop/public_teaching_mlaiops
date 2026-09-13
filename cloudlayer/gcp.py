import subprocess
from google.cloud import storage

class GcpAdapter:
    def __init__(self, config):
        self.config = config

    def _get_attr(self, key: str) -> str:
        return getattr(self.config, key.lower(), getattr(self.config, key.upper(), ""))

    def upload(self, local_path: str, remote_uri: str) -> None:
        parts = remote_uri.replace("gs://", "").split("/")
        bucket_name = parts[0]
        blob_path = "/".join(parts[1:])
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_path)
        blob.upload_from_filename(local_path)

    def download(self, remote_uri: str, local_path: str) -> None:
        parts = remote_uri.replace("gs://", "").split("/")
        bucket_name = parts[0]
        blob_path = "/".join(parts[1:])
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_path)
        blob.download_to_filename(local_path)

    def push_image(self, local_tag: str) -> None:
        registry = self._get_attr("container_registry")
        tag_suffix = local_tag.split(":")[-1] if ":" in local_tag else "latest"
        remote_tag = f"{registry}:{tag_suffix}"
        subprocess.run(["docker", "tag", local_tag, remote_tag], check=True)
        subprocess.run(["docker", "push", remote_tag], check=True)
