"""
QR Code Generator Skill for Hermes Agent
"""
import json
import base64
import io
from hermes_agent.skills import BaseSkill
from hermes_tools import write_file

try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False


class QrCodeGenerator(BaseSkill):
    """Skill for generating QR codes from URLs or text."""
    
    def __init__(self, config, platform):
        super().__init__(config, platform)
        self.name = "qr-code-generator"
        self.description = "Generates QR codes from URLs or text for sharing in chats"
        
        if not QRCODE_AVAILABLE:
            self.logger.warning("qrcode library not available. Install with: pip install qrcode[pil]")
    
    def generate_qr(self, data: str, size: int = 10, border: int = 4, 
                    error_correction: str = 'L') -> dict:
        """
        Generate a QR code from the provided data.
        
        Args:
            data: The data to encode in the QR code (URL, text, etc.)
            size: Size of each box in pixels (default: 10)
            border: Width of the border in boxes (default: 4)
            error_correction: Error correction level ('L', 'M', 'Q', 'H')
            
        Returns:
            Dict with status and base64-encoded PNG image data
        """
        if not QRCODE_AVAILABLE:
            return json.dumps({
                "status": "error",
                "message": "qrcode library not installed. Install with: pip install qrcode[pil]"
            })
        
        # Map error correction string to constant
        error_correction_map = {
            'L': ERROR_CORRECT_L,
            'M': ERROR_CORRECT_M,
            'Q': ERROR_CORRECT_Q,
            'H': ERROR_CORRECT_H
        }
        ec_level = error_correction_map.get(error_correction.upper(), ERROR_CORRECT_L)
        
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls size; 1 is 21x21 modules
            error_correction=ec_level,
            box_size=size,
            border=border,
        )
        
        # Add data
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert to base64 PNG
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return json.dumps({
            "status": "success",
            "data": img_base64,
            "format": "png",
            "encoding": "base64",
            "message": f"Generated QR code for: {data[:50]}{'...' if len(data) > 50 else ''}"
        })
    
    def _handle_slash_command(self, command_original: str, event: dict) -> str:
        """
        Handle slash commands like /qr <data>
        """
        # Extract command and arguments
        parts = command_original.strip().split()
        if not parts:
            return json.dumps({"status": "error", "message": "No command provided"})
        
        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        # Handle /qr command
        if cmd in ['/qr', 'qr']:
            if not args:
                return json.dumps({
                    "status": "error", 
                    "message": "Please provide data to encode in the QR code. Usage: /qr <url-or-text>"
                })
            
            # Join args back together to preserve spaces in text
            data = ' '.join(args)
            
            # Generate QR code
            result = self.generate_qr(data)
            
            # For Telegram delivery, we need to return the image data
            # The skill system will handle converting base64 to MEDIA: if needed
            return result
        
        # Handle help
        elif cmd in ['/help', 'help', '-h', '--help']:
            return json.dumps({
                "status": "help",
                "message": "QR Code Generator Skill\n\nUsage:\n  /qr <url-or-text> - Generate a QR code\n  /qr help - Show this help\n\nExamples:\n  /qr drip.haus/riderverse\n  /qr https://example.com\n  /qr Hello World\n\nThe QR code will be returned as an image that can be displayed in chat."
            })
        
        else:
            return json.dumps({
                "status": "error",
                "message": f"Unknown command: {cmd}. Use /qr help for usage information."
            })
    
    def on_load(self):
        """Called when the skill is loaded."""
        self.logger.info("QR Code Generator skill loaded")
        if not QRCODE_AVAILABLE:
            self.logger.warning("qrcode library not available - install with: pip install qrcode[pil]")
    
    def on_unload(self):
        """Called when the skill is unloaded."""
        self.logger.info("QR Code Generator skill unloaded")