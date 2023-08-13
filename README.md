# JSRegRecon: Sensitive Information Discovery Tool for Bug Bounty Hunters and Developers

## Introduction
JsRegRecon is an open-source tool designed to assist bug bounty hunters and developers in identifying sensitive information leaks within JavaScript (JS) files. This tool enhances the security of web applications by proactively detecting potential vulnerabilities that could lead to security breaches.

## Key Features
- **Efficient Detection:** Utilizes a customizable regex pattern to detect a wide range of sensitive information leaks in JS files.
- **Flexible Input Handling:** Accepts an input file containing URLs to JS files, accommodating various testing scenarios.
- **Automated Content Retrieval:** Fetches content from each URL for seamless analysis.
- **Detailed Reporting:** Provides detailed output for each sensitive pattern match.
- **Bug Bounty and Development:** Useful for bug bounty hunters and developers to uncover vulnerabilities and rectify leaks.

## Getting Started
1. Clone the JsRegRecon repository from GitHub.
2. Install required Python packages with `pip install -r requirements.txt`.
3. Prepare an input file (e.g., `js_links.txt`) with URLs of JS files to be scanned.

## Usage
Run the tool with the following command:

    python jsreg.py js_links.txt
    
### Output
````
Found sensitive information in: https://example.com/script.js

Pattern matched: (combined_regex_pattern)

Found sensitive information in: https://example.com/js/api.js

Pattern matched: (combined_regex_pattern)
````


## Benefits for Bug Bounty Hunters
- Enhanced Discovery: Comprehensive approach to identifying sensitive leaks.
- Time Efficiency: Automated content retrieval speeds up vulnerability identification.
- Wider Coverage: Extensive regex pattern for thorough analysis.

## Benefits for Developers
- Early Detection: Integrating JsRegRecon in development identifies leaks before production.
- Security by Design: Promotes security-first mindset among developers.
- Streamlined Review: Periodically scan codebase for sensitive leaks.

## Conclusion
JsRegRecon is a crucial tool for bug bounty hunters and developers, contributing to improved web application security. It automates sensitive information discovery in JS files, identifying vulnerabilities and enhancing overall security.

**Project Link:** [GitHub - JsRegRecon](https://github.com/syedalizain033/jsregrecon)

**Disclaimer:** JsRegRecon is intended for ethical security testing and research. Use responsibly, follow proper disclosure practices, and obtain authorization before testing on any web application. Authors and contributors are not liable for misuse or illegal activities.
