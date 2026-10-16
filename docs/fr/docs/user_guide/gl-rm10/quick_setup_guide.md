# Configuration rapide de Comet Pro (GL-RM10) {#comet-pro-gl-rm10-quick-setup}

Regardez cette vidéo ou suivez les étapes ci-dessous pour configurer votre Comet Pro.

<iframe width="560" height="315" src="https://www.youtube.com/embed/onxj5EEf9Ys" title="Lecteur vidéo YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Branchement des appareils {#connect-devices}

Dans ce guide, l’appareil A désigne l’appareil de contrôle et l’appareil B l’appareil contrôlé.

![Branchement des appareils](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/connect-devices.png){class="glboxshadow"}

1. Branchez Comet Pro à une source d’alimentation.

    ![Mise sous tension](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/01-power-on.png){class="glboxshadow"}

2. Reliez le port HD IN de Comet Pro au port HD OUT de l’appareil B à l’aide d’un câble HDMI. Si nécessaire, utilisez un autre câble HD pour relier le port HD OUT de Comet Pro à un moniteur externe.

    ![Branchement du câble HD](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/02-hd-cable.png){class="glboxshadow"}

3. Reliez le port USB Type-C de Comet Pro au port USB de l’appareil B à l’aide d’un câble USB.

    ![Branchement du câble USB](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/03-usb-cable.png){class="glboxshadow"}

4. Connectez Comet Pro à votre réseau à l’aide d’un câble Ethernet ou en Wi-Fi.

    - Ethernet : connectez le port Ethernet de Comet Pro à votre réseau.

        ![Connexion Ethernet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/04-ethernet.png){class="glboxshadow"}

    - Wi-Fi : balayez l’écran tactile vers la gauche, puis connectez Comet Pro (GL-RM10) à un réseau Wi-Fi existant (2.4G/5G pris en charge).

        ![Connexion Wi-Fi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/04-wifi.png){class="glboxshadow"}

5. Les branchements sont terminés. Vous pouvez maintenant accéder à la console de Comet Pro en local ou à distance.

## Accès local {#local-access}

Vous pouvez accéder à Comet Pro sur le réseau local de deux façons : par son nom de domaine ou par son adresse IP.

Avant de vous connecter, assurez-vous que votre appareil de contrôle se trouve sur le même réseau local que Comet Pro.

### Nom de domaine {#domain}

1. Ouvrez un navigateur sur l’appareil de contrôle. Chrome ou Edge est recommandé pour une meilleure compatibilité.

