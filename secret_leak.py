import os


def get_aws_secret_key():
    return os.environ.get("AWS_SECRET_KEY")


def mask_secret(secret):
    if not secret:
        return "missing"

    visible_prefix = secret[:4]
    return f"{visible_prefix}***"


def connect():
    secret_key = get_aws_secret_key()
    masked_secret = mask_secret(secret_key)
    print(f"Connecting with key: {masked_secret}")
