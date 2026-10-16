# Que faire si l’écran distant affiche uniquement le fond d’écran ? {#what-should-i-do-if-the-remote-screen-only-displays-the-desktop-wallpaper}

Si seul le fond d’écran est visible et qu’aucune action ne répond lors de l’accès via le KVM, l’appareil contrôlé utilise probablement plusieurs écrans en mode **Extend Displays**.

Pour résoudre le problème, passez l’appareil contrôlé en mode **Duplicate display** (Windows) ou **Mirror display** (macOS).

Choisissez la solution correspondant à votre système.

=== "Windows"
    Prenons Windows 10 comme exemple. Si **Extend these displays** est activé, suivez les étapes ci-dessous pour passer à **Duplicate display**.

    ![Affichage étendu](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/extend_displays.jpg){class="glboxshadow"}

    1. Sur l’appareil contrôlé, accédez à **Settings** -> **System** -> **Display**.

        ![Paramètres système de Windows 10](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/win10_system_settings.png){class="glboxshadow"}

    2. Faites défiler la page jusqu’à **Multiple displays**.

    3. Passez de Extend Displays à **Duplicate display**.

        ![Duplication de l’écran](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/duplicate_displays.jpg){class="glboxshadow"}

    4. Cliquez sur **Keep changes**.

        ![Confirmation des modifications](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/keep_changes.png){class="glboxshadow"}

    Vérifiez ensuite si vous pouvez accéder normalement à l’appareil contrôlé.

=== "macOS"
    1. Cliquez sur le menu Apple en haut à gauche et sélectionnez **System Settings**.

    2. Faites défiler la barre latérale et choisissez **Displays**.

        ![Réglages système sur Mac](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-system-settings.png){class="glboxshadow"}

    3. Dans la vue de disposition des écrans, cliquez sur **External display**. L’écran du MacBook et les moniteurs connectés apparaissent.

    4. Ouvrez le menu **Use as** et sélectionnez **Mirror mode**, généralement Mirror for Built-in Display.

        ![Recopie de l’écran sur Mac](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-mirror-display.png){class="glboxshadow"}

    Après la configuration, le Bureau complet et toutes les fenêtres de l’appareil contrôlé sont accessibles à distance.

!!! note "Remarque"
    Cette solution s’applique uniquement aux problèmes dus au mode d’affichage étendu. Si le problème persiste après l’activation de la recopie, vérifiez qu’une session utilisateur locale est ouverte et que l’appareil n’est pas bloqué sur l’écran de connexion.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
