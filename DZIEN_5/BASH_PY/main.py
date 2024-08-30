import subprocess

# Ścieżka do skryptu Bash
script_path = "./example.sh"

try:
    # Uruchamianie skryptu Bash za pomocą subprocess.run()
    result = subprocess.run(['bash', script_path], capture_output=True, text=True, check=True)
    
    # Wyświetlanie wyniku
    print("Wyjście skryptu Bash:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Skrypt Bash zakończył się błędem. Kod wyjścia: {e.returncode}")
    print(f"Wyjście błędu: {e.stderr}")
except FileNotFoundError:
    print("Skrypt Bash nie został znaleziony.")
except Exception as e:
    print(f"Wystąpił nieoczekiwany błąd: {e}")
