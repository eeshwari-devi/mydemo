from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Kothamasu Eeshwari Devi" 
    system_username = os.getenv("USER") or os.getenv("USERNAME") or "unknown"

    # Get server time in IST timezone
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")

    # Use 'ps aux' instead of 'top' for compatibility
    top_output = subprocess.getoutput("ps aux")

    return f"""
    <h1>Name: {full_name}</h1>
    <h2>Username: {system_username}</h2>
    <h3>Server Time: {server_time}</h3>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000, debug=True)
