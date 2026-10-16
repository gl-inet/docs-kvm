# Accéder au KVM à distance via Tailscale {#how-to-access-kvm-remotely-via-tailscale}

Le KVM GL.iNet intègre Tailscale : vous pouvez l’associer au réseau virtuel Tailscale pour y accéder à distance, sans installer l’application GLKVM ni utiliser le service Cloud. Cette méthode est particulièrement utile si votre appareil de contrôle ne fonctionne pas sous Windows, macOS, Android ou iOS, et ne peut donc pas installer l’application GLKVM, ou si vous ne souhaitez pas utiliser cette application ni le service Cloud.

Suivez ces étapes pour accéder à distance à votre KVM GL.iNet via Tailscale.

## Associer le KVM à Tailscale {#bind-kvm-to-tailscale}

**Avant de commencer, connectez votre KVM et l’appareil de contrôle au même réseau local.**

1. Ouvrez un navigateur sur l’appareil de contrôle. Chrome ou Edge est recommandé pour une meilleure compatibilité.

2. Connectez-vous localement à la console de votre KVM à l’aide de son nom de domaine ou de son adresse IP. Cet exemple utilise le nom de domaine par défaut.

    Saisissez `glkvm.local` dans la barre d’adresse. La page de connexion GLKVM s’affiche. Saisissez votre mot de passe administrateur.

    ![Accès local par nom de domaine](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

3. Après la connexion, accédez à **Apps Center** -> **Tailscale**. Activez Tailscale et cliquez sur **Bind Device**.

    ![Activation de Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enable_tailscale.png){class="glboxshadow"}

4. La page de connexion Tailscale s’affiche. Saisissez votre adresse e-mail pour vous connecter.

    ![Connexion à Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

5. Après la connexion, un message indique que vous êtes sur le point de connecter l’appareil glkvm à votre tailnet. Cliquez sur **Connect**.

    ![Connexion du KVM au tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_kvm_to_tailscale.png){class="glboxshadow"}

    Votre appareil KVM est alors associé à votre tailnet.

    ![Association du KVM réussie](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_kvm_successful.png){class="glboxshadow"}

6. Vous êtes redirigé vers la console Tailscale, où un appareil nommé **glkvm** apparaît sous **Machines**.

    ![Console Tailscale 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_1.png){class="glboxshadow"}

## Associer l’appareil de contrôle {#bind-the-controlling-device}

L’exemple ci-dessous montre comment associer un ordinateur portable Windows, utilisé comme appareil de contrôle, au réseau Tailscale.

1. Installez Tailscale sur votre ordinateur portable depuis [cette page](https://tailscale.com/download){target="_blank"}.

2. Lancez Tailscale sur l’ordinateur portable et connectez-vous avec la même adresse e-mail.

    ![Connexion à Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

3. Après la connexion, un message indique que vous êtes sur le point de connecter l’ordinateur portable, c’est-à-dire l’appareil de contrôle, à votre tailnet. Cliquez sur **Connect**.

    ![Connexion de l’ordinateur au tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_pc_to_tailscale.png){class="glboxshadow"}

    Votre ordinateur portable est alors associé à votre tailnet.

    ![Association de l’ordinateur réussie](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_pc_successful.png){class="glboxshadow"}

4. Vous êtes redirigé vers la console Tailscale, où l’appareil de contrôle apparaît également sous **Machines**.

    ![Console Tailscale 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_2.png){class="glboxshadow"}

## Accès à distance via Tailscale {#remote-access-via-tailscale}

Dans la console Tailscale, cliquez sur l’**Address** de glkvm (`100.104.185.26` dans cet exemple).

![Récupération de l’adresse IP virtuelle](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/get_vitual_ip.png){class="glboxshadow"}

Quatre valeurs s’affichent :

- glkvm (nom de l’appareil)
- glkvm.tail1fd0.ts.net (nom de domaine attribué par Tailscale)
- fd7a:115c:a1e0:301:b92f (adresse IPv6 virtuelle)
- 100.104.185.26 (adresse IPv4 virtuelle).

Ces valeurs sont attribuées par Tailscale pour identifier l’appareil et permettre les communications sur le réseau virtuel. Vous pouvez accéder à distance à votre KVM à l’aide du nom de domaine attribué par Tailscale, de l’adresse IPv4 virtuelle ou de l’adresse IPv6 virtuelle.

Prenons l’exemple de l’adresse IPv4 virtuelle.

1. Copiez l’adresse IPv4 virtuelle de votre appareil KVM.

2. Ouvrez un nouvel onglet et collez l’adresse IP dans la barre d’adresse.

    ![Accès par l’adresse IP virtuelle](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enter_vitual_ip.png){class="glboxshadow"}

    Une erreur de confidentialité peut apparaître. [Pourquoi cette erreur de confidentialité s’affiche-t-elle ?](privacy_error_from_your_browser.md){target="_blank"}

    ![Erreur de confidentialité dans le navigateur](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/privacy_error.png){class="glboxshadow"}

    Cliquez sur **Advanced**, puis sur **Proceed to 100.104.185.26**. La page de connexion GLKVM s’affiche.

    ![Poursuite de la connexion](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/proceed.png){class="glboxshadow"}

3. Saisissez votre mot de passe administrateur pour vous connecter. Vous pouvez maintenant accéder à votre KVM GL.iNet et à l’appareil contrôlé via l’adresse IP virtuelle Tailscale.

    ![Accès à distance établi](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/remote_access_via_tailscale.png){class="glboxshadow"}

---

Vous avez d’autres questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
