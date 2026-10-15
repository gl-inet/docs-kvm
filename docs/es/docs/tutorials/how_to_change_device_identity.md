# Cómo cambiar la identidad del dispositivo KVM {#how-to-change-kvm-device-identity}

## Qué es la identidad del dispositivo KVM {#what-is-kvm-device-identity}

La identidad del KVM GL.iNet es el identificador que permite al dispositivo conectado reconocerlo y distinguirlo durante la comunicación.

Normalmente, el KVM dispone de un puerto Type-C como el siguiente. Se conecta al puerto USB del dispositivo controlado para emular periféricos, como teclado, ratón, unidad USB y micrófono, además de una unidad de CD-ROM.

![Puerto Type-C del GL-RM1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/gl-rm1-type-c.png){class="glboxshadow gl-60-desktop"}

Cuando hace clic, escribe en el teclado o utiliza el micrófono en el dispositivo de control, las señales se transmiten de forma remota al KVM físico. Este las reenvía al dispositivo controlado a través de su puerto Type-C.

Por ello, el KVM suele reconocerse como un dispositivo compuesto que emula varios periféricos conectados a los puertos USB del dispositivo controlado.

![Funcionamiento de la identidad del dispositivo](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/principle.png){class="glboxshadow"}

!!! Note "Nota"

    Si el método de entrada o la distribución de teclado del dispositivo de control difiere del dispositivo controlado, algunos símbolos o letras pueden ocupar posiciones distintas. Esto puede provocar que el dispositivo controlado muestre caracteres diferentes de los introducidos. Consulte los detalles [aquí](../faq/keyboard_does_not_input_output_as_expected.md).

## Por qué cambiar la identidad del dispositivo {#why-change-device-identity}

El KVM GL.iNet emula varios dispositivos de interacción. Al conectarlo, el dispositivo controlado lo reconoce como un conjunto que incluye un monitor, dispositivos USB como ratón y teclado, y una unidad USB.

La identidad predeterminada es **GLKVM**, por lo que aparece como GLKVM o Glinet Composite Device en los ajustes del sistema del dispositivo controlado. Esto normalmente no supone un inconveniente, ya que solo el propio usuario ve estos ajustes.

![Identidad predeterminada del dispositivo](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_default.png){class="glboxshadow"}
<small>(Ajustes de Bluetooth & devices)</small>

![Ajustes del altavoz](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/speaker.png){class="glboxshadow"}
<small>(Ajustes del altavoz)</small>

Sin embargo, puede necesitar cambiar la identidad del KVM en los siguientes casos.

??? "Caso 1: evitar alertas del software de supervisión de un equipo de trabajo"

    Si el dispositivo controlado es un equipo de trabajo, puede tener software de supervisión integrado o instalado. Estas herramientas pueden considerar el acceso remoto mediante KVM una actividad anómala, generar alertas e incluso notificarlas a los sistemas de TI.

    Cambiar la identidad del KVM puede ayudar a evitar estas notificaciones innecesarias y mantener el funcionamiento normal del control remoto.

??? "Caso 2: ocultar el uso remoto del KVM al compartir pantalla en reuniones"

    En reuniones que requieren compartir pantalla, los ajustes del sistema del dispositivo controlado, como Bluetooth & devices, pueden mostrar la identidad predeterminada del KVM. Esto puede revelar a los participantes que utiliza un KVM para acceder de forma remota, algo que algunos usuarios prefieren evitar.

    Al cambiar la identidad, el KVM permanece oculto en las pantallas compartidas.

    ![Pantalla compartida](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/screen_sharing.png){class="glboxshadow"}
    <small>(Pantalla compartida)</small>

??? "Caso 3: resolver la falta de respuesta del ratón o el teclado"

    Si no puede controlar el ratón y el teclado del dispositivo mediante el KVM, pruebe a modificar su identidad para evitar incompatibilidades y permitir la transmisión correcta de señales entre ambos dispositivos.

## Limitaciones de la personalización de identidad {#limitations-of-device-identity-customization}

!!! Warning "El software de detección de comportamiento puede seguir identificando el KVM"

    Aunque personalice la identidad USB, la **estructura** de los dispositivos virtualizados, como teclado, ratón, micrófono o cámara, puede seguir resultando sospechosa para el software de detección de comportamiento.

    El problema fundamental es que todos estos periféricos virtuales pertenecen a **un único dispositivo USB compuesto**. Un dispositivo compuesto que solo incluya teclado y ratón es relativamente habitual; muchos receptores inalámbricos, como Logitech Unifying, presentan esa estructura. Sin embargo, un único dispositivo USB compuesto que incluya simultáneamente **teclado, ratón y micrófono** es muy poco frecuente.

    Por ello, cambiar únicamente la identidad **puede no ser suficiente** para evitar la detección por software avanzado de supervisión o análisis de comportamiento.

## Cómo cambiar la identidad del dispositivo {#how-to-change-device-identity}

### Firmware v1.10 y posteriores {#firmware-v110-and-above}

1. Inicie sesión en el KVM y vaya a **Settings**, en la esquina superior derecha. En **USB Devices**, busque **Device Identity** y personalícelo.

    ![Personalizar la identidad](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize1.png){class="glboxshadow"}

2. En la ventana emergente, haga clic en **Confirm** para reiniciar.

    ![Confirmar el reinicio](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize2.png){class="glboxshadow"}

3. Después del reinicio, verá la nueva Device Identity en la consola KVM.

    ![Identidad modificada en la consola](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize3.png){class="glboxshadow"}

4. Compruebe la identidad. En este ejemplo se utiliza Windows 11 Pro en el dispositivo controlado.

    En el dispositivo controlado, vaya a **Settings** -> **Bluetooth & devices**. Los dispositivos de entrada y audio se reconocerán con los nombres que haya configurado.

    ![Comprobar la identidad en Windows](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize4.png){class="glboxshadow"}

### Firmware v1.9 y anteriores {#firmware-v19-and-earlier}

1. Inicie sesión en el KVM y vaya a **Settings** -> **System** -> **Device Identity**. Seleccione una identidad predefinida en el desplegable.

    ![Seleccionar una identidad](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize1.jpg){class="glboxshadow"}

    También puede hacer clic en **Customize** e introducir los parámetros deseados en la ventana emergente.

    ![Personalizar parámetros de identidad](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize2.jpg){class="glboxshadow"}

2. En la ventana emergente, haga clic en **Confirm** para reiniciar.

    ![Confirmar el reinicio](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize3.png){class="glboxshadow"}

3. Después del reinicio, verá la nueva Device Identity en la consola KVM.

    ![Identidad modificada en la consola](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize4.jpg){class="glboxshadow"}

4. Compruebe la identidad. En este ejemplo se utiliza Windows 10 Pro en el dispositivo controlado.

    En el dispositivo controlado, vaya a **Settings** -> **Bluetooth & devices**. Los dispositivos de entrada y audio se reconocerán con los nombres que haya configurado.

    ![Comprobar la identidad en Windows](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_modified.png){class="glboxshadow"}

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
