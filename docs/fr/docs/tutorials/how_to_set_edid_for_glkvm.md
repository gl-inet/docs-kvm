# Configurer l’EDID d’un KVM GL.iNet {#how-to-set-edid-for-glinet-kvm}

## Qu’est-ce que l’EDID ? {#what-is-edid}

L’EDID (Extended Display Identification Data) est un format de données normalisé défini par la Video Electronics Standards Association (VESA). Stocké dans la mémoire non volatile de l’écran, il contient des informations essentielles comme le fabricant, la résolution maximale et la fréquence de rafraîchissement. En lisant l’EDID, un ordinateur peut adapter automatiquement les paramètres de son signal de sortie pour optimiser l’affichage.

En général, lorsqu’un ordinateur, un ordinateur portable ou une console de jeux est connecté à un écran, il lit automatiquement l’EDID pour définir des paramètres d’affichage appropriés. Cela permet d’éviter les images floues et le scintillement, et d’obtenir un affichage net et stable.

Les paramètres EDID des KVM GL.iNet visent à adapter automatiquement les paramètres optimaux de l’écran. Lorsqu’un KVM GL.iNet est connecté à l’appareil contrôlé, la lecture de l’EDID de l’écran permet d’ajuster automatiquement la sortie vidéo pour obtenir la meilleure image.

## EDID prédéfini {#preset-edid}

Dans la console du KVM GL.iNet, accédez à **Settings** -> **Video** -> **EDID**. Plusieurs réglages EDID prédéfinis sont disponibles.

![EDID prédéfini](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_preset.jpg){class="glboxshadow"}

**L’EDID par défaut des KVM GL.iNet convient à la plupart des situations et ne nécessite généralement aucune modification**.

Pour des besoins particuliers, comme la configuration de l’UEFI/BIOS ou la personnalisation de la résolution et de la fréquence de rafraîchissement, vous pouvez sélectionner une valeur prédéfinie, par exemple 1920×1280/AUO/60HZ.

## EDID personnalisé {#custom-edid}

Si vous ne trouvez pas de code EDID adapté, consultez [ce lien](https://github.com/linuxhw/EDID){target="_blank"} ou suivez les étapes ci-dessous pour personnaliser la configuration.

!!! tip "Conseil"

    Trouver un EDID correspondant exactement à la résolution et à la fréquence de rafraîchissement souhaitées peut être difficile. Vous pouvez utiliser des outils d’édition tels que **RTDtool** ou **EEditZ** pour adapter un EDID existant à vos besoins.

1. Trouvez un EDID adapté [ici](https://github.com/linuxhw/EDID){target="_blank"} et copiez-le.

2. Connectez-vous à la console du KVM GL.iNet et accédez à **Settings** -> **EDID**. Passez en mode **Customize**, collez les paramètres dans le champ de saisie, puis cliquez sur **Set Custom** pour les appliquer.

    ![Personnalisation de l’EDID](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_customize.png){class="glboxshadow"}

!!! note "Remarque"

    1. La résolution ne doit pas dépasser 2560×1440@60Hz. Par exemple, 2560×1600@60Hz n’est pas pris en charge.
    2. La fréquence de rafraîchissement maximale prise en charge est de 60Hz. Pour les résolutions supérieures à 1920x1080, une cadence de 60FPS ou moins est recommandée.
    3. Évitez d’inclure des résolutions entrelacées, qui provoquent un affichage anormal.
    4. Le nombre de blocs de code EDID saisis ne doit pas dépasser deux.
    5. La prise en charge audio de base est nécessaire. Sinon, la carte son peut ne pas être sélectionnable sur l’appareil contrôlé, entraînant une absence de son.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
