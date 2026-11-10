# Comment transmettre l’image de la caméra locale lors de réunions à distance ? {#how-can-i-use-camera-passthrough-for-remote-meetings}

**Remarque** : Cette fonctionnalité a été introduite dans le micrologiciel v1.10.0 et n’est prise en charge qu’en mode WebRTC (FEC). Elle est actuellement disponible dans les navigateurs web et le client de bureau, mais n’est pas encore prise en charge dans l’application mobile.

---

Lorsque vous travaillez à domicile, vous pouvez utiliser le KVM pour accéder à votre ordinateur de bureau et y participer à une visioconférence dans Zoom, Microsoft Teams ou une application similaire. Cependant, la caméra risque de ne montrer que votre bureau, sans vous.

La fonctionnalité **Camera** du KVM GL.iNet permet de transmettre la vidéo de la caméra de votre ordinateur personnel à votre ordinateur de bureau sous forme de caméra USB virtuelle. Sélectionnez cette caméra dans l’application de réunion pour que les autres participants puissent vous voir pendant que vous partagez des fichiers ou des applications de votre ordinateur de bureau.

## Configuration rapide {#quick-setup}

Suivez les étapes ci-dessous pour utiliser la fonctionnalité Camera, en prenant une visioconférence Zoom comme exemple.

1. Avant de rejoindre la réunion, connectez-vous à votre KVM sur l’ordinateur de contrôle et accédez à **Session** -> **Audio & Camera**. Activez Camera, puis cliquez sur l’icône de caméra pour démarrer.

    ![enable camera 1](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera.png){class="glboxshadow"}

    Si un message de limite des ressources USB apparaît à l’activation de Camera, accédez à **Settings** -> **USB Devices** et désactivez les périphériques USB émulés inutilisés pour libérer des ressources. Activez ensuite Camera et réessayez.

    ![enable camera 3](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-3.png){class="glboxshadow"}

    Votre navigateur peut vous demander l’autorisation d’accéder à la caméra. Sélectionnez la caméra à utiliser, vérifiez l’aperçu vidéo et autorisez l’accès.

    ![enable camera 2](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-2.png){class="glboxshadow"}

2. Ouvrez Zoom et rejoignez une réunion sur l’ordinateur contrôlé. Cliquez sur la flèche à côté du bouton vidéo et sélectionnez **UVC camera**.

    ![uvc-camera](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/uvc-camera.png){class="glboxshadow"}

    Activez ensuite la vidéo pour que les autres participants puissent voir l’image de la caméra de l’appareil de contrôle.

    **Remarque** : Assurez-vous de disposer d’une connexion réseau stable pour obtenir une vidéo fluide et nette pendant la réunion.

## Dépannage {#troubleshooting}

??? note "Que faire si l’image de la caméra n’arrive pas sur l’ordinateur contrôlé ?"

    Vérifiez si l’ordinateur contrôlé reconnaît la caméra virtuelle du KVM.

    Sur l’ordinateur contrôlé, accédez à **Settings** -> **Bluetooth & devices** -> **Cameras** et recherchez UVC Camera sous Connected cameras.

    ![check camera settings](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/check-camera-settings.png){class="glboxshadow"}

    Si elle n’apparaît pas, la connexion de données USB entre le KVM et l’ordinateur contrôlé est peut-être débranchée ou mal fixée.

??? note "Que faire si le message 'Camera Access Denied' apparaît lorsque j’active Camera dans la console KVM ?"

    ![camera access denied](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/camera-access-denied.png){class="glboxshadow"}

    Vérifiez les points suivants sur l’ordinateur de contrôle :

    - **Disponibilité de la caméra** : Assurez-vous que la caméra est connectée et fonctionne. Testez-la avec l’application de caméra du système, puis fermez l’application avant de réessayer.

    - **Autorisations système** : Sous Windows 11, accédez à Settings -> Privacy & security -> Camera et activez les options suivantes : Camera access, Let apps access your camera et Let desktop apps access your camera.

    - **Autorisations du navigateur** : Autorisez le site web du KVM à accéder à votre caméra. Si l’accès a été bloqué précédemment, mettez à jour les autorisations de caméra du site et actualisez la page.

    - **Utilisation de la caméra** : Fermez les autres applications ou onglets du navigateur susceptibles d’utiliser la caméra, comme Zoom ou Microsoft Teams.

    Après ces vérifications, activez à nouveau Camera dans la console KVM.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
