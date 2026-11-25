# Comment rétablir les paramètres d’usine de votre KVM GL.iNet ? {#how-do-i-factory-reset-my-glinet-kvm}

## Méthode 1 – Utiliser le bouton physique de réinitialisation {#method-1-use-the-physical-reset-button}

Vérifiez que le KVM est sous tension et que son démarrage est terminé.

Maintenez le bouton physique RESET enfoncé pendant **8 à 10 secondes**, puis relâchez-le. Si votre KVM possède un orifice de réinitialisation, utilisez une pointe pour maintenir le bouton à l’intérieur de l’orifice enfoncé pendant 8 secondes, puis relâchez-le. Sur le Comet X (GL-RM4PE), utilisez le bouton de commutation en façade.

Attendez que le KVM redémarre automatiquement. Ne coupez pas l’alimentation pendant la réinitialisation.

Ne maintenez pas le bouton de réinitialisation enfoncé lors de la mise sous tension du KVM. N’utilisez ni le bouton de réinitialisation de l’ordinateur connecté ni celui de la carte ATX.

## Méthode 2 – Utiliser l’interface web locale {#method-2-use-the-local-web-interface}

Connectez votre ordinateur et le KVM au même réseau local. Ouvrez l’adresse IP locale du KVM dans un navigateur et connectez-vous. Consultez la page [Accéder au KVM localement depuis un navigateur](local_access_via_browser.md).

Si votre KVM utilise le micrologiciel v1.10 ou une version ultérieure, ouvrez **Settings** en haut à droite et accédez à **System** -> **Reset Device**. Cliquez sur **Reset**, confirmez, puis attendez que le KVM redémarre automatiquement. Ne coupez pas l’alimentation pendant la réinitialisation.

![reset 1](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset1.png){class="glboxshadow"}

Si votre KVM utilise le micrologiciel v1.9 ou une version antérieure, ouvrez **Settings** en haut à gauche et accédez à **System** -> **Reset KVM**. Cliquez sur **Reset**, confirmez, puis attendez que le KVM redémarre automatiquement. Ne coupez pas l’alimentation pendant la réinitialisation.

![reset 2](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset2.png){class="glboxshadow"}

## Après la réinitialisation {#after-the-reset}

Le rétablissement des paramètres d’usine efface les paramètres personnalisés du KVM. Son adresse IP locale peut changer après le redémarrage. Ouvrez de nouveau l’interface web locale, suivez les instructions de configuration initiale pour définir un mot de passe administrateur, puis configurez de nouveau manuellement les paramètres dont vous avez besoin.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
