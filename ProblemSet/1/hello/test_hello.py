import os
import subprocess

def run_tests():
    filename = "main.py"

    print("🔍 Checking if main.py exists...")
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return

    print("✅ main.py found. Running test...\n")

    try:
        result = subprocess.run(["python3", filename], capture_output=True, text=True, timeout=5)
        output = result.stdout.strip()

        if output == "Hello, World!":
            print("✅ Great job! You printed the correct message.")
        else:
            print(f"❌ Output was: '{output}' — expected 'Hello, World!'")

    except subprocess.TimeoutExpired:
        print("❌ Your program took too long to run. Check your code.")
    except Exception as e:
        print(f"❌ Error while running your program: {e}")

if __name__ == "__main__":
    run_tests()
