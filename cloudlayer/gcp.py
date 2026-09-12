import subprocess
from cloudlayer.base import CloudAdapter


class GcpAdapter(CloudAdapter):
    def upload(self, local_path: str, key: str) -> str:
        raise NotImplementedError("TODO Lab 1: blob.upload_from_filename, return the gs:// URI")

    def download(self, uri: str, local_path: str) -> None:
        raise NotImplementedError("TODO Lab 1: blob.download_to_filename, creating parents")

    def push_image(self, local_tag: str) -> str:
        # 1. ดึง registry จาก self.cfg
        registry = getattr(self.cfg, "container_registry", getattr(self.cfg, "registry", ""))
        remote_tag = f"{registry}/{local_tag}"

        # 2. Tag Image
        subprocess.run(["docker", "tag", local_tag, remote_tag], check=True)

        # 3. Authenticate Docker กับ GCP
        hostname = remote_tag.split("/")[0]
        subprocess.run(["gcloud", "auth", "configure-docker", hostname, "--quiet"], check=True)

        # 4. Push Image ขึ้น Cloud Registry
        subprocess.run(["docker", "push", remote_tag], check=True)

        # 5. ดึง digest sha256 และส่งค่ากลับ
        result = subprocess.run(
            ["docker", "inspect", "--format={{index .RepoDigests 0}}", remote_tag],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
