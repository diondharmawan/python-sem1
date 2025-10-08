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

def cek_release():
  try:
    result = subprocess.run(["cat", "/etc/os-release"], capture_output=True, text=True, check=True)
    print("Ini adalah informasi sistem")
    print(result.stdout)
  except subprocess.CalledProcessError as e:
    print(f"Error menjalankan apt update: {e}")
    print(e.stderr)

if __name__ == "__main__":
  cek_release()


