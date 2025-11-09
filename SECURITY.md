# Security Policy

## Supported Versions

We actively support the following versions of gprint with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 0.0.9   | :white_check_mark: |
| < 0.0.9 | :x:                |

## Supported Python Versions

gprint officially supports the following Python versions:

- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13

## Reporting a Vulnerability

We take the security of gprint seriously. If you believe you have found a security vulnerability in gprint, please report it to us as described below.

### How to Report a Security Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please send an email to [guillermo@guillerpsanchez.dev](mailto:guillermo@guillerpsanchez.dev).

You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

Please include the following information in your report:

- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### What to Expect

After you submit a report, we will:

1. Confirm receipt of your vulnerability report
2. Assess the vulnerability and determine its severity
3. Work on a fix and prepare a security advisory
4. Release a patched version
5. Publicly disclose the vulnerability after the patch is released

## Security Best Practices

When using gprint in your projects:

- Always use the latest version of gprint
- Keep your Python version up to date
- Review the changelog for security-related updates
- Use virtual environments to isolate dependencies

## Security Scanning

This project uses:

- **CodeQL**: Automated security scanning for code vulnerabilities
- **Dependabot**: Automated dependency updates to address known vulnerabilities
- **GitHub Actions**: Automated testing across multiple Python versions

## Disclosure Policy

We follow the principle of responsible disclosure and will:

- Acknowledge receipt of security reports within 48 hours
- Provide regular updates on our progress
- Credit reporters in security advisories (unless anonymity is requested)
- Release security patches as quickly as possible

## Comments on this Policy

If you have suggestions on how this policy could be improved, please submit a pull request or open an issue.
