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
        default: 'ja',
        translations: {
            ja: {
                consentModal: {
                    title: 'Cookie を使用しています',
                    description: 'このウェブサイトでは、正常な動作に必要な Cookie と、利用状況を把握するためのトラッキング Cookie を使用します。トラッキング Cookie は同意後にのみ設定されます。<button type="button" data-cc="c-settings" class="cc-link">設定を選択</button>',
                    acceptAllBtn: 'すべて許可',
                    acceptNecessaryBtn: 'すべて拒否',
                    showPreferencesBtn: '個別設定を管理'
                },
                preferencesModal: {
                    title: 'Cookie 設定',
                    acceptAllBtn: 'すべて許可',
                    acceptNecessaryBtn: 'すべて拒否',
                    savePreferencesBtn: '現在の選択を保存',
                    closeIconLabel: '閉じる',
                    sections: [
                        {
                            title: 'Cookie の使用について 📢',
                            description: 'ウェブサイトの基本機能を提供し、オンライン体験を向上させるために Cookie を使用しています。各カテゴリーはいつでも有効または無効にできます。Cookie およびその他の機密データについては、<a href="/privacy-policy/" class="cc-link">プライバシーポリシー</a>をご覧ください。'
                        },
                        {
                            title: '必須 Cookie',
                            description: 'これらの Cookie はウェブサイトの動作に必要なため、無効にできません。ブラウザーでブロックまたは警告するよう設定できますが、サイトの一部が正常に動作しなくなる場合があります。個人を特定できる情報は保存されません。',

                            //this field will generate a toggle linked to the 'necessary' category
                            linkedCategory: 'necessary'
                        },
                        {
                            title: 'パフォーマンスと分析',
                            description: '訪問数とトラフィック元を集計し、サイトのパフォーマンス測定と改善に使用します。収集される情報は集約され、匿名化されます。',
                            linkedCategory: 'analytics'
                        },
                        {
                            title: 'チャット Cookie',
                            description: 'これらの Cookie は、チャットを通じて円滑なカスタマーサービスと技術サポートを提供するために使用されます。',
                            linkedCategory: 'chat'
                        },
                        {
                            title: '広告およびターゲティング Cookie',
                            description: '広告パートナーが、利用者の関心に合った広告を表示するために設定する場合があります。許可しない場合、表示される広告の関連性が低くなることがあります。',
                            linkedCategory: 'marketing'
                        },
                        {
                            title: '詳細情報',
                            description: 'Cookie ポリシーや選択内容についてご不明な点がある場合は、<a class="cc-link" href="/contacts/">お問い合わせください</a>。',
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
