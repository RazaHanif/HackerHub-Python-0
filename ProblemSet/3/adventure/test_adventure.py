import os
import subprocess

def run_tests():
    filename = "main.py"

    print("🔍 Checking if main.py exists...")
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return

    print("✅ main.py found. Testing story paths...\n")

    try:
        choices = ["left\n", "right\n"]
        unique_endings = set()

        for choice in choices:
            result = subprocess.run(
                ["python3", filename],
                input=choice, capture_output=True, text=True, timeout=5
            )
            output = result.stdout.strip()
            unique_endings.add(output)

        if len(unique_endings) >= 2:
            print("✅ Detected different outcomes for different choices!")
        else:
            print("❌ Story doesn't change based on the user's input.")

    except subprocess.TimeoutExpired:
        print("❌ Program took too long to run.")
    except Exception as e:
        print(f"❌ Error during story test: {e}")

if __name__ == "__main__":
    run_tests()
