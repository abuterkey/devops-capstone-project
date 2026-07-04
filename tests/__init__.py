# __init__.py (or int-.py if you really want that name)
from flask import Flask
from flask_talisman import Talisman

# Strict Content Security Policy
csp = {
    'default-src': [
        "'self'"
    ],
    'script-src': [
        "'self'",
        "'strict-dynamic'",
        "'nonce-123456'",
    ],
    'style-src': [
        "'self'",
        "'unsafe-inline'",
    ],
    'img-src': [
        "'self'",
        "data:",
    ],
    'connect-src': [
        "'self'"
    ],
}

def create_app():
    app = Flask(__name__)

    # Basic secure defaults
    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
    )

    # Talisman configuration
    Talisman(
        app,
        content_security_policy=csp,
        force_https=True,
        strict_transport_security=True,
        strict_transport_security_max_age=31536000,  # 1 year
        strict_transport_security_include_subdomains=True,
        frame_options="DENY",
        x_xss_protection=True,
        x_content_type_options=True,
        referrer_policy="no-referrer",
        session_cookie_secure=True,
    )

    @app.route("/")
    def index():
        return "CI + Talisman security headers configured."

    return app


# For local run: python int-.py
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=False)
