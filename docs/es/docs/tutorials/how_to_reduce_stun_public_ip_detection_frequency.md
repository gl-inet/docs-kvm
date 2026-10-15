# Cómo reducir la frecuencia de detección de la IP pública mediante STUN {#how-to-reduce-stun-public-ip-detection-frequency}

El KVM utiliza solicitudes STUN para detectar su IP pública y permitir el acceso remoto. De forma predeterminada, envía estas solicitudes a intervalos regulares. Si solo accede al KVM por una red local o una VPN, puede ajustar la configuración para reducir su frecuencia.

Ejecute este comando para ampliar el intervalo de detección STUN y reducir la frecuencia de las solicitudes:

```bash
cat > /etc/kvmd/override.yaml << EOF
janus:
    check:
        retries: 10000
EOF
```

> **Nota:** esta configuración reduce considerablemente las solicitudes STUN de Janus. Sin embargo, también puede reducir la tasa de éxito de la apertura de conexiones mediante STUN desde redes externas. **Aplíquela únicamente si accede al KVM exclusivamente mediante una red local o una VPN.**

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
