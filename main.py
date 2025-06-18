import streamlit as st 
from app import pgp_utils

st.set_page_config(page_title="🔐 PGP Tool", layout="centered")
st.title("🔐 StreamPGP")
st.subheader("Self-Hosted Web PGP Tool")

mode = st.radio("Choose Mode:", ["Encrypt", "Decrypt"])

if mode == "Encrypt":
    pubkey = st.text_area("Recipients Public Key")
    message = st.text_area("Message to Encrypt")

    sign = st.checkbox("✍️ Sign this message before encrypting?")
    
    privkey = ""
    passphrase = ""
    if sign:
        privkey = st.text_area("🔐 Your Private Key (for signing)")
        passphrase = st.text_input("🔑 Passphrase (if any)", type="password")

    if st.button("🔒 Encrypt"):
        if pubkey and message:
            try:
                encrypted = pgp_utils.encrypt_message(
                    pubkey_str=pubkey,
                    message=message,
                    signed=sign,
                    privkey_str=privkey if sign else None,
                    passphrase=passphrase if sign else None
                )
                st.text_area("📦 Encrypted Message", encrypted, height=300)
            except Exception as e:
                st.error(f"⚠️ Encryption Failed: {e}")
        else:
            st.warning("Please provide the public key and message.")
else:
    privkey = st.text_area("🔐 Your Private Key")
    passphrase = st.text_input("🔑 Passphrase (if any)", type="password")
    encrypted_msg = st.text_area("📦 Encrypted Message")
    sender_pubkey = st.text_area("📤 Sender's Public Key (for signature verification)")

    if st.button("📬 Decrypt"):
        if privkey and encrypted_msg:
            try:
                decrypted_obj = pgp_utils.decrypt_message(privkey, passphrase, encrypted_msg)
                st.text_area("✉️ Decrypted Message", decrypted_obj.message, height=300)

                if sender_pubkey:
                    try:
                        verified = pgp_utils.verify_signature(sender_pubkey, decrypted_obj)
                        if verified:
                            st.success("✔️ Signature is VALID and matches sender.")
                        else:
                            st.error("❌ Signature is INVALID or message tampered.")
                    except Exception as e:
                        st.warning(f"⚠️ Could not verify signature: {e}")
                else:
                    st.info("ℹ️ No sender public key provided, skipping verification.")
            except Exception as e:
                st.error(f"❌ Failed to decrypt message: {e}")
        else:
            st.warning("Please provide your private key and an encrypted message.")


                
