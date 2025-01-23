"""
Pseudo-code:
    0. Connect to random proxy
    1. Open Web Browser
    2. Go to "https://www.instagram.com/accounts/emailsignup/"
    3. Reject cookies
    4. Call tempmail API
        4.1. Get an email address
    5. Generate a random password string
    6. Generate a random human Name
    7. Generate a random username
    8. Click next
    9. Click birth year dropdown
    10. Select a random year 18 or more years in the past
    11. Click next
    12. Wait for email-message
    13. Once detected, scan the email string for a 6 number combination
    14. Click next
    15. If banned, refresh proxy and retry steps 1 to 14
    16. Go to the profile url
    17. Click follow
    18. Refresh webpage
    19. Click button to view all reccomended
    20. Recopile profile urls and save them in a file
"""

from proxy import Proxy

proxy = Proxy()
cur_proxy = proxy.proxy

def proxy_connect():
    proxy.cycle()

    while proxy.test_proxy(cur_proxy) != 0:
        print("Failed to connect to proxy. Trying with another proxy...")

        if proxy.cycle() == 0:
            print("Could not find a valid proxy")
            return -1

    print("Succesfully connected to proxy")
    print("")
    return 0

def main():
    print("debug")
    proxy_connect()
    return 0

main()