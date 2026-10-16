# Accéder au KVM à distance via NetBird {#how-to-access-kvm-remotely-via-netbird}

> Remarque : mettez à niveau le micrologiciel de votre KVM vers la version v1.9.0 avant d’utiliser cette fonction.

[NetBird](https://netbird.io/){target="_blank"} est une plateforme réseau open source fondée sur le modèle de sécurité Zero Trust. Elle permet de créer des réseaux privés sécurisés pour un usage personnel ou professionnel. Ce réseau superposé basé sur WireGuard® fournit un accès sécurisé à vos appareils à tout moment et depuis n’importe où.

Le KVM GL.iNet intègre NetBird : vous pouvez l’associer au réseau virtuel NetBird pour y accéder à distance, sans installer l’application GLKVM ni utiliser le service Cloud.

Suivez ces étapes pour accéder à distance à votre KVM GL.iNet via NetBird.

## Associer le KVM à NetBird {#bind-kvm-to-netbird}

**Avant de commencer, connectez votre KVM et l’appareil de contrôle au même réseau local.**

1. Connectez-vous localement à la console de votre KVM à l’aide de son nom de domaine ou de son adresse IP, puis accédez à **Apps Center** -> **NetBird**. Activez NetBird et cliquez sur **Bind Device**.

    ![Association de l’appareil](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/1-bind-device.png){class="glboxshadow"}

2. Vous êtes redirigé vers la page de confirmation de l’appareil. Cliquez sur **Confirm**.

    ![Confirmation de l’appareil](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/2-confirm.png){class="glboxshadow"}

3. Connectez-vous à votre compte NetBird. Si vous n’avez pas de compte, créez-en un d’abord.

    ![Connexion au compte NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/3-signin.png){class="glboxshadow"}

4. Après la connexion, l’appareil KVM est automatiquement associé à votre compte.

    ![KVM connecté](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/4-connected.png){class="glboxshadow"}

    Dans le tableau de bord NetBird, votre KVM apparaît également sur la page **Peers**.

    ![Tableau de bord NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/5-dashboard.png){class="glboxshadow"}

## Associer l’appareil de contrôle {#bind-the-controlling-device}

L’exemple ci-dessous montre comment associer un ordinateur portable Windows, utilisé comme appareil de contrôle, au réseau NetBird.

1. Installez NetBird sur votre ordinateur portable depuis [cette page](https://app.netbird.io/install){target="_blank"}.

    ![Installation de NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/6-install.png){class="glboxshadow"}

2. Lancez NetBird sur l’ordinateur portable et ajoutez-le au même réseau NetBird.

    NetBird n’ouvre pas de fenêtre ni d’interface distincte sur le bureau. Il apparaît uniquement sous la forme d’une icône dans la zone de notification, en bas à droite. Toutes les opérations s’effectuent depuis le menu contextuel de cette icône.

    Cliquez avec le bouton droit sur l’icône NetBird, puis sur **Connect**.

    ![Connexion de l’ordinateur](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/7-pc-connect.png){class="glboxshadow gl-50-desktop"}

3. Dans la fenêtre qui s’ouvre, cliquez sur **Accept** pour autoriser la connexion.

    ![Autorisation de l’appareil](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/8-authorize.png){class="glboxshadow"}

    Votre ordinateur portable est automatiquement associé à votre compte et ajouté au même réseau NetBird.

    ![Ordinateur connecté](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/9-login-success.png){class="glboxshadow"}

4. Dans le tableau de bord NetBird, la page **Peers** affiche deux appareils : votre KVM et l’ordinateur portable de contrôle.

    ![Tableau de bord NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/10-dashboard.png){class="glboxshadow"}

## Accès à distance via NetBird {#remote-access-via-netbird}

L’exemple ci-dessous montre comment accéder à distance à la console KVM à l’aide de l’adresse IP virtuelle NetBird.

1. Sur votre ordinateur portable, connectez-vous au tableau de bord NetBird et accédez à **Peers**.

    Repérez votre appareil KVM, puis cliquez sur son **NetBird IP** (`100.100.141.229` dans cet exemple) pour copier l’adresse IP virtuelle.

    ![Adresse IP NetBird du KVM](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/11-kvm-netbird-ip.png){class="glboxshadow"}

    Survolez l’adresse IP avec le curseur pour consulter d’autres informations, comme l’adresse IP publique, le domaine et la région.

2. Ouvrez un nouvel onglet du navigateur, collez l’adresse IP NetBird copiée dans la barre d’adresse, puis appuyez sur Entrée. La page de connexion GLKVM s’affiche.

    ![Connexion pour l’accès à distance](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-login.png){class="glboxshadow"}

    Saisissez votre mot de passe administrateur pour vous connecter. Vous pouvez maintenant accéder à votre KVM GL.iNet et à l’appareil contrôlé via l’adresse IP NetBird.

    ![Accès à distance établi](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-access.png){class="glboxshadow"}

    **Conseil** : une erreur de confidentialité peut apparaître lors du premier accès à cette adresse IP NetBird. Cliquez sur **Advanced** -> **Proceed** pour continuer. Consultez [Erreur de confidentialité dans votre navigateur](privacy_error_from_your_browser.md){target="_blank"} pour plus de détails.

---

Vous avez d’autres questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
