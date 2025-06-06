import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Guess the Number v2...\n")

    # Let's assume the secret number is 7
    inputs = "1\n9\n7\n"
    result = subprocess.run(["python3", filename], input=inputs, capture_output=True, text=True)
    output = result.stdout.lower()

    if "too low" in output and "too high" in output and "correct" in output:
        print("✅ Passed: Game gave correct feedback and ended.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
