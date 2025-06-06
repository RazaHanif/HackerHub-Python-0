import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Compliment Machine...\n")

    inputs = "\n\nstop\n"
    result = subprocess.run(["python3", filename], input=inputs, capture_output=True, text=True)
    output = result.stdout.lower()

    if "goodbye" in output:
        print("✅ Passed: Exit message printed.")
    elif any(phrase in output for phrase in ["you're", "you are", "awesome", "great", "smart"]):
        print("✅ Passed: Compliment was shown.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
