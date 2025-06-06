import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Pet Generator...\n")

    pets = ["dog", "cat", "bird", "fish"]
    for pet in pets:
        result = subprocess.run(
            ["python3", filename],
            input=pet + "\n",
            capture_output=True,
            text=True
        )
        output = result.stdout.lower()
        if pet in ["dog", "cat", "bird"]:
            if pet not in output:
                print(f"❌ Failed: Expected fact for {pet}, got:\n{output}")
            else:
                print(f"✅ Passed: Fact found for {pet}.")
        else:
            if "not found" in output or "sorry" in output:
                print(f"✅ Passed: Properly handled unknown pet '{pet}'.")
            else:
                print(f"❌ Failed: Unknown pet '{pet}' not handled correctly.\nOutput:\n{output}")

if __name__ == "__main__":
    run_tests()
