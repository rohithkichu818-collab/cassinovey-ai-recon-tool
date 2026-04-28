import subprocess
import requests
import json
import os
import time
from datetime import datetime
# --- COLORS ---
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"
# --- CONFIGURATION ---
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "tinyllama"

def get_ai_analysis(url, status, server):
    prompt = f"""
    Target: {url}
    Status: {status}
    Server: {server}
    Task: Act as an expert Security Researcher. Provide 3 high-impact test cases for this specific target. 
    Focus on advanced bugs like SSRF, Business Logic flaws, or IDOR. 
    Format: Bullet points, max 50 words.
    """
    try:
        r = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream": False}, timeout=120)
        return r.json().get('response', 'Analysis failed.')
    except:
        return "AI Offline: Please ensure Ollama is running with 'ollama run tinyllama'."

def generate_report(results, domain):
    report_name = f"Cassinovey_{domain}_{datetime.now().strftime('%H%M')}.html"
    html_content = f"""
    <html>
    <head>
        <title>Cassinovey Scan Report: {domain}</title>
        <style>
            body {{ font-family: 'Inter', sans-serif; background: #0b0e14; color: #cfd8dc; padding: 40px; }}
            .container {{ max-width: 950px; margin: auto; }}
            .header {{ text-align: center; border-bottom: 2px solid #6366f1; padding-bottom: 20px; margin-bottom: 30px; }}
            h1 {{ color: #6366f1; letter-spacing: 2px; text-transform: uppercase; }}
            .card {{ background: #1a1f2e; padding: 25px; margin: 20px 0; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); border: 1px solid #2d3748; }}
            .url {{ font-size: 1.1em; color: #818cf8; font-weight: bold; }}
            .status-badge {{ background: #4338ca; color: white; padding: 3px 10px; border-radius: 5px; font-size: 0.9em; }}
            .ai-section {{ background: #0f172a; padding: 15px; border-radius: 8px; margin-top: 15px; border-left: 4px solid #6366f1; line-height: 1.6; }}
            .footer {{ text-align: center; margin-top: 60px; font-size: 0.8em; color: #4b5563; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Cassinovey</h1>
                <p>Advanced AI Reconnaissance & Vulnerability Prioritization</p>
            </div>
            <p><strong>Scan Results for:</strong> {domain} | <strong>Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
    """
    
    for res in results[:5]:
        html_content += f"""
        <div class="card">
            <div class="url">{res['url']}</div>
            <div style="margin-top: 10px;">
                <span class="status-badge">HTTP {res['status']}</span> 
                <span style="margin-left: 15px; color: #94a3b8;">Server: {res['server']}</span>
            </div>
            <div class="ai-section">
                <strong>Cassinovey Intelligence Insight:</strong><br>
                {res['insight'].replace('\n', '<br>')}
            </div>
        </div>
        """
    
    html_content += """
            <div class="footer">Developed by Rohith PR | Powered by Cassinovey Engine</div>
        </div>
    </body>
    </html>
    """
    
    with open(report_name, "w") as f:
        f.write(html_content)
    return report_name

def main():
    print(rf"""
{CYAN}  ____              _                               
 / ___|__ _ ___ ___(_)_ __   _____   _____ _   _ 
| |   / _` / __/ __| | '_ \ / _ \ \ / / _ \ | | |
| |__| (_| \__ \__ \ | | | | (_) \ V /  __/ |_| |
 \____\__,_|___/___/_|_| |_|\___/ \_/ \___|\__, |
                                           |___/ {RESET}
{YELLOW} ---------------------------------------------------
{GREEN}  Advanced AI Reconnaissance Tool by Rohith PR
{YELLOW} ---------------------------------------------------{RESET}
    """)
    
    domain = input("Enter Target Domain (e.g. example.com): ").strip()
    
    if not domain:
        print("[!] Domain cannot be empty.")
        return

    try:
        # 1. Subdomain Discovery
        print(f"\n[+] Cassinovey is hunting for subdomains on {domain}...")
        sub_raw = subprocess.check_output(f"subfinder -d {domain} -silent", shell=True).decode().splitlines()
        
        if not sub_raw:
            print("[!] No subdomains found.")
            return

        with open("temp_recon.txt", "w") as f: f.write("\n".join(sub_raw))
        
        # 2. Service Probing
        print("[+] Probing live services with HTTPX...")
        httpx_raw = subprocess.check_output("httpx -l temp_recon.txt -silent -status-code -web-server -json", shell=True).decode().splitlines()
        
        final_data = []
        for line in httpx_raw:
            data = json.loads(line)
            url, status, server = data.get("url"), data.get("status_code"), data.get("webserver", "Unknown")
            
            print(f"[*] Analyzing: {url}")
            # AI വിശകലനം ഇവിടെ നടക്കുന്നു
            insight = get_ai_analysis(url, status, server)
            
            final_data.append({
                "url": url,
                "status": status,
                "server": server,
                "insight": insight
            })
        
        # 3. Final Report
        if final_data:
            report_file = generate_report(final_data, domain)
            print(f"\n[DONE] Scan finished successfully.")
            print(f"[REPORT] Cassinovey report generated: {report_file}")
        
    except Exception as e:
        print(f"\n[X] Error: {e}")
    finally:
        if os.path.exists("temp_recon.txt"): os.remove("temp_recon.txt")

if __name__ == "__main__":
    main()    
