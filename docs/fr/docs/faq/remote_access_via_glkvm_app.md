# Accéder au KVM à distance via l’application GLKVM {#how-to-access-kvm-remotely-via-glkvm-app}

Avant de commencer, vérifiez que l’appareil contrôlé est correctement raccordé au KVM GL.iNet et que le KVM est connecté à un réseau stable.

Suivez les étapes ci-dessous pour accéder à distance à votre KVM et à l’appareil contrôlé via l’application GLKVM.

## Installation et connexion {#install-and-log-in}

1. Installez l’[application GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} sur votre appareil de contrôle.

2. Ouvrez l’application GLKVM et connectez-vous avec votre compte GL.iNet.

    ![Connexion au compte](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Si vous n’avez pas de compte GL.iNet, créez-en un, puis connectez-vous.

    ![Création d’un compte](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

## Associer votre KVM {#bind-your-kvm}

Après la connexion, la page ci-dessous s’affiche. Cliquez sur **Add Device**.

Vous pouvez associer votre KVM de trois façons : Auto Discover, S/N Code et Dynamic Binding Code.

![Ajout d’un appareil](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

### Découverte automatique {#auto-discover}

Cette opération doit être effectuée sur le réseau local. Vérifiez que votre KVM et l’appareil de contrôle sont connectés au même réseau local.

1. Cliquez sur **Auto Discover**. La recherche des appareils KVM disponibles démarre automatiquement.

    ![Découverte automatique des appareils 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

2. Repérez votre KVM et saisissez son **Device ID** pour l’associer à votre compte.

    ![Découverte automatique des appareils 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

### Numéro de série {#sn-code}

Cette méthode convient lorsque votre KVM n’est pas détecté ou n’est pas sur le même réseau local, mais que vous disposez de son numéro de série (S/N).

1. Cliquez sur **S/N Code**.

2. Dans la fenêtre qui s’ouvre, donnez un nom à votre appareil et saisissez son S/N, indiqué sur l’étiquette située sous le KVM.

    ![Association par numéro de série](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

### Code d’association dynamique {#dynamic-binding-code}

Mettez à niveau le micrologiciel de votre KVM vers la version v1.7 avant d’utiliser cette fonction.

Cette opération doit être effectuée sur le réseau local. Vérifiez que votre KVM et l’appareil de contrôle sont connectés au même réseau local.

1. Connectez-vous localement à votre KVM à l’aide de son nom de domaine ou de son adresse IP. Consultez [ce guide](../faq/local_access_via_browser.md) pour plus de détails.

2. Après la connexion, accédez à **Cloud Service** dans le coin supérieur droit, puis cliquez sur **Bind With Code**.

    ![Association par code dynamique 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Un code dynamique aléatoire à 8 chiffres est généré pour associer l’appareil. Il est valable 60 secondes. Cliquez dessus pour le copier.

    ![Association par code dynamique 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Revenez à l’application GLKVM, saisissez le code d’association dynamique et cliquez sur **Bind**.

    ![Saisie du code dynamique](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

## Accès à distance {#remote-access}

Une fois votre appareil KVM associé à votre compte, il apparaît avec l’état « Online » dans l’application.

![Appareil en ligne](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

Cliquez sur votre appareil KVM. Une nouvelle fenêtre s’ouvre et la connexion démarre.

![Connexion en cours](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

Une fois la connexion établie, saisissez votre mot de passe administrateur pour vous connecter.

![Connexion à l’appareil après établissement de la liaison](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

Vous pouvez maintenant accéder à votre appareil KVM, qui vous permet d’accéder à l’appareil contrôlé.

![Accès à l’appareil connecté](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

---

Vous avez d’autres questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
