import dns.resolver
import ipaddress
import dns.name
import webbrowser

def is_valid_domain(domain_name):
    try:
        dns.name.from_text(domain_name)
        return True
    except Exception:
        return False

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

class DNSResolver:
    def __init__(self):
        self.cache = {}

    def query(self, domain):
        if domain in self.cache:
            print(f"DNS Resolver: Cached response found for {domain}: {self.cache[domain]}")
            return self.cache[domain]

        # Perform the DNS resolution process
        ip_address = self._recursive_query(domain)
        if ip_address:
            self.cache[domain] = ip_address
            self._save_to_file(domain, ip_address)  # Save resolved IP to the file
        return ip_address

    def _recursive_query(self, domain):
        print(f"Client: Requesting IP for {domain}")

        # Simulate Root DNS Server (Return the TLD part of the domain)
        tld = RootDNSServer().query(domain)
        print(f"Root DNS Server: Received query for {domain}. Returning TLD: {tld}")

        # Simulate TLD DNS Server (Return the full domain to query)
        auth_server_domain = TLDServer().query(domain)
        print(f"TLD DNS Server: Received query for {tld}. Returning authoritative server domain: {auth_server_domain}")

        # Query the authoritative server (actual DNS query to resolve IP)
        ip_address = AuthoritativeDNSServer().query(auth_server_domain)
        if ip_address:
            print(f"Authoritative DNS Server: Received query for {auth_server_domain}. Returning IP address: {ip_address}")
        else:
            print(f"Authoritative DNS Server: No IP address found for {auth_server_domain}")
            return None

        print(f"Client: Received IP for {domain}: {ip_address}")
        print(f"Client: Sending HTTP request to {ip_address}\n")
        return ip_address

    def _save_to_file(self, domain, ip_address):
        # Save the resolved domain and IP address to a file
        with open("dns_cache.txt", "a") as file:
            file.write(f"{domain}: {ip_address}\n")
        print(f"DNS Resolver: Saved {domain}: {ip_address} to dns_cache.txt")

class RootDNSServer:
    def query(self, domain):
        # Return the TLD of the domain
        return domain.split('.')[-1]

class TLDServer:
    def query(self, domain):
        # Return the full domain as the authoritative server for simplicity
        return domain

class AuthoritativeDNSServer:
    def query(self, domain):
        # Perform actual DNS query to get IP address
        try:
            resolver = dns.resolver.Resolver()
            answers = resolver.resolve(domain, 'A')  # Query for A record (IPv4 address)
            return answers[0].address
        except dns.resolver.NoAnswer:
            print(f"No answer for {domain}")
            return None
        except dns.resolver.NXDOMAIN:
            print(f"Domain {domain} does not exist")
            return None
        except Exception as e:
            print(f"An error occurred while querying authoritative server: {e}")
            return None

# User input
def main():
    dns_resolver = DNSResolver()

    while True:
        domain_name = input("Enter the domain name to query (or type 'exit' to quit): ")
        if domain_name.lower() == 'exit':
            break
        if not is_valid_domain(domain_name):
            print("Invalid domain name format.")
        else:
            ip_address = dns_resolver.query(domain_name)
            if ip_address:
                print(f"Final IP address for {domain_name}: {ip_address}")
                # Open the resolved IP address in the browser
                webbrowser.open(f"http://{ip_address}")
            else:
                print(f"Could not resolve IP address for {domain_name}")

if __name__ == "__main__":
    main()
