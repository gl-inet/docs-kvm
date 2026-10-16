# Cómo comprobar si el puerto USB-C de su dispositivo admite DP Alt Mode {#how-to-check-if-your-devices-usb-c-port-supports-dp-alt-mode}

## Qué es DP Alt Mode {#what-is-dp-alt-mode}

DP Alt Mode, o DisplayPort Alternate Mode, es una función de determinados puertos USB-C que permite transmitir vídeo de alta calidad, además de los datos y la alimentación habituales.

Permite que un único cable USB-C transmita vídeo desde un teléfono, tableta o portátil directamente a un monitor, televisor o proyector, sin adaptadores especiales ni bases de conexión. Sin DP Alt Mode, el puerto solo transfiere datos y suministra alimentación; no puede enviar vídeo a una pantalla externa.

## Por qué es importante {#why-it-matters}

DP Alt Mode es necesario para **Comet Q**, que depende de esta función para recibir vídeo del dispositivo. El dispositivo controlado debe admitir salida de vídeo nativa por su puerto USB-C. Tenga en cuenta que un adaptador DisplayLink puede no aportar esta capacidad para una conexión directa con Comet Q.

No todos los puertos USB-C ofrecen las mismas funciones. Algunos solo transmiten datos y alimentación; otros también envían vídeo. Aunque el conector sea idéntico, sus capacidades pueden ser muy diferentes. Por eso conviene comprobarlas antes de comprar un accesorio de pantalla USB-C.

## Métodos generales para comprobar DP Alt Mode {#general-methods-to-verify-dp-alt-mode}

1. **Consulte la ficha técnica**.

    Busque el modelo exacto en el sitio del fabricante. Localice términos como DisplayPort, DP Alt Mode, salida de vídeo o Thunderbolt.

2. **Busque las marcas del puerto**.

    Un logotipo DisplayPort con forma de D o el símbolo del rayo de Thunderbolt junto al puerto USB-C indica capacidad de salida de vídeo.

