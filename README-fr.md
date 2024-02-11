[![English version](https://img.shields.io/badge/Read%20in-english-blue?style=for-the-badge&logo=appveyor)](https://github.com/Sitois/Nuclear/blob/main/README.md)


# 🌌 Nuclear
### Un puissant SelfBot Discord écrit en Python utilisant [selfcord.py](https://github.com/OmegaDevStudio/Selfcord)! ###

<div align="center">
  <img src="https://media.discordapp.net/attachments/1135264530188992562/1198281648437993553/CIjvBOJ.png?ex=65be55bf&is=65abe0bf&hm=40a3c63ca07dfac28726eadae220a07412551a69deea021b73c24ae00933782e&=&format=webp&quality=lossless" alt="icône" width="50%" height="50%">

  [![GitHub release (latest by date)](https://img.shields.io/github/v/release/Sitois/Nuclear.svg?style=flat)](https://github.com/Sitois/Nuclear/releases)
  [![Téléchargements GitHub](https://img.shields.io/github/downloads/Sitois/Nuclear/total.svg?style=flat)](https://github.com/Sitois/Nuclear/releases)
  [![Étoiles GitHub](https://img.shields.io/github/stars/Sitois/Nuclear.svg?style=flat)](https://github.com/Sitois/Nuclear/stargazers)
  [![Observateurs GitHub](https://img.shields.io/github/watchers/Sitois/Nuclear.svg?style=flat)](https://github.com/Sitois/Nuclear/watchers)
  [![CodeFactor](https://www.codefactor.io/repository/github/Sitois/Nuclear/badge?style=flat)](https://www.codefactor.io/repository/github/Sitois/Nuclear)
  [![Problèmes GitHub](https://img.shields.io/github/issues/Sitois/Nuclear.svg?style=flat)](https://github.com/Sitois/Nuclear/issues)
  [![Support](https://shields.yoki-labs.xyz/shields/i/kQj8PmAp?style=flat)](https://www.guilded.gg/i/kQj8PmAp?cid=c7d78c47-5231-47fa-b388-e11d41360e2a&intent=chat)
</div>

## ⛔ Avertissement
**Les SelfBots ne sont pas autorisés par les CGU (ou TOS) de Discord et peuvent facilement entraîner le banissement de votre compte. Veuillez utiliser ce script uniquement à des fins éducatives.**

## 💾 Installation

1. Téléchargez la dernière version depuis la section [Releases](https://github.com/Sitois/Nuclear/releases) sur GitHub.
2. Assurez-vous d'avoir [Python](https://www.python.org/downloads/ "Installez Python ici") installé.
3. Ouvrez votre Terminal et rendez-vous dans le dossier Nuclear en utilisant `cd`.
3. Installez les dépendances : `pip install -r requirements.txt`
4. Exécutez le programme : `python selfbot.py`

## 🔧 Configuration
Ouvrez `config_selfbot.py` avec n'importe quel éditeur de texte et saisissez un token d'__utilisateur__.

## 🌟 Fonctionnalités
* Templates RPC personnalisés,
* Créez votre propre RPC,
* Commandes vocal,
* Nitro Sniper,
* Commande IA,
* Flood et Spam,
* Snipe,
* Et bien plus, consultez la commande `Help` !

## 📜 Comment obtenir son token
1. Rendez-vous sur [Discord Web](https://discord.com/app)
2. Faites ``CTRL + MAJ + I`` puis allez dans `Console`
3. Collez ce code:
```js
window.webpackChunkdiscord_app.push([
  [Math.random()],
  {},
  req => {
    if (!req.c) return;
    for (const m of Object.keys(req.c)
      .map(x => req.c[x].exports)
      .filter(x => x)) {
      if (m.default && m.default.getToken !== undefined) {
        return copy(m.default.getToken());
      }
      if (m.getToken !== undefined) {
        return copy(m.getToken());
      }
    }
  },
]);
console.log('%cWorked!', 'font-size: 50px');
console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px');
```
Maintenant, votre token est dans votre presse-papier.
<br>
4. Collez votre token dans `config_selfbot.py`

## 👀 Aperçu
<div align="center">
  <img src="https://media.discordapp.net/attachments/1135264530188992562/1206252733976285215/Auobz9R.png?ex=65db5566&is=65c8e066&hm=5d4cb1541f60cd7890f7837c0212ed18dbab1af291fa8d783b6a12587c3dd0f7&=&format=webp&quality=lossless&width=742&height=419" alt="preview" width="" height="">
</div>
<br>
<div align="center">
  <img src="https://media.discordapp.net/attachments/1135264530188992562/1206253306360496259/EcJ09br.png?ex=65db55ef&is=65c8e0ef&hm=078cf750eb91ca80100bf59f478fbb3254647fd825a4d622b1a6d2af6b3a9912&=&format=webp&quality=lossless" alt="preview_second" width="" height="">
</div>

<br>

## ☣️ Problèmes
Oui, le SelfBot peut se déconnecter sans raison, oui le SelfBot peut afficher des erreurs aléatoires: le problème vient de la librairie utilisé: selfcord.py.
<br>
**Mais**, le créateur travaille actuellement sur une réecriture de selfcord.py où tout les bugs seront corrigés.
<br>
Soyez patient et attendez pour la sortie de la réecriture de la librairie.
<br>
Dès que la nouvelle version sort, Nuclear va migrer vers la nouvelle version.
<br>

## ⭐ Contributeurs
<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/Lenochxd">
        <img src="https://avatars.githubusercontent.com/u/101269524?s=64&v=4" alt="Lenochxd" width="80px" height="80px" style="border-radius: 50%;">
        <br>
        Lenochxd
      </a>
    </td>
<table>

Un grand merci à elle !

Jettez un oeuil à son [projet](https://github.com/Lenochxd/Webdeck) !

# Support
- Serveur Guilded : [https://guilded.gg/nuclear](https://guilded.gg/nuclear)

<br>

---

Temps de Code du Projet: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b.svg)](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401/project/018d13ec-4c15-459c-b9a8-e02089e7681b)

Mon temps total de Code: [![wakatime](https://wakatime.com/badge/user/018af69f-9d50-4699-932d-026a9efb0401.svg?style=flat)](https://wakatime.com/@018af69f-9d50-4699-932d-026a9efb0401)