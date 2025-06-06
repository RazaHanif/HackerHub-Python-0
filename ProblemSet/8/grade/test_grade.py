import os
import subprocess

def run_tests():
    filename = "main.py"
    if not os.path.exists(filename):
        print("❌ main.py not found.")
        return
    print("✅ main.py found. Testing Grader Bot...\n")

    test_cases = {
        "95\n": "A",
        "82\n": "B",
        "74\n": "C",
        "61\n": "D",
        "45\n": "F"
    }

    for score, expected_grade in test_cases.items():
        result = subprocess.run(["python3", filename], input=score, capture_output=True, text=True)
        output = result.stdout.upper()

        if expected_grade in output:
            print(f"✅ Passed: Score {score.strip()} returned grade {expected_grade}")
        else:
            print(f"❌ Failed: Score {score.strip()} did not return expected grade {expected_grade}\nOutput was:\n{output}")

if __name__ == "__main__":
    run_tests()
