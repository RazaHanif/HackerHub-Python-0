import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing To-Do Tracker...\n")

    inputs = "Walk dog\nDo dishes\ndone\n"
    result = subprocess.run(["python3", filename], input=inputs, capture_output=True, text=True)
    output = result.stdout

    if "[1]" in output and "Walk dog" in output and "[2]" in output:
        print("✅ Passed: Numbered task list printed.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
