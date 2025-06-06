import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Tip Calculator...\n")

    meal_input = "50\n15\n"
    result = subprocess.run(["python3", filename], input=meal_input, capture_output=True, text=True)
    output = result.stdout

    if "$" in output and "57.50" in output.replace("$", ""):
        print("✅ Passed: Total cost correctly calculated and formatted.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
