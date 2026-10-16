# Restaurer un KVM via RKDevTool {#how-to-unbrick-kvm-via-rkdevtool}

Ce tutoriel explique comment restaurer un KVM GL.iNet bloqué à l’aide de RKDevTool. Cette méthode s’applique lorsque l’appareil ne peut pas être récupéré par une mise à jour normale du micrologiciel ou par le mode de secours U-Boot.

## Préparation {#preparation}

Préparez les éléments suivants pour la restauration.

- Un ordinateur Windows
- Un câble USB de données
- Un adaptateur secteur (pour le KVM)

!!! note "Remarque"

    Ne débranchez PAS le câble USB et ne coupez PAS l’alimentation du KVM pendant la restauration : cela pourrait endommager l’appareil.

    Il est recommandé de sauvegarder les données importantes avant de commencer.

## Étapes de restauration {#unbrick-steps}

Pour éviter un échec de la restauration, suivez les étapes dans l’ordre.

1. Éteignez votre KVM.

2. Téléchargez le dernier micrologiciel correspondant à votre KVM sur votre ordinateur depuis [cette page](https://dl.gl-inet.com/kvm){target="_blank"}.

3. Téléchargez le paquet de pilotes sur votre ordinateur depuis [ce lien](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/DriverAssitant_v5.11.zip) et extrayez-le dans le répertoire de votre choix.

4. Double-cliquez sur le fichier .exe pour installer le pilote.

    ![Installation du pilote](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_1.png){class="glboxshadow"}

    ![Installation du pilote](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_2.png){class="glboxshadow"}

5. Téléchargez **RKDevTool** sur votre ordinateur depuis [ce lien](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/RKDevTool_Release_v3.37.zip) et extrayez-le dans un répertoire facile d’accès.

6. Double-cliquez sur le fichier .exe pour lancer l’outil de flashage sur votre ordinateur.

    ![Exécution de RKDevTool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_1.png){class="glboxshadow"}

    ![Exécution de RKDevTool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_2.png){class="glboxshadow"}

7. Reliez le port Type-C OTG du KVM au port USB de l’ordinateur avec un câble USB de données.

    Voici le port Type-C OTG du Comet (GL-RM1), pris comme exemple.

    ![Branchement du câble USB](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/otg-port-rm1.png){class="glboxshadow gl-60-desktop"}

8. Maintenez le bouton RESET enfoncé pendant **10 secondes** tout en branchant le câble d’alimentation du KVM, puis relâchez-le. Le KVM passe en mode Loader.

    ![Bouton de réinitialisation](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/reset_button_rm1.jpg){class="glboxshadow" width="433"}

9. Dans RKDevTool, accédez à **Upgrade Firmware** -> **Firmware**, puis sélectionnez le micrologiciel téléchargé à l’étape 2 pour le charger.

    ![Sélection du micrologiciel](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/select_firmware.png){class="glboxshadow"}

    Passez ensuite à l’onglet **Upgrade** à côté de Firmware : le message « Found Loader Device » apparaît et le flashage commence.

    ![Panneau RKDevTool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/rkdevtool_panel.jpg){class="glboxshadow"}

    Le KVM redémarre automatiquement une fois la mise à jour terminée.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
