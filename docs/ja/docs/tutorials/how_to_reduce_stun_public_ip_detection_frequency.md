# STUN パブリック IP の検出頻度を減らす方法 {#how-to-reduce-stun-public-ip-detection-frequency}

KVM デバイスは、STUN リクエストを使用して、リモート アクセス用のパブリック IP アドレスを検出します。デフォルトでは、デバイスは定期的に STUN 検出リクエストを送信します。ローカル ネットワークまたは VPN 経由でのみ KVM にアクセスする場合は、構成を調整して STUN リクエストの頻度を減らすことができます。

SSH 経由で KVM にログインするか、KVM コンソールで **Toolbox** > **Terminal** を開きます。編集する前に、既存のオーバーライドファイルをバックアップしてください。

```bash
cp -p /etc/kvmd/override.yaml /etc/kvmd/override.yaml.bak
vi /etc/kvmd/override.yaml
```

すでに `override.yaml.bak` がある場合は、既存のバックアップを残すために別のファイル名を指定してください。`override.yaml` が存在しない場合は、バックアップコマンドをスキップしてエディタで新規作成します。

既存のオーバーライド設定をすべて保持したまま、次の設定をファイルに組み込みます。

```yaml
janus:
    check:
        retries: 10000
```

すでに `janus` セクションがある場合は、その中の `check.retries` を追加または更新してください。`janus` 内に `check` がある場合は、その中の `retries` の値を更新するか、項目を追加します。`janus` や `check` キーを重複させないでください。YAML のインデントにはスペースを使用し、編集が終わったらファイルを保存します。

> **注意:** この構成により、Janus によって開始される STUN リクエストの数が大幅に減少します。ただし、外部ネットワーク侵入のための STUN ホールパンチの成功率も低下する可能性があります。 **これは、ローカル ネットワークまたは VPN 経由で KVM に排他的にアクセスする場合にのみ適用します。**

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
