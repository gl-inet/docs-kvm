# Accéder au KVM localement depuis un navigateur {#how-to-access-the-kvm-locally-via-browser}

Avant de commencer, assurez-vous que l’appareil de contrôle et le KVM sont sur le même réseau local.

Vous pouvez accéder localement au KVM depuis un navigateur Web avec un nom de domaine ou une adresse IP.

## Accès local par nom de domaine {#local-access-via-domain}

1. Ouvrez un navigateur sur l’appareil de contrôle. Chrome ou Edge est recommandé pour une meilleure compatibilité.

2. Saisissez `glkvm.local` dans la barre d’adresse. Sur la page de connexion GLKVM, saisissez votre mot de passe administrateur.

    ![Accès local par nom de domaine](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    Vous pouvez maintenant accéder localement à la console du KVM et à l’appareil contrôlé.

    ![Accès local par nom de domaine](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

## Accès local par adresse IP {#local-access-via-ip-address}

Trouvez l’adresse IP du KVM dans le réseau en amont (par exemple sur votre routeur) et saisissez-la dans le navigateur. Vous pouvez ainsi accéder localement au KVM et à l’appareil contrôlé.

Prenons le **GL-AXT1800** (routeur) et le **GL-RM1 Comet** (KVM) comme exemple. Le Comet est relié au port LAN du routeur GL-AXT1800 par un câble Ethernet. L’appareil contrôlé est correctement relié au Comet avec un câble HDMI et un câble USB.

Suivez les étapes ci-dessous pour accéder à la console du KVM.

1. Connectez-vous à l’interface d’administration Web du GL-AXT1800. Le routeur doit être configuré pour accéder à Internet.

    ![Connexion à l’interface du routeur](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/log_in_router.png){class="glboxshadow"}

2. Dans l’interface du routeur, accédez à **Client** et trouvez l’adresse IP du Comet dans la liste des clients. Dans l’exemple ci-dessous, elle est **192.168.8.197**.

    ![Recherche de l’adresse IP du GLKVM](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

3. Ouvrez un nouvel onglet du navigateur et saisissez l’adresse IP du Comet, **192.168.8.197**, dans la barre d’adresse.

    Sur la page de connexion GLKVM, saisissez votre mot de passe administrateur.

    ![Accès local par adresse IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    Vous pouvez maintenant accéder localement à la console du KVM et à l’appareil contrôlé.

    ![Accès local par adresse IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
