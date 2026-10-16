# Que faire si aucun son ne provient de l’appareil contrôlé ? {#what-should-i-do-if-theres-no-audio-from-the-controlled-device}

Si vous n’entendez aucun son de l’appareil contrôlé après sa connexion au KVM (par exemple pendant la lecture d’une vidéo), essayez les solutions suivantes :

1. Vérifiez que Speaker est activé dans la console du KVM.

    Dans la console, accédez à **Settings** -> **Remote Device Settings** -> **Speaker** et activez le haut-parleur. Vérifiez également que l’icône en bas à droite est allumée, ce qui indique son activation.

    ![Haut-parleur](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/speaker.png){class="glboxshadow"}

2. Vérifiez que tous les câbles entre le KVM et l’appareil contrôlé sont bien branchés. Un mauvais branchement peut perturber la sortie audio.

3. Vérifiez si un convertisseur HDMI est utilisé. Certains ne prennent pas en charge l’audio.

    Utilisez de préférence le câble HDMI fourni, car certains câbles d’anciennes normes peuvent ne pas transmettre l’audio.

4. Vérifiez si le son est coupé sur l’appareil de contrôle et l’appareil contrôlé.

5. Dans les réglages de sortie de l’appareil contrôlé, vérifiez que le périphérique de sortie est **GLKVM**.

    ??? "macOS"

        Sur l’appareil contrôlé, accédez à **Settings** -> **Sound** -> **Output & Input** -> **Output** et choisissez **GLKVM** comme périphérique de sortie.

        ![Réglages de sortie audio sur Mac](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/mac_output_settings.png){class="glboxshadow"}

    ??? "Windows"

        Sur l’appareil contrôlé, accédez à **Settings** -> **Sound** -> **Output** et choisissez **GLKVM** comme périphérique de sortie.

        ![Paramètres de sortie audio de Windows 1](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_1.png){class="glboxshadow"}

        ![Paramètres de sortie audio de Windows 2](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_2.png){class="glboxshadow"}

        Vous pouvez aussi cliquer sur l’icône de son en bas à droite de l’appareil contrôlé et sélectionner **GLKVM** comme périphérique de lecture.

        ![Paramètres de sortie audio de Windows 3](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_3.png){class="glboxshadow"}

6. Vérifiez le pilote graphique de l’appareil contrôlé. Sans pilote graphique, l’appareil ne peut pas produire de sortie audio, donc aucun son n’est audible côté contrôle.

7. Dans les paramètres audio avancés de l’appareil de contrôle, vérifiez que le navigateur dispose d’une sortie audio active.

    Voici un exemple sous Windows 10 Pro.

    Accédez à **Settings** -> **Sound** -> **Advanced sound options**.

    ![Options audio avancées](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/advanced_sound_options.png){class="glboxshadow"}

    Réglez le volume des différentes applications et des sons système.

    ![Volume de l’application](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/app_volume.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
