# Échec de la connexion à distance via l’application GLKVM {#connection-failed-when-remote-access-via-glkvm-app}

Lors d’un accès à distance via l’application GLKVM, le KVM peut apparaître comme Online, mais rester bloqué sur « Connecting » lorsque vous cliquez dessus.

![Appareil en ligne](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/device_online.png){class="glboxshadow"}

![Connexion en cours](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connecting.png){class="glboxshadow"}

Guide de dépannage :

1. Vérifiez la stabilité de la connexion réseau.

    Assurez-vous que le KVM dispose d’une connexion Internet stable. Un voyant blanc fixe indique une connexion réseau normale.

2. Vérifiez les règles du pare-feu réseau.

    Désactivez temporairement le pare-feu local ou ajoutez les domaines GL.iNet (par exemple glkvm.com) à sa liste d’autorisation. Réessayez la connexion après avoir appliqué les modifications.

    Les étapes suivantes montrent à titre d’exemple comment modifier les règles du pare-feu sur un réseau Sky.

    ??? note "Réseau Sky (par exemple Sky Max Hub)"

        Le mécanisme de sécurité du réseau Sky peut considérer `glkvm.com` comme suspect et en bloquer l’accès. Vous pouvez lever la restriction avec l’application Sky.<br>

        1. Ouvrez l’application MySky, accédez à **Broadband** -> **Advanced Security** et vérifiez si des domaines GL.iNet sont bloqués.

            ![Configuration de MySky 1](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-1.png){class="glboxshadow"}

        2. Si le domaine est bloqué, cliquez sur la flèche vers le bas pour afficher les détails, puis sélectionnez **Allow Access** pour le débloquer.

            ![Configuration de MySky 2](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-2.png){class="glboxshadow" width="300"}

3. Désactivez le VPN ou le proxy sur l’appareil de contrôle.

    Assurez-vous qu’aucun service VPN ou proxy n’est activé sur l’appareil exécutant GLKVM, car il pourrait perturber la connexion.

4. Redémarrez le KVM si possible.

    Si possible, redémarrez physiquement le KVM pour résoudre les problèmes temporaires de réseau ou de logiciel.

    Si vous n’êtes pas à proximité du KVM, vous pouvez le redémarrer à distance depuis l’application GLKVM :

    1. Dans la liste des appareils, cliquez sur **Manage** en haut à droite de votre appareil.

        ![Redémarrage depuis l’application 1](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_1.png){class="glboxshadow"}

    2. Cliquez sur **More**, puis sélectionnez **Reboot**.

        ![Redémarrage depuis l’application 2](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_2.png){class="glboxshadow"}

Remarques techniques complémentaires :

1. Vérifiez que la résolution DNS des domaines fonctionne.

2. Assurez-vous que le trafic sortant vers les ports habituels du KVM et de l’accès à distance n’est pas bloqué.

3. Sur un réseau d’entreprise, consultez les administrateurs informatiques au sujet d’éventuelles politiques de filtrage du trafic.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
