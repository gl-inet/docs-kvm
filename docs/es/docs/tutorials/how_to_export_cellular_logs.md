# Cómo exportar los registros de la conexión móvil {#how-to-export-cellular-logs}

Este tutorial explica cómo exportar los registros de la conexión móvil del KVM para solucionar problemas.

En este ejemplo se utiliza Comet 5G (GL-RM10RC).

1. Inicie sesión en la consola KVM, vaya a **Virtual Media** y compruebe que la función esté activada.

2. Vaya a **Toolbox** -> **Terminal** y haga clic en **Access** para abrir el terminal del KVM.

    ![Acceder al terminal](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/access_terminal.png){class="glboxshadow"}

3. En el terminal, ejecute este comando para iniciar QLog.

    ```
    QLog_1.5.22 -s /userdata/media/ -f /etc/HN_default.cfg & ubus call modem at '{"AT":"AT+QCFG=\"DBGCTL\",0"}'
    ```

    ![Iniciar QLog](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog1.jpg){class="glboxshadow"}

    Se mostrará la inicialización de QLog y, después, las estadísticas en tiempo real, como el volumen de datos recibidos y el tiempo transcurrido.

    ![Estadísticas de QLog](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog2.jpg){class="glboxshadow"}

4. Pulse Intro y ejecute los siguientes comandos en orden para reiniciar el módem y capturar los registros completos del arranque.

    ```
    ubus call modem at '{"AT":"AT+CFUN=0"}'
    ```

    ```
    ubus call modem at '{"AT":"AT+CFUN=1"}'
    ```

    ![Reiniciar el módem](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog3.png){class="glboxshadow"}

5. Espere entre 3 y 5 minutos para recopilar suficientes datos. Después ejecute este comando para detener QLog.

    ```
    ps | grep QLog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Detener QLog](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog4.png){class="glboxshadow"}

6. Exporte los registros.

    Los registros del módem móvil se guardan en **/userdata/media/**, en archivos con el sufijo `xxx.qmdl`.

    Inicie sesión en la consola KVM, vaya a **Virtual Media** y busque los archivos correspondientes con el sufijo `xxx.qmdl`. Descárguelos y compártalos con el soporte técnico de GL.iNet.

    ![Descargar los registros](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog5.png){class="glboxshadow"}

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
