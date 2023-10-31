import subprocess

# Function to get WiFi profiles
def get_wifi_profiles():
    data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    return profiles

# Function to get password for a profile
def get_password(profile):
    results = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode("utf-8").split("\n")
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    return results[0] if results else ""

# Main function to print WiFi names and passwords
def print_wifi_passwords():
    profiles = get_wifi_profiles()
    for profile in profiles:
        password = get_password(profile)
        print("{:<30}|  {:<}".format(profile, password))

# Call the main function
print_wifi_passwords()
