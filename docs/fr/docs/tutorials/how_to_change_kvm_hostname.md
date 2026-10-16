# Modifier le nom d’hôte du KVM {#how-to-change-kvm-hostname}

Le nom d’hôte par défaut des KVM GL.iNet est **glkvm**. Vous pouvez donc y accéder localement via le domaine `glkvm.local` lorsque vous êtes connecté au même réseau.

Ce tutoriel présente deux méthodes pour modifier le nom d’hôte : depuis la console du KVM ou à l’aide de commandes dans le terminal.

## Méthode 1. Console du KVM {#method-1-kvm-console}

> **Remarque :** Cette fonction est disponible à partir de la version 1.7.0 du micrologiciel.

### Micrologiciel v1.10 et versions ultérieures {#firmware-v110-and-above}

1. Connectez-vous à votre KVM et cliquez sur l’icône **Settings** dans la barre de navigation pour ouvrir la page des paramètres.

    ![Paramètres réseau](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings-network.png){class="glboxshadow"}

2. Accédez à **Network**, saisissez le nom d’hôte souhaité ; la modification prend effet.

    ![Modification du nom d’hôte](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify-hostname.png){class="glboxshadow"}

### Micrologiciel v1.9 et versions antérieures {#firmware-v19-and-earlier}

1. Connectez-vous à votre KVM et accédez à **Settings** -> **Network**. Cliquez sur le nom d’hôte ou sur l’icône de flèche vers la droite.

    ![Paramètres réseau](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings_network.png){class="glboxshadow"}

2. Personnalisez le nom d’hôte et cliquez sur **Apply**.

    ![Modification du nom d’hôte](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify_hostname.png){class="glboxshadow"}

## Méthode 2. Commandes dans le terminal {#method-2-terminal-commands}

1. Connectez-vous à votre KVM et accédez à **Toolbox** -> **Terminal**. Cliquez sur **Access**.

    ![Accès au terminal](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_terminal.png){class="glboxshadow"}

2. Dans le terminal, saisissez la commande suivante et appuyez sur Entrée (remplacez « example » par le nom d’hôte souhaité). Votre KVM redémarre alors.

    `echo example > /etc/hostname && reboot`

    ![Saisie de la commande](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/input_command.png){class="glboxshadow"}

3. Attendez le redémarrage. Vous pourrez ensuite accéder à votre KVM avec le nouveau nom d’hôte.

    ![Accès via le nouveau nom d’hôte](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_new_hostname.png){class="glboxshadow"}

    Si vous avez oublié le nom d’hôte ou souhaitez vérifier que la modification a pris effet, saisissez la commande suivante dans le terminal pour afficher le nom d’hôte actuel.

    `cat /etc/hostname`

    ![Vérification du nom d’hôte](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/verify_hostname.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
