# Firmware v1.10 {#firmware-v110}

Esta versión incorpora WebRTC nativo, supervisión de datos en tiempo real, gestión centralizada de dispositivos USB y un nuevo centro de configuración. También mejora el rendimiento de arranque, la seguridad y la estabilidad del micrófono para ofrecer una experiencia de KVM remoto más fluida y fiable.

Obtenga el firmware más reciente en el [centro de descargas de firmware](https://dl.gl-inet.com/kvm){target="_blank"}

## Modo WebRTC nativo {#webrtc-native-mode}

Este firmware incorpora el modo **WebRTC (Native) Mode**, que utiliza la biblioteca WebRTC de Google para mejorar el rendimiento de la transmisión y ofrecer un control remoto más fluido en tiempo real.

![Modo WebRTC](https://static.gl-inet.com/docs/kvm/features_update/1.10/webrtc_native_mode.png){class="glboxshadow" width=400}

## Estadísticas de conexión {#connection-stats}

**Connection Stats** muestra información de conexión en tiempo real y gráficos de tendencias, incluidos la latencia de red, la fluctuación de latencia (jitter), la tasa de pérdida de paquetes, la tasa de bits, la frecuencia de fotogramas y el retardo de reproducción.

Haga clic en el icono de lista para ver los datos de conexión en tiempo real y el estado del dispositivo.

![Estadísticas de conexión: datos en tiempo real](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_1.png){class="glboxshadow"}

Haga clic en el icono de gráfico para ver las tendencias de latencia de red, fluctuación de latencia y tasa de pérdida de paquetes.

![Estadísticas de conexión: gráficos de tendencias](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_2.png){class="glboxshadow"}

## Centro de configuración {#settings-center}

Esta versión añade un nuevo **Settings Center** que centraliza la configuración de dispositivos USB, preferencias, red, seguridad, nube y sistema. Las opciones existentes, como la configuración del nombre de host, la gestión de la nube y las actualizaciones del firmware, ahora son más fáciles de encontrar en un único lugar.

### Dispositivos USB {#usb-devices}

**USB Devices** permite gestionar de forma centralizada los dispositivos USB emulados. Desde esta página puede activar o desactivar periféricos virtuales para mejorar la compatibilidad con el equipo controlado.

![Dispositivos USB](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_usb_devices.png){class="glboxshadow"}

- **USB Emulated Devices**: active o desactive los dispositivos USB emulados, incluidos el ratón, el teclado, el micrófono, la cámara y los medios virtuales. Algunos dispositivos no pueden activarse al mismo tiempo. La disponibilidad se actualiza automáticamente.

- **Device Identity**: personalice o modifique la identidad con la que el dispositivo controlado reconoce al KVM. El EDID y la identificación del dispositivo se mantienen sincronizados. Al cambiar uno de ellos, el otro se actualiza automáticamente para garantizar el reconocimiento correcto del dispositivo.

### Preferencias {#preferences}

**Preferences** permite gestionar las preferencias de distribución, los ajustes del sistema y la pantalla del dispositivo.

![Preferencias](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_preferences.png){class="glboxshadow"}

- **Layout Preferences**: configure la barra de herramientas en el modo de pantalla completa y la barra de estado en el modo de ventana.

- **System Settings**: establezca el título de la pestaña del navegador, el idioma de la interfaz, el modo de color y la zona horaria.

- **Device Screen**: previsualice y configure la pantalla integrada del dispositivo, incluidos el modo de bloqueo de pantalla, el formato de hora, el formato de fecha y el fondo de pantalla.

    **Nota**: Esta función solo está disponible en los modelos con pantalla integrada.

### Red {#network}

Puede consultar y gestionar los ajustes de red del dispositivo, incluidos el nombre de host, la conexión Ethernet y la información de la red inalámbrica.

![Red](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_network.png){class="glboxshadow"}

- **Hostname**: cambie el nombre de host del dispositivo directamente desde la consola. Esta función se incorporó en el firmware v1.7.0.

- **Ethernet Settings**: consulte y configure la conexión Ethernet. Puede utilizar DHCP para obtener los ajustes de red automáticamente o seleccionar **Static** para introducir manualmente la dirección IP, la máscara de red, la puerta de enlace y los demás parámetros necesarios.

- **Wireless**: una vez que el dispositivo se conecta a una red Wi-Fi, se muestran su dirección IP, puerta de enlace y dirección MAC.

    **Nota**: La función Wireless solo está disponible en los modelos compatibles.

### Seguridad {#security}

**Security** permite cambiar la contraseña del administrador, activar la autenticación de dos factores y personalizar el certificado TLS.

![Seguridad](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_security.png){class="glboxshadow"}

- **Access Password**: gestione la contraseña del administrador o active la autenticación de dos factores (2FA) para proteger el acceso al dispositivo.

- **TLS Certificate**: utilice el certificado predeterminado o cargue un certificado personalizado y su clave privada para el acceso mediante el navegador.

### Nube {#cloud}

Los dispositivos pueden vincularse a servicios en la nube mediante una URL o un código para su acceso y gestión remotos. También puede descargar la aplicación móvil, gestionar la conexión o desvincular el dispositivo según sea necesario.

![Nube](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_cloud.png){class="glboxshadow"}

### Sistema {#system}

En **System** encontrará las opciones de gestión del sistema, actualización del firmware y soporte.

![Sistema](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_system.png){class="glboxshadow"}

- **System**: reinicie el dispositivo o restablezca su configuración de fábrica.

- **Upgrade**: active Beta Center para recibir actualizaciones beta del firmware o utilice **Local Upgrade** para instalar el firmware desde un archivo local.

- **Help & Support**: exporte los registros del dispositivo para solucionar problemas y acceda a las guías del usuario, las preguntas frecuentes y otros documentos de soporte.

## Otras mejoras {#other-enhancements}

- **Rendimiento de arranque**: se ha mejorado la velocidad de arranque del dispositivo.

- **Política de contraseñas**: se ha reforzado la política de contraseñas para mejorar la seguridad. Se requieren al menos 10 caracteres de dos tipos distintos como mínimo.

- **Indicador de bloqueo de mayúsculas**: se ha añadido un indicador del estado de bloqueo de mayúsculas del dispositivo controlado.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contacte con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
