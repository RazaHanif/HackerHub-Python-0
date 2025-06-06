import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Copy Cat logic...\n")

    inputs = "hello\nhow are you\nstop\n"
    result = subprocess.run(["python3", filename], input=inputs, capture_output=True, text=True)
    output = result.stdout.lower()

    if "hello" in output and "how are you" in output and "goodbye" in output:
        print("✅ Passed: Copy Cat echoed and exited properly.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
