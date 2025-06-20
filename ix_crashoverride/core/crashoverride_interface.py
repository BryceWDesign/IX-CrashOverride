"""
IX-CrashOverride Command Line Interface

Enables user interaction via CLI, routing input through CrashOverrideCore to
retrieve expert responses from IX-Gibson.
"""

from core.crashoverride_core import CrashOverrideCore

def run_crashoverride_cli():
    core = CrashOverrideCore()
    print("IX-CrashOverride — Gibson-Linked Expert Agent")
    print("Type your query below, or type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Exiting IX-CrashOverride. Goodbye.")
            break
        output = core.process_input(user_input)
        print(f"CrashOverride: {output}")

if __name__ == "__main__":
    run_crashoverride_cli()
