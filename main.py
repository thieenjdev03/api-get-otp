from fastapi import FastAPI
import pyotp
import time
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Cấu hình CORS cho phép frontend truy cập
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cân nhắc giới hạn origin khi deploy thật
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👉 Secret key OTP (có thể thay bằng biến môi trường nếu cần)
SECRET_KEY = "PWIDU3KEQUCV56JUMIBZ7L24R2CW6LEB"

@app.get("/otp")
def get_otp():
    totp = pyotp.TOTP(SECRET_KEY)
    return {
        "otp": totp.now(),
        "valid_for_seconds": 30 - int(time.time()) % 30
    }