2. Saisissez `glkvm.local` dans la barre d’adresse. La page de connexion GLKVM s’affiche. Saisissez le mot de passe administrateur.

    ![Accès local par nom de domaine](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Remarque** : lors du premier accès, vous devrez définir votre mot de passe administrateur.

3. Vous pouvez alors accéder en local à la console de Comet Pro et à l’appareil contrôlé.

    ![Accès local par nom de domaine](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### Adresse IP {#ip-address}

1. Consultez l’adresse IP de Comet Pro sur l’écran tactile. Dans cet exemple, l’adresse IP de Comet Pro est `192.168.8.197`.

2. Ouvrez un navigateur et saisissez cette adresse IP dans la barre d’adresse. La page de connexion GLKVM s’affiche. Saisissez le mot de passe administrateur.

    ![Accès local par adresse IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Remarque** : lors du premier accès, vous devrez définir votre mot de passe administrateur.

3. Vous pouvez alors accéder en local à la console de Comet Pro et à l’appareil contrôlé.

    ![Accès local par adresse IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Accès à distance {#remote-access}

Plusieurs méthodes permettent d’accéder à Comet Pro à distance : le service cloud, l’application GLKVM, Tailscale, ZeroTier et NetBird.

### Service cloud {#cloud-service}

1. Associez votre appareil à KVM Cloud. Cette opération doit être effectuée sur le réseau local.

    Deux méthodes permettent d’associer votre KVM au cloud : l’association classique ou l’association par code dynamique. Cet exemple présente l’association classique. Si vous préférez utiliser un code dynamique, consultez [ce guide](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}.

    Accédez d’abord à votre Comet Pro en local, puis à **Cloud Service** dans l’angle supérieur droit. Cliquez sur **Bind To Cloud**.

    ![Association au cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    Une page de connexion s’affiche. Connectez-vous avec votre compte cloud GL.iNet.

    ![Connexion pour associer l’appareil](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Vérifiez ensuite les informations de votre appareil et cliquez sur **Bind**.

    ![Confirmation de l’association de l’appareil](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Patientez un instant, le temps que votre Comet Pro soit associé à votre compte. Cliquez sur **Done**.

    ![Appareil associé](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Accédez à distance à votre appareil via le service cloud.

    Ouvrez un navigateur, par exemple Google Chrome, et saisissez `glkvm.com` dans la barre d’adresse. Une page de connexion s’affiche. Connectez-vous avec votre compte GL.iNet.

    ![Connexion à distance](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    Une fois connecté, vous verrez les appareils associés à votre compte. Cliquez sur celui auquel vous souhaitez accéder à distance.

    ![Sélection de l’appareil distant](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    Sur la nouvelle page qui s’ouvre, saisissez votre mot de passe administrateur pour vous connecter.

    ![Authentification administrateur à distance](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Vous pouvez alors accéder à distance à votre Comet Pro et à l’appareil contrôlé via le cloud, sans installer l’application.

    ![Accès à distance établi](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

### Application GLKVM {#glkvm-app}

1. Installez l’[application GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} sur votre appareil de contrôle.

2. Connectez-vous avec votre compte GL.iNet.

    ![Connexion](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Si vous n’avez pas de compte, créez-en un, puis connectez-vous.

    ![Création d’un compte](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

3. Associez votre appareil.

    Une fois connecté, la page ci-dessous s’affiche. Cliquez sur **Add Device**.

    ![Ajout d’un appareil](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

    Vous pouvez associer votre appareil de trois façons : **Auto Discover**, **S/N Code** et **Dynamic Binding Code**.

    ??? "Auto Discover"

        Cette opération doit être effectuée sur le réseau local. Assurez-vous que votre appareil de contrôle se trouve sur le même réseau local que Comet Pro.

        Cliquez sur **Auto Discover**. La recherche démarre automatiquement.

        ![Détection automatique 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

        Repérez votre KVM et saisissez son **Device ID** pour l’associer à votre compte.

        ![Détection automatique 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

    ??? "S/N Code"

        Utilisez cette méthode si votre KVM n’est pas détecté ou ne se trouve pas sur le même réseau local, mais que vous disposez de son numéro de série (S/N).

        Cliquez sur **S/N Code**. Dans la fenêtre qui s’ouvre, personnalisez le nom de l’appareil et saisissez le S/N indiqué sur l’étiquette sous votre KVM.

        ![Code S/N](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Cette opération doit être effectuée sur le réseau local. Assurez-vous que votre appareil de contrôle se trouve sur le même réseau local que Comet Pro.

        1. Connectez-vous à votre KVM en local à l’aide de son nom de domaine ou de son adresse IP. Consultez [ce guide](../../faq/local_access_via_browser.md) pour plus de détails.

        2. Accédez à **Cloud Service** dans l’angle supérieur droit et cliquez sur **Bind With Code**.

            ![Association par code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

        3. Un code dynamique aléatoire à 8 chiffres est généré pour associer l’appareil. Il est valable 60 secondes. Cliquez sur le code pour le copier.

            ![Association par code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

        4. Revenez dans l’application GLKVM, saisissez le code d’association dynamique et cliquez sur **Bind**.

            ![Code dynamique](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

4. Accédez à distance à votre appareil via l’application GLKVM.

    Une fois votre KVM associé à votre compte, il apparaît avec le statut « Online » dans l’application.

    ![Appareil en ligne](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

    Cliquez sur votre KVM. Une nouvelle fenêtre s’ouvre et la connexion démarre.

    ![Connexion en cours](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

    Une fois la connexion établie, saisissez le mot de passe administrateur pour vous connecter à votre appareil.

    ![Authentification après connexion](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

    Vous accédez alors à votre KVM, qui vous permet d’accéder à l’appareil contrôlé.

    ![Accès après connexion](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

### Tailscale {#tailscale}

Comet Pro intègre Tailscale, ce qui vous permet d’y accéder à distance via le réseau virtuel Tailscale.

Dans la console, accédez à **Apps Center** -> **Tailscale** et activez Tailscale. Associez ensuite votre Comet Pro à votre compte Tailscale.

Associez ensuite votre appareil de contrôle au même compte. Vous pourrez alors accéder à distance à votre Comet Pro en saisissant son **adresse IP virtuelle Tailscale** dans un navigateur sur l’appareil de contrôle, sans installer l’application GLKVM.

Consultez [ce guide](../../faq/remote_access_via_tailscale.md){target="_blank"} pour plus de détails.

### ZeroTier {#zerotier}

Comet Pro intègre ZeroTier, ce qui vous permet d’y accéder à distance via le réseau virtuel ZeroTier.

Dans la console, accédez à **Apps Center** -> **ZeroTier** et activez ZeroTier.

Connectez ensuite Comet Pro (GL-RM10) et votre appareil de contrôle au même réseau ZeroTier à l’aide d’un identifiant réseau alphanumérique à 16 caractères. Vous pourrez alors accéder à distance à votre Comet Pro (GL-RM10) en saisissant son **adresse IP ZeroTier** dans un navigateur sur l’appareil de contrôle, sans installer l’application GLKVM.

Consultez [ce guide](../../faq/remote_access_via_zerotier.md){target="_blank"} pour plus de détails.

### NetBird {#netbird}

Comet Pro intègre NetBird, ce qui vous permet d’y accéder à distance via le réseau virtuel NetBird.

Dans la console, accédez à **Apps Center** -> **NetBird** et activez NetBird. Associez ensuite votre Comet Pro à votre compte NetBird.

Associez ensuite votre appareil de contrôle au même compte. Vous pourrez alors accéder à distance à votre Comet Pro en saisissant son **adresse IP virtuelle NetBird** dans un navigateur sur l’appareil de contrôle, sans installer l’application GLKVM.

Consultez [ce guide](../../faq/remote_access_via_netbird.md){target="_blank"} pour plus de détails.
