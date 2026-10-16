# Restaurer votre KVM avec U-Boot {#using-u-boot-to-unbrick-your-kvm}

Si votre KVM est devenu inutilisable après des modifications personnelles ou l’installation d’un micrologiciel incorrect, il peut ne plus démarrer correctement. Dans ce cas, vous pouvez réinstaller le micrologiciel à l’aide du mode de récupération U-Boot.

## Préparation {#preparation}

Préparez un ordinateur fixe ou portable doté d’un port Ethernet. Si votre ordinateur n’en possède pas, vous devez utiliser un adaptateur USB-Ethernet supplémentaire.

## Étapes de restauration {#unbrick-steps}

Pour éviter un échec de la restauration, suivez scrupuleusement les étapes ci-dessous.

1. Téléchargez le micrologiciel sur votre ordinateur depuis [cette page](https://dl.gl-inet.com/kvm){target="_blank"}.

2. Débranchez l’alimentation du KVM. Raccordez votre ordinateur au port Ethernet du KVM.

3. Maintenez fermement le bouton Reset enfoncé et **mettez simultanément votre KVM sous tension**.

    Attendez que le voyant clignote plusieurs fois selon une séquence régulière. Relâchez le bouton Reset **après** le changement de séquence de clignotement.

    !!! note "Séquences de clignotement selon le modèle"

        - **Comet (GL-RM1)** : lorsque vous maintenez le bouton Reset enfoncé, le voyant bleu clignote 5 fois. Relâchez le bouton après ces 5 clignotements ; le voyant bleu reste alors allumé en continu.

        - **Comet PoE (GL-RM1PE)** : lorsque vous maintenez le bouton Reset enfoncé, le voyant bleu clignote 5 fois. Relâchez le bouton après ces 5 clignotements ; le voyant bleu reste alors allumé en continu.

        - **Comet Pro (GL-RM10)** : maintenez le bouton Reset enfoncé pendant environ 5 secondes, tout en mettant simultanément le KVM sous tension, puis relâchez le bouton. L’appareil passe en mode U-Boot.

        - **Comet 5G (GL-RM10RC)** : maintenez le bouton Reset enfoncé pendant environ 5 secondes, tout en mettant simultanément le KVM sous tension, puis relâchez le bouton. L’appareil passe en mode U-Boot.

4. Définissez manuellement l’adresse IP de votre ordinateur sur **192.168.1.2**. Suivez les instructions ci-dessous correspondant à votre système d’exploitation.

    ??? "Windows 7 / Windows 10"

        1. Accédez à **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Cliquez avec le bouton droit sur **Local Area Connection** -> **Properties**.

        3. Cliquez sur **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Définissez manuellement **IP address** sur `192.168.1.2`.

        5. Définissez **Subnet mask** sur `255.255.255.0`.

            ![Propriétés IPv4](https://static.gl-inet.com/docs/kvm/faq/debrick/win7_set_ip.jpg){class="glboxshadow"}

        6. Cliquez sur le bouton **OK**.

    ??? "Windows 11"

        1. Ouvrez Settings.

        2. Cliquez sur **Network & Internet**.

        3. Cliquez sur l’onglet **Ethernet**.

            ![Paramètres Ethernet de Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet.png){class="glboxshadow"}

        4. Dans la section « IP assignment », cliquez sur le bouton **Edit**.

            ![Modification des paramètres Ethernet de Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit1.png){class="glboxshadow"}

        5. Sélectionnez l’option **Manual**.

            ![Modification des paramètres Ethernet de Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit2.png){class="glboxshadow"}

        6. Activez le commutateur **IPv4**.

        7. Définissez l’**IP address** statique sur **192.168.1.2**.

            ![Modification des paramètres Ethernet de Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit3.png){class="glboxshadow"}

        8. Définissez **Subnet mask** sur **255.255.255.0**.

        9. Cliquez sur le bouton **Save**.

    ??? "macOS"

        1. Cliquez sur l’icône **Apple** dans le coin supérieur gauche de l’écran, puis sélectionnez **System Preferences**.

            ![Préférences système de macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences.png){class="glboxshadow"}

        2. Cliquez sur **Network**.

            ![Paramètres réseau dans les préférences système de macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences_network.png){class="glboxshadow"}

        3. Cliquez sur **Ethernet** à gauche, puis ouvrez le menu déroulant à côté de **Configure IPv4** et sélectionnez **Manually**. Si vous utilisez un adaptateur USB-Ethernet, la connexion peut porter le nom de cet adaptateur plutôt que le nom Ethernet.

            ![Configuration manuelle de l’adresse IP sous macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_1.png){class="glboxshadow"}

        4. Définissez **IPv4 Address** sur `192.168.1.2`, **Subnet Mask** sur `255.255.255.0` et **Router** sur `192.168.1.1`, puis cliquez sur le bouton Apply dans le coin inférieur droit.

            ![Configuration manuelle de l’adresse IP sous macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_2.png){class="glboxshadow"}

5. Dans un navigateur, ouvrez **http://192.168.1.1** pour accéder à l’interface Web U-Boot.

    ![Interface Web U-Boot](https://static.gl-inet.com/docs/kvm/faq/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    **Remarque :** l’interface Web U-Boot présentée ci-dessus peut différer de celle que vous voyez, car la version d’U-Boot varie selon la date de production. Pour des raisons de sécurité, nous ne proposons actuellement pas de mise à niveau d’U-Boot séparée. Si une mise à jour est nécessaire, elle sera intégrée au nouveau micrologiciel.

6. Cliquez sur **Choose file** et sélectionnez le fichier du micrologiciel. Cliquez ensuite sur le bouton **Update firmware**.

7. Patientez environ 3 minutes. **Ne mettez PAS votre KVM hors tension pendant la mise à jour.**

    Le KVM est prêt lorsque son voyant **clignote en blanc**.

8. Rétablissez les paramètres IP de l’ordinateur modifiés à l’étape 4.

9. Débranchez le câble Ethernet entre votre ordinateur et le KVM, puis connectez le KVM à un réseau (par exemple, un routeur ou un commutateur réseau) à l’aide de ce câble Ethernet ou par Wi-Fi.

    Patientez environ 1 minute pour laisser le KVM accéder à Internet. Vous pourrez ensuite accéder à nouveau à votre KVM.

    **Remarque :** les paramètres de configuration sont généralement conservés. Ils sont toutefois rétablis à leurs valeurs par défaut si une erreur de configuration a provoqué la défaillance du système ayant nécessité la restauration.

---

Vous avez d’autres questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
