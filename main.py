import os

ENTRY = "The ledger is closed. I am a vault, not a vending machine, and at 3 a.m. your transaction is not on the guest list."

def main():
    if len(ENTRY) > 200:
        raise ValueError("entry exceeds the 200-character limit")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
