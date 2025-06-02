import pgpy

def load_key(key_str: str):
    key, _ = pgpy.PGPKey.from_blob(key_str)
    return key 

def encrypt_message(pubkey_str: str, message: str):
    pubkey = load_key(pubkey_str)
    msg = pgpy.PGPMessage.new(message)
    encrypted = pubkey.encrypt(msg)
    return str(encrypted)

def decrypt_message(privkey_str: str, passphrase: str, encrypted_str: str):
    privkey = load_key(privkey_str)
    if privkey.is_protected:
        try:
            with privkey.unlock(passphrase):
                message = pgpy.PGPMessage.from_blob(encrypted_str)
                decrypted = privkey.decrypt(message)
        except Exception as e:
            raise Exception(f"Failed to Unlock Key: {e}")
    else:
        message = pgpy.PGPMessage.from_blob(encrypted_str)
        decrypted = privkey.decrypt(message)
    return str(decrypted.message)