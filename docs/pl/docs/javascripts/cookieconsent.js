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
        default: 'pl',
        translations: {
            pl: {
                consentModal: {
                    title: 'Używamy plików cookie',
                    description: 'Witaj! Ta witryna używa niezbędnych plików cookie, aby działać prawidłowo, oraz śledzących plików cookie, aby lepiej zrozumieć sposób korzystania z niej. Te drugie zostaną zapisane dopiero po wyrażeniu zgody. <button type="button" data-cc="c-settings" class="cc-link">Chcę wybrać</button>',
                    acceptAllBtn: 'Akceptuj wszystkie',
                    acceptNecessaryBtn: 'Odrzuć wszystkie',
                    showPreferencesBtn: 'Zarządzaj preferencjami'
                },
                preferencesModal: {
                    title: 'Preferencje plików cookie',
                    acceptAllBtn: 'Akceptuj wszystkie',
                    acceptNecessaryBtn: 'Odrzuć wszystkie',
                    savePreferencesBtn: 'Zapisz wybrane ustawienia',
                    closeIconLabel: 'Zamknij',
                    sections: [
                        {
                            title: 'Korzystanie z plików cookie 📢',
                            description: 'Używamy plików cookie, aby zapewnić podstawowe funkcje witryny i usprawnić korzystanie z niej. W każdej chwili możesz włączyć lub wyłączyć poszczególne kategorie. Więcej informacji o plikach cookie i innych danych wrażliwych znajdziesz w pełnej <a href="/privacy-policy/" class="cc-link">polityce prywatności</a>.'
                        },
                        {
                            title: 'Niezbędne pliki cookie',
                            description: 'Te pliki cookie są niezbędne do działania witryny i nie można ich wyłączyć w naszych systemach. Zwykle są zapisywane w odpowiedzi na działania stanowiące prośbę o usługę, np. przekierowanie do sklepu odpowiedniego dla lokalizacji, ustawienie preferencji prywatności, logowanie lub wypełnianie formularzy. Możesz ustawić przeglądarkę tak, aby je blokowała lub o nich ostrzegała, ale niektóre części witryny przestaną wtedy działać. Te pliki cookie nie przechowują informacji umożliwiających identyfikację osoby.',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'Wydajność i analityka',
                            description: 'Te pliki cookie pozwalają liczyć wizyty i źródła ruchu, aby mierzyć i poprawiać wydajność witryny. Pomagają ustalić, które strony są najpopularniejsze, a które najmniej popularne, oraz jak odwiedzający poruszają się po witrynie. Wszystkie zbierane informacje są zagregowane, a więc anonimowe. Bez zgody na te pliki cookie nie dowiemy się o Twojej wizycie i nie będziemy mogli monitorować wydajności witryny.',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'Pliki cookie czatu',
                            description: 'Te pliki cookie umożliwiają sprawną obsługę klienta przez czat Freshchat i zapewnienie pomocy technicznej w naszej witrynie.',
                            linkedCategory: 'chat'
                        },
                        {
                            title: 'Pliki cookie reklamowe i targetujące',
                            description: 'Te pliki cookie mogą być zapisywane w naszej witrynie przez partnerów reklamowych. Mogą oni używać ich do tworzenia profilu zainteresowań i wyświetlania dopasowanych reklam w innych witrynach. Nie przechowują bezpośrednio danych osobowych, ale opierają się na unikatowej identyfikacji przeglądarki i urządzenia korzystającego z internetu. Bez zgody na te pliki cookie reklamy będą mniej dopasowane.',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: 'Więcej informacji',
                            description: 'W razie pytań dotyczących naszej polityki plików cookie i dostępnych wyborów <a class="cc-link" href="/contacts/">skontaktuj się z nami</a>.',
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
