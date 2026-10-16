# Que faire si le BIOS ne s’affiche pas sur l’écran distant ? {#what-should-i-do-if-the-remote-screen-does-not-show-the-bios-interface}

Si l’interface BIOS ne s’affiche pas lors de l’accès à l’appareil contrôlé via le KVM (par exemple No HDMI Signal), cela peut venir du fait que le BIOS n’envoie généralement son image qu’à l’écran principal. Voici quelques suggestions.

## Ordinateur portable {#laptop}

Sur un ordinateur portable, l’écran intégré sert d’écran principal ; le KVM externe ne peut donc pas afficher l’interface BIOS.

## Ordinateur de bureau {#desktop}

Sur un ordinateur de bureau, connectez l’écran principal au port DisplayPort si disponible. La plupart des cartes graphiques et cartes mères donnent en effet la priorité à la sortie DP sur la sortie HDMI au démarrage.

Suivez les méthodes ci-dessous pour rendre le BIOS visible via le KVM.

- Essayez différents ports d’affichage. Connectez le KVM GL.iNet au port défini comme sortie vidéo principale de l’ordinateur.

- Utilisez un répartiteur HDMI 1 vers 2 (non fourni) pour dupliquer le signal de l’écran principal vers le KVM.

> **Remarque :** Ce problème peut également se produire lorsque l’appareil démarre sous **Windows PE**, car les signaux du BIOS ne sont envoyés qu’à l’écran principal et ne s’affichent pas sur l’écran distant du KVM.

> Effectuez un test avec un écran supplémentaire. Si l’écran secondaire ne reçoit toujours aucun signal, le KVM ne pourra pas capturer le BIOS. Vous pouvez intégrer ou installer manuellement des pilotes d’affichage dans WinPE pour résoudre ce problème.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
