import requests
import os

# ---------------- CONFIGURATION ----------------
RENDER_URL = "http://127.0.0.1:5001/download_csv"
TOKEN = "equilocksdk"
LOCAL_CSV = os.path.join(os.path.dirname(__file__), "users_backup.csv")

# ---------------- DOWNLOAD FUNCTION ----------------
def download_csv():
    url = f"{RENDER_URL}?token={TOKEN}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for HTTP issues
        
        # Ensure folder exists
        os.makedirs(os.path.dirname(LOCAL_CSV), exist_ok=True)
        
        # Save CSV permanently
        with open(LOCAL_CSV, "wb") as f:
            f.write(response.content)
        
        print(f"[✓] Backup downloaded successfully: {LOCAL_CSV}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"[✗] HTTP error: {http_err} - Response content: {response.text}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"[✗] Connection error: {conn_err}")
    except requests.exceptions.Timeout:
        print("[✗] Timeout error: server took too long to respond")
    except Exception as e:
        print(f"[✗] Unexpected error: {e}")

# ---------------- RUN ----------------
if __name__ == "__main__":
    download_csv()
