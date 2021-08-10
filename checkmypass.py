import requests  # must be installed pip install requests
import hashlib
import sys

"""
Check if passwords have been hacked. Uses the pwned API database.
Usage: python3 checkmypass.py password1 password_2 "!password3"
"""

# K anonymity: - only give first 5 chars of hashed password
# password_123 SHA1 is 4dfd0d9665c9f63e437e054f57d4407867dacce5


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)  # response
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}. Check the API and try again.')
    return res


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())  # generates a list of hash, count tuples
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check password if it exists in API response.
    # API requires utf-8 encoded string, SHA1 hash digested as hex string upper case
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)  # send API first 5 chars of hex string only
    # print('Response from pwned: ' + str(response))  # API responds with tails of SHA1 with count > 0
    return get_password_leak_count(response, tail)


def main(args):
        for password in args:
            print(f'Checking pwned for instance of: {password}')
            count = pwned_api_check(password)
            if count:
                print(f'Your password has been hacked {count} times. Consider changing your password!')
            else:
                print('Good news. Your password does not appear on the list of hacked passwords.')
        return 'Done.'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        sys.exit(main(sys.argv[1:]))
    else:
        raise SyntaxError("No passwords to check. Please list passwords after the checkmypass command")
