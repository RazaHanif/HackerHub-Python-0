import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Countdown...\n")

    result = subprocess.run(["python3", filename], capture_output=True, text=True)
    output = result.stdout

    if all(str(i) in output for i in range(1, 11)) and "blast off" in output.lower():
        print("✅ Passed: Countdown ran and ended with Blast off.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
