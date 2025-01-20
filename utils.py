import hmac
from base64 import b64encode
from datetime import datetime, timezone
from typing import Tuple

from settings import OKX_API_SECRET


def sign_request(method: str, request_path: str, body: str = "") -> Tuple[str, str]:
    timestamp = get_iso_timestamp()
    message = timestamp + method + request_path + body
    signature = hmac.new(OKX_API_SECRET.encode(), message.encode(), "SHA256").digest()
    base64_signature = b64encode(signature).decode()

    return timestamp, base64_signature


def get_iso_timestamp() -> str:
    utc_timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds")

    utc_timestamp = utc_timestamp.replace("+00:00", "Z")

    return utc_timestamp
