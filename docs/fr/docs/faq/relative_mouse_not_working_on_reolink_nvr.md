# Que faire si le mode souris relative ne fonctionne pas sur un NVR Reolink ? {#what-should-i-do-if-relative-mouse-mode-doesnt-work-on-reolink-nvr}

Lorsque vous contrôlez un NVR Reolink (notamment les modèles ne prenant pas en charge deux souris) ou certains ordinateurs anciens (par exemple sans port USB) avec un KVM GL.iNet, le mode relatif peut ne pas fonctionner. Le mode peut être totalement inopérant, ou les mouvements peuvent être détectés sans que les clics répondent.

Ce problème provient principalement de la compatibilité entre l’émulation de souris du KVM et les capacités limitées d’appareils comme les NVR Reolink :

- **Avant le micrologiciel v1.4.0** : le KVM émulait une seule souris. Le passage du mode relatif au mode absolu exigeait un redémarrage, mais fonctionnait avec la plupart des appareils anciens ou spécialisés.

- **Après le micrologiciel v1.4.0** : pour changer de mode sans redémarrage, le fonctionnement par défaut a été modifié pour émuler deux souris simultanément, l’une relative et l’autre absolue. Les NVR Reolink et certains ordinateurs anciens ne prennent pas en charge deux souris, ce qui entraîne deux problèmes fréquents :

    - Le mode relatif ne fonctionne pas du tout ;
    - Le pointeur bouge, mais les clics ne répondent pas.

Vous pouvez forcer le mode relatif dans le terminal pour résoudre ce problème. Suivez ces étapes :

1. Accédez à la console du KVM, puis à **Toolbox** -> **Terminal**. Cliquez sur **Access** pour ouvrir le terminal.

2. Ouvrez le fichier de configuration avec la commande suivante :

    `vi /etc/kvmd/override.yaml`

3. Appliquez le réglage suivant pour forcer le mode relatif :

    ```
    kvmd:
        hid:
            mouse:
                absolute: false
    ```

4. Enregistrez le fichier et quittez l’éditeur.

5. Redémarrez le KVM pour appliquer les modifications.

!!! note "Remarque"

    1. Si cette méthode ne fonctionne pas, essayez de revenir à un micrologiciel antérieur à v1.4, si disponible. Il émule une seule souris et est compatible avec les appareils anciens.

    2. L’application GLKVM autonome pour macOS ne prend pas en charge le mode relatif en raison des limites de son moteur de navigateur (absence de l’API requestPointerLock). Utilisez la console Web à la place.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
