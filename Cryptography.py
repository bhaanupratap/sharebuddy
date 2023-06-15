from cryptography.fernet import Fernet

key = Fernet.generate_key()

msg = "sharebuddy".encode()
f_obj = Fernet(key)
encrpted_msg = f_obj.encrypt(msg)
print(encrpted_msg)
decrypted_msg = f_obj.decrypt(encrpted_msg)
print(decrypted_msg)