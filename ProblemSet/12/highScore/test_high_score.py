import os
import subprocess

def run_tests():
    filename = "main.py"
    score_file = "highscores.txt"

    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return

    # Clean up before test
    if os.path.exists(score_file):
        os.remove(score_file)

    print("✅ main.py found. Testing Highscore Saver...\n")

    inputs = "Alex\n250\nJamie\n300\ndone\n"
    result = subprocess.run(["python3", filename], input=inputs, capture_output=True, text=True)
    output = result.stdout

    if not os.path.exists(score_file):
        print("❌ Failed: highscores.txt was not created.")
        return

    # Check output order
    if "Jamie - 300" in output and "Alex - 250" in output:
        # Check Jamie before Alex to ensure sorting descending
        if output.index("Jamie - 300") < output.index("Alex - 250"):
            print("✅ Passed: Highscores saved and sorted correctly.")
            return
    print(f"❌ Failed: Output was:\n{output}")

if __name__ == "__main__":
    run_tests()
