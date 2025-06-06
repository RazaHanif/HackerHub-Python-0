import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Student Grades...\n")

    inputs = "Mia\nA\nLeo\nB\ndone\n"
    result = subprocess.run(["python3", filename], input=inputs, capture_output=True, text=True)
    output = result.stdout

    if "Mia" in output and "A" in output and "Leo" in output and "B" in output:
        print("✅ Passed: Class list printed correctly.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
