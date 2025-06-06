import os
import subprocess

def run_tests():
    filename = "main.py"
    print("🔍 Checking if main.py exists...")
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing FizzBuzz logic...\n")

    test_cases = [
        ("3\n", "Fizz"),
        ("5\n", "Buzz"),
        ("15\n", "FizzBuzz"),
        ("7\n", "7")
    ]

    for input_val, expected in test_cases:
        result = subprocess.run(["python3", filename], input=input_val, capture_output=True, text=True)
        output = result.stdout.strip()
        if expected.lower() in output.lower():
            print(f"✅ Passed: {input_val.strip()} -> {expected}")
        else:
            print(f"❌ Failed: {input_val.strip()} -> Got: {output}")

if __name__ == "__main__":
    run_tests()
