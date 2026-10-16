# Réduire la fréquence de détection de l’IP publique par STUN {#how-to-reduce-stun-public-ip-detection-frequency}

Le KVM utilise des requêtes STUN pour détecter son adresse IP publique afin de permettre l’accès à distance. Par défaut, l’appareil envoie ces requêtes à intervalles réguliers. Si vous accédez au KVM uniquement via un réseau local ou un VPN, vous pouvez modifier la configuration pour réduire leur fréquence.

Connectez-vous au KVM en SSH ou ouvrez **Toolbox** > **Terminal** dans la console du KVM. Sauvegardez le fichier de configuration existant avant de le modifier :

```bash
cp -p /etc/kvmd/override.yaml /etc/kvmd/override.yaml.bak
vi /etc/kvmd/override.yaml
```

Si une sauvegarde `override.yaml.bak` existe déjà, choisissez un autre nom de fichier pour la conserver. Si `override.yaml` n’existe pas, ignorez la commande de sauvegarde et créez-le avec l’éditeur.

Intégrez le réglage suivant au fichier en conservant tous les paramètres existants :

```yaml
janus:
    check:
        retries: 10000
```

Si une section `janus` existe déjà, ajoutez ou modifiez `check.retries` dans cette section. Si `check` existe déjà sous `janus`, modifiez sa valeur `retries` ou ajoutez-la à cet endroit. Ne créez pas de clés `janus` ou `check` en double. Utilisez des espaces pour l’indentation YAML et enregistrez le fichier une fois terminé.

> **Remarque :** Cette configuration réduit fortement le nombre de requêtes STUN émises par Janus. Elle peut toutefois réduire le taux de réussite de la traversée NAT par STUN pour l’accès depuis un réseau externe. **Appliquez-la uniquement si vous accédez au KVM exclusivement via un réseau local ou un VPN.**

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
