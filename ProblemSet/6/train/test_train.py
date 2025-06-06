import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Emoji Train...\n")

    emoji = "🚀"
    count = 5
    result = subprocess.run(["python3", filename], input=f"{emoji}\n{count}\n", capture_output=True, text=True)
    output = result.stdout

    if emoji * count in output:
        print("✅ Passed: Emoji train printed correctly.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
