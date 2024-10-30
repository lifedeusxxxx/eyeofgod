from flask import Flask, render_template, request, jsonify
from utils.nmap_utils import scan_ip
from utils.nikto_utils import scan_web_server
from utils.report_utils import generate_report

app = Flask(__name__)

# Página inicial com as opções de análise
@app.route('/')
def index():
    return render_template('index.html')

# Executa uma varredura com Nmap
@app.route('/nmap_scan', methods=['POST'])
def nmap_scan():
    ip_address = request.form.get('ip')
    scan_results = scan_ip(ip_address)
    return render_template('results.html', tool="Nmap", results=scan_results)

# Executa uma varredura com Nikto
@app.route('/nikto_scan', methods=['POST'])
def nikto_scan():
    ip_address = request.form.get('ip')
    nikto_results = scan_web_server(ip_address)
    return render_template('results.html', tool="Nikto", results=nikto_results)

# Página de estatísticas
@app.route('/statistics')
def statistics():
    stats = generate_report()
    return render_template('statistics.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
