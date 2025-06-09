# 🔐 Shinyeureka – SSH Log Parser

Analyze Linux `auth.log` files to detect brute-force SSH login attempts using Python.

---

## 📌 Features

- 📄 Reads standard Linux `auth.log` files
- 🔍 Detects repeated failed SSH login attempts
- 🧠 Uses regular expressions to extract attacker IPs
- 📊 Generates CSV report of brute-force attempts
- ✅ Simple, clean, and beginner-friendly code

---

## 📁 File Structure

shiny-eureka/ ├── Shinyeureka.py          # Main Python script ├── auth.log                # (Optional) Sample log file for testing └── bruteforce_report.csv   # Output CSV (generated after running script)

---

## 🚀 How to Use

1. 📥 **Clone repo / copy script**

git clone https://github.com/AnonNazi431/shiny-eureka.git cd shiny-eureka

2. 📂 **Place your log file**  
Save your `auth.log` file in the same directory.

3. ▶️ **Run the script**

python Shinyeureka.py

4. 📊 **View the result**  
Check the generated `bruteforce_report.csv` for list of suspicious IPs.

---

## 🧪 Sample Log Line Parsed

Failed password for root from 192.168.1.12 port 22 ssh2

This will be counted as one brute-force attempt from `192.168.1.12`.

---

## 💡 Future Improvements
- Add support for fail2ban-style log format
- Visualize attempts with charts (matplotlib)
- Auto-ban IPs with too many failed logins

---

## 👤 Author

**Wan Danial Aiman Bin Niraazwan**  
[LinkedIn](https://www.linkedin.com/in/wan-danial-aiman-bin-niraazwan-1b917b368)  
📧 wan.danial.azwan@gmail.com

---

## 📄 License

This project is licensed under the MIT License.
