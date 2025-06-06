import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Weather Mood Generator...\n")

    weathers = ["sunny", "rainy", "snowy", "foggy"]
    for weather in weathers:
        result = subprocess.run(
            ["python3", filename],
            input=weather + "\n",
            capture_output=True,
            text=True
        )
        output = result.stdout.lower()
        if weather in ["sunny", "rainy", "snowy"]:
            if weather not in output:
                print(f"❌ Failed: Expected mood for {weather}, got:\n{output}")
            else:
                print(f"✅ Passed: Mood found for {weather}.")
        else:
            if "default" in output or "try again" in output or "unknown" in output:
                print(f"✅ Passed: Properly handled unknown weather '{weather}'.")
            else:
                print(f"❌ Failed: Unknown weather '{weather}' not handled correctly.\nOutput:\n{output}")

if __name__ == "__main__":
    run_tests()
