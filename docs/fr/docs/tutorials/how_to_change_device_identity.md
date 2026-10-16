# Modifier l’identité du périphérique KVM {#how-to-change-kvm-device-identity}

## Qu’est-ce que l’identité du périphérique KVM ? {#what-is-kvm-device-identity}

L’identité d’un KVM GL.iNet est l’identifiant qui permet à l’appareil connecté de le reconnaître et de le distinguer lors des communications.

Le KVM dispose généralement d’un port Type-C, illustré ci-dessous, qui se connecte au port USB de l’appareil contrôlé pour émuler des périphériques (clavier, souris, clé USB, microphone, etc.) et un lecteur de CD-ROM.

![Port Type-C du GL-RM1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/gl-rm1-type-c.png){class="glboxshadow gl-60-desktop"}

Lorsque vous cliquez avec la souris, saisissez du texte au clavier ou utilisez le microphone côté contrôle, ces signaux sont transmis à distance au KVM physique. Celui-ci les transmet ensuite à l’appareil contrôlé via son port Type-C.

Le KVM est donc généralement considéré comme un périphérique composite qui émule plusieurs périphériques connectés aux ports USB de l’appareil contrôlé.

![Principe de l’identité de l’appareil](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/principle.png){class="glboxshadow"}

!!! note "Remarque"

    Si la méthode de saisie ou le clavier de l’appareil de contrôle ne correspond pas à celui de l’appareil contrôlé, certains symboles ou lettres peuvent être placés différemment. La sortie sur l’appareil contrôlé peut alors différer de la saisie côté contrôle. Cliquez [ici](../faq/keyboard_does_not_input_output_as_expected.md) pour en savoir plus.

## Pourquoi modifier l’identité du périphérique ? {#why-change-device-identity}

Le KVM GL.iNet émule plusieurs appareils destinés aux interactions avec l’utilisateur. Lorsqu’il est connecté à l’appareil contrôlé, il est reconnu comme un ensemble d’appareils : un écran et plusieurs périphériques USB, dont une souris, un clavier et une clé USB.

Par défaut, l’identité du périphérique est **GLKVM**. Il apparaît donc sous le nom GLKVM ou Glinet Composite Device dans les paramètres système de l’appareil contrôlé. Cela ne pose généralement pas de problème, car ces paramètres sont visibles uniquement par les utilisateurs eux-mêmes.

![Identité par défaut de l’appareil](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_default.png){class="glboxshadow"}
<small>(Paramètres Bluetooth et appareils)</small>

![Paramètres du haut-parleur](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/speaker.png){class="glboxshadow"}
<small>(Paramètres du haut-parleur)</small>

Il peut cependant être utile de modifier l’identité du KVM dans les situations suivantes.

??? "Scénario 1 : Éviter les alertes des logiciels de surveillance sur un ordinateur professionnel"

    Un ordinateur professionnel utilisé comme appareil contrôlé peut disposer d’un logiciel de surveillance intégré ou installé. Ces outils peuvent considérer l’accès à distance par KVM comme une activité anormale, déclencher des alertes et les signaler aux systèmes informatiques.

    Modifier l’identité du KVM peut aider à éviter ces notifications inutiles tout en conservant les fonctions de contrôle à distance.

??? "Scénario 2 : Masquer l’utilisation du KVM lors du partage d’écran en réunion en ligne"

    Pendant une réunion en ligne avec partage d’écran, les paramètres système de l’appareil contrôlé (par exemple Bluetooth & devices) peuvent afficher l’identité par défaut du KVM. Cela peut révéler l’utilisation du KVM aux participants, ce qui peut être indésirable pour certains utilisateurs.

    La modification de l’identité permet de masquer le KVM sur les écrans partagés.

    ![Partage d’écran](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/screen_sharing.png){class="glboxshadow"}
    <small>(Partage d’écran)</small>

??? "Scénario 3 : Rétablir le contrôle d’une souris ou d’un clavier qui ne répond pas"

    Si vous ne pouvez pas contrôler la souris et le clavier de l’appareil contrôlé via le KVM, essayez de modifier l’identité du KVM pour éviter les problèmes de compatibilité et permettre une transmission correcte des signaux.

## Limites de la personnalisation de l’identité {#limitations-of-device-identity-customization}

!!! warning "Les logiciels de détection comportementale peuvent toujours identifier le KVM"

    Quelle que soit la personnalisation de l’identité USB, la **structure** USB des périphériques virtualisés (clavier, souris, microphone, caméra, etc.) peut toujours sembler suspecte à un logiciel de détection comportementale.

    Tous ces périphériques virtualisés appartiennent en effet à **un seul périphérique USB composite**. Un périphérique composite regroupant uniquement un clavier et une souris est relativement courant : de nombreux récepteurs sans fil, comme Logitech Unifying, présentent une structure similaire. En revanche, un seul périphérique USB composite regroupant simultanément **clavier, souris et microphone** est extrêmement rare en pratique.

    La modification de l’identité seule **peut donc ne pas suffire** à éviter la détection par des logiciels avancés de surveillance ou d’analyse comportementale.

## Comment modifier l’identité du périphérique {#how-to-change-device-identity}

### Micrologiciel v1.10 et versions ultérieures {#firmware-v110-and-above}

1. Connectez-vous au KVM et accédez à **Settings** en haut à droite. Dans **USB Devices**, trouvez **Device Identity** et personnalisez cette valeur.

    ![Personnalisation de l’identité 1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize1.png){class="glboxshadow"}

2. Dans la fenêtre qui s’ouvre, cliquez sur **Confirm** pour redémarrer.

    ![Personnalisation de l’identité 2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize2.png){class="glboxshadow"}

3. Après le redémarrage, la nouvelle identité apparaît dans la console du KVM.

    ![Personnalisation de l’identité 3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize3.png){class="glboxshadow"}

4. Vérifiez l’identité du périphérique. L’exemple suivant utilise Windows 11 Pro comme appareil contrôlé.

    Sur l’appareil contrôlé, accédez à **Settings** -> **Bluetooth & devices**. Les périphériques d’entrée et audio sont reconnus avec les identités que vous avez définies.

    ![Personnalisation de l’identité 4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize4.png){class="glboxshadow"}

### Micrologiciel v1.9 et versions antérieures {#firmware-v19-and-earlier}

1. Connectez-vous au KVM et accédez à **Settings** -> **System** -> **Device Identity**. Sélectionnez une identité prédéfinie dans la liste déroulante.

    ![Personnalisation de l’identité 1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize1.jpg){class="glboxshadow"}

    Vous pouvez aussi cliquer sur **Customize** et renseigner les paramètres souhaités dans la fenêtre qui s’ouvre.

    ![Personnalisation de l’identité 2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize2.jpg){class="glboxshadow"}

2. Dans la fenêtre qui s’ouvre, cliquez sur **Confirm** pour redémarrer.

    ![Personnalisation de l’identité 3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize3.png){class="glboxshadow"}

3. Après le redémarrage, la nouvelle identité apparaît dans la console du KVM.

    ![Personnalisation de l’identité 4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize4.jpg){class="glboxshadow"}

4. Vérifiez l’identité du périphérique. L’exemple suivant utilise Windows 10 Pro comme appareil contrôlé.

    Sur l’appareil contrôlé, accédez à **Settings** -> **Bluetooth & devices**. Les périphériques d’entrée et audio sont reconnus avec les identités que vous avez définies.

    ![Personnalisation de l’identité 5](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_modified.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
