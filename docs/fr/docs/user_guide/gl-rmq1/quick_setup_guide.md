# Configuration rapide du Comet Q (GL-RMQ1) {#comet-q-gl-rmq1-quick-setup}

Regardez cette vidéo ou suivez les étapes ci-dessous pour configurer votre Comet Q.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6-f-XFkgYoU" title="Lecteur vidéo YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Raccorder les appareils {#connect-devices}

Pour plus de clarté, l’appareil A désigne l’appareil de contrôle et l’appareil B, l’appareil contrôlé.

![Raccordement des appareils 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect1.png){class="glboxshadow"}

1. Raccordez le câble Type-C du Comet Q au port Type-C de l’appareil B.

    ![Raccordement des appareils 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect2.png){class="glboxshadow"}

2. Si l’appareil B est un appareil mobile à écran tactile, tel qu’un smartphone ou une tablette, activez d’abord les commandes d’accessibilité pour permettre au Comet Q de contrôler l’écran tactile.

    - iOS : **Settings** > **Accessibility** > **Touch** > activez **AssistiveTouch**.

    - Android : recherchez **Mouse** ou **Accessibility** dans les paramètres. Les chemins de menu varient selon la marque et le modèle de l’appareil.

    ![Raccordement des appareils 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect3.png){class="glboxshadow" width="600"}

3. Suivez les instructions à l’écran pour terminer la configuration initiale. Consultez [cette section](../gl-rmq1/product_overview.md#touchscreen) pour plus de détails.

    ![Raccordement des appareils 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect4.png){class="glboxshadow"}

## Accès local {#local-access}

Vous pouvez accéder au Comet Q sur le réseau local de deux façons : par son nom de domaine ou par son adresse IP.

Avant de commencer, vérifiez que votre appareil de contrôle est connecté au même réseau local que le Comet Q.

### Nom de domaine {#domain}

1. Ouvrez un navigateur sur l’appareil de contrôle. Chrome ou Edge est recommandé pour une meilleure compatibilité.

2. Saisissez `glkvm.local` dans la barre d’adresse. La page de connexion GLKVM s’affiche. Saisissez le mot de passe administrateur.

    ![Accès local par nom de domaine](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Remarque** : vous devez définir votre mot de passe administrateur lors du premier accès.

3. Vous pouvez alors accéder localement à la console du Comet Q, puis à l’appareil contrôlé.

    ![Accès local par nom de domaine](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### Adresse IP {#ip-address}

1. Connectez le Comet Q à un réseau Wi-Fi et relevez son adresse IP sur l’écran tactile. Dans cet exemple, l’adresse IP du Comet Q est `192.168.8.197`.

2. Ouvrez un navigateur et saisissez cette adresse IP dans la barre d’adresse. La page de connexion GLKVM s’affiche. Saisissez le mot de passe administrateur.

    ![Accès local par adresse IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Remarque** : vous devez définir votre mot de passe administrateur lors du premier accès.

3. Vous pouvez alors accéder localement à la console du Comet Q, puis à l’appareil contrôlé.

    ![Accès local par adresse IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Accès à distance {#remote-access}

Plusieurs méthodes permettent d’accéder au Comet Q à distance : le service Cloud, l’application GLKVM, Tailscale et ZeroTier.

### Service Cloud {#cloud-service}

1. Associez votre appareil à KVM Cloud. Cette opération doit être effectuée sur le réseau local.

    Vous pouvez associer votre KVM au Cloud de deux façons : par association standard ou par code dynamique. Cet exemple utilise l’association standard. Pour l’association par code dynamique, consultez [ce guide](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}.

    Commencez par accéder localement à votre Comet Q, puis cliquez sur **Cloud Service** dans le coin supérieur droit. Cliquez sur **Bind To Cloud**.

    ![Association au Cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    Vous êtes redirigé vers une page de connexion. Connectez-vous avec votre compte cloud GL.iNet.

    ![Connexion pour associer l’appareil](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Vérifiez ensuite les informations de votre appareil et cliquez sur **Bind**.

    ![Confirmation de l’association de l’appareil](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Patientez un instant, le temps que votre Comet Q soit associé à votre compte. Cliquez sur **Done**.

    ![Association de l’appareil réussie](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Accédez à distance via le service Cloud.

    Ouvrez un navigateur (Google Chrome, par exemple) et saisissez `glkvm.com` dans la barre d’adresse. Sur la page de connexion, connectez-vous avec votre compte GL.iNet.

    ![Connexion pour l’accès à distance](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    Après la connexion, les appareils associés à votre compte s’affichent. Cliquez sur celui auquel vous souhaitez accéder à distance.

    ![Sélection de l’appareil pour l’accès à distance](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    Sur la nouvelle page Web, saisissez votre mot de passe administrateur pour vous connecter.

    ![Saisie du mot de passe administrateur pour l’accès à distance](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Vous pouvez ensuite accéder à distance à votre Comet Q et à l’appareil contrôlé via le Cloud, sans installer l’application.

    ![Accès à distance établi](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

### Application GLKVM {#glkvm-app}

1. Installez l’[application GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} sur votre appareil de contrôle.

2. Connectez-vous avec votre compte GL.iNet.

    ![Connexion au compte](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Si vous n’avez pas de compte, créez-en un, puis connectez-vous.

    ![Création d’un compte](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

3. Associez votre appareil.

    Après la connexion, la page ci-dessous s’affiche. Cliquez sur **Add Device**.

    ![Ajout d’un appareil](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

    Vous pouvez associer votre appareil de trois façons : Auto Discover, S/N Code et Dynamic Binding Code.

    ??? "Auto Discover"

        Cette opération doit être effectuée sur le réseau local. Vérifiez que votre appareil de contrôle est sur le même réseau local que le Comet Q.

        Cliquez sur **Auto Discover**. La recherche démarre automatiquement.

        ![Découverte automatique des appareils 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

        Repérez votre KVM et saisissez son Device ID pour l’associer à votre compte.

        ![Découverte automatique des appareils 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

    ??? "S/N Code"

        Cette méthode convient lorsque votre KVM n’est pas détecté ou n’est pas sur le même réseau local, mais que vous disposez de son numéro de série (S/N).

        Cliquez sur **S/N Code**. Dans la fenêtre qui s’ouvre, personnalisez le nom de l’appareil et saisissez le S/N indiqué sur l’étiquette située sous le KVM.

        ![Association par numéro de série](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Cette opération doit être effectuée sur le réseau local. Vérifiez que votre appareil de contrôle est sur le même réseau local que le Comet Q.

        1. Connectez-vous localement à votre KVM à l’aide de son nom de domaine ou de son adresse IP. Consultez [ce guide](../../faq/local_access_via_browser.md) pour plus de détails.

        2. Cliquez sur **Cloud Service** dans le coin supérieur droit, puis sur **Bind With Code**.

            ![Association par code dynamique 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

        3. Un code dynamique aléatoire à 8 chiffres est généré pour associer l’appareil. Il est valable 60 secondes. Cliquez dessus pour le copier.

            ![Association par code dynamique 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

        4. Revenez à l’application GLKVM, saisissez le code d’association dynamique et cliquez sur **Bind**.

            ![Saisie du code dynamique](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

4. Accédez à distance via l’application GLKVM.

    Une fois votre appareil KVM associé à votre compte, il apparaît avec l’état « Online » dans l’application.

    ![Appareil en ligne](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

    Cliquez sur votre appareil KVM. Une nouvelle fenêtre s’ouvre et la connexion démarre.

    ![Connexion en cours](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

    Une fois la connexion établie, saisissez le mot de passe administrateur pour vous connecter à votre appareil.

    ![Connexion à l’appareil après établissement de la liaison](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

    Vous accédez alors à votre appareil KVM, qui vous permet d’accéder à l’appareil contrôlé.

    ![Accès à l’appareil connecté](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

### Tailscale {#tailscale}

Le Comet Q intègre Tailscale pour vous permettre d’y accéder à distance via le réseau virtuel Tailscale.

Dans la console, accédez à **Apps Center** -> **Tailscale**, activez le service et associez votre Comet Q à votre compte Tailscale.

Associez ensuite votre appareil de contrôle au même compte. Vous pourrez accéder à distance à votre Comet Q en saisissant son **adresse IP virtuelle Tailscale** dans un navigateur Web sur l’appareil de contrôle, sans installer l’application GLKVM.

Consultez [ce guide](../../faq/remote_access_via_tailscale.md){target="_blank"} pour plus de détails.

### ZeroTier {#zerotier}

Le Comet Q intègre ZeroTier pour vous permettre d’y accéder à distance via le réseau virtuel ZeroTier.

Dans la console, accédez à **Apps Center** -> **ZeroTier** et activez le service.

Ajoutez ensuite le Comet Q et votre appareil de contrôle au même réseau ZeroTier (à l’aide d’un Network ID alphanumérique de 16 caractères). Vous pourrez accéder à distance à votre Comet Q en saisissant son **adresse IP ZeroTier** dans un navigateur Web sur l’appareil de contrôle, sans installer l’application GLKVM.

Consultez [ce guide](../../faq/remote_access_via_zerotier.md){target="_blank"} pour plus de détails.
