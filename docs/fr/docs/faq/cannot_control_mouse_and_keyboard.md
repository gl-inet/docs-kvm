# Que faire si je ne peux pas contrôler la souris et le clavier ? {#what-should-i-do-if-i-cannot-control-the-mouse-and-keyboard}

Si vous ne pouvez pas contrôler la souris et le clavier de l’appareil contrôlé via le KVM alors que tous les câbles sont correctement branchés, essayez les solutions suivantes.

1. Vérifiez les branchements.

    Prenons le Comet (GL-RM1) comme exemple. Il possède deux ports USB Type-C :

    - Celui sur le côté porte la mention « 5V 2A » et sert à l’alimentation (connexion à un adaptateur secteur).
    - Celui à l’arrière porte les symboles de souris et de clavier ; il se connecte au port USB de l’appareil contrôlé pour recevoir les signaux du clavier et de la souris.

    Si ces branchements sont inversés, le KVM ne démarre pas et la souris et le clavier ne répondent pas.

    Vérifiez que les deux ports Type-C sont correctement branchés.

    ![Ports du GL-RM1](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/gl-rm1-ports.png){class="glboxshadow gl-80-desktop"}

2. Vérifiez le câble USB.

    Utilisez le câble USB fourni. Assurez-vous qu’il relie le port USB de l’appareil contrôlé à celui du KVM et qu’il permet le transfert de données.

    Seuls les câbles permettant le transfert de données autorisent le contrôle du clavier et de la souris de l’appareil distant.

    Rebranchez le câble USB et redémarrez l’appareil contrôlé.

3. Passez la souris en mode relatif.

    Connectez-vous au KVM, accédez à Settings -> Mouse Mode, sélectionnez Relative et vérifiez si le problème est résolu.

    ![Mode de souris](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/mouse_mode.jpg){class="glboxshadow"}

4. Désactivez Virtual Media.

    Connectez-vous au KVM, accédez à Virtual Media, cliquez sur l’icône à trois points et désactivez cette fonction.

    ![Désactivation des supports virtuels](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/disable_virtual_media.png){class="glboxshadow" width="422"}

    Lorsque Virtual Media est activé, le KVM peut émuler un support de stockage USB connecté à l’appareil contrôlé. Certains appareils désactivent toutefois toutes les entrées USB lorsqu’ils détectent un support de stockage inconnu, ce qui empêche la souris et le clavier de répondre.

5. Modifiez l’identité du périphérique.

    Connectez-vous au KVM, accédez à Settings -> System -> Device Identity et modifiez l’identité sous laquelle l’appareil contrôlé reconnaît le KVM.

    ![Modification de l’identité de l’appareil](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/change_device_identity.png){class="glboxshadow"}

6. Mettez à jour le micrologiciel du KVM vers la dernière version. [Centre de téléchargement des micrologiciels KVM](https://dl.gl-inet.com/kvm){target="_blank"}

7. Vérifiez dans le Gestionnaire de périphériques de l’ordinateur contrôlé si des pilotes fonctionnent mal.

8. Vérifiez si un logiciel de sécurité informatique bloque l’appareil contrôlé.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
