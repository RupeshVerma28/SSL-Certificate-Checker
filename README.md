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
-Launch the GUI.
-Enter a domain name (like google.com).
-Click “Check SSL Certificate”.
-View the results instantly in the app.
-Click “Download Report” to export a PDF.

## 📄 PDF Report Includes
-Domain Name
-Expiry Date & Remaining Days
-Issuer Organization
-Hostname Match Info
-Protocol Used (TLS version)
-Overall Validity Status ✅/❌

##📂 Folder Structure
```graphql
SSL-Certificate-Checker/
├── ssl_checker_tool.py        # Main Python GUI app
├── scan_report.pdf            # Output PDF report
├── README.md                  # Documentation
└── assets/
    └── screenshot.png         # GUI preview (optional)
```

---

## 🖼️ Screenshot

![image](https://github.com/user-attachments/assets/d6823e67-d73f-44fa-b74b-d31423057568)

---

## 🚧 Limitations

- Only supports **HTTPS** websites.
- Requires an **active internet connection**.
- Does **not validate wildcard certificates in-depth**.

---

## 📈 Future Enhancements

- Batch domain scanning.
- CSV & Excel export options.
- Certificate chain analysis.
- Notifications for expiry alerts.

---

## 🙋‍♂️ Author

- 👨‍💻 **Rupesh Verma**
- 🎓 *BCA | Full-Stack Developer | Cybersecurity Enthusiast*
- 📧 **Email:** errupesh28@gmail.com  
- 📞 **Phone:** +91-9340909789  
- 🌐 **GitHub:** [@RupeshVerma28](https://github.com/RupeshVerma28)
