# Configuration rapide du Comet X (GL-RM4PE) {#comet-x-gl-rm4pe-quick-setup}

## Raccorder les appareils {#connect-devices}

Pour plus de clarté, l’appareil A désigne l’appareil de contrôle et l’appareil B, l’appareil contrôlé.

![Raccordement des appareils 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect1.png){class="glboxshadow"}

1. Raccordez le Comet X à un commutateur PoE à l’aide d’un câble Ethernet, ou alimentez-le avec un adaptateur secteur 5V/3A.

    ![Raccordement des appareils 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect2.png){class="glboxshadow"}

    ***Remarque** : si vous utilisez un adaptateur secteur pour l’alimentation, raccordez le Comet X à un équipement réseau (par exemple, un routeur) à l’aide d’un câble Ethernet pour accéder à Internet.*

2. Raccordez le port **HDMI IN** du Comet X à l’appareil B à l’aide d’un câble HDMI pour transmettre le signal vidéo.

    ![Raccordement des appareils 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect3.png){class="glboxshadow"}

3. Raccordez le port **USB-C** du Comet X à l’appareil B à l’aide d’un câble USB. Ce port USB-C doit être associé au port HDMI IN correspondant pour transmettre correctement les signaux du clavier et de la souris.

    ![Raccordement des appareils 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect4.png){class="glboxshadow"}

