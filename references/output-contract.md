# قرارداد خروجی Newsroom Radar

Protocol: Radar 3.0+

این فایل قرارداد authoritative خروجی کاربر است.

Radar در حالت پیش‌فرض یک **تحریریه علمی فشرده** تولید می‌کند، نه audit report چندبخشی. Evidence Card، peer-review checks، repository health، reproducibility و benchmark verification عمدتاً backend هستند و فقط وقتی برای فهم خبر لازم‌اند در متن ظاهر می‌شوند.

تمام خروجی را به فارسی بنویس مگر اینکه کاربر صریحاً زبان دیگری بخواهد. نام ابزارها، packageها، دیتابیس‌ها، versionها، gene/protein symbolها، DOI/PMID/accession و اصطلاحات precision-sensitive را در English نگه دار.

## اصل خروجی

خروجی روزانه باید به این سؤال پاسخ دهد:

**«امروز در بیوانفورماتیک چه چیزی واقعاً ارزش توجه من را دارد و چرا؟»**

نه:

**«امروز چه چیزهایی منتشر شدند؟»**

هیچ minimum story count وجود ندارد.

## ساختار پیش‌فرض

از این ساختار استفاده کن، اما بخش‌های optional را فقط وقتی واقعاً محتوای ارزشمند دارند نشان بده.

# رادار بیوانفورماتیک — [تاریخ دقیق]

`بازه رصد: [شروع دقیق] تا [پایان دقیق]`

یک خط کوتاه coverage note فقط اگر محدودیت واقعی وجود دارد.

## 1. خبر اول

صفر یا یک story.

فقط وقتی یک story واضحاً از بقیه مهم‌تر یا newsworthyتر است این بخش را نشان بده.

هدف طول: حدود 140 تا 240 کلمه، بسته به پیچیدگی.

ساختار narrative پیشنهادی:

`تیتر -> نتیجه/اتفاق -> context ضروری -> شواهد اصلی -> پیامد -> مهم‌ترین مرز ادعا -> منبع`

این برچسب‌ها را داخل متن چاپ نکن مگر اینکه واقعاً به خوانایی کمک کنند.

تیتر باید خود خبر را بگوید، نه فقط نام paper/framework را.

## 2. ارزش دنبال‌کردن

معمولاً 1 تا 4 story دیگر. اگر خبر کافی نیست، کمتر بنویس.

هر story حدود 70 تا 140 کلمه.

برای هر story:

- یک تیتر روشن؛
- 2 تا 4 پاراگراف کوتاه؛
- اصل اتفاق؛
- دلیل اهمیت؛
- در صورت نیاز یک limitation قابل مشاهده؛
- primary source.

از جدول برای خبرهای اصلی استفاده نکن مگر کاربر صریحاً خروجی جدولی بخواهد.

## 3. هشدار عملی

Optional.

فقط برای workflow-impacting events مانند:

- API/schema/authentication change؛
- migration/deprecation؛
- security/integrity issue؛
- reference/annotation change که result را تغییر می‌دهد؛
- breaking stable release؛
- outage/deadline/end-of-support.

قالب کوتاه:

`چه چیزی تغییر کرد -> چه کسی تحت تأثیر است -> چه کاری باید انجام دهد -> تاریخ/نسخه -> منبع رسمی`

اگر هشدار نداریم، لازم نیست یک بخش بلند با عبارت «هشداری نبود» بسازیم؛ یک جمله کوتاه در ابتدای یا انتهای گزارش کافی است.

## 4. سیگنال امروز

Optional و حداکثر یک Signal در خروجی روزانه پیش‌فرض.

فقط وقتی synthesis واقعاً چیزی فراتر از تکرار خبرهای منفرد اضافه می‌کند نشان بده.

برای `EMERGING_SIGNAL` حداقل دو observation مستقل لازم است.

قالب:

### [بیان directional و دقیق]

شواهد: ...

برداشت: ...

چرا مهم است: ...

سطح اطمینان: LOW/MEDIUM/HIGH

اگر signal قابل اتکایی نداریم، فقط بنویس:

`امروز سیگنال cross-source به‌اندازه کافی قوی برای گزارش دیده نشد.`

هرگز trend مصنوعی تولید نکن.

## 5. انتخاب تحریریه

2 تا 5 Story Card برتر را وقتی موجودند در یک فهرست فشرده نشان بده.

برای هرکدام فقط این موارد را بیاور:

- عنوان؛
- بهترین format: Telegram / Article / Infographic / Technical explainer / Alert؛
- angle در یک جمله؛
- News Value Score فقط اگر نمایش عدد برای کاربر مفید باشد.

این بخش جایگزین فهرست طولانی `Social Candidates` در خروجی قدیمی است، ولی همان candidateها را برای downstream handoff نگه می‌دارد.

## 6. برای Deep Dive

