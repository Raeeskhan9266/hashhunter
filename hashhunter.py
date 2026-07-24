import hashlib

print("HashHunter - Hash Identifier & Dictionary Cracker")

user_hash = input("Enter the hash to identify/crack: ").strip()

length = len(user_hash)

print(f"\nHash length: {length} characters")

if length == 32:
    hash_type = "md5"
    print("Likely type: MD5")
elif length == 40:
    hash_type = "sha1"
    print("Likely type: SHA-1")
elif length == 64:
    hash_type = "sha256"
    print("Likely type: SHA-256")
elif length == 128:
    hash_type = "sha512"
    print("Likely type: SHA-512")
else:
    hash_type = None
    print("Unknown hash type (length doesn't match common algorithms)")

if hash_type:
    words = None
    while words is None:
        wordlist_file = input("\nEnter wordlist filename to attempt cracking (e.g. passwords.txt): ")
        try:
            with open(wordlist_file, "r") as f:
                words = f.read().splitlines()
        except FileNotFoundError:
            print(f"[ERROR] File '{wordlist_file}' not found. Please check the filename and try again.")

    print(f"\nLoaded {len(words)} passwords. Attempting to crack...\n")

    found = False

    for word in words:
        word_bytes = word.encode()

        if hash_type == "md5":
            computed_hash = hashlib.md5(word_bytes).hexdigest()
        elif hash_type == "sha1":
            computed_hash = hashlib.sha1(word_bytes).hexdigest()
        elif hash_type == "sha256":
            computed_hash = hashlib.sha256(word_bytes).hexdigest()
        elif hash_type == "sha512":
            computed_hash = hashlib.sha512(word_bytes).hexdigest()

        print(f"Trying: {word} -> {computed_hash}")

        if computed_hash == user_hash:
            print(f"\n[CRACKED] The password is: {word}")
            found = True
            break

    if not found:
        print("\nNo match found in the provided wordlist.")
