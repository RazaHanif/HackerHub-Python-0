import os
import subprocess

def run_tests():
    filename = "main.py"
    fav_file = "favorites.txt"

    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return

    # Clean up before test
    if os.path.exists(fav_file):
        os.remove(fav_file)

    print("✅ main.py found. Testing Favorite Thing Log...\n")

    inputs = "Pizza\nVideo games\ndone\n"
    result = subprocess.run(["python3", filename], input=inputs, capture_output=True, text=True)
    output = result.stdout

    if not os.path.exists(fav_file):
        print("❌ Failed: favorites.txt was not created.")
        return

    if "- Pizza" in output and "- Video games" in output:
        print("✅ Passed: Favorites saved and displayed correctly.")
    else:
        print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
