import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Gift List Maker...\n")

    inputs = "Laptop\nHeadphones\ndone\n"
    result = subprocess.run(["python3", filename], input=inputs, capture_output=True, text=True)
    output = result.stdout.lower()

    if "laptop" in output and "headphones" in output and "-" in output:
        print("✅ Passed: List built and printed correctly.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
