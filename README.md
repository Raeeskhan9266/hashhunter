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

1. Takes a hash as input
2. Identifies the likely hash algorithm based on output length
   (MD5: 32 chars, SHA-1: 40 chars, SHA-256: 64 chars, SHA-512: 128 chars)
3. Optionally accepts a salt value and its position (before/after the
   password), to support cracking salted hashes
4. Hashes each word in a provided wordlist (combined with the salt, if
   provided) using the identified algorithm
5. Compares each computed hash against the target hash to find a match

## Requirements

- Python 3 (uses the built-in `hashlib` module, no extra installs needed)

## Usage

```bash
python3 hashhunter.py
```

Enter the hash you want to identify/crack, then provide a wordlist file
when prompted.

## Limitations

Dictionary attacks are only as effective as the wordlist used. If the
actual password isn't present in the wordlist — even a common one — the
tool won't find a match, regardless of how correct the algorithm/salt
handling is. Real-world cracking tools (Hashcat, John the Ripper) rely on
much larger wordlists (e.g. rockyou.txt, 14M+ entries) and apply rule-based
mutations (e.g. appending numbers, capitalizing letters) to expand
effective coverage beyond the raw wordlist.

## Planned Improvements

- [ ] Save cracking results to a report file
- [ ] Timing/performance stats (hashes tested per second)
- [ ] Support for additional hash types (bcrypt, NTLM)
- [ ] Rule-based wordlist mutations (e.g. append numbers, capitalize)

## Disclaimer

This tool is intended for authorized security testing, password auditing
of your own accounts, and educational purposes only. Do not use it against
hashes or systems you don't own or have explicit permission to test.

## Author

Muhammad Raees Ahmad Khan — [LinkedIn](https://www.linkedin.com/in/raeeskhan9266)
