# Exporter les journaux cellulaires {#how-to-export-cellular-logs}

Ce tutoriel explique comment exporter les journaux liés à la connexion cellulaire du KVM pour le dépannage.

Les étapes suivantes prennent le Comet 5G (GL-RM10RC) comme exemple.

1. Connectez-vous à la console du KVM, accédez à **Virtual Media** et assurez-vous que cette fonction est activée.

2. Accédez à **Toolbox** -> **Terminal**. Cliquez sur **Access** pour ouvrir le terminal du KVM.

    ![Accès au terminal](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/access_terminal.png){class="glboxshadow"}

3. Dans le terminal, exécutez la commande suivante pour lancer le programme QLog.

    ```
    QLog_1.5.22 -s /userdata/media/ -f /etc/HN_default.cfg & ubus call modem at '{"AT":"AT+QCFG=\"DBGCTL\",0"}'
    ```

    ![Collecte des journaux QLog 1](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog1.jpg){class="glboxshadow"}

    La page affiche les informations d’initialisation de QLog, puis les statistiques en temps réel (par exemple le volume de données reçues et le temps écoulé), comme illustré ci-dessous.

    ![Collecte des journaux QLog 2](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog2.jpg){class="glboxshadow"}

4. Appuyez sur Entrée et exécutez successivement les commandes suivantes pour redémarrer le modem afin d’enregistrer l’intégralité du processus de démarrage.

    ```
    ubus call modem at '{"AT":"AT+CFUN=0"}'
    ```

    ```
    ubus call modem at '{"AT":"AT+CFUN=1"}'
    ```

    ![Collecte des journaux QLog 3](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog3.png){class="glboxshadow"}

5. Patientez 3 à 5 minutes pour recueillir suffisamment de données, puis saisissez la commande suivante pour arrêter le processus QLog.

    ```
    ps | grep QLog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Collecte des journaux QLog 4](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog4.png){class="glboxshadow"}

6. Exportez les journaux.

    Les journaux du modem cellulaire sont enregistrés dans le répertoire **/userdata/media/**, dans des fichiers portant le suffixe `xxx.qmdl`.

    Connectez-vous à la console du KVM, accédez à **Virtual Media** et trouvez les fichiers portant le suffixe `xxx.qmdl`. Téléchargez-les et transmettez-les à l’assistance technique GL.iNet.

    ![Collecte des journaux QLog 5](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog5.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
