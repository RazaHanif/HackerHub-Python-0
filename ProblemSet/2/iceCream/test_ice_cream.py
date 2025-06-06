import os
import subprocess

def run_tests():
    filename = "main.py"

    print("🔍 Checking if main.py exists...")
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return

    print("✅ main.py found. Testing input/output...\n")

    try:
        result = subprocess.run(
            ["python3", filename],
            input="Strawberry\n3\n", capture_output=True, text=True, timeout=5
        )
        output = result.stdout.strip().splitlines()
        final_line = output[-1] if output else ""

        if "Strawberry" in final_line and "3" in final_line:
            print("✅ Output includes correct scoop count and flavor!")
        else:
            print(f"❌ Output: '{final_line}' — missing flavor or scoop count.")

    except subprocess.TimeoutExpired:
        print("❌ Program timed out.")
    except Exception as e:
        print(f"❌ Error during test: {e}")

if __name__ == "__main__":
    run_tests()
