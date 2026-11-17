# 🛡️ httpsentinel

![httpsentinel](docs/assets/banner.png)

> 🌐 **Page du projet :** [vbenji23.github.io/httpsentinel](https://vbenji23.github.io/httpsentinel/)

Scanner de sécurité web en ligne de commande. Donne-lui une URL, il analyse la surface exposée et produit un rapport de durcissement.

`httpsentinel` effectue une **reconnaissance passive** (aucune charge offensive, aucune exploitation) : il ne fait que des requêtes HTTP normales et inspecte les réponses. Il est pensé pour auditer **vos propres sites** ou des cibles pour lesquelles vous avez une autorisation explicite.

## Fonctionnalités

- **En-têtes de sécurité** — détecte la présence/absence de `Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`.
- **TLS / certificat** — version TLS négociée, émetteur et date d'expiration du certificat, alerte si expiration proche.
- **Fingerprinting** — identifie le serveur et les technologies via les en-têtes (`Server`, `X-Powered-By`, cookies connus).
- **Fichiers sensibles exposés** — teste une liste de chemins à risque (`.git/HEAD`, `.env`, `robots.txt`, `backup.zip`, etc.).
- **Rapports** — sortie terminal colorée, ou export `--json` / `--html`.

## Installation

```bash
git clone https://github.com/vbenji23/httpsentinel.git
cd httpsentinel
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Utilisation

```bash
# Scan simple
python -m httpsentinel https://exemple.fr

# Export JSON
python -m httpsentinel https://exemple.fr --json rapport.json

# Export HTML
python -m httpsentinel https://exemple.fr --html rapport.html

# Ignorer la vérif TLS (labo / certificat auto-signé)
python -m httpsentinel https://10.0.0.5 --insecure
```

## ⚠️ Cadre légal

N'utilisez `httpsentinel` que sur des systèmes qui vous appartiennent ou pour lesquels vous disposez d'une **autorisation écrite**. Scanner un système tiers sans permission est illégal (en France, art. 323-1 et suivants du Code pénal).

## Roadmap

- [ ] Détection de cookies sans `Secure` / `HttpOnly` / `SameSite`
- [ ] Vérification des enregistrements DNS (SPF, DMARC)
- [ ] Mode batch (liste d'URL depuis un fichier)
- [ ] Scoring global A–F

## Licence

MIT — voir [LICENSE](LICENSE).
