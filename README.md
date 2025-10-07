# Scan-Ports-Multi-Threading

![](./_images/tux.png)  

## Introduction

Le script `Scan-Ports-Multi-Threading.py` permet de scanner les ports d'une IP en multi-threading  

## Dépendances
> [!NOTE] 
> Assurez vous d'avoir [python](https://www.python.org/downloads/) d'installer sur votre pc 

## Utilisation

Faire un git clone du repository :
```bash
git clone https://github.com/Quirky1869/Scan-Ports-Multi-Threading.git
cd Scan-Ports-Multi-Threading
``` 

Une fois dans le dossier git vous pouvez lancé le script avec :
```bash
./Scan-Ports-Multi-Threading.py <adresse-ip>
```

## Release

Une [release](releases) est disponible  

Une fois la release récupérée vous pouvez la placer dans `/otp` et faire un lien logique pour l'utiliser depuis n'importe où :
```bash
mv Scan-Ports-Multi-Threading /otp
ln -s /otp/Scan-Ports-Multi-Threading /usr/local/bin/Scan-Ports-Multi-Threading
```

> [!NOTE]
> Assurez vous d'avoir les droits nécessaires sur `/otp/Scan-Ports-Multi-Threading`

## Paramètres

Une aide est disponible afin de connaitre les paramètres possible du script :
```bash
./Scan-Ports-Multi-Threading.py -h
./Scan-Ports-Multi-Threading.py --help
```

Les paramètres disponibles sont :
```bash
-p, --ports      Spécifie la plage de ports (format: start-end, ex: 80-443)
-t, --threads    Nombre de threads à utiliser (défaut: 500)
-s, --settimeout Timeout en secondes pour chaque connexion (défaut: 0.5)
```

## Exemples

Permet de faire un scan de ports d'une IP avec les paramètres par défaut (65535 ports scannés) :  
```bash
./Scan_Ports-Multi-Threading.py 45.86.97.8
```

![tape](./_images/gif/Scan-Ports-Multi-Threading.gif)  

Permet de faire un scan des ports 20 à 80 avec un thread de 100 d'une IP :  
```bash
./Scan_Ports-Multi-Threading.py -p 20-80 -t 100 45.86.97.8 
```

Permet de faire un scan des ports 80 à 443 avec un timeout de 1 seconde et avec un thread de 200 d'une IP :  
```bash
./Scan_Ports-Multi-Threading.py -p 80-443 -s 1.0 -t 200 45.86.97.8 
```

Permet de faire un scan des 65535 ports avec un timeout de 2 secondes et un thread de 100 d'une IP :
```bash
./Scan_Ports-Multi-Threading.py --settimeout 2 --threads 100 45.86.97.8 
```
