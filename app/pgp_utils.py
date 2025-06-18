import pgpy

def load_key(key_str: str):
    key, _ = pgpy.PGPKey.from_blob(key_str)
    return key 

def sign_message(privkey_str: str, passphrase: str, message: str):
    privkey = load_key(privkey_str)
    pgp_message = pgpy.PGPMessage.new(message)
    if privkey.is_protected:
        with privkey.unlock(passphrase):
            signature = privkey.sign(pgp_message)
    else:
        signature = privkey.sign(pgp_message)
    pgp_message |= signature  # Embed the signature inside the message
    return str(pgp_message)

def encrypt_message(pubkey_str: str, message: str, signed=False, privkey_str=None, passphrase=None):
    pubkey = load_key(pubkey_str)
    
    if signed and privkey_str:
        message = sign_message(privkey_str, passphrase, message)
        msg = pgpy.PGPMessage.from_blob(message)
    else:
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
    return decrypted  # Return the full object so you can verify signature

def verify_signature(pubkey_str: str, decrypted_msg):
    pubkey = load_key(pubkey_str)
    verified = pubkey.verify(decrypted_msg)
    return verified
