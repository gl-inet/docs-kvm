# USB OTG 経由で KVM を解除する方法

このチュートリアルでは、USB OTG を使用して GL.iNet KVM デバイスのブリックを解除する方法について説明します。この方法は、KVM デバイスがブリックされており、標準のファームウェア アップデートまたは U-Boot セーフ モードでは復元できない状況に適しています。

## サポートされているデバイス

- RMQ1

## 前提条件

デバイスのブロックを解除するには、次のツールを準備してください。

- Windows、macOS、または Ubuntu が動作するコンピューター

**Note**

- USB-C ポートを介して RMQ1 を電源アダプターに接続しないでください。

- ファームウェアをフラッシュする前に、`factory` パーティションをバックアップして、デバイス固有のデータ (MAC アドレスや証明書など) を保存します。 Web UI にアクセス可能な場合は、**Toolbox** → **Terminal** → **Access** に移動し、次のコマンドを実行してください。

      ```
      dd if=/dev/mtd6 of=/userdata/media/factory.bin
      ```

      バックアップ ファイルは **Virtual Media** に表示され、ローカル コンピューターにダウンロードできます。

- リカバリ プロセス中に、RMQ1 とコンピューターの間の USB-C ケーブルを取り外さないでください。そうしないと、デバイスが損傷する可能性があります。

- 点滅後にデバイスを自動的に再起動する場合は、開始する前に、**Settings** → **Options** → **Reboot to Normal Mode After Download** に移動して有効にします。このオプションが有効になっていない場合は、フラッシュの完了後にデバイスを手動で再起動する必要があります (つまり、電源ケーブルを取り外して再接続することによって)。

## 復旧手順

### Windows

1. RMQ1 デバイスの U-Boot ファームウェアを[こちら](https://dl.gl-inet.com/kvm/rmq1/stable)からコンピューターにダウンロードします（**DOWNLOAD FOR USB OTG** を選択してください）。

      ![rmq1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

2. USB ドライバーをインストールします。

      * [ここ](https://fw.gl-inet.com/tools/ax/Driver_V1.20.46.1.7z) からドライバー パッケージをコンピューターにダウンロードし、任意のディレクトリに解凍します。

      * `DriverSetup.exe` ファイルをダブルクリックしてインストーラーを実行します。

         ![driver-1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-1.png){class="glboxshadow"}

         ![driver-2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-2.png){class="glboxshadow"}

         ![driver-3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-3.png){class="glboxshadow"}

3. AXDL ツールをインストールします。

      * [ここ](https://fw.gl-inet.com/tools/ax/AXDL_V1.24.22.1.7z) から AXDL をコンピュータにダウンロードし、簡単にアクセスできるディレクトリに解凍します。

      * `AXDL.exe` ファイルをダブルクリックして、フラッシュ ツールを実行します。

         ![axdl-1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-1.png){class="glboxshadow"}

4. AXDL パネルを開き、`load.axp` をクリックし、手順 1 でダウンロードしたファームウェアを選択してアップロードします。

      ![axdl-2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-2.png){class="glboxshadow"}

      「`Start downloading`」をクリックします。

      ![axdl-3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-3.png){class="glboxshadow"}

5. KVM デバイスの電源を切ります。 RMQ1 の底部にある RESET ボタンを押したままにし、付属の USB-C ケーブルを使用してデバイスをコンピュータに接続します。

6. ステータス列に `Downloading...` が表示されたら、RESET ボタンを放します。

      ![axdl-4](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-4.png){class="glboxshadow"}

7. AXDL ツールに `Passed` が表示されるまで待って、フラッシュ プロセスが完了したことを確認します。

      ![axdl-5](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-5.png){class="glboxshadow"}

### macOS / Linux

公式 AXDL ツールは Windows のみです。 macOS および Linux の場合は、Rust で書かれたオープンソースの非公式 Axera イメージ ダウンローダーである axdl-rs を使用できます。

1. [rustup](https://rustup.rs/) 経由で Rust ツールチェーンをインストールします

2. RMQ1 デバイスの U-Boot ファームウェアを[こちら](https://dl.gl-inet.com/kvm/rmq1/stable)からコンピューターにダウンロードします（**DOWNLOAD FOR USB OTG** を選択してください）。

      ![rmq1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

3. プラットフォーム固有の依存関係をインストールします。

      - **Linux (Debian ベース)**

         ```
         sudo apt install -y libudev-dev libusb-1.0-0-dev
         ```
         通常のユーザーがデバイスにアクセスできるように udev ルールを構成します。

         ```
         # Clone the repository
         git clone https://github.com/gl-inet/axdl-rs.git

         # Change directory
         cd axdl-rs

         # Copy the udev rule file to the system directory
         sudo cp 99-axdl.rules /etc/udev/rules.d/

         # Reload udev rules to apply changes
         sudo udevadm control --reload
         ```

         ユーザーが `plugdev` グループに属していない場合は、そのユーザーをグループに追加し、変更を有効にするために再ログインしてください。

         ```
         sudo usermod -a -G plugdev $USER
         ```

      - **macOS**

         `brew` 経由で `libusb` をインストールし、USB と KVM デバイスとの通信を有効にします。

         ```
         brew install libusb
         ```

         `axdl-cli` ツールをビルドする

         ```
         cargo build --bin axdl-cli --package axdl-cli
         ```

4. 次のコマンドを入力してファームウェアをフラッシュします。 ` /path/to/firmware.axp ` を、ダウンロードしたファームウェア ファイルへの実際のパスに置き換えてください。

      ```
      cargo run --bin axdl-cli --package axdl-cli -- --file /path/to/firmware.axp --wait-for-device
      ```

      ツールは `Waiting for device to be ready` を表示し、待機状態になります。

5. KVM デバイスの電源を切ります。 RMQ1 の底部にある RESET ボタンを押したままにし、付属の USB-C ケーブルを使用してデバイスをコンピュータに接続します。

6. フラッシュプロセスが完了するまで待ちます。

      **注意:** フラッシュが完了しても、デバイスは自動的に再起動しない場合があります。 RMQ1 を手動で **電源を入れ直し** (電源をオフにしてからオンにします)、新しいファームウェアをアクティブにします。

      **Expected Output**

      フラッシュが成功すると、端末には以下の出力が表示されます。

      注: コンパイラの警告は無視しても問題ありません。

      ```
      $ cargo run --bin axdl-cli --package axdl-cli -- --file glkvm-RMQ1-nand-1.8.1-0518-1779101289.axp --wait-for-device
      warning: `axdl` (lib) generated 6 warnings
         Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.07s
         Running `target/debug/axdl-cli --file glkvm-RMQ1-nand-1.8.1-0518-1779101289.axp --wait-for-device`
      Waiting for the device to be ready
      Loading the AXP image configuration
      Start download
      Handshaking with the device
      Downloading the flash downloaders
      [00:00:03] [############################################################################]
      Downloading the partition table
      Skipping partition: FACTORY (excluded by default)
      Downloading image DDRINIT
      Downloading image UBOOT
      Downloading image LOGO
      Downloading image DTB
      Downloading image KERNEL
      Downloading image RECOVERY
      Downloading image MEDIA
      Downloading image ROOTFS
      [00:00:26] [############################################################################]
      Downloading image SPL
      Done
      ```

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
