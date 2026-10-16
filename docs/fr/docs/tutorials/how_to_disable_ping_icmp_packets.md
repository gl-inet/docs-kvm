# Désactiver les paquets PING/ICMP sortants du KVM {#how-to-disable-outgoing-pingicmp-packets-from-kvm}

Le KVM envoie périodiquement des paquets PING (ICMP) pour vérifier la connectivité réseau. Ce document explique comment désactiver ce comportement et les effets associés.

## Appareils avec connexion Ethernet uniquement {#for-ethernet-only-devices}

Pour les appareils disposant uniquement d’une connexion Ethernet, comme le Comet (GL-RM1) et le Comet PoE (GL-RM1PE), le système envoie des paquets PING à la passerelle par défaut pour vérifier la connexion à Internet. Le résultat est indiqué par le voyant.

Pour désactiver temporairement ce comportement, exécutez la commande suivante :

```bash
/etc/init.d/S23led stop
```

> **Remarque :** La désactivation de ce service rend également le **bouton de réinitialisation** inutilisable.

## Appareils avec connexions Ethernet et Wi-Fi {#for-devices-with-both-ethernet-and-wi-fi}

Pour les appareils équipés d’Ethernet et du Wi-Fi, le système envoie des paquets PING à des serveurs DNS publics pour vérifier l’accès à Internet de chaque interface réseau. Ce mécanisme assure le basculement dynamique multi-WAN : l’appareil peut passer au Wi-Fi si la connexion Ethernet perd l’accès à Internet.

Pour désactiver temporairement ce comportement, exécutez la commande suivante :

```bash
/etc/init.d/S98multi-wan stop
```

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
