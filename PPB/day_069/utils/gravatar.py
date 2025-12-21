import hashlib
from urllib.parse import urlencode


def gravatar_url(email: str, size: int = 100, default: str = "identicon", rating: str = "g") -> str:
    email_clean = (email or "").strip().lower().encode("utf-8")
    email_hash = hashlib.md5(email_clean).hexdigest()
    params = urlencode({"s": str(size), "d": default, "r": rating})
    return f"https://www.gravatar.com/avatar/{email_hash}?{params}"
