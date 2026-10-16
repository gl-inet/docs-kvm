# Questions fréquentes sur le Comet Q {#frequently-asked-questions-about-comet-q}

## Généralités {#general}

1. **Q : Que faire si l’écran de contrôle KVM affiche « Unable to Display » lorsque le Comet Q est connecté à l’appareil contrôlé ?**

    R : L’appareil contrôlé ne prend pas en charge **USB-C DisplayPort Alt Mode**, ce qui empêche la sortie du flux vidéo.

    Consultez [ce guide](../../tutorials/how_to_check_usb-c_port_dp_alt_mode.md) pour vérifier si votre appareil prend en charge DisplayPort Alt Mode.

2. **Q : Pourquoi l’appareil de contrôle ne peut-il pas afficher le clavier de saisie du mot de passe lorsque l’écran de l’appareil contrôlé est verrouillé ?**

    R : Les restrictions de sécurité d’iOS et d’Android empêchent l’affichage de la page de saisie du mot de passe pendant la recopie de l’écran ou le contrôle à distance. Vous pouvez saisir directement le mot de passe depuis l’appareil de contrôle pour déverrouiller votre appareil.

3. **Q : Pourquoi le son n’est-il pas transmis à l’appareil de contrôle pendant un appel vocal sur l’appareil contrôlé ?**

    R : Ce problème est fréquent sur les iPhone et certains appareils Android. Lorsqu’une application d’appels vocaux (par exemple, WhatsApp ou Microsoft Teams) est utilisée sur l’appareil contrôlé, les restrictions d’iOS et d’Android imposent la sortie audio par les haut-parleurs locaux de cet appareil. Le son ne peut alors pas être transmis à l’appareil de contrôle via le KVM.

    **Conseil** : le son multimédia (vidéos, musique, jeux, etc.) peut être transmis normalement à l’appareil de contrôle via le KVM lorsque les applications d’appels vocaux ne sont pas actives.

## iOS {#ios}

1. **Q : Pourquoi ne puis-je plus régler le volume système de l’appareil iOS après sa connexion au Comet Q ?**

    R : En raison des restrictions d’iOS, lorsqu’un iPhone ou iPad est connecté à un appareil de recopie d’écran tel qu’un KVM GL.iNet défini comme sortie audio, le réglage natif du volume système devient indisponible.

2. **Q : Pourquoi l’appareil iOS n’affiche-t-il pas la vidéo localement lors de la lecture dans une application vidéo ?**

    R : Lorsqu’un appareil iOS est connecté à un appareil de recopie d’écran tel qu’un KVM GL.iNet, certaines applications vidéo (par exemple, YouTube ou Netflix) utilisent par défaut **AirPlay** pour la sortie vidéo. L’appareil iOS n’affiche donc pas la vidéo localement. Ce comportement ne peut pas être désactivé au niveau du système.

    Si vous souhaitez que l’appareil contrôlé affiche les vidéos localement pendant la recopie d’écran, lisez-les dans un navigateur Web.

3. **Q : Que faire si le clavier à l’écran de l’appareil iOS disparaît après la connexion au Comet Q ?**

    R : iOS identifie probablement le Comet Q comme un clavier physique externe et masque automatiquement son clavier à l’écran. Utilisez alors le clavier de l’appareil de contrôle ou le clavier virtuel intégré à la console KVM.

    Si vous devez utiliser le clavier à l’écran d’iOS, accédez à **Settings** > **Accessibility** > **Touch** > **AssistiveTouch**, puis activez **Show Onscreen Keyboard**.

    ![AssistiveTouch](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/assistive_touch.png){class="glboxshadow" width="360"}

4. **Q : Lors de la recopie de l’écran d’un iPhone ou iPad en mode portrait ou paysage, le pointeur de l’appareil de contrôle reste décalé même après avoir ajusté l’orientation de l’écran dans la console KVM. Que faire ?**

    R : Un suivi précis du pointeur sur un iPhone ou iPad nécessite un alignement parfait entre l’orientation mesurée par le gyroscope et celle de l’écran affiché. Pendant le contrôle à distance, le système peut ne pas détecter correctement l’état du gyroscope, ce qui décale le pointeur.

    Pour résoudre ce problème, activez **Portrait Orientation Lock**/**Rotation Lock** sur votre iPhone ou iPad afin de garantir un suivi précis du pointeur.

    ![Verrouillage de l’orientation portrait](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/portrait_lock.png){class="glboxshadow" width="360"}
    <small>(Verrouillage de l’orientation portrait sur iPhone)</small>

5. **Q : Pourquoi le clavier fonctionne-t-il mal sur les appareils iOS, avec certaines touches inactives ou un pointeur de souris qui se déplace ?**

    R : Ce problème est généralement dû à l’activation de **Mouse Keys** sur l’appareil iOS. Cette fonction permet de déplacer le pointeur de la souris à l’aide d’un clavier ou d’un pavé numérique.

    Pour résoudre le problème, accédez à **Settings** > **Accessibility** > **Touch** > **AssistiveTouch** > **Mouse Keys**, puis désactivez Mouse Keys.

## Android {#android}

1. **Q : Pourquoi ne puis-je pas contrôler l’appareil en mode souris absolue ?**

    R : En raison des restrictions du système d’exploitation Android, les appareils Android ne peuvent être contrôlés qu’en mode souris relative.

    Lorsque vous utilisez l’application mobile GLKVM pour le contrôle, recouvrez entièrement le pointeur de la souris avec votre doigt pour effectuer les opérations.

2. **Q : Que faire si l’écran affiché sur l’appareil de contrôle n’est pas synchronisé avec celui du téléphone Android contrôlé ?**

    R : Certains téléphones Android identifient le Comet Q comme un écran étendu plutôt que comme un écran recopié. Pour résoudre ce problème, réglez l’affichage du téléphone sur le mode **Screen Mirroring**.

    Exemple avec la série Samsung S :

    Accédez à **Settings** > **Device Connections** > **Samsung DeX** > **Connected Display**, puis sélectionnez le mode **Screen Mirroring**.

---

Vous avez d’autres questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
