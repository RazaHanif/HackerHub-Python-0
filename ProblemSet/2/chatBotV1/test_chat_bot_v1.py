import os
import subprocess

def run_tests():
    filename = "main.py"

    print("🔍 Checking if main.py exists...")
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return

    print("✅ main.py found. Simulating user input...\n")

    try:
        result = subprocess.run(
            ["python3", filename],
            input="Alice\n", capture_output=True, text=True, timeout=5
        )
        output = result.stdout.strip().splitlines()
        final_line = output[-1] if output else ""

        if "Alice" in final_line and "Hello" in final_line:
            print("✅ Greeting includes user's name and is friendly!")
        else:
            print(f"❌ Output: '{final_line}' — should greet Alice by name.")

    except subprocess.TimeoutExpired:
        print("❌ Your chatbot timed out.")
    except Exception as e:
        print(f"❌ Error while running your chatbot: {e}")

if __name__ == "__main__":
    run_tests()
