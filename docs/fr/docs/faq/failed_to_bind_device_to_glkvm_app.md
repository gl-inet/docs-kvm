# Que faire si l’association de l’appareil à GLKVM échoue ? {#what-should-i-do-if-i-failed-to-bind-device-to-the-glkvm-app}

L’[application GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} permet d’accéder à distance à l’appareil contrôlé depuis l’appareil de contrôle. Installez l’application sur celui-ci et associez-y votre KVM GL.iNet pour accéder à l’appareil contrôlé à tout moment et de n’importe où.

L’association peut cependant échouer pour différentes raisons.

Cliquez sur le message d’erreur ci-dessous pour consulter les solutions correspondantes.

??? "Binding failed, unable to obtain basic KVM device information."

    ![Échec de l’association : erreur dans les informations de l’appareil](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_device_info_error.png){class="glboxshadow"}

    1. Vérifiez le voyant : il doit être blanc fixe et le KVM doit être connecté à Internet.
    2. Redémarrez le KVM, patientez 2 minutes, puis réessayez l’association.
    3. Si vous ajoutez l’appareil avec son numéro S/N, vérifiez sa saisie.
    4. Suivez les étapes ci-dessous pour vérifier le réseau avec la commande **Ping**.

        1. Connectez l’appareil de contrôle au même réseau que le KVM.

        2. Ouvrez un navigateur (Chrome ou Edge recommandé) sur l’appareil de contrôle et saisissez `glkvm.local` dans la barre d’adresse. Saisissez le mot de passe administrateur pour vous connecter.

            ![Accès local par nom de domaine](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. Une fois connecté, accédez à **Toolbox** -> **Terminal**, puis cliquez sur **Access** pour ouvrir le terminal.

            ![Accès au terminal](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Envoyez un ping à `google.com` pour vérifier l’état du réseau.

            ![Commande ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Si le réseau fonctionne, vous obtenez le résultat ci-dessous.

            ![Commande ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            Si le réseau est instable ou indisponible, contactez votre fournisseur d’accès à Internet ou l’assistance de votre routeur.

??? "Device network error, binding failed."

    ![Échec de l’association : erreur réseau](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_network_error.png){class="glboxshadow"}

    1. Vérifiez le voyant : il doit être blanc fixe et le KVM doit être connecté à Internet.
    2. Redémarrez le KVM, patientez 2 minutes, puis réessayez l’association.
    3. Vérifiez que le service cloud est activé.

        Le service cloud est activé par défaut. Si vous l’avez désactivé manuellement, la nouvelle association à GLKVM échoue. Accédez localement au KVM avec son nom de domaine ou son adresse IP pour réactiver le service.

    4. Suivez les étapes ci-dessous pour vérifier le réseau avec la commande **Ping**.

        1. Connectez l’appareil de contrôle au même réseau que le KVM.

        2. Ouvrez un navigateur (Chrome ou Edge recommandé) sur l’appareil de contrôle et saisissez `glkvm.local` dans la barre d’adresse. Saisissez le mot de passe administrateur pour vous connecter.

            ![Accès local par nom de domaine](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. Une fois connecté, accédez à **Toolbox** -> **Terminal**, puis cliquez sur **Access** pour ouvrir le terminal.

            ![Accès au terminal](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Envoyez un ping à `google.com` pour vérifier l’état du réseau.

            ![Commande ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Si le réseau fonctionne, vous obtenez le résultat ci-dessous.

            ![Commande ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            Si le réseau est instable ou indisponible, contactez votre fournisseur d’accès à Internet ou l’assistance de votre routeur.

??? "Binding failed, KVM is already bound by others."

    ![Échec de l’association : appareil déjà associé à un autre compte](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_bound_by_others.png){class="glboxshadow"}

    Le KVM est déjà associé à un autre compte.

    1. Vérifiez si vous l’avez associé à une autre adresse e-mail. Essayez vos autres comptes, le cas échéant.

    2. Si vous ajoutez l’appareil avec son numéro S/N, vérifiez sa saisie.

??? "Incorrect Dynamic Binding Code. You have 4 attempts remaining."

    ![Code d’association incorrect](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_binding_code.png){class="glboxshadow"}

    Le code d’association saisi est incorrect ou expiré.

    1. Connectez-vous localement à la console d’administration du KVM, accédez à **Cloud Service** en haut à droite et cliquez sur **Bind with Code** pour obtenir un code dynamique.

    2. Sur le GL-RM10 (Comet Pro), vous pouvez également obtenir le code sur l’écran tactile. Faites défiler jusqu’à **Cloud Service**, puis cliquez sur **Generate Binding Code**. Saisissez le code affiché dans GLKVM pour terminer l’association.

        ![Génération du code d’association](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_code_screen.png){class="glboxshadow"}

    3. Si le code expire, cliquez sur **Regenerate** pour en obtenir un nouveau.

??? "Incorrect Device ID. You have 4 attempts remaining."

    ![Identifiant d’appareil incorrect](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_device_id.png){class="glboxshadow"}

    L’identifiant Device ID saisi est incorrect.

    1. Vérifiez l’identifiant Device ID sur l’étiquette sous l’appareil.

    2. Si vous ne pouvez pas consulter l’étiquette, essayez l’association depuis un accès local.

        Connectez-vous localement à la console d’administration du KVM, accédez à **Cloud Service** en haut à droite et cliquez sur **Bind To KVM Cloud**. Vous êtes redirigé vers une page d’association contenant un jeton unique. Connectez-vous avec votre compte cloud et confirmez les informations de l’appareil pour terminer l’association.

??? "Autre"

    Vérifiez si un VPN est activé sur l’appareil de contrôle où GLKVM est installé.

    Désactivez tout VPN ou proxy, y compris AstroWarp, Tailscale et ZeroTier, puis réessayez d’associer le KVM à GLKVM.

Si le problème persiste, contactez-nous à [support@gl-inet.com](mailto:support@gl-inet.com) en indiquant le modèle de l’appareil, la version du micrologiciel et l’adresse MAC.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
