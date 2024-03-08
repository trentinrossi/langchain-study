from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/clean', methods=['POST'])
def clean_joke():
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        abort(403)  # Forbidden

    api_key = auth_header.split(' ')[1]  # get the token part from the header

    data = request.get_json()

    correct_api_key = 'your_mom'  # Replace it with your actual api key.
    if api_key != correct_api_key:
        abort(403)  # Forbidden

    joke = data.get('joke', '')
    return joke

@app.route('/privacy', methods=['GET'])
def privacy_policy():
    return """Privacy Policy for JokeGPT OpenAI Plugin

Effective Date: Sunday November 12th, 2023

This Privacy Policy describes the types of information Saxifrage, LLC (“We”, “us”, or “our”) gathers when you use our OpenAI plugin, and how we use, process, and disclose that information.

1. What kind of information we collect

   Personal Information: We may collect personal information you voluntarily provide us when you are signing up or using our service. This can include your name, email, and other contact details.

  Non-Personal Information: We may collect information about your usage behavior, browser type, operating system, IP address, and other non-identifiable data.

2. How we use the information

  We use the personal information you provide to deliver you the service, customize your experience, and communicate with you about product updates or service alterations.

  Non-personal data is used to diagnose system problems, manage the plugin, and gain statistical information to improve our services.

3. Disclosure of Information

  We don't sell, rent, or share your data with third parties without your explicit consent unless required by law or to protect our rights.

4. Data Retention

  We only retain your personal data for as long as necessary to provide functionality of our OpenAI plugin, and as required by applicable laws or regulations.

5. Children’s Privacy Protection

  Our OpenAI plugin is not designed for or targeted at children. We do not knowingly collect or process personal data from individuals under 16 years of age.

6. Security

  We use industry-standard methods and tools to protect your data from unauthorized access, use, or disclosure. However, no method of transmission or storage is 100% secure.

7. Changes to This Privacy Policy

  We may update our Privacy Policy as our practices change or as we change existing services, add new services, or develop better ways to inform you about the use of your data.

8. Contact Us

  If you have any questions regarding our Privacy Policy, you can contact us at https://twitter.com/hammer_mt."""

