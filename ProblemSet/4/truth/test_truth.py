import os
import subprocess

def run_tests():
    filename = "main.py"
    print("🔍 Checking if main.py exists...")
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing fortune-telling output...\n")

    responses = set()
    for _ in range(5):
        result = subprocess.run(["python3", filename], input="Will I win?\n", capture_output=True, text=True)
        responses.add(result.stdout.strip())

    if len(responses) >= 3:
        print("✅ Detected randomized answers — fortune teller works!")
    else:
        print("❌ Answers not random or too repetitive.")

if __name__ == "__main__":
    run_tests()
