# Accéder à la console série via USB TTL {#how-to-access-serial-console-via-usb-ttl}

Suivez les étapes ci-dessous pour utiliser l’adaptateur USB TTL à des fins de débogage série :

1. Branchez l’adaptateur USB TTL sur le port USB de votre KVM.
2. Exécutez la commande suivante pour ouvrir la connexion au port série :

```bash
minicom -D /dev/ttyUSB0 -b 115200
```

Cette commande établit une connexion série à `/dev/ttyUSB0` à un débit de `115200` bauds.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