3. **Compruebe los ajustes del sistema**.

    Los ajustes del sistema pueden ayudar a identificar una pantalla conectada, pero no siempre permiten determinar si un puerto USB-C concreto admite DP Alt Mode nativo. Combine estas comprobaciones con las especificaciones del fabricante y una prueba de conexión directa. Consulte las instrucciones de cada plataforma.

    - [Cómo comprobarlo en Windows](#how-to-check-on-windows)
    - [Cómo comprobarlo en Mac](#how-to-check-on-mac)
    - [Cómo comprobarlo en Android](#how-to-check-on-android)
    - [Cómo comprobarlo en iPhone y iPad](#how-to-check-on-iphone-and-ipad)
    - [Consolas portátiles, tabletas y otros dispositivos](#handhelds-tablets-and-other-devices)

4. **Haga una prueba rápida**.

    Conecte el dispositivo a un monitor o televisor mediante un cable o adaptador USB-C a HDMI o DisplayPort que requiera expresamente DP Alt Mode. Si puede duplicar o extender la pantalla, la salida de vídeo nativa funciona en ese puerto. No utilice un adaptador DisplayLink para esta prueba.

---

## Cómo comprobarlo en Windows {#how-to-check-on-windows}

1. Pulse `Win + X` y abra **Device Manager**.
2. Busque entradas que mencionen *"USB4"* o *"Thunderbolt"*. Pueden ayudar a identificar el hardware, pero Device Manager por sí solo no confirma la compatibilidad de un puerto concreto con DP Alt Mode.
3. Consulte las especificaciones del puerto exacto en el manual del portátil o en su página en el sitio del fabricante. Busque *"DisplayPort over USB-C"* o *"DP Alt Mode"*.
4. Conecte Comet Q directamente, o una pantalla mediante un adaptador que requiera expresamente DP Alt Mode. Abra **Settings** > **System** > **Display** > **Multiple displays** para comprobar si se detecta la pantalla.

**Nota**:

1. **DisplayLink no demuestra la compatibilidad con DP Alt Mode.** DisplayLink transmite vídeo mediante datos USB y también funciona por USB-A. Una entrada DisplayLink en Device Manager, o una pantalla que funcione conectada a una base DisplayLink, no demuestra que exista salida de vídeo USB-C nativa. Consulte [Synaptics: USB-C con DisplayLink](https://www.synaptics.com/products/displaylink-graphics/usb-c){target="_blank"}.

2. Si el portátil tiene varios puertos USB-C, es posible que solo algunos admitan salida de vídeo. Compruebe cada uno por separado.

## Cómo comprobarlo en Mac {#how-to-check-on-mac}

1. Haga clic en **Apple menu** > **About This Mac** > **More Info**.
2. Desplácese hacia abajo y haga clic en **System Report**.
3. En **Hardware**, seleccione **Thunderbolt / USB4** o **USB**.
4. Los puertos USB-C que aparecen en Thunderbolt / USB4 admiten DisplayPort Alt Mode de forma predeterminada.

**Consejo**: todos los Mac modernos con puertos USB-C o Thunderbolt admiten DisplayPort Alt Mode sin configuración adicional.

!!! note "Modelos compatibles"

    - MacBook Neo (A18 Pro)
    - MacBook Air
        - MacBook Air 13-in. (M5)
        - MacBook Air 15-in. (M5)
        - MacBook Air 13-in. (M4)
        - MacBook Air 13-in. (M3)
        - MacBook Air 13-in. (M2)
        - MacBook Air 13-in. (M1, 2020)
        - MacBook Air 15-in. (M4)
        - MacBook Air 15-in. (M3)
        - MacBook Air 15-in. (M2, 2023)
        - MacBook Air (Intel, 2020)
    - MacBook Pro
        - MacBook Pro 14-in. (M5)
        - MacBook Pro 14-in. (M5 Pro)
        - MacBook Pro 14-in. (M5 Max)
        - MacBook Pro 16-in. (M5 Pro)
        - MacBook Pro 16-in. (M5 Max)
        - MacBook Pro 13-in. (M2, 2022)
        - MacBook Pro 13-in. (M1, 2020)
        - MacBook Pro 13-in. (Intel, dos puertos, 2020)
        - MacBook Pro 13-in. (Intel, cuatro puertos, 2020)
        - MacBook Pro 14-in. (M4 Max)
        - MacBook Pro 14-in. (M4 Pro)
        - MacBook Pro 14-in. (M4)
        - MacBook Pro 14-in. (M3)
        - MacBook Pro 14-in. (M3 Pro o M3 Max)
        - MacBook Pro 14-in. (M2 Pro o M2 Max, 2023)
        - MacBook Pro 14-in. (M1 Pro o M1 Max, 2021)
        - MacBook Pro 16-in. (M4 Max)
        - MacBook Pro 16-in. (M4 Pro)
        - MacBook Pro 16-in. (M3 Pro o M3 Max)
        - MacBook Pro 16-in. (M2 Pro o M2 Max, 2023)
        - MacBook Pro 16-in. (M1 Pro o M1 Max, 2021)
        - MacBook Pro 16-in. (Intel, 2019)
    - iMac
        - iMac (M4, dos puertos)
        - iMac (M4, cuatro puertos)
        - iMac (M3, dos puertos)
        - iMac (M3, cuatro puertos)
        - iMac 21.5-in. (Intel, 2019)
        - iMac 21.5-in. (Intel, 2017)
        - iMac 24-in. (M1, dos puertos, 2021)
        - iMac 24-in. (M1, cuatro puertos, 2021)
        - iMac27-in. (Intel,2020)
        - iMac Pro (Intel, 2017)
    - Mac mini
        - Mac mini (M4)
        - Mac mini (M4 Pro)
        - Mac mini (M2 o M2 Pro)
        - Mac mini (M1, 2020)
        - Mac mini (Intel, 2018)
    - Mac Studio
        - Mac Studio (M4 Max)
        - Mac Studio (M3 UIitra)
        - Mac Studio (M2 Max o M2 UItra)
        - Mac Studio (M1 Max o M1 UItra, 2022)
    - Mac Pro
        - Mac Pro (M2 UItra)
        - Mac Pro (Intel, 2019)

## Cómo comprobarlo en Android {#how-to-check-on-android}

1. Abra **Settings** del teléfono y busque *"display"*, *"HDMI"* o *"desktop mode"*.
2. Busque funciones como **Samsung DeX**, **Motorola Ready For**, **Huawei EasyProjection** o *"External display"*. Consulte la documentación del fabricante para confirmar que el modelo exacto admite una **conexión por cable a una pantalla USB-C**; una función de pantalla inalámbrica por sí sola no demuestra la compatibilidad con DP Alt Mode.
3. Si el teléfono es compatible, normalmente aparecerá una notificación como *"External display connected"* al conectarlo a un monitor.
4. Confirme la salida de vídeo conectando directamente Comet Q o una pantalla mediante un adaptador que requiera DP Alt Mode. Las aplicaciones de información USB por sí solas no permiten confirmar con fiabilidad la salida de vídeo nativa.

**Nota**: muchos teléfonos Android económicos no admiten DP Alt Mode aunque tengan USB-C. Confírmelo antes de comprar Comet Q.

!!! note "Ejemplos de dispositivos Samsung con salida de vídeo por cable"

    Los modelos Samsung siguientes se han contrastado con la [información de compatibilidad de DeX de Samsung](https://www.samsung.com/us/support/answer/ANS10001955/){target="_blank"}.

    - Galaxy A90 5G
    - Galaxy Book
    - Galaxy Fold
    - Galaxy Note
        - Galaxy Note 8
        - Galaxy Note 9
        - Serie Galaxy Note 10
        - Serie Galaxy Note20
    - Galaxy S
        - Galaxy Tab S7 / 7+
        - Galaxy Tab S8 / 8+ / S8 Ultra
        - Galaxy S8 y S8+
        - Galaxy S9 y S9+
        - Serie Galaxy S10
        - Serie Galaxy S20
        - Serie Galaxy S21
        - Serie Galaxy S22
        - Serie Galaxy S23
        - Serie Galaxy S24
        - Serie Galaxy S25
    - Galaxy Tab
        - Galaxy Tab S4
        - Galaxy Tab S5e
        - Galaxy Tab S6
    - Galaxy Z
        - Galaxy Z Flip7
        - Galaxy Z Flip8
        - Galaxy Z Fold2
        - Galaxy Z Fold3
        - Galaxy Z Fold4
        - Galaxy Z Fold7

## Cómo comprobarlo en iPhone y iPad {#how-to-check-on-iphone-and-ipad}

1. La serie iPhone 15 y posteriores (excepto iPhone 16e y iPhone 17e) admiten DisplayPort Alt Mode mediante su puerto USB-C. Consulte la [documentación de Apple sobre la conexión de pantallas](https://support.apple.com/en-ie/105099#displays){target="_blank"} para su modelo exacto.
2. Los iPhone 14 y anteriores utilizan Lightning y no son compatibles.
3. Todos los iPad con USB-C admiten salida de vídeo: iPad Pro, iPad Air de 4.ª generación y posteriores, iPad mini de 6.ª generación y posteriores, e iPad de 10.ª generación y posteriores.
4. Los iPad con el antiguo puerto Lightning no son compatibles.

!!! note "Ejemplos de modelos con salida de vídeo USB-C"

    Los modelos de iPhone siguientes se han contrastado con la [documentación de Apple sobre pantallas externas](https://support.apple.com/en-ie/105099#displays){target="_blank"}.

    - iPhone
        - iPhone 18 Pro
        - iPhone 18 Pro Max
        - iPhone 17 Pro
        - iPhone 17 Pro Max
        - iPhone 17
        - iPhone 16 Pro
        - iPhone 16 Pro Max
        - iPhone 16
        - iPhone 16 Plus
        - iPhone 15 Pro
        - iPhone 15 Pro Max
        - iPhone 15
        - iPhone 15 Plus
    - iPad
        - iPad (A16)
        - iPad (10.ª generación)
    - iPad mini
        - iPad mini (6.ª generación)
        - iPad mini (A17 Pro)
    - iPad Air
        - iPad Air (5.ª generación)
        - iPad Air (4.ª generación)
        - iPad Air 11-inch (M4)
        - iPad Air 11-inch (M3)
        - iPad Air 11-inch (M2)
        - iPad Air 13-inch (M4)
        - iPad Air 13‑inch (M3)
        - iPad Air 13-inch (M2)
    - iPad Pro
        - iPad Pro 11‑inch (M5)
        - iPad Pro 11‑inch (M4)
        - iPad Pro 11-inch (4.ª generación)
        - iPad Pro 11-inch (3.ª generación)
        - iPad Pro 12.9-inch (5.ª generación)
        - iPad Pro 12.9-inch (6.ª generación)
        - iPad Pro 13‑inch (M5)
        - iPad Pro 13‑inch (M4)

## Consolas portátiles, tabletas y otros dispositivos {#handhelds-tablets-and-other-devices}

1. **Steam Deck**, **ROG Ally** y **Lenovo Legion Go** admiten DP Alt Mode.
2. La **mayoría de las tabletas Windows** con USB-C, como Surface Pro 8 y posteriores, son compatibles.
3. Para otros dispositivos, consulte la ficha técnica oficial y busque *"DisplayPort"*, *"Alt Mode"*, *"video output"* o *"Thunderbolt"*.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
