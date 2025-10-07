#!/usr/bin/python3
################# Multi threading #################

import socket, threading, sys

def show_help():
    help_text = """
Usage: python Scan_Ports-Multi-Threading.py [OPTIONS] <target_ip>

DESCRIPTION:
    Scanner de ports multi-threadé pour identifier les ports ouverts sur une cible.

ARGUMENTS OBLIGATOIRE:
    target_ip        Adresse IP de la cible à scanner

OPTIONS:
    -h, --help       Affiche cette aide et quitte
    -p, --ports      Spécifie la plage de ports (format: start-end, ex: 80-443)
    -t, --threads    Nombre de threads à utiliser (défaut: 500)
    -s, --settimeout Timeout en secondes pour chaque connexion (défaut: 0.5)

EXEMPLES:
    python Scan_Ports-Multi-Threading.py 192.168.1.1
    python Scan_Ports-Multi-Threading.py -p 20-80 -t 100 192.168.1.1
    python Scan_Ports-Multi-Threading.py -p 80-443 -s 1.0 -t 200 192.168.1.1
    python Scan_Ports-Multi-Threading.py --settimeout 2 --threads 100 192.168.1.1
    python Scan_Ports-Multi-Threading.py --help

NOTES:
    - Par défaut, scanne les ports 1-65535
    - Timeout par défaut: 0.5 seconde par port
    - Utilise 500 threads par défaut pour optimiser la vitesse
    - Un timeout plus élevé augmente la précision mais ralentit le scan
"""
    print(help_text)

def scan_port(ip, port, timeout, open_ports):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
                print(f"Port {port} is open.")
    except Exception as e:
        pass

def threaded_port_scanner(ip, start_port, end_port, threads=500, timeout=0.5):
    print(f"On scan l'IP {ip} du port {start_port} au port {end_port} en utilisant {threads} threads (timeout: {timeout}s)...")
    open_ports = []
    port_range = range(start_port, end_port + 1)

    thread_list = []
    for port in port_range:
        t = threading.Thread(target=scan_port, args=(ip, port, timeout, open_ports))
        thread_list.append(t)
        t.start()

        if len(thread_list) >= threads:
            for t in thread_list:
                t.join()
            thread_list = []

    for t in thread_list:
        t.join()

    print("\nScan complete.")
    if open_ports:
        open_ports.sort()
        print("Open ports:", open_ports)
    else:
        print("No open ports found.")

def parse_arguments():
    args = sys.argv[1:]
    
    target_ip = None
    start_port = 1
    end_port = 65535
    threads = 500
    timeout = 0.5
    
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg in ['-h', '--help', '-help']:
            show_help()
            sys.exit(0)
        elif arg in ['-p', '--ports']:
            if i + 1 >= len(args):
                print("Erreur: L'option -p/--ports nécessite une valeur (ex: 80-443)")
                sys.exit(1)
            try:
                port_range = args[i + 1]
                start_port, end_port = map(int, port_range.split('-'))
                i += 1
            except ValueError:
                print("Erreur: Format de ports invalide. Utilisez: start-end (ex: 80-443)")
                sys.exit(1)
        elif arg in ['-t', '--threads']:
            if i + 1 >= len(args):
                print("Erreur: L'option -t/--threads nécessite une valeur")
                sys.exit(1)
            try:
                threads = int(args[i + 1])
                if threads <= 0:
                    raise ValueError
                i += 1
            except ValueError:
                print("Erreur: Le nombre de threads doit être un entier positif")
                sys.exit(1)
        elif arg in ['-s', '--settimeout']:
            if i + 1 >= len(args):
                print("Erreur: L'option -s/--settimeout nécessite une valeur")
                sys.exit(1)
            try:
                timeout = float(args[i + 1])
                if timeout <= 0:
                    raise ValueError
                i += 1
            except ValueError:
                print("Erreur: Le timeout doit être un nombre positif (en secondes)")
                sys.exit(1)
        elif not arg.startswith('-'):
            target_ip = arg
        else:
            print(f"Option inconnue: {arg}")
            print("Utilisez -h ou --help pour voir l'aide")
            sys.exit(1)
        
        i += 1
    
    return target_ip, start_port, end_port, threads, timeout

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Erreur: Adresse IP cible manquante")
        print("Usage: python Scan_Ports-Multi-Threading.py <target_ip>")
        print("Utilisez -h ou --help pour plus d'informations")
        sys.exit(1)
    
    target_ip, start_port, end_port, threads, timeout = parse_arguments()
    
    if not target_ip:
        print("Erreur: Adresse IP cible manquante")
        print("Utilisez -h ou --help pour voir l'aide")
        sys.exit(1)
    
    try:
        socket.inet_aton(target_ip)
    except socket.error:
        print(f"Erreur: '{target_ip}' n'est pas une adresse IP valide")
        sys.exit(1)
    
    threaded_port_scanner(target_ip, start_port, end_port, threads, timeout)