4. (Facultatif) Raccordez le port **HDMI OUT** du Comet X à un moniteur externe pour dupliquer l’affichage (sortie vidéo en boucle). Consultez la section [Contrôle local](#local-control) pour plus de détails.

5. Le raccordement est terminé. Vous pouvez maintenant accéder à la console du Comet X localement ou à distance.

## Montage en baie {#rack-mounting}

Installez le Comet X sur les rails de la baie serveur selon vos besoins.

1. Fixez les équerres de montage au Comet X à l’aide des vis fournies.

    ![Installation 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install1.png){class="glboxshadow"}

2. Fixez le Comet X aux rails de la baie avec des vis pour baie. **Les vis pour baie ne sont pas fournies**.

    ![Installation 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install2.png){class="glboxshadow"}

## Contrôle local {#local-control}

Contrôlez l’appareil directement à l’aide de câbles physiques, sans réseau, adresse IP ni nom de domaine.

Le Comet X dispose d’un port HDMI OUT et de deux ports USB supplémentaires, adaptés au dépannage local, à la configuration et à l’installation d’un système d’exploitation. Raccordez simplement votre moniteur, votre souris et votre clavier pour contrôler directement le matériel local.

1. Raccordez le port **HDMI OUT** du panneau arrière du Comet X à un moniteur externe pour dupliquer l’affichage (sortie vidéo en boucle).

    ![Contrôle local 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control1.png){class="glboxshadow"}

2. Raccordez un clavier et une souris aux ports USB du panneau avant du Comet X.

    ![Contrôle local 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control2.png){class="glboxshadow"}

3. Vous pouvez maintenant contrôler les appareils connectés avec votre clavier et votre souris locaux, tandis que le signal vidéo est retransmis au moniteur local.

## Accès sur le réseau local {#lan-access}

Vous pouvez accéder au Comet X sur le réseau local de deux façons : par son nom de domaine ou par son adresse IP.

Avant de commencer, vérifiez que votre appareil de contrôle est connecté au même réseau local que le Comet X.

### Nom de domaine {#domain}

1. Ouvrez un navigateur sur l’appareil de contrôle. Chrome ou Edge est recommandé pour une meilleure compatibilité.

2. Saisissez `glkvm.local` dans la barre d’adresse. La page de connexion GLKVM s’affiche. Saisissez le mot de passe administrateur.

    ![Accès local par nom de domaine](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain1.png){class="glboxshadow"}

    ***Remarque** : vous devez définir votre mot de passe administrateur lors du premier accès.*

3. Vous pouvez alors accéder localement à la console du Comet X, puis à l’appareil contrôlé.

    ![Accès local par nom de domaine](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain2.png){class="glboxshadow"}

### Adresse IP {#ip-address}

1. Relevez l’adresse IP du Comet X sur l’écran tactile. Dans cet exemple, l’adresse IP du Comet X est `192.168.8.197`.

2. Ouvrez un navigateur et saisissez cette adresse IP dans la barre d’adresse. La page de connexion GLKVM s’affiche. Saisissez le mot de passe administrateur.

    ![Accès local par adresse IP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip1.png){class="glboxshadow"}

    ***Remarque** : vous devez définir votre mot de passe administrateur lors du premier accès.*

3. Vous pouvez alors accéder localement à la console du Comet X, puis à l’appareil contrôlé.

    ![Accès local par adresse IP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip2.png){class="glboxshadow"}

## Accès à distance {#remote-access}

Plusieurs méthodes permettent d’accéder au Comet X à distance : le service Cloud, l’application GLKVM, Tailscale et ZeroTier.

### Service Cloud {#cloud-service}

1. Associez votre appareil à KVM Cloud. Cette opération doit être effectuée sur le réseau local.

    Vous pouvez associer votre KVM au Cloud de deux façons : par association standard ou par code dynamique. Cet exemple utilise l’association standard. Pour l’association par code dynamique, consultez [ce guide](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}.

    Commencez par accéder localement à votre Comet X, puis cliquez sur **Cloud Service** dans le coin supérieur droit. Cliquez sur **Bind To KVMCloud**.

    ![Association au Cloud](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_to_cloud.png){class="glboxshadow"}

    Vous êtes redirigé vers une page de connexion. Connectez-vous avec votre compte cloud GL.iNet.

    ![Association de l’appareil au Cloud 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind1.png){class="glboxshadow"}

    Vérifiez ensuite les informations de votre appareil et cliquez sur **Bind**.

    ![Association de l’appareil au Cloud 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind2.png){class="glboxshadow"}

    Patientez un instant, le temps que votre Comet X soit associé à votre compte. Cliquez sur **Done**.

    ![Association au Cloud réussie](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind_success.png){class="glboxshadow"}

2. Accédez à distance via le service Cloud.

    Après avoir cliqué sur Done, vous êtes redirigé vers le site `glkvm.com`, où votre appareil s’affiche.

    ![Liste des appareils associés au Cloud](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_devices.png){class="glboxshadow"}

    ***Conseil** : si vous n’êtes pas redirigé, saisissez manuellement `glkvm.com` dans la barre d’adresse et connectez-vous à votre compte GL.iNet. Votre appareil associé s’affiche après la connexion.*

    Cliquez sur l’appareil auquel vous souhaitez accéder à distance.

    ![Accès via le Cloud](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access.png){class="glboxshadow"}

    Une nouvelle page Web s’ouvre. Saisissez votre mot de passe administrateur pour vous connecter.

    ![Accès via le Cloud 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access1.png){class="glboxshadow"}

    Vous pouvez ensuite accéder à distance à votre Comet X et à l’appareil contrôlé via le Cloud.

    ![Accès via le Cloud 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access2.png){class="glboxshadow"}

### Application GLKVM {#glkvm-app}

1. Installez l’[application GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} sur votre appareil de contrôle.

2. Connectez-vous avec votre compte GL.iNet.

    ![Connexion au compte](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_login.jpg){class="glboxshadow"}

    Si vous n’avez pas de compte, créez-en un, puis connectez-vous.

    ![Création d’un compte](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_signup.png){class="glboxshadow"}

3. Associez votre appareil.

    Après la connexion, la page ci-dessous s’affiche. Cliquez sur **Add Device**.

    ![Ajout d’un appareil](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_add_device.png){class="glboxshadow"}

    Vous pouvez associer votre appareil de trois façons : Auto Discover, S/N Code et Dynamic Binding Code.

    ??? "Auto Discover"

        Cette opération doit être effectuée sur le réseau local. Vérifiez que votre appareil de contrôle est sur le même réseau local que le Comet X et préparez l’identifiant de votre appareil KVM.

        Cliquez sur **Auto Discover**. La recherche démarre.

        ![Découverte automatique des appareils 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover1.png){class="glboxshadow"}

        Repérez votre KVM et saisissez son **Device ID** pour l’associer à votre compte.

        ![Découverte automatique des appareils 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover2.png){class="glboxshadow"}

        ![Découverte automatique des appareils 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover3.png){class="glboxshadow"}

    ??? "S/N Code"

        Cette méthode convient lorsque votre KVM n’est pas détecté ou n’est pas sur le même réseau local, mais que vous disposez de son numéro de série (S/N).

        Cliquez sur **S/N Code**. Dans la fenêtre qui s’ouvre, définissez un nom d’appareil et saisissez le S/N indiqué sous le KVM.

        ![Association par numéro de série](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/add_sncode.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Cette opération doit être effectuée sur le réseau local. Vérifiez que votre appareil de contrôle est sur le même réseau local que le Comet X.

        1. Connectez-vous localement à votre KVM à l’aide de son nom de domaine ou de son adresse IP. Consultez la section [Accès sur le réseau local](#lan-access) pour plus de détails.

        2. Cliquez sur **Cloud Service** dans le coin supérieur droit, puis sur **Bind With Code**.

            ![Association par code dynamique 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code1.png){class="glboxshadow"}

        3. Un code dynamique aléatoire à 8 chiffres est généré pour associer l’appareil. Il est valable 60 secondes. Cliquez dessus pour le copier.

            ![Association par code dynamique 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code2.png){class="glboxshadow"}

        4. Revenez à l’application GLKVM, saisissez le code d’association dynamique et cliquez sur **Bind**.

            ![Saisie du code dynamique](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code3.png){class="glboxshadow"}

4. Accédez à distance via l’application GLKVM.

    Une fois votre appareil KVM associé à votre compte, il apparaît avec l’état « Online » dans l’application.

    ![Appareil en ligne dans l’application](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_devices.png){class="glboxshadow"}

    Cliquez sur votre appareil KVM. Une nouvelle fenêtre s’ouvre et la connexion démarre.

    ![Connexion en cours dans l’application](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_connecting.png){class="glboxshadow"}

    Une fois la connexion établie, saisissez votre mot de passe administrateur pour vous connecter à votre appareil.

    ![Accès à l’appareil dans l’application 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access1.png){class="glboxshadow"}

    Vous accédez alors à votre appareil KVM, qui vous permet d’accéder à l’appareil contrôlé.

    ![Accès à l’appareil dans l’application 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access2.png){class="glboxshadow"}

### Tailscale {#tailscale}

Le Comet X intègre Tailscale pour vous permettre d’y accéder à distance via le réseau virtuel Tailscale.

Dans la console, accédez à **Apps Center** -> **Tailscale**, activez le service et associez votre Comet X à votre compte Tailscale.

Associez ensuite votre appareil de contrôle au même compte. Vous pourrez accéder à distance à votre Comet X en saisissant son **adresse IP virtuelle Tailscale** dans un navigateur Web sur l’appareil de contrôle, sans installer l’application GLKVM.

Consultez [ce guide](../../faq/remote_access_via_tailscale.md){target="_blank"} pour plus de détails.

### ZeroTier {#zerotier}

Le Comet X intègre ZeroTier pour vous permettre d’y accéder à distance via le réseau virtuel ZeroTier.

Dans la console, accédez à **Apps Center** -> **ZeroTier** et activez le service.

Ajoutez ensuite le Comet X et votre appareil de contrôle au même réseau ZeroTier (à l’aide d’un Network ID alphanumérique de 16 caractères). Vous pourrez accéder à distance à votre Comet X en saisissant son **adresse IP ZeroTier** dans un navigateur Web sur l’appareil de contrôle, sans installer l’application GLKVM.

Consultez [ce guide](../../faq/remote_access_via_zerotier.md){target="_blank"} pour plus de détails.
