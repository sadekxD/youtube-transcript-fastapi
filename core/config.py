import os

class Settings():
    ALLOWED_ORIGINS: list = [
        "http://localhost:3000",
        "https://testwhiz-v2-86p5.vercel.app",
        "https://testwhiz.co"
        "https://qfk4umwqdsipvt6y4taptqhgoy0ppwhy.lambda-url.us-east-2.on.aws",
    ]
    PROXY_URL: str = "sp9zdkm9bh:8gj2Ltdsp16NrDwZg_@gate.smartproxy.com:10002"

settings = Settings()