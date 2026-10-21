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
        default: 'nl',
        translations: {
            nl: {
                consentModal: {
                    title: 'Wij gebruiken cookies',
                    description: 'Hallo, deze website gebruikt essentiële cookies om goed te functioneren en trackingcookies om te begrijpen hoe u de website gebruikt. Trackingcookies worden alleen geplaatst nadat u toestemming hebt gegeven. <button type="button" data-cc="c-settings" class="cc-link">Zelf kiezen</button>',
                    acceptAllBtn: 'Alles accepteren',
                    acceptNecessaryBtn: 'Alles weigeren',
                    showPreferencesBtn: 'Voorkeuren beheren'
                },
                preferencesModal: {
                    title: 'Cookievoorkeuren',
                    acceptAllBtn: 'Alles accepteren',
                    acceptNecessaryBtn: 'Alles weigeren',
                    savePreferencesBtn: 'Huidige selectie opslaan',
                    closeIconLabel: 'Sluiten',
                    sections: [
                        {
                            title: 'Gebruik van cookies 📢',
                            description: 'We gebruiken cookies om de basisfuncties van de website te garanderen en uw online-ervaring te verbeteren. U kunt per categorie op elk moment kiezen of u cookies toestaat of weigert. Lees voor meer informatie over cookies en andere gevoelige gegevens het volledige <a href="/privacy-policy/" class="cc-link">privacybeleid</a>.'
                        },
                        {
                            title: 'Strikt noodzakelijke cookies',
                            description: 'Deze cookies zijn nodig om de website te laten functioneren en kunnen niet worden uitgeschakeld in onze systemen. Ze worden meestal alleen geplaatst als reactie op uw acties die neerkomen op een verzoek om diensten, zoals het doorsturen naar de webwinkel voor uw locatie, het instellen van uw privacyvoorkeuren, inloggen of het invullen van formulieren. U kunt uw browser zo instellen dat deze cookies worden geblokkeerd of dat u erover wordt gewaarschuwd, maar sommige delen van de website werken dan niet. Deze cookies slaan geen persoonlijk identificeerbare informatie op.',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'Prestaties en analyse',
                            description: 'Met deze cookies kunnen we bezoeken en verkeersbronnen tellen, zodat we de prestaties van onze website kunnen meten en verbeteren. Ze helpen ons te zien welke pagina\'s het meest en het minst populair zijn en hoe bezoekers zich over de website bewegen. Alle informatie die deze cookies verzamelen, wordt samengevoegd en is daarom anoniem. Als u deze cookies niet toestaat, weten we niet wanneer u onze website hebt bezocht en kunnen we de prestaties ervan niet controleren.',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'Chatcookies',
                            description: 'Met deze cookies kunnen we u via de Freshchat-chat een soepele klantenservice en naadloze technische ondersteuning op onze website bieden.',
                            linkedCategory: 'chat'
                        },
                        {
                            title: 'Advertentie- en targetingcookies',
                            description: 'Deze cookies kunnen via onze website worden geplaatst door onze advertentiepartners. Deze bedrijven kunnen ze gebruiken om een profiel van uw interesses op te bouwen en u relevante advertenties op andere websites te tonen. Ze slaan niet rechtstreeks persoonlijke gegevens op, maar zijn gebaseerd op de unieke identificatie van uw browser en internetapparaat. Als u deze cookies niet toestaat, ziet u minder gerichte advertenties.',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: 'Meer informatie',
                            description: 'Voor vragen over ons cookiebeleid en uw keuzes kunt u <a class="cc-link" href="/contacts/">contact met ons opnemen</a>.',
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
