import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Character States...\n")

    result = subprocess.run(["python3", filename], capture_output=True, text=True)
    output = result.stdout.lower()

    if "health" in output and "strength" in output and "speed" in output:
        print("✅ Passed: All character stats printed.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
