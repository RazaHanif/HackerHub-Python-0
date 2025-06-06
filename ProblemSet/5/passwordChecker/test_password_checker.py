import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Password Checker...\n")

    inputs = "wrong\nnope\nsecret123\n"
    result = subprocess.run(["python3", filename], input=inputs, capture_output=True, text=True)
    output = result.stdout.lower()

    if "welcome" in output:
        print("✅ Passed: Accepted correct password after retries.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
