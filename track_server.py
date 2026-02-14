#!/usr/bin/env python3
"""
Track Web API
Flask backend for the Track web UI
"""

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import requests
import json
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    """Serve the main HTML file"""
    return send_file('track_ui.html')

@app.route('/api/ip/<ip_address>', methods=['GET'])
def track_ip(ip_address):
    """Track IP address and return detailed information"""
    try:
        response = requests.get(f"https://ipwho.is/{ip_address}", timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if not data.get('success', True):
            return jsonify({
                'success': False,
                'error': data.get('message', 'Invalid IP address')
            }), 400
        
        result = {
            'success': True,
            'data': {
                'ip': ip_address,
                'type': data.get('type', 'N/A'),
                'country': data.get('country', 'N/A'),
                'country_code': data.get('country_code', 'N/A'),
                'flag': data.get('flag', {}).get('emoji', ''),
                'city': data.get('city', 'N/A'),
                'region': data.get('region', 'N/A'),
                'continent': data.get('continent', 'N/A'),
                'latitude': data.get('latitude'),
                'longitude': data.get('longitude'),
                'maps_url': f"https://www.google.com/maps/@{data.get('latitude')},{data.get('longitude')},8z" if data.get('latitude') else None,
                'timezone': data.get('timezone', {}).get('id', 'N/A'),
                'timezone_offset': data.get('timezone', {}).get('offset', 'N/A'),
                'current_time': data.get('timezone', {}).get('current_time', 'N/A'),
                'isp': data.get('connection', {}).get('isp', 'N/A'),
                'org': data.get('connection', {}).get('org', 'N/A'),
                'asn': data.get('connection', {}).get('asn', 'N/A'),
                'domain': data.get('connection', {}).get('domain', 'N/A'),
                'postal': data.get('postal', 'N/A'),
                'calling_code': data.get('calling_code', 'N/A')
            }
        }
        return jsonify(result)
        
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': f'Network error: {str(e)}'
        }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Unexpected error: {str(e)}'
        }), 500

@app.route('/api/phone/<phone_number>', methods=['GET'])
def track_phone(phone_number):
    """Track phone number and return information"""
    try:
        default_region = "US"
        
        # Parse the phone number
        parsed = phonenumbers.parse(phone_number, default_region)
        
        # Validate the number
        if not phonenumbers.is_valid_number(parsed):
            return jsonify({
                'success': False,
                'error': 'Invalid phone number'
            }), 400
        
        # Get information
        region_code = phonenumbers.region_code_for_number(parsed)
        carrier_name = carrier.name_for_number(parsed, "en")
        location = geocoder.description_for_number(parsed, "en")
        timezones = timezone.time_zones_for_number(parsed)
        number_type = phonenumbers.number_type(parsed)
        
        # Determine type string
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            type_str = "Mobile"
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            type_str = "Fixed Line"
        else:
            type_str = "Unknown"
        
        result = {
            'success': True,
            'data': {
                'phone': phone_number,
                'valid': phonenumbers.is_valid_number(parsed),
                'possible': phonenumbers.is_possible_number(parsed),
                'international': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
                'e164': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164),
                'national': str(parsed.national_number),
                'country_code': f"+{parsed.country_code}",
                'region': region_code,
                'location': location if location else 'Unknown',
                'carrier': carrier_name if carrier_name else 'Unknown',
                'timezone': ', '.join(timezones) if timezones else 'Unknown',
                'type': type_str
            }
        }
        return jsonify(result)
        
    except phonenumbers.NumberParseException as e:
        return jsonify({
            'success': False,
            'error': f'Error parsing phone number: {str(e)}'
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Unexpected error: {str(e)}'
        }), 500

@app.route('/api/username/<username>', methods=['GET'])
def track_username(username):
    """Search for username across social media platforms"""
    try:
        platforms = [
            {"name": "GitHub", "url": "https://github.com/{}"},
            {"name": "Twitter", "url": "https://twitter.com/{}"},
            {"name": "Instagram", "url": "https://instagram.com/{}"},
            {"name": "LinkedIn", "url": "https://linkedin.com/in/{}"},
            {"name": "Reddit", "url": "https://reddit.com/user/{}"},
            {"name": "YouTube", "url": "https://youtube.com/@{}"},
            {"name": "TikTok", "url": "https://tiktok.com/@{}"},
            {"name": "Facebook", "url": "https://facebook.com/{}"},
            {"name": "Pinterest", "url": "https://pinterest.com/{}"},
            {"name": "Medium", "url": "https://medium.com/@{}"},
            {"name": "Twitch", "url": "https://twitch.tv/{}"},
            {"name": "Spotify", "url": "https://open.spotify.com/user/{}"},
        ]
        
        results = []
        found_count = 0
        
        for platform in platforms:
            url = platform['url'].format(username)
            try:
                response = requests.get(url, timeout=5, allow_redirects=True)
                found = response.status_code == 200
                if found:
                    found_count += 1
                
                results.append({
                    'platform': platform['name'],
                    'url': url,
                    'found': found
                })
            except:
                results.append({
                    'platform': platform['name'],
                    'url': url,
                    'found': False,
                    'error': True
                })
        
        return jsonify({
            'success': True,
            'data': {
                'username': username,
                'total_checked': len(platforms),
                'found_count': found_count,
                'platforms': results
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Unexpected error: {str(e)}'
        }), 500

@app.route('/api/myip', methods=['GET'])
def get_my_ip():
    """Get the client's public IP address"""
    try:
        # Try to get from request headers first (if behind proxy)
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        
        # Verify with external API
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        data = response.json()
        
        return jsonify({
            'success': True,
            'data': {
                'ip': data['ip']
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error getting IP: {str(e)}'
        }), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    print("=" * 60)
    print("🔍 Track Web Server Starting...")
    print("=" * 60)
    print("\n📡 Server running on: http://localhost:3000")
    print("🌐 Open your browser and visit: http://localhost:3000")
    print("\n💡 API Endpoints:")
    print("   GET  /api/ip/<ip_address>")
    print("   GET  /api/phone/<phone_number>")
    print("   GET  /api/username/<username>")
    print("   GET  /api/myip")
    print("\n⌨️  Press CTRL+C to stop the server")
    print("=" * 60)
    print()
    
    app.run(host='0.0.0.0', port=3000, debug=True)
