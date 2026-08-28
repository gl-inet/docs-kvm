# USB TTL 経由でシリアル コンソールにアクセスする方法

シリアル デバッグに USB TTL アダプターを使用するには、次の手順に従います。

1. USB TTL アダプターを KVM デバイスの USB ポートに接続します。
2. 次のコマンドを実行して、シリアル ポート接続を開きます。

```bash
minicom -D /dev/ttyUSB0 -b 115200
```

このコマンドは、`115200` のボーレートで `/dev/ttyUSB0` へのシリアル接続を確立します。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
