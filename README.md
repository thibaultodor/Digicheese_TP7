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
digicheese/
├── __init__.py
├── decorator/
│   └── role_required.py
├── enums/
│   └── role_enum.py
├── models/
│   ├── __init__.py
│   ├── adresse.py
│   ├── boutique.py
│   ├── client.py
│   ├── commande.py
│   ├── commune.py
│   ├── conditionnement.py
│   ├── detail_commande.py
│   ├── mise_a_jour_stock.py
│   ├── objet_goodies.py
│   ├── prix_objet.py
│   ├── regles_conditionnement.py
│   ├── role.py
│   ├── roles_utilisateur.py
│   ├── stock.py
│   ├── stock_ligne.py
│   └── utilisateur.py
├── repositories/
│   ├── __init__.py
│   ├── base_repository.py
│   ├── r_adresse.py
│   ├── r_boutique.py
│   ├── r_client.py
│   ├── r_commande.py
│   ├── r_commune.py
│   ├── r_conditionnement.py
│   ├── r_detail_commande.py
│   ├── r_mise_a_jour.py
│   ├── r_objet.py
│   ├── r_prix.py
│   ├── r_rel_cond.py
│   ├── r_role.py
│   ├── r_roles_utilisateur.py
│   ├── r_stock.py
│   ├── r_stock_ligne.py
│   └── r_utilisateur.py
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   ├── main.py
│   ├── admin/
│   │   ├── __init__.py
│   │   ├── commune_route.py
│   │   ├── conditionnemens_route.py
│   │   ├── objet_route.py
│   │   └── user_route.py
│   └── colis/
│       ├── __init__.py
│       ├── adresse_route.py
│       ├── client_route.py
│       ├── commande_route.py
│       ├── detail_commande_route.py
│       ├── mailler_route.py
│       └── statistique_route.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── profile.html
│   └── signup.html
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_admin.py
    ├── test_auth.py
    └── test_base_view.py

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
