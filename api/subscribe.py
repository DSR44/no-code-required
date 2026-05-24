"""
Subscribe endpoint for No Code Required
Handles email subscriptions via Resend API
"""

import base64
import json
import os
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler

RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "")
AUDIENCE_ID = os.environ.get("RESEND_AUDIENCE_ID", "")
STARTER_KIT_PDF = os.path.join(os.path.dirname(__file__), "assets", "the-0-dollar-ai-starter-kit.pdf")

WELCOME_HTML = """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; margin: 0 auto; background: #0a0a0b;">
    <!-- Header -->
    <div style="background: linear-gradient(135deg, #131316 0%, #1a1a1d 100%); padding: 40px 20px; text-align: center; border-bottom: 3px solid #e8a87c;">
        <h1 style="color: #e8e6e1; font-size: 28px; margin: 0; letter-spacing: 2px;">NO CODE REQUIRED</h1>
        <p style="color: #e8a87c; font-size: 13px; margin: 10px 0 0 0; letter-spacing: 1px;">i test it so you don't have to</p>
    </div>
    
    <!-- Body -->
    <div style="padding: 32px 24px;">
        <p style="font-size: 18px; color: #e8e6e1; margin-bottom: 16px;">Hey,</p>
        <p style="font-size: 16px; line-height: 1.7; color: #8a8880; margin-bottom: 16px;">Thanks for subscribing to No Code Required.</p>
        <p style="font-size: 16px; line-height: 1.7; color: #8a8880; margin-bottom: 16px;">I test AI tools so you don't waste money on the ones that don't work. Every review is based on real experience. Not product pages. Not press releases.</p>
        <p style="font-size: 16px; line-height: 1.7; color: #8a8880; margin-bottom: 16px;">You will get an email when I publish something new. No daily digests. No spam. Just honest reviews from someone who started from zero.</p>
        <p style="font-size: 16px; line-height: 1.7; color: #8a8880; margin-bottom: 24px;">Hit reply if you ever want to suggest a tool for me to test. I actually read them.</p>
        <p style="font-size: 16px; color: #e8a87c; font-weight: 600;">Manal</p>
    </div>
    
    <!-- Footer -->
    <div style="background: #131316; padding: 20px 24px; text-align: center;">
        <p style="font-size: 12px; color: #555; line-height: 1.5; margin: 0;"><a href="https://www.nocoderequired.net" style="color: #e8a87c; text-decoration: none;">nocoderequired.net</a> | Reply "unsubscribe" to stop</p>
    </div>
</div>
"""

STARTER_KIT_HTML = """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; margin: 0 auto; background: #0a0a0b;">
    <div style="background: linear-gradient(135deg, #131316 0%, #1a1a1d 100%); padding: 40px 20px; text-align: center; border-bottom: 3px solid #e8a87c;">
        <h1 style="color: #e8e6e1; font-size: 26px; margin: 0; letter-spacing: 1px;">YOUR STARTER KIT IS READY</h1>
        <p style="color: #e8a87c; font-size: 13px; margin: 10px 0 0 0;">The $0 AI Starter Kit · No Code Required</p>
    </div>
    <div style="padding: 32px 24px;">
        <p style="font-size: 18px; color: #e8e6e1; margin-bottom: 16px;">Hey,</p>
        <p style="font-size: 16px; line-height: 1.7; color: #8a8880; margin-bottom: 16px;">Here's your starter kit — <strong style="color: #e8e6e1;">the PDF is attached to this email</strong>. 5 free tools and a step-by-step client follow-up automation you can build tonight.</p>
        <p style="font-size: 15px; line-height: 1.7; color: #8a8880; margin-bottom: 12px;"><strong style="color: #e8e6e1;">Start with Path A</strong> — the client follow-up sequence. Full blog walkthrough with screenshots:</p>
        <p style="margin-bottom: 20px;"><a href="https://www.nocoderequired.net/posts/automate-client-follow-ups-no-code/" style="color: #6bc4c4;">How I automated my client follow-ups in an afternoon</a></p>
        <p style="font-size: 15px; line-height: 1.7; color: #8a8880; margin-bottom: 8px;">New to AI tools? Follow the <a href="https://www.nocoderequired.net/start-here/" style="color: #6bc4c4;">Start Here</a> path after you build your first workflow.</p>
        <p style="font-size: 16px; color: #e8a87c; font-weight: 600; margin-top: 24px;">Manal</p>
    </div>
    <div style="background: #131316; padding: 20px 24px; text-align: center;">
        <p style="font-size: 12px; color: #555; line-height: 1.5; margin: 0;">You'll also get new posts when I publish. Reply "unsubscribe" anytime.</p>
    </div>
</div>
"""


def _resend_post(url: str, payload: dict) -> dict:
    if not RESEND_API_KEY:
        raise RuntimeError("RESEND_API_KEY not configured")
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8")
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {"error": raw or str(e)}


def add_contact(email: str) -> dict:
    return _resend_post(
        "https://api.resend.com/contacts",
        {"email": email, "audience_id": AUDIENCE_ID, "unsubscribed": False},
    )


def send_welcome_email(email: str, source: str | None = None) -> dict:
    html = STARTER_KIT_HTML if source == "starter-kit" else WELCOME_HTML
    subject = "Your $0 AI Starter Kit is ready" if source == "starter-kit" else "Welcome to No Code Required"
    payload = {
        "from": "hello@nocoderequired.net",
        "reply_to": "hello@manal.pro",
        "to": email,
        "subject": subject,
        "html": html,
    }
    if source == "starter-kit" and os.path.exists(STARTER_KIT_PDF):
        with open(STARTER_KIT_PDF, "rb") as f:
            payload["attachments"] = [{
                "filename": "The-0-Dollar-AI-Starter-Kit.pdf",
                "content": base64.b64encode(f.read()).decode("ascii"),
            }]
    return _resend_post("https://api.resend.com/emails", payload)


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)
            email = data.get("email", "").strip()
            source = data.get("source", "").strip() or None

            if not email or "@" not in email:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Invalid email"}).encode())
                return

            if not RESEND_API_KEY or not AUDIENCE_ID:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Email service not configured"}).encode())
                return

            response = add_contact(email)

            if response.get("id") or response.get("message") == "Contact already exists":
                send_welcome_email(email, source=source)

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
                self.wfile.write(json.dumps({"error": response.get("message") or response.get("error", "Unknown error")}).encode())

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
