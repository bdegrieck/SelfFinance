import os
import base64
import hashlib


def hash_password(password: str) -> str:
    """Hash ``password`` using PBKDF2 with SHA-256."""
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    return base64.b64encode(salt + hashed).decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """Return ``True`` if ``password`` matches ``hashed_password``."""
    decoded = base64.b64decode(hashed_password.encode("utf-8"))
    salt, stored_hash = decoded[:16], decoded[16:]
    new_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    return hashlib.compare_digest(new_hash, stored_hash)
