# Erreur de confidentialité lors de l’accès au KVM par navigateur {#privacy-error-when-accessing-kvm-via-browser}

Lorsque vous accédez au KVM GL.iNet depuis un navigateur, celui-ci peut afficher **Your connection isn’t private**.

![Erreur de confidentialité](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_1.png){class="glboxshadow"}

Cet avertissement signifie que le navigateur ne peut pas valider le certificat SSL/TLS présenté par le KVM. Par exemple, il peut ne pas avoir été émis par une autorité de certification reconnue par le navigateur, ou ne pas correspondre à l’adresse IP ou au nom d’hôte utilisé pour accéder à la console.

## Pourquoi cet avertissement apparaît-il ? {#why-do-i-get-this-warning}

Dans l’exemple ci-dessus, **192.168.8.11** est l’adresse IP locale attribuée au KVM par le routeur en amont via DHCP.

!!! note "Remarque"

    Si la passerelle du routeur auquel le KVM est connecté est « 192.168.x.1 » (où x vaut généralement 0, 1 ou 8 dans les réseaux privés), l’adresse IP locale du KVM doit être « 192.168.x.y » (où y est une adresse d’hôte valide du sous-réseau).

Cette adresse IP locale sert à accéder à la console du KVM GL.iNet, et non à un site Web public.

Le KVM utilise un certificat TLS par défaut pour l’accès HTTPS par navigateur. Les navigateurs vérifient les certificats des consoles locales comme ceux des sites publics : ils doivent être fiables, valides et correspondre à l’adresse consultée.

Si le navigateur ne reconnaît pas le certificat par défaut ou si celui-ci ne couvre pas l’adresse IP locale ou le nom d’hôte saisi, un avertissement apparaît. Cela ne signifie pas que le KVM n’a aucun certificat. HTTPS peut toujours chiffrer la connexion, mais le navigateur ne peut pas vérifier l’identité du KVM.

## Comment résoudre cet avertissement ? {#how-to-resolve-the-warning}

Pour un accès local, vérifiez d’abord que l’adresse appartient bien à votre KVM. Cliquez ensuite sur **Advanced**, puis **Continue to "192.168.8.11"** (le libellé exact dépend du navigateur).

![Continue to 192.168.8.11](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_2.jpg){class="glboxshadow"}

Vous êtes alors redirigé vers la console du KVM GL.iNet.

![Accès local à la console d’administration du KVM](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/local_access.png){class="glboxshadow"}

## Puis-je utiliser mon propre certificat ? {#can-i-use-my-own-certificate}

Oui. Vous pouvez installer et utiliser votre propre certificat SSL/TLS sur le KVM. Suivez les étapes ci-dessous.

1. Obtenez un certificat SSL/TLS couvrant le nom d’hôte ou l’adresse IP utilisé pour accéder au KVM. Pour éviter les avertissements, il doit être valide et émis par une autorité de certification reconnue par le navigateur. Un certificat autosigné déclenche toujours un avertissement, sauf si vous configurez explicitement l’appareil de contrôle pour lui faire confiance.

2. Connectez-vous à la console du KVM. Cliquez sur l’icône de bouclier en haut à droite pour accéder à **Security** -> **TLS Certificate**.

    ![Certificat personnalisé 1](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert1.png){class="glboxshadow"}

    Dans la fenêtre qui s’ouvre, sélectionnez **Custom Certificate**, puis importez votre certificat et votre clé privée. Cette fonction est disponible depuis le micrologiciel v1.8.0.

    ![Certificat personnalisé 2](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert2.png){class="glboxshadow"}

    Vous pouvez également remplacer le certificat et la clé privée sur le KVM via un terminal SSH ou WinSCP. Ils sont stockés dans le répertoire suivant :

    `/etc/kvmd/user/ssl`

    Remplacez-les par votre nouveau certificat SSL et votre clé privée.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
