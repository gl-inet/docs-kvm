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
        default: 'sv',
        translations: {
            sv: {
                consentModal: {
                    title: 'Vi använder cookies',
                    description: 'Hej! Den här webbplatsen använder nödvändiga cookies för att fungera korrekt och spårningscookies för att förstå hur du använder den. Spårningscookies sätts bara efter ditt samtycke. <button type="button" data-cc="c-settings" class="cc-link">Låt mig välja</button>',
                    acceptAllBtn: 'Acceptera alla',
                    acceptNecessaryBtn: 'Avvisa alla',
                    showPreferencesBtn: 'Hantera inställningar'
                },
                preferencesModal: {
                    title: 'Cookieinställningar',
                    acceptAllBtn: 'Acceptera alla',
                    acceptNecessaryBtn: 'Avvisa alla',
                    savePreferencesBtn: 'Spara aktuellt val',
                    closeIconLabel: 'Stäng',
                    sections: [
                        {
                            title: 'Användning av cookies 📢',
                            description: 'Vi använder cookies för att säkerställa webbplatsens grundläggande funktioner och förbättra din upplevelse online. Du kan när som helst välja att tillåta eller neka varje kategori. Mer information om cookies och andra känsliga uppgifter finns i den fullständiga <a href="/privacy-policy/" class="cc-link">integritetspolicyn</a>.'
                        },
                        {
                            title: 'Strikt nödvändiga cookies',
                            description: 'Dessa cookies krävs för att webbplatsen ska fungera och kan inte stängas av i våra system. De sätts vanligtvis bara som svar på dina åtgärder som motsvarar en begäran om tjänster, till exempel omdirigering till webbutiken för din plats, inställning av dina integritetsinställningar, inloggning eller ifyllning av formulär. Du kan ställa in webbläsaren så att den blockerar eller varnar för dessa cookies, men då fungerar inte vissa delar av webbplatsen. Dessa cookies lagrar ingen personligt identifierbar information.',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'Prestanda och analys',
                            description: 'Dessa cookies gör att vi kan räkna besök och trafikkällor så att vi kan mäta och förbättra webbplatsens prestanda. De hjälper oss att se vilka sidor som är mest och minst populära och hur besökare rör sig på webbplatsen. All information som dessa cookies samlar in är sammanställd och därmed anonym. Om du inte tillåter dessa cookies vet vi inte när du har besökt webbplatsen och kan inte övervaka dess prestanda.',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'Chattcookies',
                            description: 'Dessa cookies gör att vi kan erbjuda smidig kundservice via Freshchat-chatten och sömlös teknisk support på webbplatsen.',
                            linkedCategory: 'chat'
                        },
                        {
                            title: 'Cookies för annonsering och målinriktning',
                            description: 'Dessa cookies kan sättas via vår webbplats av våra annonspartner. Företagen kan använda dem för att skapa en profil över dina intressen och visa relevanta annonser på andra webbplatser. De lagrar inte personuppgifter direkt, utan bygger på unik identifiering av din webbläsare och internetanslutna enhet. Om du inte tillåter dessa cookies får du mindre målinriktad annonsering.',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: 'Mer information',
                            description: 'Om du har frågor om vår cookiepolicy och dina val är du välkommen att <a class="cc-link" href="/contacts/">kontakta oss</a>.',
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
