```markdown
# 🎧 Discord Voice Channel Switcher Bot

Bu proje, Discord sunucularındaki belirli bir kategorideki dolu ses kanallarına rastgele bağlanıp, belirli bir süre (0-5 saniye) sonra başka bir dolu ses kanalına geçiş yapan bir bot içerir. Bu bot, `discord.py-self` kütüphanesi kullanılarak geliştirilmiştir ve kullanıcıların aktif olduğu ses kanalları arasında dolaşarak dinamik bir etkileşim sağlar.

## 🚀 Özellikler

- **Otomatik Ses Kanalı Bağlantısı:** Bot, belirtilen kategori içindeki ses kanallarına otomatik olarak bağlanır ve rastgele aralıklarla ses kanalını değiştirir.
- **Boş Kanallardan Kaçınma:** Bot, yalnızca içinde en az bir kullanıcı bulunan (dolu) ses kanallarına bağlanır ve boş kanalları atlar.
- **Dinamik Zamanlama:** Her ses kanalı değişimi arasında rastgele bir süre (0-5 saniye) bekler.
- **Hata Yönetimi:** Bağlantı sırasında oluşabilecek hataları kontrol eder ve konsola bilgi verir.

## 🛠️ Kurulum ve Kullanım

Bu projeyi kendi makinenizde çalıştırmak için aşağıdaki adımları izleyin:

### Gereksinimler

- Python 3.7 veya üzeri
- `discord.py-self`
- `colorama`
- `termcolor` kütüphaneleri

### Kurulum

1. **Depoyu Klonlayın:**
   ```bash
   git clone https://github.com/kullanıcı_adı/discord-voice-channel-switcher.git
   cd discord-voice-channel-switcher
   ```

2. **Gerekli Kütüphaneleri Yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **`config.json` Dosyasını Ayarlayın:**

   Proje dizininde bir `config.json` dosyası oluşturun ve aşağıdaki örnekteki gibi düzenleyin:

   ```json
   {
     "token": "ACC-TOKEN",
     "category_id": "CATEGORY-ID"
   }
   ```

   - `ACC-TOKEN`: Discord botunuzun token'i.
   - `CATEGORY-ID`: Ses kanallarının bulunduğu kategori ID'si.

4. **Botu Çalıştırın:**
   ```bash
   python main.py
   ```

## 📜 Çalışma Prensibi

| Aşama                        | Açıklama                                                                            |
|------------------------------|--------------------------------------------------------------------------------------|
| **Başlatma**                 | Bot, belirtilen token ile Discord sunucusuna giriş yapar.                           |
| **Kategori Kontrolü**        | Bot, belirtilen kategori ID'sini kontrol eder ve geçerli olup olmadığını doğrular.  |
| **Dolu Kanal Kontrolü**      | Kategorideki dolu ses kanallarını (en az bir üyesi olan) filtreler.                 |
| **Rastgele Kanal Bağlantısı**| Bot, dolu ses kanallarından rastgele birini seçer ve bağlanır.                     |
| **Bekleme Süresi**           | Bot, 0-5 saniye arasında rastgele bir süre bekler.                                  |
| **Kanal Değiştirme**         | Bot, mevcut ses kanalından ayrılır ve başka bir rastgele dolu kanala bağlanır.      |
| **Hata Yönetimi**            | Herhangi bir bağlantı hatası oluşursa konsola bilgi verir ve yeniden dener.         |

## ⚙️ Yapılandırma

- **`token` (string):** Botun Discord token'i.
- **`category_id` (integer):** Botun dolu ses kanallarını arayacağı kategori ID'si.

## 📝 Notlar

- Bu bot, sadece kullanıcıların aktif olduğu ses kanallarına bağlanır ve böylece boş kanallardan kaçınır.
- Botun düzgün çalışabilmesi için doğru izinlere ve uygun ayarlara sahip olması gerekmektedir.
- Bu botu kullanırken Discord'un [Kullanım Şartları](https://discord.com/terms) ve [Topluluk Kuralları](https://discord.com/guidelines) ile uyumlu olduğundan emin olun.

## 🤖 Katkıda Bulunun

Bu projeye katkıda bulunmak isterseniz, lütfen bir **pull request** açın veya bir **issue** oluşturun. Her türlü geri bildiriminiz ve katkılarınız için şimdiden teşekkür ederiz!

## 📞 İletişim

- **GitHub:** [xz2r](https://github.com/xz2r)
- **Destek:** [xz2r](https://discord.gg/alura)
- **Discord:** xz2r

## 📜 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

---

Projemizi incelediğiniz için teşekkür ederiz! Eğer faydalı bulduysanız, ⭐ vererek projeye destek olabilirsiniz.
```
