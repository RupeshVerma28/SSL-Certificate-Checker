import customtkinter as ctk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from datetime import datetime
import ssl, socket

# Initialize GUI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("SSL Certificate Checker")
app.geometry("500x550")

ssl_result_data = {}

# Function to get SSL certificate info
def get_ssl_info(domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            return {
                "Domain": domain,
                "Issuer": dict(x[0] for x in cert['issuer']).get('organizationName', 'N/A'),
                "Valid From": cert['notBefore'],
                "Valid To": cert['notAfter'],
                "Expired": datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z") < datetime.utcnow()
            }

# Function to generate PDF report
def generate_pdf(data, filename="ssl_report.pdf"):
    c = canvas.Canvas(filename)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "SSL Certificate Report")
    c.setFont("Helvetica", 12)
    y = 750
    for k, v in data.items():
        c.drawString(100, y, f"{k}: {v}")
        y -= 25
    c.save()

# Callback for Check SSL button
def check_ssl():
    global ssl_result_data
    domain = domain_entry.get().strip()
    if not domain:
        messagebox.showerror("Error", "Please enter a domain name.")
        return
    try:
        result = get_ssl_info(domain)
        ssl_result_data = result
        result_textbox.configure(state="normal")
        result_textbox.delete("1.0", ctk.END)
        for key, value in result.items():
            result_textbox.insert(ctk.END, f"{key}: {value}\n")
        result_textbox.configure(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Callback for Download Report button
def download_report():
    if not ssl_result_data:
        messagebox.showerror("Error", "No data to generate report. Please check SSL first.")
        return
    try:
        generate_pdf(ssl_result_data)
        messagebox.showinfo("Success", "Report downloaded as ssl_report.pdf")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {e}")

# GUI Components
ctk.CTkLabel(app, text="🔐 Website SSL Certificate Checker", font=("Arial", 18, "bold")).pack(pady=20)

ctk.CTkLabel(app, text="Enter Domain:").pack()
domain_entry = ctk.CTkEntry(app, width=400)
domain_entry.pack(pady=10)

ctk.CTkButton(app, text="Check SSL", command=check_ssl).pack(pady=10)

result_textbox = ctk.CTkTextbox(app, height=200, width=450)
result_textbox.pack(pady=10)
result_textbox.configure(state="disabled")

ctk.CTkButton(app, text="Download Report", command=download_report).pack(pady=10)

app.mainloop()
