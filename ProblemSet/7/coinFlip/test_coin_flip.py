import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Coin Flipper...\n")

    inputs = "yes\nyes\nstop\n"
    result = subprocess.run(["python3", filename], input=inputs, capture_output=True, text=True)
    output = result.stdout.lower()

    if "heads" in output or "tails" in output:
        print("✅ Passed: Coin was flipped at least once.")
    elif "thanks for playing" in output:
        print("✅ Passed: Exit message shown.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
