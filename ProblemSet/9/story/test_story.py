import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Emoji Story Builder...\n")

    inputs = "🐶\n🚀\n🌈\n🍕\n🏖️\n"
    result = subprocess.run(["python3", filename], input=inputs, capture_output=True, text=True)
    output = result.stdout

    if all(emoji in output for emoji in ["🐶", "🚀", "🌈", "🍕", "🏖️"]):
        print("✅ Passed: All emojis shown in story.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
