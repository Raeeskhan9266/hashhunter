# HashHunter

A Python tool that identifies common hash types by length and attempts to
crack them using a dictionary (wordlist) attack.

## What It Does

1. Takes a hash as input
2. Identifies the likely hash algorithm based on output length
   (MD5: 32 chars, SHA-1: 40 chars, SHA-256: 64 chars, SHA-512: 128 chars)
3. Hashes each word in a provided wordlist using the identified algorithm
4. Compares each computed hash against the target hash to find a match

## Why I Built This

To understand how password cracking tools like Hashcat and John the
Ripper work at a fundamental level — hashing is one-way, so cracking
relies on hashing guesses and comparing results rather than reversing
the hash directly.

## Requirements

- Python 3 (uses the built-in `hashlib` module, no extra installs needed)

## Usage

```bash
python3 hashhunter.py
```

Enter the hash you want to identify/crack, then provide a wordlist file
when prompted.

## Planned Improvements

- [ ] Salted hash support
- [ ] Save cracking results to a report file
- [ ] Timing/performance stats (hashes tested per second)
- [ ] Support for additional hash types (bcrypt, NTLM)

## Disclaimer

This tool is intended for authorized security testing, password auditing
of your own accounts, and educational purposes only. Do not use it against
hashes or systems you don't own or have explicit permission to test.

## Author

Muhammad Raees Ahmad Khan — [LinkedIn](https://www.linkedin.com/in/raeeskhan9266)
