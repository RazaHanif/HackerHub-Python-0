import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Phonebook...\n")

    inputs = "Alice\n123\nBob\n456\ndone\nBob\n"
    result = subprocess.run(["python3", filename], input=inputs, capture_output=True, text=True)
    output = result.stdout

    if "456" in output:
        print("✅ Passed: Phonebook lookup worked.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
