# CLI entry point
import sys
from .sdk import SentinelSDK

def main():
    sdk = SentinelSDK()
    if len(sys.argv) < 2:
        print("Usage: sentinel-cli <command>")
        return
    command = sys.argv[1]
    if command == "connect":
        print("Connecting to board...")
    elif command == "send":
        if len(sys.argv) < 3:
            print("Usage: sentinel-cli send <command>")
            return
        print(f"Sending command: {sys.argv[2]}")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()