# 🌐 DNS Recursive Resolver

A Python-based recursive DNS resolver that simulates the full domain resolution process (Root ➝ TLD ➝ Authoritative DNS servers) and implements caching to optimize speed and reduce redundant traffic.

---

## 📄 Project Overview

This project demonstrates how a recursive DNS resolver works, replicating real DNS behavior by:
- Validating user input (domain names)
- Simulating traversal from Root to TLD to Authoritative servers
- Implementing in-memory and file-based caching
- Logging DNS lookups
- Opening resolved IPs in a browser (simulated access)

---

## ⚙️ Technologies Used

- Python 3
- `dnspython`
- `socket`
- `ipaddress`
- `os`, `time`, `webbrowser`
- Optional DB support: `PyMySQL` (for advanced caching)

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Ravendrannamogar/dns-recursive-resolver.git
   cd dns-recursive-resolver
2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the resolver:
    ```bash
    python dns_resolver.py

---

## 📘 Documents

- 📄 DNS Resolver Project Report (DOCX)
- 📄 DNS Recursive Querying Research Paper (DOCX)


## 📊 Output Highlights

- Average latency without cache: ~150ms
- With cache enabled: ~50ms
- Cache hit ratio: Up to 85%
The project shows how optimized caching drastically improves DNS performance.


## 📈 Future Enhancements

- Machine learning-based query prediction
- Real-time monitoring dashboard
- DNSSEC validation implementation
- Full MySQL backend caching with TTL expiry


## 🧠 Author

- Ravendran Manogar
- B.Tech Final Year Project


## 📌 License

- This project is open for educational and academic use. Attribution appreciated.

