#!/usr/bin/env python3
"""
QR Code Generator for Hermes Agent
Generates QR codes and sends them via Telegram
"""

import qrcode
import json
import sys
import os
from pathlib import Path
from io import BytesIO
import base64

def generate_qr_code(data, box_size=10, border=4, fill_color="black", back_color="white"):
    """
    Generate a QR code from the given data
    
    Args:
        data (str): The data to encode in the QR code
        box_size (int): Size of each box in pixels
        border (int): Border size in boxes
        fill_color (str): Color of the QR code modules
        back_color (str): Background color
    
    Returns:
        BytesIO: PNG image data
    """
    qr = qrcode.QRCode(
        version=None,  # Auto-determine version
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Save to BytesIO object
    img_buffer = BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    
    return img_buffer

def save_qr_to_file(data, filename, **kwargs):
    """
    Generate QR code and save to file
    
    Args:
        data (str): Data to encode
        filename (str): Output filename
        **kwargs: Additional arguments for generate_qr_code
    
    Returns:
        str: Path to saved file
    """
    img_buffer = generate_qr_code(data, **kwargs)
    
    # Ensure directory exists
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    
    # Save to file
    with open(filename, 'wb') as f:
        f.write(img_buffer.getbuffer())
    
    return filename

def main():
    """Main entry point for the QR code generator"""
    if len(sys.argv) < 2:
        print("Usage: python qr_generator.py '<data>' [output_file]")
        print("Example: python qr_generator.py 'https://example.com' qr.png")
        sys.exit(1)
    
    data = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        if output_file:
            # Save to file
            saved_path = save_qr_to_file(data, output_file)
            print(json.dumps({
                "status": "success",
                "message": f"QR code saved to {saved_path}",
                "file_path": saved_path
            }))
        else:
            # Generate and return base64 encoded image (for direct sending)
            img_buffer = generate_qr_code(data)
            img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
            
            print(json.dumps({
                "status": "success",
                "image_base64": img_base64,
                "message": "QR code generated successfully"
            }))
            
    except Exception as e:
        print(json.dumps({
            "status": "error",
            "message": f"Failed to generate QR code: {str(e)}"
        }), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()