# 🔐 StreamPGP – Self-Hosted Web PGP Tool

![Screenshot 2025-06-02 192434](https://github.com/user-attachments/assets/15d20e1d-cb8d-4354-96c2-3d0d19fbf591)

A simple web-based PGP tool built using Python + Streamlit. Encrypt and decrypt messages directly in your browser. 100% client-side, nothing stored.

## 🚀 Features
- Encrypt messages with a public key
- Decrypt messages with a private key + passphrase
- Streamlit UI for mobile & desktop
- Dockerized for easy self-hosting

## 🐳 Usage

```bash
docker build -t streampgp .
docker run -p 8501:8501 streampgp
```

Then visit ``` http://localhost:8501 ```

## 🔐 Security

All crypto operations done in memory

No key or message data is stored

Suitable for use behind a VPN or reverse proxy (traefik) for internal use only. 
