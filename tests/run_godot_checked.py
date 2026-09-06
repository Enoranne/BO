"""Reject engine errors even when Godot exits with status zero."""
import re
import subprocess
import sys


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: run_godot_checked.py GODOT_BIN [Godot arguments]")
        return 2
    try:
        result = subprocess.run(
            sys.argv[1:], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, timeout=90, check=False,
        )
    except subprocess.TimeoutExpired as exc:
        output = exc.stdout or b""
        print(output.decode(errors="replace") if isinstance(output, bytes) else output)
        print("FAIL: Godot exceeded the 90-second validation timeout.")
        return 1
    except OSError as exc:
        print(f"FAIL: cannot start Godot: {exc}")
        return 1
    print(result.stdout, end="")
    output = re.sub(r"\x1b\[[0-9;]*[A-Za-z]", "", result.stdout)
    engine_error = re.search(r"^(?:SCRIPT ERROR:|ERROR:|FAIL:)", output, re.MULTILINE)
    leaked_objects = "ObjectDB instances were leaked at exit" in output
    incomplete_test = "-s" in sys.argv and not re.search(
        r"tests complete\. Failures: 0", output, re.IGNORECASE
    )
    if result.returncode or engine_error or leaked_objects or incomplete_test:
        print("FAIL: engine exit, diagnostics or test completion did not pass.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
