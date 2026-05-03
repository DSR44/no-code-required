"""
Subscribe endpoint for No Code Required
Handles email subscriptions via Resend API
"""

import json
import os
import subprocess
from http.server import BaseHTTPRequestHandler

RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "")
AUDIENCE_ID = os.environ.get("RESEND_AUDIENCE_ID", "")

WELCOME_HTML = """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; margin: 0 auto; padding: 0; background: #0a0a0b;">
    <!-- Header -->
    <div style="background: linear-gradient(135deg, #131316 0%, #1a1a1d 100%); padding: 40px 20px; text-align: center; border-bottom: 3px solid #e8a87c;">
        <h1 style="color: #e8e6e1; font-size: 28px; margin: 0; letter-spacing: 2px;">NO CODE REQUIRED</h1>
        <p style="color: #e8a87c; font-size: 12px; margin: 8px 0 0 0; letter-spacing: 3px; text-transform: uppercase;">I test it so you don't have to</p>
    </div>
    
    <!-- Body -->
    <div style="padding: 32px 20px;">
        <p style="font-size: 18px; color: #e8e6e1; margin-bottom: 16px;">Hey,</p>
        <p style="font-size: 16px; line-height: 1.7; color: #8a8880; margin-bottom: 16px;">Thanks for subscribing to No Code Required.</p>
        <p style="font-size: 16px; line-height: 1.7; color: #8a8880; margin-bottom: 16px;">I test AI tools so you don't waste money on the ones that don't work. Every review is based on real experience — not product pages and press releases.</p>
        <p style="font-size: 16px; line-height: 1.7; color: #8a8880; margin-bottom: 16px;">You'll get an email when I publish something new. No daily digests. No "5 reasons you NEED this tool" spam. Just honest reviews from someone who started from zero.</p>
        <p style="font-size: 16px; line-height: 1.7; color: #8a8880; margin-bottom: 24px;">Hit reply if you ever want to suggest a tool for me to test. I actually read them.</p>
        <p style="font-size: 16px; color: #e8a87c;">— Manal</p>
    </div>
    
    <!-- Footer -->
    <div style="background: #111; padding: 20px; text-align: center; border-top: 1px solid #222;">
        <p style="font-size: 12px; color: #555; line-height: 1.5; margin: 0;">No Code Required | <a href="https://www.nocoderequired.net" style="color: #e8a87c; text-decoration: none;">nocoderequired.net</a><br>You're receiving this because you subscribed. Reply "unsubscribe" to stop.</p>
    </div>
</div>
"""

def send_welcome_email(email):
    cmd = [
        "curl", "-s", "-X", "POST", "https://api.resend.com/emails",
        "-H", f"Authorization: Bearer {RESEND_API_KEY}",
        "-H", "Content-Type: application/json",
        "-d", json.dumps({
            "from": "hello@nocoderequired.net",
            "reply_to": "hello@manal.pro",
            "to": email,
            "subject": "Welcome to No Code Required",
            "html": WELCOME_HTML
        })
    ]
    subprocess.run(cmd, capture_output=True, text=True, timeout=30)


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        
        try:
            data = json.loads(body)
            email = data.get("email", "").strip()
            
            if not email or "@" not in email:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Invalid email"}).encode())
                return
            
            # Add to Resend audience
            cmd = [
                "curl", "-s", "-X", "POST", "https://api.resend.com/contacts",
                "-H", f"Authorization: Bearer {RESEND_API_KEY}",
                "-H", "Content-Type: application/json",
                "-d", json.dumps({
                    "email": email,
                    "audience_id": AUDIENCE_ID,
                    "unsubscribed": False
                })
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            response = json.loads(result.stdout) if result.returncode == 0 else {}
            
            if response.get("id") or response.get("error") == "Contact already exists":
                # Send welcome email
                send_welcome_email(email)
                
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "subscribed", "email": email}).encode())
            else:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"error": response.get("error", "Unknown error")}).encode())
                
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
