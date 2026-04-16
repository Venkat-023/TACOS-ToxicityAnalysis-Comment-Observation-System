import os
import signal
import subprocess
import sys
import time


PORT = os.environ.get("PORT", "7860")
API_PORT = os.environ.get("API_PORT", "8000")
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def start_process(command, cwd=None, extra_env=None):
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    return subprocess.Popen(command, cwd=cwd or ROOT_DIR, env=env)


def terminate_processes(processes):
    for process in processes:
        if process.poll() is None:
            process.terminate()

    deadline = time.time() + 10
    for process in processes:
        if process.poll() is None:
            timeout = max(0, deadline - time.time())
            try:
                process.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                process.kill()


def main():
    backend = start_process(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "app:app",
            "--host",
            "0.0.0.0",
            "--port",
            API_PORT,
        ],
        cwd=os.path.join(ROOT_DIR, "Backend"),
    )

    frontend = start_process(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            os.path.join(ROOT_DIR, "Frontend", "front.py"),
            "--server.address",
            "0.0.0.0",
            "--server.port",
            PORT,
            "--browser.gatherUsageStats",
            "false",
        ],
        extra_env={
            "API_URL": f"http://127.0.0.1:{API_PORT}/moderate",
        },
    )

    processes = [backend, frontend]

    def handle_signal(signum, frame):
        terminate_processes(processes)
        raise SystemExit(0)

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    try:
        while True:
            for process in processes:
                code = process.poll()
                if code is not None:
                    terminate_processes(processes)
                    raise SystemExit(code)
            time.sleep(1)
    finally:
        terminate_processes(processes)


if __name__ == "__main__":
    main()
