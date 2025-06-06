import os
import subprocess

def run_tests():
    filename = "main.py"
    secret = 7  # This should match the hardcoded value in the student's file

    print("🔍 Checking if main.py exists...")
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return

    print("✅ main.py found. Running tests...\n")

    try:
        test_inputs = [
            (str(secret - 1), "Too low"),
            (str(secret + 1), "Too high"),
            (str(secret), "Correct")
        ]

        for guess, expected in test_inputs:
            result = subprocess.run(
                ["python3", filename],
                input=guess + "\n", capture_output=True, text=True, timeout=5
            )
            output = result.stdout.strip().lower()

            if expected.lower() in output:
                print(f"✅ Correct response for guess {guess}: {expected}")
            else:
                print(f"❌ For guess {guess}, expected '{expected}' but got:\n{output}")

    except subprocess.TimeoutExpired:
        print("❌ Script timed out.")
    except Exception as e:
        print(f"❌ Error during test: {e}")

if __name__ == "__main__":
    run_tests()
