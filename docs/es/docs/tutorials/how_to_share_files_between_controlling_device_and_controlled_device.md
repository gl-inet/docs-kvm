# Cómo compartir archivos entre los dispositivos de control y controlado {#how-to-share-files-between-controlling-and-controlled-devices}

El KVM GL.iNet emula una unidad USB de lectura y escritura para compartir y administrar archivos entre el dispositivo de control y el dispositivo controlado.

En este ejemplo se utiliza Comet (GL-RM1).

## Enviar archivos al dispositivo controlado {#send-files-to-controlled-device}

Siga estos pasos para compartir archivos desde el dispositivo de control con el dispositivo controlado.

1. En la consola, vaya a **Virtual Media**. Arrastre los archivos desde el dispositivo de control o haga clic en el cuadro para cargarlos. También puede cargarlos desde una URL.

    Una vez cargados, aparecerán de la siguiente manera.

    ![Cargar archivos](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing1.png){class="glboxshadow"}

2. Haga clic en **Mount To Remote** -> **File Sharing**.

    ![Compartir archivos](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing2.png){class="glboxshadow"}

3. Aparecerá una ventana en la consola con los pasos para compartir archivos.

    ![Instrucciones para compartir archivos](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing3.png){class="glboxshadow"}

4. Espere un momento. Aparecerá automáticamente en la pantalla una unidad llamada **"GLKVM"**. Comet estará emulando una unidad USB de lectura y escritura en el dispositivo controlado, donde verá los archivos cargados anteriormente.

    Ahora puede ver, mover o eliminar los archivos de esa unidad desde el dispositivo controlado.

    ![Archivos compartidos](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing4.png){class="glboxshadow"}

    **Consejo**: si la unidad no aparece automáticamente, abra **This PC** en el dispositivo controlado.

    ![This PC](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/thispc.png){class="glboxshadow"}

    Busque la unidad **"GLKVM"**. Desde ella puede ver, mover o eliminar los archivos.

5. Para dejar de compartir, haga clic en **Virtual Media** en la barra de herramientas y después en **Stop Sharing**.

    ![Dejar de compartir](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing1.png){class="glboxshadow"}

## Obtener archivos del dispositivo controlado {#get-files-from-controlled-device}

Siga estos pasos para recibir archivos del dispositivo controlado.

1. En el dispositivo controlado, mueva o copie los archivos que desea compartir a la unidad **GLKVM**.

    En este ejemplo se ha movido un archivo del escritorio del dispositivo controlado a la unidad **GLKVM**.

    ![Copiar un archivo a la unidad](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing5.png){class="glboxshadow"}

2. Vuelva a la consola de Comet, haga clic en **Virtual Media** en la barra de herramientas y después en **Stop Sharing**.

    ![Dejar de compartir](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing2.png){class="glboxshadow"}

3. El archivo aparecerá en **Virtual Media**. Ya puede descargarlo de Comet al dispositivo de control.

    ![Archivo disponible para descargar](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing6.png){class="glboxshadow"}

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
