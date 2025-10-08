import subprocess

def apt_update():
  try:
    result = subprocess.run(["sudo", "apt", "update"], capture_output=True, text=True, check=True)
    print("apt update selesai.")
    print(result.stdout)
  except subprocess.CalledProcessError as e:
    print(f"Error menjalankan apt update: {e}")
    print(e.stderr)

if __name__ == "__main__":
  apt_update()