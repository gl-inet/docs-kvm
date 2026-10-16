# Définir une adresse IP statique pour le KVM {#how-to-set-a-static-ip-for-kvm}

Ce tutoriel explique comment définir une adresse IP statique pour votre KVM GL.iNet directement dans la console lorsque le routeur en amont ne peut pas lui en attribuer une.

Suivez les étapes correspondant à la version de votre micrologiciel.

## Micrologiciel v1.9 et versions antérieures {#firmware-v19-and-earlier}

Les étapes suivantes prennent le Comet (GL-RM1) comme exemple.

1. Connectez-vous à la console du Comet et accédez à **Settings** -> **Network**. Cliquez sur l’adresse IP ou sur l’icône de flèche vers la droite.

    ![Paramètres réseau](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/settings-network.png){class="glboxshadow"}

2. Passez en mode **Static**. Saisissez une adresse IP dans le sous-réseau, ainsi que le masque de sous-réseau, la passerelle et les serveurs DNS du Comet, puis cliquez sur **Confirm**.

    ![Paramètres Ethernet avec adresse IP statique](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/ethernet-settings-static.png){class="glboxshadow"}

## Micrologiciel v1.10 et versions ultérieures {#firmware-v110-and-above}

Les étapes suivantes prennent le Comet Pro (GL-RM10) comme exemple.

1. Connectez-vous à la console du Comet Pro et cliquez sur l’icône **Settings** dans la barre de navigation pour ouvrir la page des paramètres.

    ![Paramètres réseau](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/setting_network.png){class="glboxshadow"}

2. Accédez à **Network**, puis cliquez sur **Static** dans les paramètres Ethernet. Saisissez une adresse IP dans le sous-réseau, ainsi que le masque de sous-réseau, la passerelle et les serveurs DNS du Comet Pro, puis cliquez sur **Confirm**.

    ![Paramètres Ethernet avec adresse IP statique](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/ethernet_settings_static.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
