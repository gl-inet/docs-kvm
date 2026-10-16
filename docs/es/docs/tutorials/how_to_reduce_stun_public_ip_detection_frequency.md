# Cómo reducir la frecuencia de detección de la IP pública mediante STUN {#how-to-reduce-stun-public-ip-detection-frequency}

El KVM utiliza solicitudes STUN para detectar su IP pública y permitir el acceso remoto. De forma predeterminada, envía estas solicitudes a intervalos regulares. Si solo accede al KVM por una red local o una VPN, puede ajustar la configuración para reducir su frecuencia.

Inicie sesión en el KVM mediante SSH o abra **Toolbox** > **Terminal** en la consola KVM. Haga una copia de seguridad del archivo de ajustes antes de editarlo:

```bash
cp -p /etc/kvmd/override.yaml /etc/kvmd/override.yaml.bak
vi /etc/kvmd/override.yaml
```

Si ya existe una copia llamada `override.yaml.bak`, elija otro nombre para conservarla. Si `override.yaml` no existe, omita el comando de copia de seguridad y créelo con el editor.

Integre el siguiente ajuste en el archivo y conserve todos los ajustes existentes:

```yaml
janus:
    check:
        retries: 10000
```

Si ya existe una sección `janus`, añada o actualice `check.retries` dentro de ella. Si `janus` ya contiene `check`, actualice su valor `retries` o añádalo allí. No duplique las claves `janus` ni `check`. Utilice espacios para la sangría YAML y guarde el archivo al terminar.

> **Nota:** esta configuración reduce considerablemente las solicitudes STUN de Janus. Sin embargo, también puede reducir la tasa de éxito de la apertura de conexiones mediante STUN desde redes externas. **Aplíquela únicamente si accede al KVM exclusivamente mediante una red local o una VPN.**

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
