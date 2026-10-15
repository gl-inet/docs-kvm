(function () {
    const host = window.location.hostname;
    const isLocalPreview = window.location.protocol === 'file:' ||
        host === 'localhost' ||
        host === '127.0.0.1' ||
        host === '0.0.0.0' ||
        host === '::1' ||
        host === '[::1]';

    if (isLocalPreview) {
        return;
    }

    CookieConsent.run({
    guiOptions: {
        consentModal: {
            layout: "box",
            position: "bottom left",
            equalWeightButtons: true,
            flipButtons: false
        },
        preferencesModal: {
            layout: "box",
            position: "right",
            equalWeightButtons: true,
            flipButtons: false
        }
    },

    categories: {
        necessary: {
            enabled: true,  // this category is enabled by default
            readOnly: true  // this category cannot be disabled
        },
        analytics: {
            services: {}
        },
        chat: {},
        marketing: {}
    },
    cookie: { domain: '.gl-inet.com' },
    language: {
        default: 'es',
        translations: {
            es: {
                consentModal: {
                    title: 'Utilizamos cookies',
                    description: 'Este sitio utiliza cookies esenciales para funcionar correctamente y cookies de seguimiento para comprender cómo interactúa con él. Estas últimas solo se establecerán con su consentimiento. <button type="button" data-cc="c-settings" class="cc-link">Elegir mis preferencias</button>',
                    acceptAllBtn: 'Aceptar todas',
                    acceptNecessaryBtn: 'Rechazar todas',
                    showPreferencesBtn: 'Gestionar preferencias individuales'
                },
                preferencesModal: {
                    title: 'Preferencias de cookies',
                    acceptAllBtn: 'Aceptar todas',
                    acceptNecessaryBtn: 'Rechazar todas',
                    savePreferencesBtn: 'Aceptar la selección actual',
                    closeIconLabel: 'Cerrar',
                    sections: [
                        {
                            title: 'Uso de cookies 📢',
                            description: 'Utilizamos cookies para garantizar las funciones básicas del sitio web y mejorar su experiencia en línea. Puede aceptar o rechazar cada categoría cuando lo desee. Para obtener más información sobre las cookies y otros datos sensibles, consulte nuestra <a href="/privacy-policy/" class="cc-link">política de privacidad</a> completa.'
                        },
                        {
                            title: 'Cookies estrictamente necesarias',
                            description: 'Estas cookies son necesarias para que el sitio web funcione y no se pueden desactivar en nuestros sistemas. Normalmente solo se establecen en respuesta a acciones con las que solicita un servicio, como la redirección a la tienda en línea según la ubicación, la configuración de sus preferencias de privacidad, el inicio de sesión o el envío de formularios. Puede configurar su navegador para bloquear estas cookies o avisarle de su uso, pero algunas partes del sitio dejarán de funcionar. Estas cookies no almacenan información que permita identificarle personalmente.',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'Rendimiento y análisis',
                            description: 'Estas cookies nos permiten contar las visitas y sus fuentes de tráfico para medir y mejorar el rendimiento del sitio. Nos ayudan a saber qué páginas reciben más o menos visitas y cómo navegan los visitantes por el sitio. Toda la información que recopilan se agrega y, por tanto, es anónima. Si no permite estas cookies, no sabremos cuándo ha visitado nuestro sitio y no podremos supervisar su rendimiento.',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'Cookies de chat',
                            description: 'Estas cookies nos permiten ofrecerle una experiencia fluida de atención al cliente mediante el chat de Freshchat y proporcionarle soporte técnico en nuestro sitio.',
                            linkedCategory: 'chat'
                        },
                        {
                            title: 'Cookies de publicidad y segmentación',
                            description: 'Nuestros socios publicitarios pueden establecer estas cookies a través de nuestro sitio. Estas empresas pueden utilizarlas para crear un perfil de sus intereses y mostrarle anuncios relevantes en otros sitios. No almacenan información personal directamente, sino que identifican de forma única su navegador y el dispositivo con el que accede a Internet. Si no permite estas cookies, verá publicidad menos adaptada a sus intereses.',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: 'Más información',
                            description: 'Si tiene alguna pregunta sobre nuestra política de cookies y sus opciones, <a class="cc-link" href="/contacts/">contacte con nosotros</a>.',
                        }
                    ]
                }
            }
        }
    },

    onConsent: ({ cookie }) => {
        gtag('consent', 'update', {
            'ad_storage': cookie.categories.includes('marketing') ? 'granted' : 'denied',
            'ad_user_data': cookie.categories.includes('marketing') ? 'granted' : 'denied',
            'ad_personalization': cookie.categories.includes('marketing') ? 'granted' : 'denied',
            'analytics_storage': cookie.categories.includes('analytics') ? 'granted' : 'denied',
            'functionality_storage': cookie.categories.includes('necessary') ? 'granted' : 'denied',
            'personalization_storage': cookie.categories.includes('necessary') ? 'granted' : 'denied',
            'security_storage': 'granted',
        });
    },


    onChange: ({ cookie, changedCategories, changedServices }) => {
        console.log(cookie, changedCategories, changedServices)
        gtag('consent', 'update', {
            'ad_storage': cookie.categories.includes('marketing') ? 'granted' : 'denied',
            'ad_user_data': cookie.categories.includes('marketing') ? 'granted' : 'denied',
            'ad_personalization': cookie.categories.includes('marketing') ? 'granted' : 'denied',
            'analytics_storage': cookie.categories.includes('analytics') ? 'granted' : 'denied',
            'functionality_storage': cookie.categories.includes('necessary') ? 'granted' : 'denied',
            'personalization_storage': cookie.categories.includes('necessary') ? 'granted' : 'denied',
            'security_storage': 'granted',
        });
    }
    });
})();
