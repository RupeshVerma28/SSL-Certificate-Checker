# 🔐 SSL Certificate Checker Tool – Python GUI with Report Generation

A modern Python-based **SSL Certificate Checker** that allows users to verify the security and validity of any website's SSL certificate using a GUI interface. It provides **detailed results** and supports exporting scan reports as professional **PDF documents**.

> ✅ Built using **CustomTkinter** (dark mode GUI) and **ReportLab** for PDF reports  
> 🔗 GitHub: [RupeshVerma28/SSL-Certificate-Checker](https://github.com/RupeshVerma28/SSL-Certificate-Checker/tree/main)

---

## 🧭 Overview

This tool is perfect for:
- Ethical hackers and cybersecurity learners
- Web developers validating site certificates
- Students building security-focused Python projects

It fetches SSL certificate information of any website (domain), analyzes it for key details such as:
- Expiry Date
- Issuer Authority
- Hostname Match
- Protocol Strength
- Validity Status

You can also **download a full PDF report** with all this information.

---

## ✨ Features

| Feature                       | Description |
|------------------------------|-------------|
| 🌐 SSL Domain Scan            | Check SSL details of any HTTPS domain |
| 🧾 PDF Report Export          | Generate downloadable PDF report |
| ⚙️ CustomTkinter GUI          | Clean and modern dark-mode interface |
| ✅ Live Domain Verification   | Real-time result fetching |
| 📌 Certificate Expiry Alerts  | Warns if certificate is expired or about to |
| 🧠 Smart Validation           | Domain and hostname match analysis |

---

## 📦 Tech Stack

- **Python 3.8+**
- `customtkinter` – for modern GUI
- `ssl`, `socket`, `datetime` – for SSL analysis
- `reportlab` – for PDF generation
- `tkinter.filedialog`, `os`, `re`, `pandas` (optional)

---

## 🛠 Installation

> ✅ Python 3.8 or newer is recommended.

### 1. Clone the Repository

```bash
git clone https://github.com/RupeshVerma28/SSL-Certificate-Checker.git
cd SSL-Certificate-Checker
```
## 2. Install the Required Libraries 
```bash
pip install customtkinter reportlab
pip install customtkinter reportlab
```
## 3. How to run
```bash
python ssl_checker_tool.py
```
## 🖥️ Usage Instructions
1.Launch the GUI.
2.Enter a domain name (like google.com).
3.Click “Check SSL Certificate”.
4.View the results instantly in the app.
5.Click “Download Report” to export a PDF.

## 📄 PDF Report Includes
1.Domain Name
2.Expiry Date & Remaining Days
3.Issuer Organization
4.Hostname Match Info
5.Protocol Used (TLS version)
6.Overall Validity Status ✅/❌

##📂 Folder Structure
```graphql
SSL-Certificate-Checker/
├── ssl_checker_tool.py        # Main Python GUI app
├── scan_report.pdf            # Output PDF report
├── README.md                  # Documentation
└── assets/
    └── screenshot.png         # GUI preview (optional)
```

##🖼️ Screenshot
![image](https://github.com/user-attachments/assets/34a9c64d-1331-4dfb-8273-6cb345c97c2c)

##🚧 Limitations
1.Only supports HTTPS websites.
2.Requires internet connection.
3.Does not validate wildcard certificates in-depth.

##📈 Future Enhancements
 1.Batch domain scanning
 2.CSV & Excel export options
 3.Certificate chain analysis
 4.Notifications for expiry alerts

##🙋‍♂️ Author
👨‍💻 Rupesh Verma 
🎓BCA| Full-stack Developer | Cybersecurity Enthusiast
📧 errupesh28@gmail.com
📞 +91-9340909789
🌐 GitHub – @RupeshVerma28

