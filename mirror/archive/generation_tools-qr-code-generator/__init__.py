"""
QR Code Generator Skill for Hermes Agent
Handles QR code generation via direct Python execution with proper environment setup
"""

import json
import os
import sys
import subprocess
import tempfile
import time
from pathlib import Path

def generate_qr_direct(data: str) -> dict:
    """
    Generate QR code by running Python script in subprocess with proper environment
    
    Args:
        data (str): Data to encode in QR code
        
    Returns:
        dict: Result with status and file path
    """
    # Create a temporary file path for the output
    timestamp = int(time.time())
    output_path = f"/tmp/qr_{abs(hash(data))}_{timestamp}.png"
    
    # Create the Python script to generate QR code
    # Escape quotes properly for the data string
    escaped_data = data.replace('"', '\\"').replace("'", "\\'")
    qr_script = f'''
import sys
import os
# Add user site-packages to path
user_site = "/home/midnight/.local/lib/python3.10/site-packages"
if user_site not in sys.path:
    sys.path.insert(0, user_site)

import qrcode
import io

# Generate QR code
url = "{escaped_data}"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
buffer = io.BytesIO()
img.save(buffer, format='PNG')
buffer.seek(0)

# Save to file
with open(r"{output_path}", 'wb') as f:
    f.write(buffer.getvalue())

print("SUCCESS:{output_path}")
'''
    
    # Run the script using python3.10 explicitly
    try:
        result = subprocess.run(
            ['python3.10', '-c', qr_script],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Check if successful
        if result.returncode == 0 and os.path.exists(output_path) and os.path.getsize(output_path) > 0:
            return {
                "status": "success",
                "output_path": output_path,
                "message": f"QR code generated for: {data}",
                "data": data
            }
        else:
            # Check if we can extract success message from stdout
            if "SUCCESS:" in result.stdout:
                # Extract path from success message
                success_part = result.stdout.strip().split("SUCCESS:")[1].strip()
                if os.path.exists(success_part) and os.path.getsize(success_part) > 0:
                    return {
                        "status": "success",
                        "output_path": success_part,
                        "message": f"QR code generated for: {data}",
                        "data": data
                    }
            
            error_msg = result.stderr.strip() if result.stderr.strip() else result.stdout.strip()
            return {
                "status": "error",
                "message": f"QR code generation failed: {error_msg}",
                "data": data
            }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to execute QR code generation: {str(e)}",
            "data": data
        }

def handle_qr_request(text: str) -> dict:
    """
    Handle a QR code generation request from user input
    
    Args:
        text (str): User input like "drip.haus/riderverse" or "https://example.com"
        
    Returns:
        dict: Result for Telegram response with MEDIA: path
    """
    # Clean up the input
    data = text.strip()
    
    # Remove common command prefixes if present
    if data.startswith('/qr '):
        data = data[4:].strip()
    elif data.startswith('/qr'):
        data = data[3:].strip()
    
    if not data:
        return {
            "status": "error",
            "message": "Please provide data to encode in the QR code. Usage: /qr <url_or_text>",
            "data": None
        }
    
    # Generate the QR code directly
    return generate_qr_direct(data)

def format_telegram_response(result: dict) -> str:
    """
    Format the skill result for Telegram delivery
    
    Args:
        result (dict): Result from handle_qr_request
        
    Returns:
        str: Formatted response string with MEDIA: prefix
    """
    if result.get("status") != "success":
        return f"❌ {result.get('message', 'Unknown error')}"
    
    output_path = result.get("output_path")
    message = result.get("message", "QR code generated")
    data = result.get("data", "")
    
    # Format for Telegram: MEDIA: path followed by caption
    if output_path:
        return f"MEDIA:{output_path}\\n{message}\\n🔗 Encoded: {data}"
    else:
        return f"❌ No output path generated"

# For testing/direct execution
if __name__ == "__main__":
    # Test with sample data
    test_data = "https://drip.haus/riderverse"
    result = handle_qr_request(test_data)
    formatted = format_telegram_response(result)
    print("Test Result:")
    print(json.dumps(result, indent=2))
    print("\nFormatted for Telegram:")
    print(formatted)
