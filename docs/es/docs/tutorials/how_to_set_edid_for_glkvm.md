# Cómo configurar el EDID del KVM GL.iNet {#how-to-set-edid-for-glinet-kvm}

## Qué es EDID {#what-is-edid}

EDID, Extended Display Identification Data, es un formato de datos estándar definido por Video Electronics Standards Association (VESA). Se guarda en la memoria no volátil de la pantalla y contiene información como el fabricante, la resolución máxima y la frecuencia de actualización. Al leer el EDID, los equipos pueden ajustar automáticamente los parámetros de salida para que la pantalla muestre la imagen en condiciones óptimas.

Cuando un equipo de escritorio, portátil o consola se conecta a una pantalla, normalmente lee su EDID para establecer los parámetros adecuados. Así evita problemas como imagen borrosa o parpadeos y proporciona una imagen clara y estable.

Los ajustes EDID del KVM GL.iNet permiten seleccionar automáticamente los parámetros óptimos de pantalla. Al conectarse al dispositivo controlado, el KVM puede ajustar la salida de imagen leyendo el EDID de la pantalla.

## EDID predefinidos {#preset-edid}

En la consola KVM GL.iNet, vaya a **Settings** -> **Video** -> **EDID**. Encontrará varios EDID predefinidos.

![EDID predefinidos](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_preset.jpg){class="glboxshadow"}

**El EDID predeterminado del KVM GL.iNet es adecuado para la mayoría de los casos y normalmente no necesita modificarse**.

En situaciones especiales, como configurar UEFI/BIOS o personalizar la resolución o frecuencia de actualización, puede seleccionar un valor predefinido, por ejemplo 1920×1280/AUO/60HZ.

## EDID personalizado {#custom-edid}

Si no encuentra un código EDID adecuado, consulte [este enlace](https://github.com/linuxhw/EDID){target="blank"} o siga los pasos siguientes para personalizarlo.

!!! Tip "Consejo"

    Puede resultar difícil encontrar un EDID que coincida exactamente con la resolución y la frecuencia de actualización deseadas. Utilice herramientas de edición como **RTDtool** o **EEditZ** para modificar un EDID existente según sus necesidades.

1. Busque un EDID adecuado [aquí](https://github.com/linuxhw/EDID){target="blank"} y cópielo.

2. Inicie sesión en la consola KVM GL.iNet y vaya a **Settings** -> **EDID**. Cambie al modo **Customize**, pegue los parámetros en el cuadro de entrada y haga clic en **Set Custom** para aplicar los ajustes.

    ![Personalizar el EDID](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_customize.png){class="glboxshadow"}

!!! Note "Nota"

    1. La resolución no debe superar 2560×1440@60Hz. Por ejemplo, 2560×1600@60Hz no es compatible.
    2. La frecuencia de actualización máxima es de 60Hz. Para resoluciones superiores a 1920x1080, se recomienda una velocidad de 60FPS o inferior.
    3. Evite incluir resoluciones entrelazadas, ya que provocarían una visualización incorrecta.
    4. El EDID introducido no debe contener más de dos bloques de código.
    5. Es necesario admitir audio básico. De lo contrario, puede que no sea posible seleccionar la tarjeta de sonido en el dispositivo controlado y no se escuche audio.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
