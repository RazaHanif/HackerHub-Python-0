import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Name Animation...\n")

    name = "Amy"
    result = subprocess.run(["python3", filename], input=f"{name}\n", capture_output=True, text=True)
    output = result.stdout

    if all(letter.lower() in output.lower() for letter in name) and "✨" in output:
        print("✅ Passed: Name letters animated with emoji.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
