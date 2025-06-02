import streamlit as st 
from app import pgp_utils

st.set_page_config(page_title="🔐 StreamPGP – Self-Hosted Web PGP Tool", layout="centered")
st.title(" PGP Encryption/Decryption Tool")

mode = st.radio("Choose Mode:", ["Encrypt", "Decrypt"])

if mode == "Encrypt":
    pubkey = st.text_area("Recipients Public Key")
    message = st.text_area("Message to Encrypt")
    
    if st.button("Encrypyt"):
        if pubkey and message:
            try:
                encrypted = pgp_utils.encrypt_message(pubkey, message)
                st.text_area("Encrypted Message", encrypted, height=300)
            except Exception as e:
                st.error(f"Encryption Failed: {e}")
else:
    privkey = st.text_area("Your Private Key")
    passphrase = st.text_input("Please enter your Passphrase (if any)", type="password", value="")
    encrypted_msg =st.text_area("Encrypted Message")
    if st.button("Decrypt"):
        if privkey and encrypted_msg:
            try:
                decrypted = pgp_utils.decrypt_message(privkey, passphrase, encrypted_msg)
                st.text_area("Decrypted Message", decrypted, height=300)
            except Exception as e:
                st.error(f"Failed to decrypt message: {e}")
                