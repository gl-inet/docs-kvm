# Échec de l’installation de GLKVM sous Windows : « The code execution cannot proceed » {#failed-to-install-glkvm-app-on-windows-the-code-execution-cannot-proceed}

Lors de l’installation de GLKVM sous Windows, l’erreur suivante peut apparaître : « The code execution cannot proceed because VCRUNTIME140_1.dll was not found ».

![Erreur système](https://static.gl-inet.com/docs/kvm/faq/failed_to_install_glkvm_app/system_error.png){class="glboxshadow"}

Cette erreur est due à l’absence de dépendances d’exécution Visual C++. L’application nécessite certains fichiers DLL fournis par le paquet Visual C++ Redistributable.

Suivez ces étapes :

1. Téléchargez la dernière version de Visual C++ Redistributable pour Visual Studio depuis le [site officiel de Microsoft](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170){target="_blank"}.

2. Installez le paquet et redémarrez votre ordinateur.

    Désactivez temporairement l’antivirus : certains outils de sécurité peuvent bloquer les fichiers d’installation par erreur.

    ??? "Comment vérifier que les dépendances Visual C++ sont installées correctement ?"

        1. Sous Windows, accédez à Control Panel > Programs > Programs and Features.

        2. Recherchez des entrées comme « Microsoft Visual C++ 2015-2022 Redistributable » (x64/x86). Si elles sont absentes, installez-les avec le lien ci-dessus.

3. Relancez le programme d’installation de GLKVM.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
