import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Emoji Generator...\n")

    result = subprocess.run(["python3", filename], capture_output=True, text=True)
    output = result.stdout

    if any(emoji in output for emoji in ["👃", "😎", "👀", "😄", "😱", "😆"]):
        print("✅ Passed: Emojis were printed.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
