# Que faire si le pointeur local et le pointeur distant ne se superposent pas ? {#what-should-i-do-if-the-local-and-remote-cursors-dont-match}

Si le pointeur local (sur l’appareil de contrôle) et le pointeur distant (sur l’appareil contrôlé) ne se superposent pas, suivez les étapes de dépannage ci-dessous.

![Désalignement des curseurs](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/mouse_cursor.png){class="glboxshadow"}

1. Si les pointeurs sont alignés à l’arrêt, mais se désynchronisent pendant les mouvements, vérifiez la stabilité du réseau aux deux extrémités.

    Vous pouvez également masquer le pointeur local pour afficher uniquement le pointeur distant sur l’écran de contrôle et éviter les problèmes d’alignement.

    Dans la console du KVM, accédez à **Settings** -> **Remote Device Settings** -> **Show Local Cursor** et désactivez cette option.

    ![Masquage du curseur local](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/hide_local_cursor.jpg){class="glboxshadow"}

2. Si les pointeurs ne se superposent pas même lorsque la souris est immobile et que votre KVM est un Comet Q (GL-RMQ1), sélectionnez de nouveau le type d’appareil dans la console du KVM. Si le problème persiste, passez à l’étape suivante.

    ![Type d’appareil](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/device_type.png){class="glboxshadow"}

3. Si l’appareil contrôlé est un ordinateur portable, une résolution d’affichage incorrecte est probablement en cause.

    Vérifiez le format de l’écran du portable. Vous pouvez modifier sa résolution ou le réglage EDID du KVM.

    ??? note "Modifier la résolution sur l’ordinateur portable contrôlé"

        **Sous macOS :**

        1. Accédez à **Settings** -> **Displays** -> **Optimize for**.

            ![Réglages des écrans sur Mac](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos1.png){class="glboxshadow" width="582"}

        2. Sélectionnez **GLKVM**.

            ![Sélection de GLKVM](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos2.png){class="glboxshadow" width="582"}

        3. Choisissez la résolution correspondante et vérifiez si les pointeurs se superposent.

            ![Résolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos3.png){class="glboxshadow"}

        **Sous Windows :**

        1. Accédez à **Settings** -> **System** -> **Displays**.

            ![Paramètres d’affichage de Windows](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows1.png){class="glboxshadow"}

        2. Faites défiler jusqu’à **Display resolution** et cliquez sur la case à droite.

            ![Résolution de l’écran](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows2.png){class="glboxshadow"}

        3. Sélectionnez la résolution appropriée, puis cliquez sur **Keep changes** dans la fenêtre qui s’ouvre.

            ![Résolution de l’écran](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows3.png){class="glboxshadow"}

            ![Résolution de l’écran](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows4.png){class="glboxshadow"}

    ??? note "Modifier le réglage EDID du KVM"

        L’EDID (Extended Display Identification Data) permet d’adapter automatiquement les paramètres d’affichage. L’EDID par défaut convient à la plupart des situations et ne nécessite généralement aucune modification. Consultez [Configurer l’EDID d’un KVM GL.iNet](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} pour en savoir plus.

        Si l’écran ne change pas après la modification de l’EDID, essayez de redémarrer l’appareil contrôlé.

4. Si l’appareil contrôlé n’est pas un ordinateur portable (par exemple un PC de bureau avec un écran externe), vérifiez le format de son écran principal, puis adaptez l’EDID du KVM. Consultez [Configurer l’EDID d’un KVM GL.iNet](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} pour en savoir plus.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
