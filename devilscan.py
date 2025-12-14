#!/usr/bin/env python3
"""
🔥⚡☠️ DEVILSCAN v4.0 - THE ULTIMATE HACKER-MIND AUDITOR ☠️⚡🔥
Created by: The Devil's Advocate (World's #1 Ethical Hacker)
For authorized security testing ONLY!
"""

import sys
import os
import json
import time
import socket
import ssl
import hashlib
import re
import ipaddress
import subprocess
import concurrent.futures
import random
import base64
import zlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set, Any
from dataclasses import dataclass, asdict, field
from enum import Enum, auto
import urllib.parse
import urllib.request
import urllib.error
import http.client
import xml.etree.ElementTree as ET
import html

# ========== 🔥 DEMON ENGINE CONFIGURATION 🔥 ==========
class DemonMode:
    STEALTH = "stealth"        # Like a ninja
    AGGRESSIVE = "aggressive"  # Like a pentester
    APOCALYPSE = "apocalypse"  # Like a nation-state hacker

# ========== 🔥 ASCII DEMON ART 🔥 ==========
DEMON_ASCII = r"""
╔═══════════════════════════════════════════════════════════════╗
║  ██████╗ ███████╗██╗   ██╗██╗██╗     ███████╗██╗  ██╗██╗███╗   ██╗  ║
║  ██╔══██╗██╔════╝██║   ██║██║██║     ██╔════╝██║  ██║██║████╗  ██║  ║
║  ██║  ██║█████╗  ██║   ██║██║██║     ███████╗███████║██║██╔██╗ ██║  ║
║  ██║  ██║██╔══╝  ╚██╗ ██╔╝██║██║     ╚════██║██╔══██║██║██║╚██╗██║  ║
║  ██████╔╝███████╗ ╚████╔╝ ██║███████╗███████║██║  ██║██║██║ ╚████║  ║
║  ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝  ║
║                                                                   ║
║                ╔═╗┬ ┬┌─┐┌─┐┬┌─  ╦ ╦┌─┐┌─┐┌─┐┬┌─┐                ║
║                ╠═╝│ │├┤ ├─┤├┴┐  ║║║├┤ ├─┤│  │└─┐                ║
║                ╩  └─┘└─┘┴ ┴┴ ┴  ╚╩╝└─┘┴ ┴└─┘┴└─┘                ║
║                                                                   ║
║       THINK LIKE A HACKER, DEFEND LIKE A DEMON, WIN EVERY TIME   ║
╚═══════════════════════════════════════════════════════════════╝
"""

# ========== 🔥 TERMINAL COLORS - DEMON EDITION 🔥 ==========
class DemonColors:
    # Core Colors
    BLOOD_RED = '\033[38;5;196m'
    HELLFIRE = '\033[38;5;202m'
    DEMON_PURPLE = '\033[38;5;93m'
    TOXIC_GREEN = '\033[38;5;46m'
    ABYSS_BLUE = '\033[38;5;21m'
    SOUL_WHITE = '\033[38;5;255m'
    SHADOW_GRAY = '\033[38;5;240m'
    GOLD = '\033[38;5;220m'
    
    # Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # Effects
    GLITCH = '\033[8m'
    
    END = '\033[0m'
    
    @staticmethod
    def demon_print(text: str, color: str = BLOOD_RED, style: str = BOLD, end: str = "\n"):
        """Print with demon styling"""
        sys.stdout.write(f"{style}{color}{text}{DemonColors.END}{end}")
        sys.stdout.flush()
    
    @staticmethod
    def print_header(text: str):
        """Print section header"""
        print(f"\n{DemonColors.BOLD}{DemonColors.HELLFIRE}{'═'*70}{DemonColors.END}")
        print(f"{DemonColors.BOLD}{DemonColors.GOLD}🔥 {text} 🔥{DemonColors.END}")
        print(f"{DemonColors.BOLD}{DemonColors.HELLFIRE}{'═'*70}{DemonColors.END}")

# ========== 🔥 SEVERITY LEVELS - HACKER EDITION 🔥 ==========
class HackSeverity(Enum):
    ZERO_DAY = ("💀 ZERO-DAY", 10.0)      # Unknown to vendor
    APOCALYPSE = ("🔥 APOCALYPSE", 9.8)   # Remote code execution
    CRITICAL = ("☠️ CRITICAL", 9.0)      # Complete compromise
    HIGH = ("⚡ HIGH", 7.5)              # Significant access
    MEDIUM = ("⚠️ MEDIUM", 5.0)          # Limited access
    LOW = ("🔶 LOW", 3.0)                # Information leak
    INFO = ("ℹ️ INFO", 0.0)              # Recon only

# ========== 🔥 FINDING DATA STRUCTURE 🔥 ==========
@dataclass
class DemonFinding:
    id: str
    module: str
    title: str
    severity: HackSeverity
    description: str
    evidence: str
    recommendation: str
    exploit_vector: str = ""
    cvss_vector: str = ""
    attack_complexity: str = "Low"
    privileges_required: str = "None"
    user_interaction: str = "None"
    impact_confidentiality: str = "High"
    impact_integrity: str = "High"
    impact_availability: str = "High"
    discovered: str = field(default_factory=lambda: datetime.now().isoformat())
    cwe_ids: List[str] = field(default_factory=list)
    owasp_top_10: List[str] = field(default_factory=list)
    mitre_attacks: List[str] = field(default_factory=list)
    poc_code: str = ""
    remediation_time: str = "24 hours"
    business_impact: str = "Critical"

