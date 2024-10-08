# # Security Measures

## Django Settings

- **DEBUG = False**: Disables debug mode to prevent sensitive data leaks.
- **SECURE_BROWSER_XSS_FILTER = True**: Enables browser XSS filtering.
- **CSRF_COOKIE_SECURE = True**: Ensures CSRF cookies are sent over HTTPS.

## Content Security Policy (CSP)

- **CSP_DEFAULT_SRC = "'self'"**: Restricts all content to the same origin.
- **CSP_SCRIPT_SRC and CSP_STYLE_SRC**: Defines allowed sources for scripts and styles.

