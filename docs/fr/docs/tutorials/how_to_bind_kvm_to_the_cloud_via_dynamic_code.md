# Associer un KVM au cloud avec un code dynamique {#how-to-bind-kvm-to-the-cloud-via-dynamic-code}

> Remarque : Mettez le micrologiciel de votre KVM à jour vers la version 1.7 avant d’utiliser cette fonction.

Ce tutoriel explique comment associer facilement un KVM GL.iNet au cloud à l’aide d’un code dynamique.

## Étapes d’association {#binding-steps}

1. Connectez-vous localement à votre KVM GL.iNet à l’aide de son nom de domaine ou de son adresse IP. Cliquez [ici](../faq/local_access_via_browser.md) pour en savoir plus.

2. Une fois connecté, accédez à **Cloud Service** en haut à droite, puis cliquez sur **Bind With Code**.

    ![Association par code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Un code dynamique aléatoire à 8 chiffres est généré pour associer l’appareil. Il est valable 60 secondes. Cliquez sur le code pour le copier.

    ![Association par code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Ouvrez [https://glkvm.com/](https://glkvm.com/){target="_blank"} et connectez-vous avec votre compte cloud GL.iNet.

    ![Association par code 3](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. Une fois connecté, la page ci-dessous s’affiche.

    ![Association par code 4](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    Cliquez sur **Add Device**, puis sélectionnez **Bind with Code**.

    ![Association par code 5](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. Dans la fenêtre qui s’ouvre, saisissez le code dynamique à 8 chiffres et cliquez sur **Bind**.

    ![Association par code 6](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Remarque :** Le code dynamique est valable 60 secondes. S’il expire, revenez à la console du KVM et cliquez sur **Regenerate Code** pour en obtenir un nouveau.

    ![Génération d’un nouveau code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

7. L’appareil est associé à votre compte cloud. Cliquez sur **Done**.

    ![Association par code 7](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_7.png){class="glboxshadow"}

    Le KVM apparaît dans la liste des appareils. Vous pouvez désormais y accéder à distance via le service cloud.

    ![Association par code 8](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_8.png){class="glboxshadow"}

8. Cliquez sur l’appareil auquel vous souhaitez accéder à distance. Dans la nouvelle page Web, saisissez votre mot de passe administrateur pour vous connecter.

    ![Authentification administrateur à distance](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Vous pouvez ensuite accéder à distance au KVM et à l’appareil contrôlé via le cloud.

    ![Accès à distance établi](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

## FAQ {#faq}

1. **Q : Combien de temps le code dynamique est-il valable ? Que faire s’il expire ?**

    R : Le code dynamique est valable 60 secondes. S’il expire, revenez à la console du KVM et cliquez sur **Regenerate Code** pour en obtenir un nouveau.

    ![Génération d’un nouveau code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

2. **Q : Que faire si le code dynamique ne peut pas être généré ?**

    R : Cela peut être dû à une connexion réseau instable ou à la configuration du DNS en amont.

    - Vérifiez que le réseau est stable, ou essayez un autre réseau.

    - Modifiez les paramètres DNS en amont et générez un nouveau code.

    Si le problème persiste, contactez notre assistance à l’adresse [support@gl-inet.com](mailto:support@gl-inet.com).

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
