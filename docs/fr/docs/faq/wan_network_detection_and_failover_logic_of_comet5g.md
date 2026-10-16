# Détection des réseaux WAN et logique de basculement du Comet 5G {#what-is-the-wan-network-detection-and-failover-logic-of-comet-5g}

1. Le système utilise une détection par ping : il envoie des sondes à toutes les interfaces toutes les **3 secondes** et évalue les conditions de basculement toutes les **9 secondes**.

2. Si tous les tests ping vers l’interface prioritaire échouent pendant **9 secondes**, alors qu’une interface moins prioritaire reste joignable, le basculement intervient à l’issue de cette période. Aucun basculement ne se produit si toutes les interfaces sont injoignables.

3. Les interfaces marquées hors ligne continuent de recevoir des sondes ping en arrière-plan.

4. Rétablissement : si l’interface prioritaire redevient joignable par ping pendant une période de **9 secondes**, le système rebascule vers elle à l’issue de cette période.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
