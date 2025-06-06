import os
import subprocess

def run_tests():
    filename = "main.py"

    print("🔍 Checking if main.py exists...")
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return

    print("✅ main.py found. Testing story generation...\n")

    try:
        result = subprocess.run(
            ["python3", filename],
            input="Raza\nMars\nspaceship\n", capture_output=True, text=True, timeout=5
        )
        output = result.stdout.strip()

        if "Raza" in output and "Mars" in output and "spaceship" in output:
            print("✅ Story includes all three inputs — nice job!")
        else:
            print(f"❌ Output: '{output}' — missing one or more story parts.")

    except subprocess.TimeoutExpired:
        print("❌ Script timed out.")
    except Exception as e:
        print(f"❌ Error while running: {e}")

if __name__ == "__main__":
    run_tests()
