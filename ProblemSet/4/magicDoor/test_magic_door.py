import os
import subprocess

def run_tests():
    filename = "main.py"
    print("🔍 Checking if main.py exists...")
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Magic Door logic...\n")

    choices = {
        "Red\n": "red",
        "Blue\n": "blue",
        "Green\n": "green",
        "Banana\n": "invalid"
    }

    for input_val, key in choices.items():
        result = subprocess.run(["python3", filename], input=input_val, capture_output=True, text=True)
        output = result.stdout.strip().lower()
        if key in output:
            print(f"✅ Passed: {input_val.strip()} triggered expected output.")
        else:
            print(f"❌ Failed: {input_val.strip()} -> Got: {output}")

if __name__ == "__main__":
    run_tests()
