import hashlib
import hmac
def generate_hash(message):
    """Generate the SHA-256 hash of a message."""
    return hashlib.sha256(message.encode("utf-8")).hexdigest()


def verify_integrity(message, original_hash):
    """Check whether a message matches its original hash."""
    current_hash = generate_hash(message)
    return hmac.compare_digest(current_hash, original_hash)

print("===== MESSAGE INTEGRITY USING SHA-256 =====")

# Sender creates a message and its hash
message = input("\nEnter the original message: ")
original_hash = generate_hash(message)

print("\n--- Sender Side ---")
print("Original Message:", message)
print("Generated SHA-256 Hash:", original_hash)

# Receiver verifies the received message
received_message = input("\nEnter the received message: ")

print("\n--- Receiver Side ---")
print("Received Message:", received_message)

if verify_integrity(received_message, original_hash):
    print("Integrity Status: VERIFIED")
    print("The message has not been modified.")
else:
    print("Integrity Status: FAILED")
    print("The message has been modified.")
