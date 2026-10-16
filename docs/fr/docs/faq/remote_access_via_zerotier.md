# Accéder au KVM à distance via ZeroTier {#how-to-access-kvm-remotely-via-zerotier}

> Remarque : mettez à niveau le micrologiciel de votre KVM vers la version v1.8.0 avant d’utiliser cette fonction.

Le KVM GL.iNet intègre ZeroTier : vous pouvez l’associer au réseau ZeroTier pour y accéder à distance, sans installer l’application GLKVM ni utiliser le service Cloud.

Suivez ces étapes pour accéder à distance à votre KVM GL.iNet via ZeroTier.

## Activer ZeroTier {#enable-zerotier}

**Avant de commencer, connectez votre KVM et l’appareil de contrôle au même réseau local.**

1. Ouvrez un navigateur sur l’appareil de contrôle. Chrome ou Edge est recommandé pour une meilleure compatibilité.

2. Connectez-vous localement à la console de votre KVM à l’aide de son nom de domaine ou de son adresse IP. Cet exemple utilise l’adresse IP locale.

    Saisissez l’**adresse IP locale du KVM**, visible sur l’écran tactile ou dans l’interface de votre routeur, dans la barre d’adresse. La page de connexion GLKVM s’affiche. Saisissez votre mot de passe administrateur.

    ![Accès local par adresse IP](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/1_local_access.png){class="glboxshadow"}

3. Après la connexion, accédez à **Apps Center** -> **ZeroTier**. Activez ZeroTier. Un message jaune apparaît, comme illustré ci-dessous.

    Cliquez sur le lien du message ou sur [ce lien](https://my.zerotier.com/){target="_blank"} pour vous connecter à ZeroTier Central et créer votre réseau ZeroTier.

    ![Activation de ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/2_enable_zerotier.png){class="glboxshadow"}

## Associer le KVM à ZeroTier {#bind-kvm-to-zerotier}

1. Lors de votre première connexion à [ZeroTier](https://my.zerotier.com/){target="_blank"}, il peut vous être demandé de choisir une version de ZeroTier Central.

    ![Sélection de la version de ZeroTier Central](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/3_select_central.png){class="glboxshadow"}

    Sélectionnez la version appropriée pour continuer. Cet exemple utilise **New Central**.

    Connectez-vous avec votre adresse e-mail et votre mot de passe. Si vous n’avez pas de compte, créez-en un d’abord.

    ![Connexion à ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/4_zerotier_signin.png){class="glboxshadow"}

2. Après la connexion, créez une organisation.

    ![Création d’une organisation](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/5_create_org.png){class="glboxshadow"}

3. Sélectionnez une offre. Cet exemple utilise l’offre **Personal**, qui comprend 10 appareils, 1 administrateur réseau et 1 réseau. Pour créer davantage de réseaux, ajouter davantage d’appareils ou définir des routes et un DNS personnalisés, choisissez l’offre Essential ou Scale.

    ![Sélection d’une offre](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/6_select_plan.png){class="glboxshadow"}

4. Votre réseau ZeroTier est maintenant créé. Copiez son **Network ID**, une chaîne alphanumérique de 16 caractères. Vous en aurez besoin pour ajouter des appareils au réseau ZeroTier. Gardez cet onglet ouvert.

    ![Identifiant du réseau](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/7_copy_network_id.png){class="glboxshadow"}

5. Revenez à la console KVM et accédez à **Apps Center** -> **ZeroTier**. Repérez **Network ID** et cliquez sur **Set**.

    ![Identifiant du réseau](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id1.png){class="glboxshadow"}

    Dans la fenêtre qui s’ouvre, collez le **Network ID**, puis cliquez sur **Confirm**.

    ![Identifiant du réseau](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id2.png){class="glboxshadow"}

    Un message jaune apparaît dans la console pour indiquer que cet appareil doit être autorisé.

    ![Autorisation de l’appareil 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize1.png){class="glboxshadow"}

6. Revenez à ZeroTier Central. Un appareil, votre KVM, est en attente d’approbation. Cliquez sur **Authorize**.

    ![Autorisation de l’appareil 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize2.png){class="glboxshadow"}

    Après l’autorisation, l’état passe à Authorized en vert, comme illustré ci-dessous.

    ![Appareil autorisé 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized1.png){class="glboxshadow"}

    Dans la console KVM, vous pouvez également consulter **Network ID** et **Virtual IP**, comme illustré ci-dessous.

    ![Appareil autorisé 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized2.png){class="glboxshadow"}

## Associer l’appareil de contrôle {#bind-the-controlling-device}

L’exemple ci-dessous montre comment associer un ordinateur portable Windows, utilisé comme appareil de contrôle, au réseau ZeroTier.

1. Installez ZeroTier sur votre ordinateur portable depuis [cette page](https://www.zerotier.com/download/){target="_blank"}.

2. Lancez ZeroTier sur l’ordinateur portable et ajoutez-le au même réseau ZeroTier.

    ZeroTier n’ouvre pas de fenêtre ni d’interface distincte sur le bureau. Il apparaît uniquement sous la forme d’une icône dans la zone de notification, en bas à droite. Toutes les opérations s’effectuent depuis le menu contextuel de cette icône.

    Cliquez avec le bouton droit sur l’icône ZeroTier, puis sur **Join New Network**. Dans la fenêtre qui s’ouvre, saisissez le même **Network ID** pour ajouter ce PC au même réseau ZeroTier.

    ![Ajout au réseau](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/11_pc_join_network.jpg){class="glboxshadow"}

    Dans ZeroTier Central, repérez ensuite l’appareil Pending et autorisez-le.

    ![Autorisation de l’appareil](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/12_authorize.png){class="glboxshadow"}

3. Après l’autorisation, l’état passe à Authorized en vert, comme illustré ci-dessous.

    ![Appareil autorisé](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/13_authorized.png){class="glboxshadow"}

4. Votre KVM et l’ordinateur portable sont maintenant ajoutés au même réseau ZeroTier. Vous pouvez le vérifier grâce à leur Network ID, comme illustré ci-dessous.

    ![Appareils sur le même réseau ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/14_same_zt_network.png){class="glboxshadow"}

## Accès à distance via ZeroTier {#remote-access-via-zerotier}

L’exemple ci-dessous montre comment accéder à distance à la console KVM à l’aide de l’adresse IP ZeroTier.

1. Sur votre ordinateur portable, connectez-vous à ZeroTier Central avec votre compte, repérez votre appareil KVM et cliquez sur son **ZT IP** pour copier l’adresse.

    ![Adresse IP ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/15_zerotier_ip.png){class="glboxshadow"}

2. Ouvrez un nouvel onglet du navigateur, collez l’adresse IP ZeroTier copiée dans la barre d’adresse, puis appuyez sur Entrée. La page de connexion GLKVM s’affiche.

    Saisissez votre mot de passe administrateur pour vous connecter. Vous pouvez maintenant accéder à votre KVM GL.iNet et à l’appareil contrôlé via l’adresse IP ZeroTier.

    ![Accès à distance](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/16_remote_access.png){class="glboxshadow"}

    **Conseil** : une erreur de confidentialité peut apparaître lors du premier accès à cette adresse IP ZeroTier. Cliquez sur **Advanced** -> **Proceed** pour continuer. Consultez [Erreur de confidentialité dans votre navigateur](privacy_error_from_your_browser.md){target="_blank"} pour plus de détails.

---

Vous avez d’autres questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
