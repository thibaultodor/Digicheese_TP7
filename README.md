# 🧀 DigiCheese – TP7 API Backend

## 📌 Présentation du projet

Ce projet correspond au **TP7 – Activité 3** du parcours *Lead Dev / DevOps* (Diginamic).
Il consiste à concevoir et développer une **API Backend en Python (Flask)** pour la **Fromagerie DigiCheese**, dans le cadre d’une refonte du système d’information existant.

L’application permet :
- la gestion des **utilisateurs et des rôles**,
- la **gestion des commandes et des colis**,
- la **gestion des stocks**,
- l’authentification et la sécurisation des accès,
- l’exposition d’une **API REST** testable via Swagger.

---

## 👥 Équipe projet

- **Nom** : Julien Milhau Villar
- **Nom** : Thibault Odor
- **Nom** : Victor Odin  

---

## 🏗️ Architecture du projet

```
Digicheese_TP7/
│
├── .venv/
├── digicheese/
│   ├── __init__.py
│   ├── auth.py
│   ├── main.py
│   ├── models.py
│   └── templates/
│       └── base.html
│       └── index.html
│       └── login.html
│       └── profile.html
│       └── signup.html
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Technologies utilisées

- Python 3.11+
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLite / MySQL
- Swagger / OpenAPI
- PyCharm

---

## 🚀 Lancement rapide

```bash
python -m venv .venv
source .venv/bin/activate
python -m flask run
```

---

## Insert Database

Insérer le fichier sql sur la database afin d'avoir les utilisateurs pour se connecter

---

## 📅 Informations pédagogiques

- Formation : Diginamic – Lead Dev / DevOps
- Projet : TP7 – Activité 3
- Année : 2025–2026