# Comment utiliser l’audio bidirectionnel lors de réunions à distance ? {#how-can-i-use-two-way-audio-for-remote-meetings}

Lorsque vous travaillez à domicile, vous pouvez utiliser le KVM pour accéder à votre ordinateur de bureau et participer à des réunions audio dans Zoom, Microsoft Teams ou une application similaire. La fonction audio bidirectionnelle du KVM de GL.iNet vous permet de parler dans le microphone de votre ordinateur local et d’entendre les autres participants dans ses haut-parleurs ou votre casque.

## Configuration rapide {#quick-setup}

Suivez les étapes ci-dessous pour utiliser le microphone et le haut-parleur de votre appareil local lors d’une réunion à distance. L’exemple utilise Zoom.

1. Avant de rejoindre la réunion, connectez-vous à votre KVM sur l’ordinateur de contrôle et accédez à **Session** -> **Audio & Camera**. Activez **Speaker** et **Microphone**. Vérifiez que les deux icônes en bas à droite sont actives.

    ![Activer le haut-parleur et le microphone](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/enable-speaker-and-microphone.png){class="glboxshadow"}

    Par exemple, lorsque vous activez **Microphone**, votre navigateur peut vous demander l’autorisation d’accéder au microphone. Sélectionnez le microphone souhaité et autorisez l’accès.

    ![Demande d’accès au microphone](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/microphone-permission-popup.png){class="glboxshadow"}

2. Ouvrez Zoom et rejoignez la réunion sur l’ordinateur contrôlé. Cliquez sur la flèche à côté du bouton audio et sélectionnez les appareils suivants, comme dans cet exemple :

    - **Microphone** : Microphone (6-Comet Microphone)

    - **Speaker** : EPSON PJ (HD Audio Driver for Display Audio)

    ![Sélectionner le microphone et le haut-parleur](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/select-microphone-and-speaker.png){class="glboxshadow"}

    Réactivez ensuite votre microphone pour parler aux autres participants. Vous les entendez dans les haut-parleurs ou le casque de l’ordinateur de contrôle.

    Si vous souhaitez également montrer l’image de votre caméra locale aux participants, consultez le [guide d’utilisation de la caméra locale](../faq/use_camera_passthrough_for_remote_meetings.md).

## Dépannage {#troubleshooting}

??? note "Que faire si les autres participants ne m’entendent pas ?"

    Sur l’ordinateur contrôlé, accédez à **Settings** -> **System** -> **Sound**. Sous **Input**, recherchez le microphone virtuel du KVM, nommé **Comet Microphone** dans cet exemple. Vérifiez qu’il est aussi sélectionné dans votre application de réunion.

    ![Vérifier l’entrée](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-input.png){class="glboxshadow"}

    - Si le microphone virtuel du KVM ne s’affiche pas, vérifiez la liaison de données USB entre le KVM et l’ordinateur contrôlé. Cette liaison transmet le son du microphone à l’ordinateur contrôlé.

    - Si le microphone virtuel du KVM s’affiche et est sélectionné mais qu’aucun son n’est capté, vérifiez que le microphone n’est pas coupé sur l’ordinateur de contrôle ni dans l’application de réunion sur l’ordinateur contrôlé. Sur l’ordinateur de contrôle, vérifiez les autorisations du microphone dans le système et le navigateur, puis fermez les autres applications ou onglets qui pourraient utiliser le microphone.

??? note "Que faire si je n’entends pas les autres participants ?"

    Sur l’ordinateur contrôlé, accédez à **Settings** -> **System** -> **Sound**. Sous **Output**, recherchez la sortie audio HDMI reliée au KVM, nommée **EPSON PJ** dans cet exemple. Vérifiez que le même appareil est sélectionné comme haut-parleur dans votre application de réunion.

    ![Vérifier la sortie](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-output.png){class="glboxshadow"}

    - Si la sortie audio HDMI ne s’affiche pas, vérifiez la liaison HDMI entre l’ordinateur contrôlé et le KVM. Elle transmet le son provenant de l’ordinateur contrôlé. Si vous utilisez un adaptateur HDMI, vérifiez qu’il prend en charge l’audio.

    - Si la sortie audio HDMI s’affiche et est sélectionnée mais que vous n’entendez toujours pas les autres participants, vérifiez que le son n’est coupé ni sur l’ordinateur de contrôle, ni dans l’onglet du navigateur, ni sur les haut-parleurs ou le casque.

    Pour en savoir plus, consultez [Aucun son provenant de l’appareil contrôlé](../faq/no_audio_from_the_controlled_device.md).

??? note "Que faire si le son se coupe après l’actualisation de la page ou la reconnexion ?"

    Vérifiez à nouveau **Speaker** et **Microphone** dans la console KVM. Les règles de sécurité du navigateur peuvent désactiver la lecture sur le haut-parleur ou couper le microphone après l’actualisation de la page ou la reconnexion.

    Pour en savoir plus, consultez [Les réglages du haut-parleur et du microphone ne sont pas conservés](../faq/speaker_microphone_settings_cannot_be_retained.md).

??? note "Que faire si le message « Microphone Access Denied » s’affiche ?"

    Sur l’ordinateur de contrôle, vérifiez les points suivants :

    - **Autorisations système** : sous Windows 11, accédez à **Settings** -> **Privacy & security** -> **Microphone**. Activez **Microphone access**, **Let apps access your microphone** et **Let desktop apps access your microphone**.

    - **Autorisations du navigateur** : autorisez le site web du KVM à accéder à votre microphone. Si l’accès a été bloqué, mettez à jour les autorisations du microphone pour ce site et actualisez la page.

    - **Utilisation du microphone** : fermez les autres applications ou onglets du navigateur qui pourraient utiliser le microphone.

    Après ces vérifications, réactivez **Microphone** dans la console KVM.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