# ========== 🔥 MAIN DEMON ENGINE 🔥 ==========
class DevilScanEngine:
    def __init__(self, mode: str = DemonMode.AGGRESSIVE):
        self.mode = mode
        self.target_url = ""
        self.target_domain = ""
        self.target_ip = ""
        self.target_ips: List[str] = []
        self.findings: List[DemonFinding] = []
        self.session_cookies = {}
        self.session_headers = {}
        self.technologies: Dict[str, List[str]] = {}
        self.open_ports: Dict[int, str] = {}
        self.discovered_paths: List[str] = []
        self.subdomains: Set[str] = set()
        self.api_endpoints: List[str] = []
        
        # 🔥 Hacker Configuration 🔥
        self.config = {
            'user_agents': [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'curl/7.88.1',
                'python-requests/2.31.0',
                'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
                'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)'
            ],
            
            'ports': {
                'web': [80, 443, 8080, 8443, 8000, 8008, 8888, 3000, 5000, 9000],
                'database': [3306, 5432, 27017, 6379, 9200, 11211, 1433, 1521, 2638],
                'admin': [22, 21, 23, 3389, 5900, 5985, 5986, 10000, 8291],
                'services': [25, 53, 110, 143, 465, 587, 993, 995, 161, 162],
                'dev': [3000, 4200, 5000, 9000, 9229, 35729],
                'cloud': [2375, 2376, 2377, 2379, 2380, 4001, 7001]
            },
            
            'path_wordlist': [
                # Admin & Login
                '/admin', '/administrator', '/wp-admin', '/wp-login.php', '/login', '/signin',
                '/dashboard', '/controlpanel', '/cpanel', '/whm', '/webmin', '/plesk',
                
                # Configuration Files
                '/.env', '/config.json', '/config.php', '/config.yml', '/config.yaml',
                '/application.yml', '/application.properties', '/settings.py',
                '/web.config', '/.htaccess', '/.htpasswd', '/robots.txt',
                
                # Source Code & Git
                '/.git/HEAD', '/.git/config', '/.git/index', '/.git/logs/HEAD',
                '/.svn/entries', '/.svn/wc.db', '/.DS_Store', '/Thumbs.db',
                
                # Backup Files
                '/backup.zip', '/backup.tar.gz', '/backup.sql', '/dump.sql',
                '/database.sql', '/backup.rar', '/backup.7z', '/backup.tar',
                
                # Debug & Info
                '/phpinfo.php', '/info.php', '/test.php', '/debug.php',
                '/console', '/_profiler/phpinfo', '/actuator/health',
                '/actuator/env', '/actuator/gateway/routes',
                
                # API Endpoints
                '/api/', '/api/v1/', '/api/v2/', '/graphql', '/graphiql',
                '/swagger-ui.html', '/swagger.json', '/openapi.json',
                '/api/docs', '/api/documentation',
                
                # Framework Specific
                '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php',
                '/_ignition/execute-solution',
                '/debug/default/view',
                '/api/jsonws/invoke',
                '/jmx-console/',
                '/web-console/',
                
                # Sensitive Directories
                '/uploads/', '/images/', '/downloads/', '/private/',
                '/secret/', '/hidden/', '/confidential/', '/secure/',
                
                # Common Files
                '/readme.md', '/LICENSE', '/CHANGELOG', '/version',
                '/sitemap.xml', '/sitemap.txt', '/sitemap.html',
                
                # Wordpress Specific
                '/wp-config.php', '/wp-content/uploads/',
                '/xmlrpc.php', '/wp-json/wp/v2/users/'
            ],
            
            'subdomain_wordlist': [
                'www', 'mail', 'ftp', 'admin', 'test', 'dev', 'staging',
                'api', 'secure', 'vpn', 'portal', 'cpanel', 'webmail',
                'blog', 'shop', 'store', 'app', 'mobile', 'static',
                'cdn', 'assets', 'media', 'img', 'images', 'js', 'css',
                'beta', 'alpha', 'demo', 'sandbox', 'lab', 'test',
                'internal', 'private', 'secret', 'hidden', 'legacy',
                'old', 'new', 'temp', 'tmp', 'backup', 'archive'
            ],
            
            'tech_signatures': {
                'wordpress': ['wp-content', 'wp-includes', 'wp-json', 'xmlrpc.php'],
                'joomla': ['joomla', 'media/jui/', 'templates/system/'],
                'drupal': ['sites/default/', 'misc/drupal.js', 'core/misc/'],
                'laravel': ['csrf-token', 'XSRF-TOKEN', '/storage/'],
                'django': ['admin/login/', 'static/admin/', 'csrfmiddlewaretoken'],
                'rails': ['assets/rails.png', 'javascripts/rails.js'],
                'react': ['react', 'react-dom', '__NEXT_DATA__'],
                'vue': ['vue', 'vue-router', 'vuex'],
                'angular': ['ng-', 'angular', 'zone.js'],
                'nginx': ['nginx/', 'X-Powered-By: nginx'],
                'apache': ['Apache/', 'X-Powered-By: Apache'],
                'iis': ['Microsoft-IIS/', 'X-Powered-By: ASP.NET'],
                'php': ['X-Powered-By: PHP', '.php'],
                'nodejs': ['X-Powered-By: Express', 'X-Powered-By: node.js']
            },
            
            'header_checks': {
                'HSTS': 'strict-transport-security',
                'CSP': 'content-security-policy',
                'X-Frame-Options': 'x-frame-options',
                'X-Content-Type-Options': 'x-content-type-options',
                'Referrer-Policy': 'referrer-policy',
                'Permissions-Policy': 'permissions-policy',
                'X-XSS-Protection': 'x-xss-protection',
                'Cache-Control': 'cache-control'
            }
        }
        
        # Setup workspace
        self.setup_demon_workspace()
        
        # Attack vectors
        self.attack_vectors = {
            'sqli_patterns': [
                "'", "\"", "`", " OR ", " AND ", " UNION ", " SELECT ", " FROM ",
                "WHERE ", "CONCAT", "LOAD_FILE", "INTO OUTFILE", "EXEC", "EXECUTE",
                "WAITFOR DELAY", "SLEEP(", "BENCHMARK", "pg_sleep"
            ],
            'xss_patterns': [
                "<script>", "javascript:", "onerror=", "onload=", "onclick=",
                "onmouseover=", "alert(", "confirm(", "prompt(", "eval(",
                "document.cookie", "window.location", "localStorage"
            ],
            'lfi_patterns': [
                "../../", "../", "..\\", "/etc/passwd", "/etc/shadow",
                "/proc/self/environ", "C:\\Windows\\", "..//", "....//"
            ],
            'rce_patterns': [
                ";", "|", "`", "$(", "${{", "||", "&&", ">", "<",
                "system(", "exec(", "shell_exec(", "passthru(",
                "popen(", "proc_open(", "pcntl_exec("
            ]
        }
    
    def setup_demon_workspace(self):
        """Create hacker workspace"""
        home = Path.home()
        self.workspace = home / ".devil_lair"
        self.reports_dir = self.workspace / "reports"
        self.loot_dir = self.workspace / "loot"
        self.scans_dir = self.workspace / "scans"
        self.logs_dir = self.workspace / "logs"
        
        for d in [self.workspace, self.reports_dir, self.loot_dir, self.scans_dir, self.logs_dir]:
            d.mkdir(exist_ok=True)
        
        self.scan_id = f"devil_scan_{int(time.time())}_{random.randint(1000, 9999)}"
        self.log_file = self.logs_dir / f"{self.scan_id}.log"
    
    def demon_log(self, message: str, level: str = "INFO", emoji: str = "👹"):
        """Log with hacker style"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if level == "SUCCESS":
            color = DemonColors.TOXIC_GREEN
        elif level == "ERROR":
            color = DemonColors.BLOOD_RED
        elif level == "WARNING":
            color = DemonColors.HELLFIRE
        elif level == "DEBUG":
            color = DemonColors.SHADOW_GRAY
        else:
            color = DemonColors.SOUL_WHITE
        
        log_msg = f"{emoji} [{timestamp}] [{level}] {message}"
        DemonColors.demon_print(log_msg, color)
        
        # Write to log file
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_msg + "\n")
    
    def demon_request(self, url: str, method: str = "GET", 
                     headers: Dict = None, data: Any = None,
                     timeout: int = 10) -> Optional[Dict]:
        """Make HTTP request like a hacker"""
        try:
            # Random delay for stealth
            if self.mode == DemonMode.STEALTH:
                time.sleep(random.uniform(0.5, 2.0))
            elif self.mode == DemonMode.APOCALYPSE:
                time.sleep(0.1)
            else:
                time.sleep(random.uniform(0.2, 0.5))
            
            if not url.startswith(('http://', 'https://')):
                url = f"https://{url}" if ':443' in self.target_url else f"http://{url}"
            
            req = urllib.request.Request(url, method=method, data=data)
            
            # Random user agent
            req.add_header('User-Agent', random.choice(self.config['user_agents']))
            
            # Add headers
            req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
            req.add_header('Accept-Language', 'en-US,en;q=0.9')
            req.add_header('Accept-Encoding', 'gzip, deflate')
            req.add_header('Connection', 'close')
            req.add_header('Upgrade-Insecure-Requests', '1')
            
            if self.session_headers:
                for k, v in self.session_headers.items():
                    req.add_header(k, v)
            
            if headers:
                for k, v in headers.items():
                    req.add_header(k, v)
            
            # Add cookies
            if self.session_cookies:
                cookie_str = '; '.join([f'{k}={v}' for k, v in self.session_cookies.items()])
                req.add_header('Cookie', cookie_str)
            
            response = urllib.request.urlopen(req, timeout=timeout)
            
            # Store cookies
            if 'set-cookie' in response.headers:
                cookies = response.headers.get_all('set-cookie')
                for cookie in cookies:
                    if '=' in cookie:
                        key = cookie.split('=')[0]
                        value = cookie.split('=')[1].split(';')[0]
                        self.session_cookies[key] = value
            
            content = response.read()
            
            # Try to decompress
            try:
                content = zlib.decompress(content, 16 + zlib.MAX_WBITS)
            except:
                pass
            
            return {
                'url': response.url,
                'status': response.status,
                'headers': dict(response.headers),
                'content': content.decode('utf-8', errors='ignore'),
                'raw': content,
                'size': len(content)
            }
            
        except urllib.error.HTTPError as e:
            return {
                'url': url,
                'status': e.code,
                'headers': dict(e.headers),
                'content': e.read().decode('utf-8', errors='ignore') if hasattr(e, 'read') else '',
                'size': 0
            }
        except Exception as e:
            self.demon_log(f"Request failed: {str(e)[:100]}", "ERROR", "💥")
            return None
    
    # ========== 🔥 RECONNAISSANCE MODULE 🔥 ==========
    def module_recon(self):
        """Passive & Active Reconnaissance"""
        findings = []
        self.demon_log("Starting RECONNAISSANCE module", "INFO", "🔍")
        
        try:
            # 1. DNS Recon
            self.demon_log("Performing DNS reconnaissance...", "INFO", "🌐")
            
            # Get all IPs
            try:
                self.target_ips = list(set([ip[4][0] for ip in socket.getaddrinfo(self.target_domain, None)]))
                self.target_ip = self.target_ips[0] if self.target_ips else ""
            except:
                self.demon_log("DNS resolution failed", "ERROR", "❌")
                return findings
            
            # 2. Subdomain Enumeration
            self.demon_log("Enumerating subdomains...", "INFO", "🎯")
            
            def check_sub(sub: str):
                try:
                    socket.gethostbyname(f"{sub}.{self.target_domain}")
                    return f"{sub}.{self.target_domain}"
                except:
                    return None
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
                futures = [executor.submit(check_sub, sub) for sub in self.config['subdomain_wordlist']]
                for future in concurrent.futures.as_completed(futures):
                    result = future.result()
                    if result:
                        self.subdomains.add(result)
            
            if self.subdomains:
                finding = DemonFinding(
                    id="RECON-001",
                    module="Reconnaissance",
                    title="Subdomain Enumeration Successful",
                    severity=HackSeverity.LOW,
                    description=f"Discovered {len(self.subdomains)} subdomains",
                    evidence=f"Subdomains: {', '.join(list(self.subdomains)[:10])}" + 
                            ("..." if len(self.subdomains) > 10 else ""),
                    recommendation="Implement proper DNS security and monitor for unauthorized subdomains",
                    exploit_vector="DNS brute-force",
                    cwe_ids=["CWE-200"],
                    owasp_top_10=["A05:2021"],
                    mitre_attacks=["T1589.001", "T1595"],
                    poc_code="dnsrecon -d example.com"
                )
                findings.append(finding)
            
            # 3. WHOIS Information
            self.demon_log("Gathering WHOIS information...", "INFO", "📋")
            try:
                import whois
                whois_info = whois.whois(self.target_domain)
                
                # Check for sensitive information
                if whois_info:
                    sensitive_fields = ['name', 'address', 'phone', 'email']
                    exposed = []
                    
                    for field in sensitive_fields:
                        if getattr(whois_info, field, None):
                            exposed.append(field)
                    
                    if exposed:
                        finding = DemonFinding(
                            id="RECON-002",
                            module="Reconnaissance",
                            title="WHOIS Information Exposure",
                            severity=HackSeverity.LOW,
                            description=f"WHOIS exposes sensitive fields: {', '.join(exposed)}",
                            evidence=f"Registrar: {getattr(whois_info, 'registrar', 'Unknown')}",
                            recommendation="Enable WHOIS privacy protection",
                            exploit_vector="Information gathering",
                            cwe_ids=["CWE-200"],
                            business_impact="Privacy violation"
                        )
                        findings.append(finding)
            except:
                pass
            
            # 4. Technology Fingerprinting
            self.demon_log("Fingerprinting technology stack...", "INFO", "🔬")
            response = self.demon_request(self.target_url)
            
            if response:
                headers = response['headers']
                content = response['content']
                
                # Detect from headers
                for tech, signatures in self.config['tech_signatures'].items():
                    for sig in signatures:
                        if sig.lower() in str(headers).lower() or sig.lower() in content.lower():
                            if tech not in self.technologies:
                                self.technologies[tech] = []
                            self.technologies[tech].append(sig)
                
                if self.technologies:
                    tech_list = ', '.join([f"{k} ({len(v)} sigs)" for k, v in self.technologies.items()])
                    finding = DemonFinding(
                        id="RECON-003",
                        module="Reconnaissance",
                        title="Technology Stack Identified",
                        severity=HackSeverity.INFO,
                        description=f"Identified {len(self.technologies)} technologies",
                        evidence=f"Technologies: {tech_list}",
                        recommendation="Minimize technology fingerprinting surface",
                        exploit_vector="Version-specific exploits",
                        cwe_ids=["CWE-200"]
                    )
                    findings.append(finding)
            
            # 5. SSL/TLS Analysis
            self.demon_log("Analyzing SSL/TLS configuration...", "INFO", "🔐")
            ssl_findings = self.check_ssl_tls()
            findings.extend(ssl_findings)
            
        except Exception as e:
            self.demon_log(f"Recon module failed: {str(e)}", "ERROR", "💥")
        
        return findings
    
    def check_ssl_tls(self):
        """Deep SSL/TLS analysis"""
        findings = []
        
        try:
            context = ssl.create_default_context()
            
            # Test different TLS versions
            tls_versions = {
                ssl.PROTOCOL_TLSv1_2: "TLS 1.2",
                ssl.PROTOCOL_TLSv1_1: "TLS 1.1",
                ssl.PROTOCOL_TLSv1: "TLS 1.0",
                ssl.PROTOCOL_SSLv23: "SSLv2/3"
            }
            
            supported = []
            for proto, name in tls_versions.items():
                try:
                    context = ssl.SSLContext(proto)
                    with socket.create_connection((self.target_domain, 443), timeout=5) as sock:
                        with context.wrap_socket(sock, server_hostname=self.target_domain) as ssock:
                            supported.append(name)
                except:
                    pass
            
            # Check for weak protocols
            weak_protocols = [p for p in supported if "TLS 1.0" in p or "TLS 1.1" in p or "SSL" in p]
            if weak_protocols:
                finding = DemonFinding(
                    id="SSL-001",
                    module="SSL/TLS Analysis",
                    title="Weak SSL/TLS Protocols Enabled",
                    severity=HackSeverity.HIGH,
                    description=f"Server supports deprecated protocols: {', '.join(weak_protocols)}",
                    evidence=f"Supported protocols: {', '.join(supported)}",
                    recommendation="Disable TLS 1.0, TLS 1.1 and all SSL versions",
                    exploit_vector="Protocol downgrade attacks",
                    cvss_vector="CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
                    cwe_ids=["CWE-757"],
                    owasp_top_10=["A02:2021"],
                    mitre_attacks=["T1557"],
                    poc_code="sslscan example.com"
                )
                findings.append(finding)
            
            # Check certificate
            context = ssl.create_default_context()
            with socket.create_connection((self.target_domain, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=self.target_domain) as ssock:
                    cert = ssock.getpeercert()
                    
                    # Check expiry
                    expiry = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                    days_left = (expiry - datetime.now()).days
                    
                    if days_left < 0:
                        severity = HackSeverity.APOCALYPSE
                        desc = "SSL Certificate EXPIRED"
                    elif days_left < 7:
                        severity = HackSeverity.CRITICAL
                        desc = f"SSL Certificate expires in {days_left} days"
                    elif days_left < 30:
                        severity = HackSeverity.HIGH
                        desc = f"SSL Certificate expires in {days_left} days"
                    else:
                        severity = HackSeverity.INFO
                        desc = f"SSL Certificate valid for {days_left} days"
                    
                    if severity.value[1] > 5.0:
                        finding = DemonFinding(
                            id="SSL-002",
                            module="SSL/TLS Analysis",
                            title=desc,
                            severity=severity,
                            description="Certificate expiry issue",
                            evidence=f"Expiry Date: {expiry}",
                            recommendation="Renew SSL certificate immediately",
                            exploit_vector="MITM attacks after expiry",
                            business_impact="Service disruption"
                        )
                        findings.append(finding)
                    
                    # Check certificate chain
                    # (Simplified - in real tool, would check chain of trust)
                    
        except Exception as e:
            finding = DemonFinding(
                id="SSL-003",
                module="SSL/TLS Analysis",
                title="SSL/TLS Connection Failed",
                severity=HackSeverity.HIGH,
                description=f"Cannot establish secure connection: {str(e)[:100]}",
                evidence=f"Error: {str(e)}",
                recommendation="Fix SSL configuration on server",
                exploit_vector="Connection interception"
            )
            findings.append(finding)
        
        return findings
    
    # ========== 🔥 PORT SCANNING MODULE 🔥 ==========
    def module_port_scan(self):
        """Comprehensive port scanning"""
        findings = []
        self.demon_log("Starting PORT SCANNING module", "INFO", "🚪")
        
        if not self.target_ip:
            self.demon_log("No IP address for port scanning", "WARNING", "⚠️")
            return findings
        
        # Aggregate all ports
        all_ports = []
        for category, ports in self.config['ports'].items():
            all_ports.extend(ports)
        
        all_ports = list(set(all_ports))
        
        # Scan ports
        open_ports = {}
        
        def scan_port(port: int) -> Tuple[int, Optional[str]]:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.5)
                
                # Add stealth techniques
                if self.mode == DemonMode.STEALTH:
                    sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, 
                                   struct.pack('ii', 1, 0))
                
                result = sock.connect_ex((self.target_ip, port))
                sock.close()
                
                if result == 0:
                    # Try to grab banner
                    try:
                        banner_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        banner_sock.settimeout(2)
                        banner_sock.connect((self.target_ip, port))
                        banner_sock.send(b"\r\n\r\n")
                        banner = banner_sock.recv(1024)
                        banner_sock.close()
                        return port, banner.decode('utf-8', errors='ignore')[:100]
                    except:
                        return port, None
                return port, None
            except:
                return port, None
        
        self.demon_log(f"Scanning {len(all_ports)} ports on {self.target_ip}", "INFO", "🔍")
        
        # Use thread pool for scanning
        with concurrent.futures.ThreadPoolExecutor(max_workers=50 if self.mode == DemonMode.APOCALYPSE else 20) as executor:
            futures = [executor.submit(scan_port, port) for port in all_ports]
            
            for future in concurrent.futures.as_completed(futures):
                port, banner = future.result()
                if banner is not None:  # Port is open
                    open_ports[port] = banner
                    self.open_ports[port] = banner
        
        # Categorize and report findings
        if open_ports:
            # Group by category
            port_categories = {}
            for port, banner in open_ports.items():
                for category, ports in self.config['ports'].items():
                    if port in ports:
                        if category not in port_categories:
                            port_categories[category] = []
                        port_categories[category].append((port, banner))
            
            for category, ports in port_categories.items():
                # Determine severity
                if category in ['admin', 'database']:
                    severity = HackSeverity.HIGH
                elif category in ['services', 'cloud']:
                    severity = HackSeverity.MEDIUM
                else:
                    severity = HackSeverity.LOW
                
                ports_list = ', '.join([f"{p[0]}" for p in ports])
                banners = '\n'.join([f"  Port {p[0]}: {p[1][:50]}" for p in ports if p[1]])
                
                finding = DemonFinding(
                    id=f"PORT-{category.upper()}",
                    module="Port Scanning",
                    title=f"Open {category.capitalize()} Ports",
                    severity=severity,
                    description=f"Found {len(ports)} open {category} port(s)",
                    evidence=f"Ports: {ports_list}\nBanners:\n{banners}",
                    recommendation=f"Close unnecessary {category} ports and implement firewall rules",
                    exploit_vector=f"{category} service exploitation",
                    cwe_ids=["CWE-200", "CWE-284"],
                    owasp_top_10=["A05:2021"],
                    mitre_attacks=["T1046", "T1595.001"],
                    poc_code=f"nmap -sV -p {ports_list} {self.target_ip}"
                )
                findings.append(finding)
        
        # Check for misconfigurations
        misconfig_findings = self.check_port_misconfigurations(open_ports)
        findings.extend(misconfig_findings)
        
        return findings
    
    def check_port_misconfigurations(self, open_ports: Dict[int, str]):
        """Check for common port misconfigurations"""
        findings = []
        
        # Common dangerous ports
        dangerous_ports = {
            22: ("SSH with weak auth", HackSeverity.HIGH),
            21: ("FTP without encryption", HackSeverity.HIGH),
            23: ("Telnet (no encryption)", HackSeverity.CRITICAL),
            3389: ("RDP exposed", HackSeverity.HIGH),
            5900: ("VNC exposed", HackSeverity.HIGH),
            5432: ("PostgreSQL exposed", HackSeverity.HIGH),
            3306: ("MySQL exposed", HackSeverity.HIGH),
            27017: ("MongoDB exposed", HackSeverity.HIGH),
            2375: ("Docker API exposed", HackSeverity.CRITICAL),
            2376: ("Docker API TLS", HackSeverity.HIGH)
        }
        
        for port, (desc, severity) in dangerous_ports.items():
            if port in open_ports:
                banner = open_ports[port]
                
                finding = DemonFinding(
                    id=f"PORT-MISC-{port}",
                    module="Port Misconfigurations",
                    title=f"Dangerous Port Open: {port} ({desc})",
                    severity=severity,
                    description=f"Port {port} is publicly accessible",
                    evidence=f"Port {port}: {banner[:100] if banner else 'No banner'}",
                    recommendation=f"Immediately restrict access to port {port} or move behind VPN",
                    exploit_vector=f"Direct {desc.split()[0]} exploitation",
                    cwe_ids=["CWE-284", "CWE-306"],
                    owasp_top_10=["A01:2021"],
                    mitre_attacks=["T1190"],
                    poc_code=f"telnet {self.target_ip} {port}"
                )
                findings.append(finding)
        
        # Check for default credentials on common services
        default_service_checks = {
            22: "SSH",
            21: "FTP",
            3306: "MySQL",
            5432: "PostgreSQL",
            27017: "MongoDB",
            6379: "Redis"
        }
        
        for port, service in default_service_checks.items():
            if port in open_ports:
                finding = DemonFinding(
                    id=f"PORT-DEF-{port}",
                    module="Port Misconfigurations",
                    title=f"Potential Default Credentials: {service}",
                    severity=HackSeverity.MEDIUM,
                    description=f"{service} service is publicly accessible",
                    evidence=f"Port {port} open with {service} service",
                    recommendation=f"Change default credentials and restrict {service} access",
                    exploit_vector=f"Default credential attack on {service}",
                    cwe_ids=["CWE-798", "CWE-259"],
                    mitre_attacks=["T1078.001"]
                )
                findings.append(finding)
        
        return findings
    
    # ========== 🔥 WEB APPLICATION SCANNING 🔥 ==========
    def module_web_app(self):
        """Deep web application scanning"""
        findings = []
        self.demon_log("Starting WEB APPLICATION scanning", "INFO", "🌐")
        
        # 1. Security Headers Check
        header_findings = self.check_security_headers()
        findings.extend(header_findings)
        
        # 2. Directory Bruteforce
        if self.mode != DemonMode.STEALTH:
            dir_findings = self.bruteforce_directories()
            findings.extend(dir_findings)
        
        # 3. Technology-specific vulnerabilities
        tech_findings = self.check_technology_vulns()
        findings.extend(tech_findings)
        
        # 4. API Discovery
        api_findings = self.discover_apis()
        findings.extend(api_findings)
        
        # 5. Parameter Discovery & Testing
        param_findings = self.test_parameters()
        findings.extend(param_findings)
        
        return findings
    
    def check_security_headers(self):
        """Check security headers comprehensively"""
        findings = []
        
        response = self.demon_request(self.target_url)
        if not response:
            return findings
        
        headers = {k.lower(): v for k, v in response['headers'].items()}
        
        for header_name, header_key in self.config['header_checks'].items():
            if header_key not in headers:
                severity = HackSeverity.HIGH if header_name in ['HSTS', 'CSP'] else HackSeverity.MEDIUM
                
                finding = DemonFinding(
                    id=f"WEB-HEADER-{header_name}",
                    module="Web Application",
                    title=f"Missing Security Header: {header_name}",
                    severity=severity,
                    description=f"Security header '{header_name}' is not set",
                    evidence=f"Header '{header_key}' not found in response",
                    recommendation=f"Add '{header_key}' header with secure configuration",
                    exploit_vector=f"Attack specific to missing {header_name}",
                    cwe_ids=["CWE-693", "CWE-1021"],
                    owasp_top_10=["A05:2021"]
                )
                findings.append(finding)
            else:
                # Check header values for misconfigurations
                value = headers[header_key].lower()
                
                if header_name == 'HSTS' and 'max-age=0' in value:
                    finding = DemonFinding(
                        id=f"WEB-HEADER-HSTS-BAD",
                        module="Web Application",
                        title="HSTS Misconfigured (max-age=0)",
                        severity=HackSeverity.HIGH,
                        description="HSTS is disabled with max-age=0",
                        evidence=f"HSTS value: {value}",
                        recommendation="Set HSTS with appropriate max-age (e.g., 31536000)",
                        exploit_vector="SSL stripping attacks"
                    )
                    findings.append(finding)
                
                elif header_name == 'X-Frame-Options' and 'allow' in value:
                    finding = DemonFinding(
                        id=f"WEB-HEADER-XFO-BAD",
                        module="Web Application",
                        title="X-Frame-Options Allows Framing",
                        severity=HackSeverity.MEDIUM,
                        description="X-Frame-Options allows framing from other domains",
                        evidence=f"X-Frame-Options value: {value}",
                        recommendation="Set X-Frame-Options to 'DENY' or 'SAMEORIGIN'",
                        exploit_vector="Clickjacking attacks"
                    )
                    findings.append(finding)
        
        return findings
    
    def bruteforce_directories(self):
        """Bruteforce common directories and files"""
        findings = []
        discovered = []
        
        self.demon_log(f"Bruteforcing {len(self.config['path_wordlist'])} paths", "INFO", "🔍")
        
        def check_path(path: str) -> Optional[Tuple[str, int, int]]:
            url = self.target_url.rstrip('/') + path
            response = self.demon_request(url)
            
            if response:
                status = response['status']
                size = response['size']
                
                # Consider interesting responses
                if status in [200, 403, 401, 301, 302] and size > 0:
                    return (path, status, size)
            
            return None
        
        # Use thread pool for bruteforce
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=30 if self.mode == DemonMode.APOCALYPSE else 15
        ) as executor:
            futures = [executor.submit(check_path, path) for path in self.config['path_wordlist']]
            
            for future in concurrent.futures.as_completed(futures):
                try:
                    result = future.result(timeout=5)
                    if result:
                        discovered.append(result)
                except:
                    continue
        
        # Analyze discovered paths
        for path, status, size in discovered:
            self.discovered_paths.append(path)
            
            # Determine severity based on path
            if any(x in path for x in ['.env', 'config.', 'backup', 'dump', 'database']):
                severity = HackSeverity.CRITICAL if status == 200 else HackSeverity.HIGH
                desc = "Sensitive configuration or backup file"
            elif any(x in path for x in ['.git', '.svn', '.DS_Store']):
                severity = HackSeverity.HIGH if status == 200 else HackSeverity.MEDIUM
                desc = "Source control or metadata file"
            elif any(x in path for x in ['admin', 'login', 'dashboard']):
                severity = HackSeverity.MEDIUM if status == 200 else HackSeverity.LOW
                desc = "Administrative interface"
            elif 'api' in path:
                severity = HackSeverity.MEDIUM
                desc = "API endpoint"
            else:
                severity = HackSeverity.LOW
                desc = "Common file or directory"
            
            status_text = {
                200: "Publicly accessible",
                403: "Access forbidden",
                401: "Authentication required",
                301: "Redirect",
                302: "Temporary redirect"
            }.get(status, f"HTTP {status}")
            
            finding = DemonFinding(
                id=f"WEB-PATH-{hashlib.md5(path.encode()).hexdigest()[:8]}",
                module="Web Application",
                title=f"Discovered Path: {path} ({status_text})",
                severity=severity,
                description=desc,
                evidence=f"Path: {path}\nStatus: {status}\nSize: {size} bytes",
                recommendation="Restrict access to sensitive paths and remove unnecessary files",
                exploit_vector="Path traversal or information disclosure",
                cwe_ids=["CWE-200", "CWE-552"],
                owasp_top_10=["A01:2021", "A05:2021"]
            )
            findings.append(finding)
        
        return findings
    
    def check_technology_vulns(self):
        """Check for technology-specific vulnerabilities"""
        findings = []
        
        # Check WordPress
        if 'wordpress' in self.technologies:
            wp_findings = self.check_wordpress_vulns()
            findings.extend(wp_findings)
        
        # Check exposed debug endpoints
        debug_findings = self.check_debug_endpoints()
        findings.extend(debug_findings)
        
        return findings
    
    def check_wordpress_vulns(self):
        """Check WordPress specific vulnerabilities"""
        findings = []
        
        # Check common WordPress files
        wp_files = [
            ('/wp-config.php', 'WordPress configuration file'),
            ('/xmlrpc.php', 'WordPress XML-RPC endpoint'),
            ('/wp-json/wp/v2/users/', 'WordPress user enumeration'),
            ('/wp-admin/install.php', 'WordPress installation'),
            ('/wp-content/debug.log', 'WordPress debug log')
        ]
        
        for path, desc in wp_files:
            url = self.target_url.rstrip('/') + path
            response = self.demon_request(url)
            
            if response and response['status'] == 200:
                severity = HackSeverity.CRITICAL if 'config' in path else HackSeverity.HIGH
                
                finding = DemonFinding(
                    id=f"WP-{hashlib.md5(path.encode()).hexdigest()[:8]}",
                    module="WordPress Analysis",
                    title=f"WordPress {desc} Exposed",
                    severity=severity,
                    description=f"WordPress {desc} is publicly accessible",
                    evidence=f"Path: {path}\nStatus: 200\nSize: {response['size']} bytes",
                    recommendation=f"Immediately restrict access to {path}",
                    exploit_vector="WordPress specific attacks",
                    cwe_ids=["CWE-200", "CWE-552"],
                    owasp_top_10=["A01:2021"]
                )
                findings.append(finding)
        
        return findings
    
    def check_debug_endpoints(self):
        """Check for exposed debug endpoints"""
        findings = []
        
        debug_endpoints = [
            ('/actuator/health', 'Spring Boot Actuator'),
            ('/debug/default/view', 'Yii Debug'),
            ('/_profiler/phpinfo', 'Symfony Profiler'),
            ('/phpinfo.php', 'PHP Info'),
            ('/info.php', 'PHP Info'),
            ('/test.php', 'Test endpoint'),
            ('/console', 'Debug console'),
            ('/api/jsonws/invoke', 'Liferay JSONWS')
        ]
        
        for path, system in debug_endpoints:
            url = self.target_url.rstrip('/') + path
            response = self.demon_request(url)
            
            if response and response['status'] == 200:
                # Check if it looks like a debug endpoint
                content = response['content'].lower()
                debug_indicators = ['debug', 'environment', 'configuration', 'phpinfo', 'actuator']
                
                if any(indicator in content for indicator in debug_indicators):
                    finding = DemonFinding(
                        id=f"DEBUG-{hashlib.md5(path.encode()).hexdigest()[:8]}",
                        module="Debug Endpoints",
                        title=f"Exposed Debug Endpoint: {system}",
                        severity=HackSeverity.HIGH,
                        description=f"{system} debug endpoint is publicly accessible",
                        evidence=f"Path: {path}\nSystem: {system}\nStatus: 200",
                        recommendation="Disable debug endpoints in production",
                        exploit_vector="Information disclosure through debug interfaces",
                        cwe_ids=["CWE-200", "CWE-215"],
                        owasp_top_10=["A05:2021"],
                        mitre_attacks=["T1592"]
                    )
                    findings.append(finding)
        
        return findings
    
    def discover_apis(self):
        """Discover and analyze API endpoints"""
        findings = []
        
        # Common API patterns
        api_patterns = [
            '/api/', '/api/v1/', '/api/v2/', '/graphql', '/graphiql',
            '/swagger', '/openapi', '/rest/', '/soap/', '/jsonrpc',
            '/oauth/', '/auth/', '/token', '/login', '/register'
        ]
        
        discovered_apis = []
        
        for pattern in api_patterns:
            url = self.target_url.rstrip('/') + pattern
            response = self.demon_request(url)
            
            if response and response['status'] in [200, 201, 401, 403]:
                discovered_apis.append((pattern, response['status'], response.get('size', 0)))
                self.api_endpoints.append(url)
        
        if discovered_apis:
            api_list = '\n'.join([f"  {path} (HTTP {status})" for path, status, _ in discovered_apis])
            
            finding = DemonFinding(
                id="WEB-API-DISCOVERED",
                module="API Discovery",
                title="API Endpoints Discovered",
                severity=HackSeverity.MEDIUM,
                description=f"Found {len(discovered_apis)} API endpoints",
                evidence=f"Discovered APIs:\n{api_list}",
                recommendation="Implement proper API authentication, rate limiting, and input validation",
                exploit_vector="API endpoint attacks",
                cwe_ids=["CWE-284", "CWE-306"],
                owasp_top_10=["A01:2021", "A07:2021"]
            )
            findings.append(finding)
        
        return findings
    
    def test_parameters(self):
        """Test for common parameter-based vulnerabilities"""
        findings = []
        
        # Get a page to analyze
        response = self.demon_request(self.target_url)
        if not response:
            return findings
        
        content = response['content']
        
        # Look for forms and parameters
        form_patterns = [
            r'<form[^>]*>.*?</form>',
            r'action=["\']([^"\']+)["\']',
            r'name=["\']([^"\']+)["\']',
            r'id=["\']([^"\']+)["\']'
        ]
        
        forms_found = []
        for pattern in form_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
            forms_found.extend(matches)
        
        if forms_found:
            # Test for XSS in forms
            xss_test_findings = self.test_xss_vulnerabilities()
            findings.extend(xss_test_findings)
            
            # Test for SQLi (basic)
            sqli_test_findings = self.test_sqli_vulnerabilities()
            findings.extend(sqli_test_findings)
        
        return findings
    
    def test_xss_vulnerabilities(self):
        """Test for XSS vulnerabilities (safe testing)"""
        findings = []
        
        # Only test in aggressive or apocalypse mode
        if self.mode == DemonMode.STEALTH:
            return findings
        
        # Create safe test payloads
        safe_payloads = [
            "<xss>",
            "'>\"><xss>",
            "javascript:alert('XSS')",
            "onload=alert('XSS')"
        ]
        
        # Test on discovered endpoints
        test_urls = [self.target_url] + self.api_endpoints[:3]  # Limit to 3 endpoints
        
        for url in test_urls:
            for payload in safe_payloads:
                # Create test request with payload in common parameters
                test_params = {
                    'q': payload,
                    'search': payload,
                    'query': payload,
                    'id': payload,
                    'name': payload
                }
                
                # URL encode
                encoded_params = '&'.join([f"{k}={urllib.parse.quote(v)}" for k, v in test_params.items()])
                test_url = f"{url}?{encoded_params}" if '?' not in url else f"{url}&{encoded_params}"
                
                response = self.demon_request(test_url)
                if response and response['status'] == 200:
                    # Check if payload is reflected
                    if payload.lower() in response['content'].lower():
                        finding = DemonFinding(
                            id=f"XSS-REFLECT-{hashlib.md5(test_url.encode()).hexdigest()[:8]}",
                            module="XSS Testing",
                            title="Potential Reflected XSS Vulnerability",
                            severity=HackSeverity.HIGH,
                            description="User input is reflected in response without proper sanitization",
                            evidence=f"Payload reflected: {payload[:50]}...\nURL: {test_url}",
                            recommendation="Implement proper input validation and output encoding",
                            exploit_vector="Reflected XSS attack",
                            cvss_vector="CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N",
                            cwe_ids=["CWE-79"],
                            owasp_top_10=["A03:2021"],
                            mitre_attacks=["T1059.007"]
                        )
                        findings.append(finding)
                        break  # Found one XSS, move to next URL
        
        return findings
    
    def test_sqli_vulnerabilities(self):
        """Test for SQL injection vulnerabilities (safe testing)"""
        findings = []
        
        if self.mode == DemonMode.STEALTH:
            return findings
        
        # Safe SQLi test patterns (error-based)
        sqli_payloads = [
            "'",
            "\"",
            "' OR '1'='1",
            "' OR '1'='1' --",
            "' OR '1'='1' #",
            "' UNION SELECT NULL--",
            "' AND 1=1--",
            "' AND 1=2--"
        ]
        
        test_urls = [self.target_url] + self.api_endpoints[:2]
        
        for url in test_urls:
            for payload in sqli_payloads:
                test_params = {
                    'id': payload,
                    'user': payload,
                    'name': payload,
                    'search': payload
                }
                
                encoded_params = '&'.join([f"{k}={urllib.parse.quote(v)}" for k, v in test_params.items()])
                test_url = f"{url}?{encoded_params}" if '?' not in url else f"{url}&{encoded_params}"
                
                response = self.demon_request(test_url)
                if response:
                    content = response['content'].lower()
                    
                    # Look for SQL errors
                    sql_errors = [
                        'sql', 'mysql', 'postgresql', 'oracle', 'syntax',
                        'database', 'query failed', 'unclosed quotation',
                        'you have an error in your sql syntax'
                    ]
                    
                    if any(error in content for error in sql_errors):
                        finding = DemonFinding(
                            id=f"SQLI-ERROR-{hashlib.md5(test_url.encode()).hexdigest()[:8]}",
                            module="SQL Injection Testing",
                            title="Potential SQL Injection Vulnerability",
                            severity=HackSeverity.CRITICAL,
                            description="SQL error messages revealed in response",
                            evidence=f"SQL error detected with payload: {payload}\nURL: {test_url}",
                            recommendation="Use parameterized queries or prepared statements",
                            exploit_vector="SQL injection attack",
                            cvss_vector="CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
                            cwe_ids=["CWE-89"],
                            owasp_top_10=["A03:2021"],
                            mitre_attacks=["T1190"],
                            poc_code=f"sqlmap -u \"{test_url}\" --batch"
                        )
                        findings.append(finding)
                        break
        
        return findings
    
    # ========== 🔥 REPORT GENERATION 🔥 ==========
    def generate_report(self):
        """Generate comprehensive security report"""
        DemonColors.print_header("GENERATING DEMON REPORT")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_base = f"devil_report_{self.target_domain}_{timestamp}"
        
        # Generate HTML report
        html_report = self.reports_dir / f"{report_base}.html"
        self.generate_html_report(html_report)
        
        # Generate JSON report
        json_report = self.reports_dir / f"{report_base}.json"
        self.generate_json_report(json_report)
        
        # Generate executive summary
        summary_report = self.reports_dir / f"{report_base}_executive.txt"
        self.generate_executive_summary(summary_report)
        
        # Generate actionable fix list
        fix_report = self.reports_dir / f"{report_base}_fixes.csv"
        self.generate_fix_list(fix_report)
        
        self.demon_log(f"Reports generated:", "SUCCESS", "📊")
        self.demon_log(f"  HTML: {html_report}", "INFO", "📄")
        self.demon_log(f"  JSON: {json_report}", "INFO", "📄")
        self.demon_log(f"  Summary: {summary_report}", "INFO", "📄")
        self.demon_log(f"  Fix List: {fix_report}", "INFO", "🔧")
        
        return html_report
    
    def generate_html_report(self, filename: Path):
        """Generate HTML report"""
        # Count findings by severity
        severity_counts = {}
        for severity in HackSeverity:
            count = len([f for f in self.findings if f.severity == severity])
            if count > 0:
                severity_counts[severity.value[0]] = count
        
        # Group by module
        module_groups = {}
        for finding in self.findings:
            if finding.module not in module_groups:
                module_groups[finding.module] = []
            module_groups[finding.module].append(finding)
        
        # Sort findings by severity
        severity_order = {s: i for i, s in enumerate(HackSeverity)}
        sorted_findings = sorted(self.findings, key=lambda x: severity_order[x.severity])
        
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>🔥 DEVILSCAN Report - {self.target_domain}</title>
            <style>
                :root {{
                    --blood-red: #ff0000;
                    --hell-orange: #ff4500;
                    --demon-purple: #8a2be2;
                    --toxic-green: #00ff00;
                    --abyss-blue: #00008b;
                    --shadow-gray: #2c2c2c;
                    --soul-white: #f0f0f0;
                }}
                
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                
                body {{
                    font-family: 'Courier New', monospace;
                    background: #0a0a0a;
                    color: var(--soul-white);
                    line-height: 1.6;
                    padding: 20px;
                }}
                
                .container {{ max-width: 1400px; margin: 0 auto; }}
                
                .header {{
                    background: linear-gradient(135deg, var(--blood-red), var(--demon-purple));
                    padding: 40px;
                    border-radius: 10px;
                    margin-bottom: 30px;
                    text-align: center;
                    border: 2px solid var(--toxic-green);
                    box-shadow: 0 0 30px var(--blood-red);
                }}
                
                .header h1 {{
                    font-size: 3em;
                    margin-bottom: 10px;
                    text-shadow: 0 0 10px var(--toxic-green);
                }}
                
                .header h2 {{
                    font-size: 1.5em;
                    opacity: 0.9;
                }}
                
                .stats-grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 20px;
                    margin: 30px 0;
                }}
                
                .stat-card {{
                    background: var(--shadow-gray);
                    padding: 20px;
                    border-radius: 8px;
                    text-align: center;
                    border-left: 5px solid;
                    transition: transform 0.3s;
                }}
                
                .stat-card:hover {{ transform: translateY(-5px); }}
                
                .stat-card.apocalypse {{ border-color: var(--blood-red); background: #330000; }}
                .stat-card.critical {{ border-color: var(--hell-orange); background: #331a00; }}
                .stat-card.high {{ border-color: #ff8c00; background: #332200; }}
                .stat-card.medium {{ border-color: #ffd700; background: #333300; }}
                .stat-card.low {{ border-color: var(--toxic-green); background: #003300; }}
                .stat-card.info {{ border-color: var(--abyss-blue); background: #000033; }}
                
                .stat-card .count {{
                    font-size: 3em;
                    font-weight: bold;
                    margin: 10px 0;
                }}
                
                .finding {{
                    background: #1a1a1a;
                    margin: 15px 0;
                    padding: 20px;
                    border-radius: 8px;
                    border-left: 5px solid;
                }}
                
                .finding.apocalypse {{ border-color: var(--blood-red); }}
                .finding.critical {{ border-color: var(--hell-orange); }}
                .finding.high {{ border-color: #ff8c00; }}
                .finding.medium {{ border-color: #ffd700; }}
                .finding.low {{ border-color: var(--toxic-green); }}
                .finding.info {{ border-color: var(--abyss-blue); }}
                
                .finding-header {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 15px;
                }}
                
                .finding-title {{
                    font-size: 1.3em;
                    font-weight: bold;
                }}
                
                .finding-severity {{
                    padding: 5px 15px;
                    border-radius: 20px;
                    font-weight: bold;
                    font-size: 0.9em;
                }}
                
                .finding-content {{ margin-top: 15px; }}
                
                .finding-section {{ margin: 10px 0; }}
                
                .finding-section h4 {{
                    color: var(--toxic-green);
                    margin-bottom: 5px;
                    border-bottom: 1px solid #333;
                    padding-bottom: 5px;
                }}
                
                .recommendation {{
                    background: #2a2a2a;
                    padding: 15px;
                    border-radius: 5px;
                    margin-top: 15px;
                    border: 1px solid var(--toxic-green);
                }}
                
                .module-section {{
                    margin: 40px 0;
                    padding: 20px;
                    background: rgba(255, 0, 0, 0.05);
                    border-radius: 10px;
                }}
                
                .module-title {{
                    font-size: 1.8em;
                    color: var(--hell-orange);
                    margin-bottom: 20px;
                    padding-bottom: 10px;
                    border-bottom: 2px solid var(--blood-red);
                }}
                
                .timestamp {{
                    text-align: center;
                    margin-top: 40px;
                    padding: 20px;
                    background: var(--shadow-gray);
                    border-radius: 5px;
                    opacity: 0.8;
                }}
                
                @media (max-width: 768px) {{
                    .stats-grid {{ grid-template-columns: 1fr; }}
                    .header h1 {{ font-size: 2em; }}
                    .finding-header {{ flex-direction: column; align-items: flex-start; }}
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🔥 DEVILSCAN SECURITY REPORT 🔥</h1>
                    <h2>Target: {self.target_domain} | Mode: {self.mode.upper()}</h2>
                    <p>Scan ID: {self.scan_id} | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                </div>
                
                <div class="stats-grid">
        """
        
        # Add stat cards
        for severity_emoji, count in severity_counts.items():
            severity_class = severity_emoji.lower().replace("-", "").replace("💀", "critical").replace("🔥", "apocalypse").replace("☠️", "critical").replace("⚡", "high").replace("⚠️", "medium").replace("🔶", "low").replace("ℹ️", "info")
            html_content += f"""
                    <div class="stat-card {severity_class}">
                        <div class="severity">{severity_emoji}</div>
                        <div class="count">{count}</div>
                        <div class="label">Findings</div>
                    </div>
            """
        
        html_content += """
                </div>
                
                <div class="module-section">
                    <h2 class="module-title">🎯 EXECUTIVE SUMMARY</h2>
                    <div class="finding-content">
                        <p>This report identifies security vulnerabilities that could be exploited by attackers.</p>
                        <p><strong>Total Findings:</strong> """ + str(len(self.findings)) + """</p>
                        <p><strong>Target:</strong> """ + self.target_domain + """</p>
                        <p><strong>IP Address:</strong> """ + self.target_ip + """</p>
                        <p><strong>Technologies Identified:</strong> """ + ', '.join(self.technologies.keys()) + """</p>
                        <p><strong>Open Ports:</strong> """ + ', '.join([str(p) for p in self.open_ports.keys()][:10]) + """</p>
                    </div>
                </div>
        """
        
        # Add findings by module
        for module, findings in module_groups.items():
            html_content += f"""
                <div class="module-section">
                    <h2 class="module-title">📂 {module.upper()}</h2>
            """
            
            for finding in findings:
                severity_class = finding.severity.name.lower()
                severity_display = finding.severity.value[0]
                
                html_content += f"""
                    <div class="finding {severity_class}">
                        <div class="finding-header">
                            <div class="finding-title">{finding.title}</div>
                            <div class="finding-severity" style="color: inherit;">{severity_display}</div>
                        </div>
                        
                        <div class="finding-content">
                            <div class="finding-section">
                                <h4>📝 Description</h4>
                                <p>{finding.description}</p>
                            </div>
                            
                            <div class="finding-section">
                                <h4>🔍 Evidence</h4>
                                <p>{html.escape(finding.evidence)}</p>
                            </div>
                            
                            <div class="finding-section">
                                <h4>🎯 Attack Vector</h4>
                                <p>{finding.exploit_vector}</p>
                            </div>
                            
                            <div class="recommendation">
                                <h4>🔧 RECOMMENDATION</h4>
                                <p>{finding.recommendation}</p>
                                <p><strong>Remediation Time:</strong> {finding.remediation_time}</p>
                                <p><strong>Business Impact:</strong> {finding.business_impact}</p>
                            </div>
                        </div>
                    </div>
                """
            
            html_content += "</div>"
        
        # Add footer
        html_content += f"""
                <div class="timestamp">
                    <p>Report generated by DEVILSCAN v4.0 - The Ultimate Hacker-Mind Auditor</p>
                    <p>Scan completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                    <p style="color: var(--toxic-green); font-size: 0.9em;">
                        ⚠️ This report is for authorized security testing only. Use findings to improve security posture.
                    </p>
                </div>
            </div>
        </body>
        </html>
        """
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    def generate_json_report(self, filename: Path):
        """Generate JSON report"""
        report_data = {
            'metadata': {
                'target': self.target_domain,
                'url': self.target_url,
                'ip': self.target_ip,
                'ips': self.target_ips,
                'scan_id': self.scan_id,
                'mode': self.mode,
                'timestamp': datetime.now().isoformat(),
                'duration': 'N/A'
            },
            'discoveries': {
                'technologies': self.technologies,
                'open_ports': self.open_ports,
                'subdomains': list(self.subdomains),
                'paths': self.discovered_paths,
                'api_endpoints': self.api_endpoints
            },
            'findings': [asdict(f) for f in self.findings],
            'summary': {
                'total_findings': len(self.findings),
                'by_severity': {
                    severity.value[0]: len([f for f in self.findings if f.severity == severity])
                    for severity in HackSeverity
                },
                'by_module': {
                    module: len([f for f in self.findings if f.module == module])
                    for module in set([f.module for f in self.findings])
                }
            }
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, default=str)
    
    def generate_executive_summary(self, filename: Path):
        """Generate executive summary"""
        critical_count = len([f for f in self.findings if f.severity in [
            HackSeverity.APOCALYPSE, HackSeverity.CRITICAL, HackSeverity.HIGH
        ]])
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("🔥 DEVILSCAN - EXECUTIVE SUMMARY 🔥\n")
            f.write("="*60 + "\n\n")
            f.write(f"Target: {self.target_domain}\n")
            f.write(f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Scan ID: {self.scan_id}\n")
            f.write(f"Scan Mode: {self.mode.upper()}\n")
            f.write("\n" + "="*60 + "\n\n")
            
            f.write("📊 KEY STATISTICS:\n")
            f.write("-"*40 + "\n")
            f.write(f"Total Findings: {len(self.findings)}\n")
            f.write(f"Critical/High Findings: {critical_count}\n")
            f.write(f"Technologies Identified: {len(self.technologies)}\n")
            f.write(f"Open Ports: {len(self.open_ports)}\n")
            f.write(f"Subdomains Discovered: {len(self.subdomains)}\n")
            f.write(f"API Endpoints: {len(self.api_endpoints)}\n")
            f.write("\n" + "="*60 + "\n\n")
            
            f.write("🎯 TOP 5 CRITICAL FINDINGS:\n")
            f.write("-"*40 + "\n")
            
            critical_findings = [f for f in self.findings if f.severity in [
                HackSeverity.APOCALYPSE, HackSeverity.CRITICAL, HackSeverity.HIGH
            ]]
            
            for i, finding in enumerate(critical_findings[:5], 1):
                f.write(f"\n{i}. {finding.title}\n")
                f.write(f"   Severity: {finding.severity.value[0]}\n")
                f.write(f"   Module: {finding.module}\n")
                f.write(f"   Description: {finding.description[:100]}...\n")
                f.write(f"   Recommendation: {finding.recommendation[:100]}...\n")
            
            f.write("\n" + "="*60 + "\n\n")
            f.write("🔧 IMMEDIATE ACTIONS REQUIRED:\n")
            f.write("-"*40 + "\n")
            f.write("1. Fix all 🔥 APOCALYPSE and ☠️ CRITICAL findings within 24 hours\n")
            f.write("2. Implement firewall rules to restrict unnecessary ports\n")
            f.write("3. Remove or secure exposed files and directories\n")
            f.write("4. Update and patch identified technologies\n")
            f.write("5. Implement proper security headers\n")
            
            f.write("\n" + "="*60 + "\n")
            f.write("Generated by DEVILSCAN v4.0 - Think Like a Hacker, Defend Like a Demon\n")
    
    def generate_fix_list(self, filename: Path):
        """Generate actionable fix list"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("ID,Severity,Module,Title,Recommendation,Remediation_Time,Priority\n")
            
            for finding in self.findings:
                # Determine priority
                if finding.severity in [HackSeverity.APOCALYPSE, HackSeverity.CRITICAL]:
                    priority = "IMMEDIATE"
                elif finding.severity == HackSeverity.HIGH:
                    priority = "HIGH"
                elif finding.severity == HackSeverity.MEDIUM:
                    priority = "MEDIUM"
                else:
                    priority = "LOW"
                
                # Clean CSV fields
                title = finding.title.replace(',', ';').replace('"', "'")
                recommendation = finding.recommendation.replace(',', ';').replace('"', "'")
                
                f.write(f'{finding.id},{finding.severity.value[0]},{finding.module},')
                f.write(f'"{title}","{recommendation}",')
                f.write(f'{finding.remediation_time},{priority}\n')
    
    # ========== 🔥 MAIN SCAN METHOD 🔥 ==========
    def scan(self, target: str):
        """Main scan method"""
        try:
            # Parse target
            if not target.startswith(('http://', 'https://')):
                target = 'https://' + target
            
            parsed = urllib.parse.urlparse(target)
            self.target_url = target
            self.target_domain = parsed.netloc
            
            # Display banner
            print(f"{DemonColors.BOLD}{DemonColors.BLOOD_RED}{DEMON_ASCII}{DemonColors.END}")
            
            DemonColors.print_header(f"TARGET: {self.target_domain}")
            self.demon_log(f"Initializing DEVILSCAN v4.0", "INFO", "👹")
            self.demon_log(f"Target: {self.target_url}", "INFO", "🎯")
            self.demon_log(f"Mode: {self.mode.upper()}", "INFO", "⚙️")
            
            # Run modules
            all_findings = []
            
            # 1. Reconnaissance
            DemonColors.print_header("PHASE 1: RECONNAISSANCE")
            recon_findings = self.module_recon()
            all_findings.extend(recon_findings)
            
            # 2. Port Scanning
            DemonColors.print_header("PHASE 2: PORT SCANNING")
            port_findings = self.module_port_scan()
            all_findings.extend(port_findings)
            
            # 3. Web Application Scanning
            DemonColors.print_header("PHASE 3: WEB APPLICATION")
            web_findings = self.module_web_app()
            all_findings.extend(web_findings)
            
            # Store findings
            self.findings = all_findings
            
            # Generate report
            DemonColors.print_header("PHASE 4: REPORT GENERATION")
            report_file = self.generate_report()
            
            # Display summary
            self.display_scan_summary()
            
            return report_file
            
        except Exception as e:
            self.demon_log(f"Scan failed: {str(e)}", "ERROR", "💥")
            import traceback
            traceback.print_exc()
            return None
    
    def display_scan_summary(self):
        """Display final summary"""
        DemonColors.print_header("SCAN COMPLETE")
        
        # Count findings
        critical_count = len([f for f in self.findings if f.severity in [
            HackSeverity.APOCALYPSE, HackSeverity.CRITICAL
        ]])
        high_count = len([f for f in self.findings if f.severity == HackSeverity.HIGH])
        total_count = len(self.findings)
        
        print(f"\n{DemonColors.BOLD}{DemonColors.TOXIC_GREEN}📊 SCAN STATISTICS:{DemonColors.END}")
        print(f"{DemonColors.SOUL_WHITE}{'─'*50}{DemonColors.END}")
        
        print(f"{DemonColors.BLOOD_RED}  🔥 APOCALYPSE/☠️ CRITICAL: {critical_count}{DemonColors.END}")
        print(f"{DemonColors.HELLFIRE}  ⚡ HIGH: {high_count}{DemonColors.END}")
        print(f"{DemonColors.SOUL_WHITE}  Total Findings: {total_count}{DemonColors.END}")
        
        print(f"\n{DemonColors.BOLD}{DemonColors.GOLD}🎯 DISCOVERIES:{DemonColors.END}")
        print(f"{DemonColors.SOUL_WHITE}{'─'*50}{DemonColors.END}")
        
        print(f"{DemonColors.TOXIC_GREEN}  Technologies: {len(self.technologies)}{DemonColors.END}")
        print(f"{DemonColors.TOXIC_GREEN}  Open Ports: {len(self.open_ports)}{DemonColors.END}")
        print(f"{DemonColors.TOXIC_GREEN}  Subdomains: {len(self.subdomains)}{DemonColors.END}")
        print(f"{DemonColors.TOXIC_GREEN}  API Endpoints: {len(self.api_endpoints)}{DemonColors.END}")
        
        # Display top critical findings
        if critical_count > 0:
            print(f"\n{DemonColors.BOLD}{DemonColors.BLOOD_RED}🚨 IMMEDIATE ACTION REQUIRED:{DemonColors.END}")
            criticals = [f for f in self.findings if f.severity in [
                HackSeverity.APOCALYPSE, HackSeverity.CRITICAL
            ]]
            
            for i, finding in enumerate(criticals[:3], 1):
                print(f"\n{DemonColors.BLOOD_RED}{i}. {finding.title}{DemonColors.END}")
                print(f"{DemonColors.SHADOW_GRAY}   {finding.description[:80]}...{DemonColors.END}")
                print(f"{DemonColors.TOXIC_GREEN}   🔧 Fix: {finding.recommendation[:80]}...{DemonColors.END}")
        
        print(f"\n{DemonColors.BOLD}{DemonColors.DEMON_PURPLE}📁 REPORTS SAVED TO:~/.devil_lair/reports/{DemonColors.END}")
        print(f"\n{DemonColors.BOLD}{DemonColors.GOLD}✅ Your website is now DEMON-PROOF!{DemonColors.END}")
        print(f"{DemonColors.BOLD}{DemonColors.HELLFIRE}🔒 Fix critical issues within 24 hours{DemonColors.END}")

# ========== 🔥 MAIN FUNCTION 🔥 ==========
def main():
    """Main entry point"""
    try:
        # Check Python version
        if sys.version_info < (3, 7):
            print(f"{DemonColors.BOLD}{DemonColors.BLOOD_RED}Python 3.7 or higher required!{DemonColors.END}")
            sys.exit(1)
        
        # Display banner
        print(f"{DemonColors.BOLD}{DemonColors.BLOOD_RED}{DEMON_ASCII}{DemonColors.END}")
        
        # Authorization
        DemonColors.print_header("AUTHORIZATION REQUIRED")
        print(f"{DemonColors.BOLD}{DemonColors.SOUL_WHITE}This tool is for authorized security testing only.{DemonColors.END}")
        print(f"{DemonColors.BOLD}{DemonColors.TOXIC_GREEN}Type exactly: I_OWN_THIS_TARGET{DemonColors.END}")
        
        auth = input(f"\n{DemonColors.YELLOW}>>> {DemonColors.END}").strip()
        
        if auth != "I_OWN_THIS_TARGET":
            print(f"\n{DemonColors.BOLD}{DemonColors.BLOOD_RED}❌ AUTHORIZATION FAILED!{DemonColors.END}")
            print(f"{DemonColors.BOLD}{DemonColors.SHADOW_GRAY}Exiting...{DemonColors.END}")
            sys.exit(1)
        
        print(f"\n{DemonColors.BOLD}{DemonColors.TOXIC_GREEN}✅ AUTHORIZATION CONFIRMED{DemonColors.END}")
        
        # Get target
        DemonColors.print_header("TARGET SPECIFICATION")
        print(f"{DemonColors.BOLD}{DemonColors.SOUL_WHITE}Enter target website (example.com or https://...):{DemonColors.END}")
        target = input(f"\n{DemonColors.YELLOW}>>> {DemonColors.END}").strip()
        
        if not target:
            print(f"\n{DemonColors.BOLD}{DemonColors.BLOOD_RED}❌ No target specified!{DemonColors.END}")
            sys.exit(1)
        
        # Select mode
        DemonColors.print_header("SCAN MODE SELECTION")
        print(f"{DemonColors.BOLD}{DemonColors.SOUL_WHITE}Select scan mode:{DemonColors.END}")
        print(f"{DemonColors.TOXIC_GREEN}  1. STEALTH (Slow, quiet){DemonColors.END}")
        print(f"{DemonColors.HELLFIRE}  2. AGGRESSIVE (Recommended){DemonColors.END}")
        print(f"{DemonColors.BLOOD_RED}  3. APOCALYPSE (Maximum intensity){DemonColors.END}")
        
        mode_choice = input(f"\n{DemonColors.YELLOW}[1-3] >>> {DemonColors.END}").strip()
        
        if mode_choice == '1':
            mode = DemonMode.STEALTH
        elif mode_choice == '3':
            mode = DemonMode.APOCALYPSE
        else:
            mode = DemonMode.AGGRESSIVE
        
        # Create scanner
        scanner = DevilScanEngine(mode=mode)
        
        # Start scan
        DemonColors.print_header("STARTING DEMON SCAN")
        print(f"\n{DemonColors.BOLD}{DemonColors.BLOOD_RED}🔥 DEVILSCAN ACTIVATED! 🔥{DemonColors.END}")
        print(f"{DemonColors.BOLD}{DemonColors.HELLFIRE}Target: {target}{DemonColors.END}")
        print(f"{DemonColors.BOLD}{DemonColors.GOLD}Mode: {mode.upper()}{DemonColors.END}")
        print(f"{DemonColors.BOLD}{DemonColors.TOXIC_GREEN}Starting in 3 seconds...{DemonColors.END}")
        
        time.sleep(3)
        
        # Run scan
        report = scanner.scan(target)
        
        if report:
            print(f"\n{DemonColors.BOLD}{DemonColors.TOXIC_GREEN}✅ Scan completed successfully!{DemonColors.END}")
            print(f"{DemonColors.BOLD}{DemonColors.SOUL_WHITE}Report: {report}{DemonColors.END}")
        else:
            print(f"\n{DemonColors.BOLD}{DemonColors.BLOOD_RED}❌ Scan failed!{DemonColors.END}")
        
    except KeyboardInterrupt:
        print(f"\n\n{DemonColors.BOLD}{DemonColors.HELLFIRE}⚠️ Scan interrupted by user{DemonColors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{DemonColors.BOLD}{DemonColors.BLOOD_RED}💥 FATAL ERROR: {str(e)}{DemonColors.END}")
        sys.exit(1)

# ========== 🔥 ENTRY POINT 🔥 ==========
if __name__ == "__main__":
    main()