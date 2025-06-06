import os
import subprocess

def run_tests():
    filename = "main.py"
    dream_file = "dreams.txt"

    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return

    # Clean up before test
    if os.path.exists(dream_file):
        os.remove(dream_file)

    print("✅ main.py found. Testing Dream Journal...\n")

    inputs = "Flying over mountains\nSwimming with dolphins\ndone\n"
    result = subprocess.run(["python3", filename], input=inputs, capture_output=True, text=True)
    output = result.stdout

    # Check file creation
    if not os.path.exists(dream_file):
        print("❌ Failed: dreams.txt was not created.")
        return

    # Check contents printed
    if "1. Flying over mountains" in output and "2. Swimming with dolphins" in output:
        print("✅ Passed: Dreams saved and displayed correctly.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
