# Qué hacer si el teclado no introduce o muestra los caracteres esperados {#what-shoud-i-do-if-keyboard-does-not-input-or-output-as-expected}

Si los dispositivos de control y controlado utilizan **métodos de entrada o distribuciones de teclado diferentes**, los símbolos y caracteres como "!", "@" o "#" introducidos de forma local pueden no aparecer correctamente en el dispositivo remoto.

## Por qué ocurre {#why-does-it-happen}

El dispositivo controlado reconoce el KVM como un teclado. Las teclas pulsadas en el dispositivo de control se transmiten al KVM según su posición y después se asignan al dispositivo controlado.

Si el método de entrada o la distribución del teclado de ambos dispositivos no coinciden, algunos símbolos o letras tendrán posiciones diferentes y el dispositivo controlado mostrará caracteres distintos de los introducidos en el dispositivo de control.

![Comparación de teclados US y JIS](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/apple-keyboards-US-JIS.jpg){class="glboxshadow"}

## Soluciones {#solutions}

Instale en el dispositivo controlado el método de entrada o la distribución de teclado del idioma correspondiente para que la asignación de teclas coincida.

??? "Windows"

    1. Vaya a **Settings** -> **Time & Language** -> **Language** -> **Preferred Language**. Haga clic en **Add a language**.

        ![Añadir un idioma](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/add_language.png){class="glboxshadow"}

    2. Elija el idioma que desea instalar.

        ![Elegir un idioma](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/choose_language.png){class="glboxshadow"}

??? "MacOS"

    1. En el Mac, seleccione **Apple menu** > **System Settings** y haga clic en **Keyboard** en la barra lateral. Puede que necesite desplazarse hacia abajo.

    2. Vaya a **Text Input** y haga clic en **Edit**.

    3. Haga clic en **Add** y busque un idioma. Seleccione una o varias fuentes de entrada para cada idioma que desee utilizar y haga clic en **Add**.

    4. Para escribir en otro idioma, selecciónelo en el menú Input de la barra de menús.

        Puede hacer clic en **Show Keyboard Viewer** en el menú Input para ver la distribución del teclado del idioma seleccionado.

        Después de añadir una fuente de entrada, el menú Input aparece automáticamente en la barra de menús. Su idioma también se añade a la lista de idiomas preferidos de Language & Region y a la lista de idiomas de Dictation, si está disponible, en los ajustes de Keyboard.

    Referencia: [Escribir en otro idioma en el Mac: soporte de Apple](https://support.apple.com/guide/mac-help/write-in-another-language-on-mac-mchlp1406/mac){target="_blank"}

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
