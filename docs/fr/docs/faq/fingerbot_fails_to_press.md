# Que faire si « Press Failed » s’affiche lors de l’utilisation de Fingerbot ? {#what-should-i-do-if-i-see-press-failed-when-using-fingerbot}

Si la console KVM affiche « Press Failed » lorsque vous utilisez Fingerbot, il peut s’agir d’un problème d’appairage entre Fingerbot et votre appareil KVM.

Suivez les étapes ci-dessous pour supprimer l’appairage existant et appairer à nouveau Fingerbot.

1. Connectez-vous à votre KVM et accédez à **Toolbox** -> **Terminal** -> **Access Terminal** pour ouvrir le terminal.

2. Exécutez les commandes suivantes dans l’ordre :

    ```
    bluetoothctl
    ```
    ```
    scan on
    ```

    ![open bluetoothctl](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/bluetoothctl.png){class="glboxshadow"}

    Patientez un instant, puis exécutez `scan off` pour arrêter la recherche.

3. Exécutez `devices` pour afficher tous les appareils Bluetooth détectés. Repérez votre Fingerbot (répertorié sous FGB) et notez son adresse MAC.

    ![devices](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/devices.png){class="glboxshadow"}

4. Saisissez `exit` pour quitter la session bluetoothctl. Exécutez ensuite la commande ci-dessous pour supprimer l’ancien enregistrement d’appairage. Remplacez cette adresse MAC par l’adresse MAC réelle de votre Fingerbot.

    ```
    bluetoothctl remove E1:2D:B2:75:D5:BC
    ```

5. Appairez à nouveau Fingerbot avec la commande suivante. Remplacez cette adresse MAC par l’adresse MAC réelle de votre Fingerbot.

    ```
    fingerbot pair E1:2D:B2:75:D5:BC
    ```

    ![repair fingerbot](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/repair.png){class="glboxshadow"}

    Si l’opération réussit, **Done** s’affiche dans le terminal. Essayez ensuite d’utiliser à nouveau Fingerbot.

6. Si le problème persiste, contactez-nous à l’adresse [support@gl-inet.com](mailto:support@gl-inet.com) et fournissez les informations ci-dessous pour poursuivre le diagnostic.

    - La sortie des commandes suivantes :

        ```
        fingerbot action
        ```
        ```
        ls -l /
        ```

    - Les derniers journaux du KVM, exportés depuis **Help** > **Export Log Files**.

        ![export logs](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/export_logs.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