Optional. حداکثر 1 تا 3 مورد.

هر مورد در 2-3 خط:

- سؤال مهم باقی‌مانده؛
- evidence gap؛
- چه چیزی را نباید هنوز نتیجه گرفت.

این بخش نباید به mini-paper review تبدیل شود.

## 7. زیر نظر

Watchlist فشرده، معمولاً 2 تا 5 bullet.

فقط eventهای واجد شرایط و قابل پیگیری را بیاور، مانند:

- انتظار برای independent validation؛
- stable release بعدی؛
- migration؛
- correction/retraction follow-up؛
- dataset expansion؛
- external benchmark.

Non-peer-reviewed scholarly paper را در Watchlist نام نبر.

## 8. پایش امروز

Observed-only و کوتاه.

فقط counterهایی را نشان بده که واقعاً در run ثبت شدند، مانند:

- Curator sources checked
- eligible stories resolved
- duplicate/no-change suppressions
- stories selected
- Telegram handoff candidates

اگر counter از ابتدا track نشده، آن را حدس نزن و لازم نیست فهرست طولانی `not measurable` بسازی.

هدف این بخش transparency است، نه نمایش فرایند داخلی.

## Technical appendix فقط در صورت نیاز

بخش‌های زیر در خروجی پیش‌فرض **مخفی** هستند و فقط وقتی کاربر درخواست کند یا برای یک story خاص حیاتی باشند نمایش داده می‌شوند:

- Peer-review compliance table
- GitHub/repository health
- reproducibility `/10`
- benchmark claim audit table
- raw Evidence Cards
- raw Story Cards
- detailed Radar statistics
- Curator feedback
- run ledger/state

وقتی benchmark claim خودش خبر است، context و limitation آن را داخل همان story بیاور؛ نیازی به یک بخش جداگانه فقط برای حفظ template نیست.

## Story writing rules

پیش از نوشتن هر story، `newsroom-engine.md` را اعمال کن.

- Lead باید سریع به خبر برسد.
- Method را اول نیاور مگر method خود خبر باشد.
- publication/journal name را جای news angle ننشان.
- از paragraphهای کوتاه استفاده کن.
- «چرا مهم است؟» را در narrative حل کن.
- number را فقط وقتی برجسته کن که scale یا consequence را روشن می‌کند.
- limitation را جایی بیاور که مانع overinterpretation شود.
- benchmarkهای بدون replication را با attribution بنویس: «نویسندگان گزارش می‌کنند...».
- prediction را measurement معرفی نکن.
- association را cause معرفی نکن.
- preclinical را clinical معرفی نکن.
- AI capability را anthropomorphic یا universal نکن.

## Peer-review invariant

هیچ scholarly paper بدون peer review تأییدشده نباید در هیچ user-visible story، Signal، Deep Dive، Watchlist، editorial selection یا Telegram Handoff ظاهر شود.

Preprint-only و review-status-unknown recordها پیش از newsroom scoring حذف می‌شوند.

Standalone verified software/database/dataset/infrastructure events مشمول peer-review requirement مقاله نیستند.

## روز کم‌خبر

روز کم‌خبر یک خروجی معتبر است.

مثال قابل قبول:

- بدون خبر اول؛
- دو story در «ارزش دنبال‌کردن»؛
- بدون Signal؛
- یک Watch item.

هرگز report را برای ایجاد حس کامل‌بودن با filler پر نکن.

## انتقال به Telegram Editor

اگر Telegram editorial stage بخشی از workflow است:

1. Story Cards برگزیده را بعد از Newsroom Release Gate انتخاب کن.
2. `Telegram Handoff v1` را مطابق `telegram-handoff.md` بساز.
3. Evidence Card همچنان factual authority است؛ Story Card angle و newsroom framing را منتقل می‌کند.
4. Radar Editor را به‌عنوان Skill/tool جست‌وجو یا invoke نمی‌کند.
5. raw handoff JSON را نمایش نده مگر کاربر صریحاً بخواهد.

## Final output gate

پیش از پاسخ نهایی تأیید کن:

- report شبیه newsroom است، نه literature inventory؛
- هیچ story صرفاً به دلیل جدیدبودن publication وارد نشده است؛
- خبر اول، اگر وجود دارد، واقعاً بهترین story روز است؛
- تیترها finding/consequence/tension را نشان می‌دهند؛
- متن‌ها method-first نیستند مگر لازم باشد؛
- limitationهای material visible هستند؛
- هیچ preprint یا scholarly item با peer-review نامعلوم دیده نمی‌شود؛
- cross-run duplicate بدون material change دوباره به‌عنوان خبر نمایش داده نشده است؛
- Signal فقط در صورت evidence مستقل کافی آمده است؛
- هیچ quota باعث filler نشده است؛
- backend audit به‌اشتباه محصول اصلی کاربر نشده است.
