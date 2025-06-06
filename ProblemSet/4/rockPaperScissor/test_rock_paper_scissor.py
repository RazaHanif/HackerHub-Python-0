import os
import subprocess

def run_tests():
    filename = "main.py"
    print("🔍 Checking if main.py exists...")
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing RPS logic...\n")

    try:
        result = subprocess.run(["python3", filename], input="rock\n", capture_output=True, text=True, timeout=5)
        output = result.stdout.lower()
        if any(word in output for word in ["you win", "you lose", "draw"]):
            print("✅ Valid RPS outcome detected.")
        else:
            print(f"❌ Unexpected output: {output}")

    except subprocess.TimeoutExpired:
        print("❌ Program timed out.")

if __name__ == "__main__":
    run_tests()
