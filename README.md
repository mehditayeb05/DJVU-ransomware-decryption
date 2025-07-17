# 🛡️ DJVU Ransomware Decryption Tool

Ce projet a pour objectif d'assister les victimes du ransomware **DJVU/STOP** en analysant les fichiers chiffrés et en essayant de restaurer les fichiers originaux lorsque cela est possible.

---

## 🔍 À propos

Le ransomware **DJVU** chiffre les fichiers personnels des utilisateurs et ajoute une extension spécifique (comme `.djvu`, `.gero`, `.seto`, `.boop`, etc.).  
Ce projet propose un outil de détection de fichiers chiffrés par DJVU et intègre les bases d'une tentative de déchiffrement (quand la clé est connue ou que le fichier original est accessible pour comparaison).

---

## 📁 Fonctionnalités

- 🔎 Détection de fichiers chiffrés par DJVU
- 📂 Analyse automatique d’un dossier contenant les fichiers chiffrés
- 🔐 Tentative de déchiffrement avec clés statiques ou comparaison fichier chiffré/fichier original
- 📊 Affichage des résultats (réussite ou échec du déchiffrement)
- 🛠️ Conçu pour être facilement extensible à d'autres variantes de STOP/DJVU
