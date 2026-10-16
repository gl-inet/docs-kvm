# Accéder au KVM à distance via le Cloud {#how-to-access-kvm-remotely-via-cloud}

Avant de commencer, vérifiez les points suivants :

- L’appareil contrôlé est correctement raccordé au KVM.

- Le KVM est connecté à un réseau stable.

- Vous pouvez accéder localement au KVM, car l’association de l’appareil au Cloud doit être effectuée sur le réseau local.

Suivez les étapes ci-dessous pour accéder à distance à votre KVM et à l’appareil contrôlé via le service Cloud.

## Associer votre KVM au Cloud {#bind-your-kvm-to-the-cloud}

Vous pouvez associer votre KVM au Cloud de deux façons : par association standard ou par code dynamique.

- **Association standard** : cliquez sur « Bind To KVMCloud » dans la console KVM pour être redirigé vers la page d’association contenant le jeton. Connectez-vous à votre compte cloud, puis confirmez les informations de l’appareil pour terminer l’association.

- **Association par code dynamique** : cliquez sur « Bind With Code » dans la console KVM pour générer un code dynamique aléatoire à 8 chiffres. Connectez-vous à votre compte cloud, puis saisissez ce code pour terminer l’association.

### Association standard {#regular-binding}

Connectez-vous localement à votre KVM à l’aide de son adresse IP ou de son nom de domaine, puis accédez à **Cloud Service** dans le coin supérieur droit. Cliquez sur **Bind To Cloud**.

![Association au Cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

Vous êtes redirigé vers une page de connexion. Saisissez les identifiants de votre compte GL.iNet et cliquez sur **Log In**.

![Connexion pour associer l’appareil](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

Vérifiez les informations de votre appareil, puis cliquez sur **Bind**.

![Confirmation de l’association de l’appareil](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

Patientez un instant, le temps que votre appareil soit associé à votre compte. Cliquez sur **Done**.

![Association de l’appareil réussie](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

### Association par code dynamique {#dynamic-code-binding}

Remarque : mettez à niveau le micrologiciel de votre KVM vers la version 1.7 avant d’utiliser cette fonction.

1. Connectez-vous localement à votre KVM GL.iNet à l’aide de son nom de domaine ou de son adresse IP. Consultez [ce guide](../faq/local_access_via_browser.md) pour plus de détails.

2. Après la connexion, accédez à **Cloud Service** dans le coin supérieur droit, puis cliquez sur **Bind With Code**.

    ![Association par code dynamique 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Un code dynamique aléatoire à 8 chiffres est généré pour associer l’appareil. Il est valable 60 secondes. Cliquez dessus pour le copier.

    ![Association par code dynamique 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Rendez-vous sur [https://glkvm.com/](https://glkvm.com/){target="_blank"} et connectez-vous avec votre compte cloud GL.iNet.

    ![Association par code dynamique 3](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. Après la connexion, la page ci-dessous s’affiche.

    ![Association par code dynamique 4](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    Cliquez sur **Add Device**, puis sélectionnez **Bind with Code**.

    ![Association par code dynamique 5](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. Dans la fenêtre qui s’ouvre, saisissez le code dynamique à 8 chiffres et cliquez sur **Bind**.

    ![Association par code dynamique 6](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Remarque** : le code dynamique est valable 60 secondes. S’il expire, revenez à la console KVM et cliquez sur **Regenerate Code** pour en obtenir un nouveau.

    ![Génération d’un nouveau code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

    L’appareil est alors associé à votre compte cloud.

## Accès à distance via le Cloud {#remote-access-via-cloud}

Ouvrez un navigateur (Google Chrome, par exemple) et saisissez `glkvm.com` dans la barre d’adresse. Sur la page de connexion, connectez-vous avec votre compte GL.iNet.

![Connexion pour l’accès à distance](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

Après la connexion, les appareils associés à votre compte s’affichent. Cliquez sur celui auquel vous souhaitez accéder à distance.

![Sélection de l’appareil pour l’accès à distance](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

Sur la nouvelle page Web, saisissez votre mot de passe administrateur pour vous connecter.

![Saisie du mot de passe administrateur pour l’accès à distance](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

Vous pouvez maintenant accéder à distance au KVM et à l’appareil contrôlé via le Cloud.

![Accès à distance établi](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

---

Vous avez d’autres questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
