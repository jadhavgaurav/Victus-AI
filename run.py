import os
import subprocess

def main():
    print("\n🚀 Launching Victus AI backend...\n")

    # Ensure .env is loaded
    from dotenv import load_dotenv
    load_dotenv()

    # Set src folder in PYTHONPATH
    os.environ["PYTHONPATH"] = "src"

    # Run FastAPI with uvicorn
    subprocess.run([
        "poetry", "run", "uvicorn", "victus_ai.main:app",
        "--reload", "--host", "0.0.0.0", "--port", "8000"
    ])

if __name__ == "__main__":
    main()
