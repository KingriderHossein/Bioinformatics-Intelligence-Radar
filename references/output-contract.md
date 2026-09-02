# قرارداد خروجی

## فهرست محتوا

- 1. خلاصه مدیریتی
- 2. هشدارهای حیاتی
- 3. رادار اصلی
- 4. رادار ابزار و نرم‌افزار
- 5. رادار دیتابیس و زیرساخت
- 6. رادار Dataset
- 7. رادار مقالات داوری‌شده
- 8. کنترل وضعیت داوری
- 9. سلامت GitHub / Repository
- 10. رادار بازتولیدپذیری
- 11. ادعاهای Benchmark
- 12. سیگنال امروز
- 13. کاندیدهای سوشال
- 14. کاندیدهای Deep-Dive
- 15. Watchlist
- 16. آمار رادار
- رفتار در روزهای کم‌خبر
- انتقال به Telegram Editor
- Final output gate

تمام خروجی رادار را به فارسی بنویس، مگر اینکه کاربر صریحاً زبان دیگری درخواست کند. نام ابزارها، دیتابیس‌ها، packageها، repositoryها، نسخه‌ها، شناسه‌ها و اصطلاحات فنی استاندارد را در صورت نیاز به English نگه دار.

پیش از نوشتن متن، `peer-review-policy.md` و سپس `editorial-tone-engine.md` را اعمال کن.

قاعده غیرقابل‌مذاکره: هیچ مقاله‌ای بدون peer review تأییدشده نباید در هیچ بخش قابل مشاهده رادار، Watchlist، Signal، Social Candidate، Deep Dive، Benchmark Claims یا Telegram Handoff ظاهر شود. اگر وضعیت داوری مقاله نامعلوم است، آن را حذف کن.

از ترتیب زیر استفاده کن. «خلاصه مدیریتی» باید فشرده و «رادار اصلی» باید گسترده باشد.

# رادار هوشمندی بیوانفورماتیک — [تاریخ دقیق]

بازه رصد: [شروع] تا [پایان]

## 1. خلاصه مدیریتی

حداکثر پنج مورد. برای هر مورد: عنوان، اهمیت در یک خط، نوع، اولویت، منبع.

برای scholarly literature فقط مقالات peer-reviewed تأییدشده مجازند. Software/database/dataset/infrastructure events طبق منبع رسمی خود قابل گزارش‌اند.

لحن پیش‌فرض داخلی: `ANALYTICAL_NEWS`، اما قوی‌ترین محدودیت شواهد هر آیتم را از نسخه کامل آن به ارث ببر.

## 2. هشدارهای حیاتی

فقط تغییرات زمان‌حساس یا مواردی که می‌توانند workflow را مختل کنند. اگر موردی وجود ندارد، بنویس: «در این بازه هشدار حیاتی تأییدشده‌ای پیدا نشد.»

لحن پیش‌فرض داخلی: `TECHNICAL_ALERT` با `WORKFLOW_IMPACT` و در صورت واقعی بودن فوریت، `BREAKING_URGENCY`.

برای هر هشدار بیاور:
- چه چیزی تغییر کرده است
- تاریخ اثرگذاری
- چه کسانی تحت تأثیرند
- اقدام لازم
- اولویت
- منبع رسمی

## 3. رادار اصلی

وقتی حجم خبر اجازه می‌دهد، 15 تا 30 مورد متمایز و واجد شرایط را هدف بگیر. سهم مقالات باید فقط از peer-reviewed literature باشد.

از جدول فشرده استفاده کن:

| # | حوزه | مورد | نوع | اولویت | چرا مهم است |
|---|---|---|---|---|---|

متن «خلاصه مدیریتی» را عیناً تکرار نکن.

## 4. رادار ابزار و نرم‌افزار

تغییرات معنادار stable و pre-release را پوشش بده و نوع release را مشخص کن.

برای تغییرات مهم مشخص کن:
- نسخه و نوع release
- تغییر اصلی
- backward compatibility یا migration در صورت تأیید
- اثر عملی
- منبع رسمی release/changelog

لحن پیش‌فرض داخلی: `NEUTRAL_TECHNICAL`. اگر release یا deprecation می‌تواند workflow را بشکند، به `TECHNICAL_ALERT` ارتقا بده.

## 5. رادار دیتابیس و زیرساخت

releaseها، تغییرات schema/API، migration، به‌روزرسانی annotation/reference و deprecationها را پوشش بده.

تغییر reference/annotation را صرفاً یک release معمولی معرفی نکن اگر می‌تواند نتیجه تحلیل را تغییر دهد. اثر عملی را صریح کن.

## 6. رادار Dataset

برای هر dataset مهم این موارد را ثبت کن: modality، species/disease، scale، دسترسی raw/processed، license در صورت معلوم بودن، و کاربرد محتمل.

Standalone official dataset releases می‌توانند بدون مقاله peer-reviewed وارد این بخش شوند، به شرط اینکه خود رویداد dataset از منبع رسمی تأیید شود. اگر فقط یک preprint dataset را توصیف می‌کند، preprint را به‌عنوان مقاله یا authority علمی وارد گزارش نکن.

## 7. رادار مقالات داوری‌شده

فقط مقالاتی را وارد کن که peer review آن‌ها طبق `peer-review-policy.md` تأیید شده باشد.

برای قوی‌ترین مقالات بیاور:
- مسئله
- ادعا
- روش یا طراحی کلیدی
- شواهد/benchmark
- کد
- داده
- validation
- محدودیت اصلی
- ارزش عملی

لحن پیش‌فرض داخلی: `PAPER_SPOTLIGHT`.

برای benchmark بزرگ، clinical implication، causal claim یا ادعای AI پرریسک، محدودیت‌های `EVIDENCE_CRITICAL` را اعمال کن.

## 8. کنترل وضعیت داوری

این بخش فقط compliance را گزارش می‌کند و نباید عنوان یا claim مقاله‌های حذف‌شده را نشان دهد.

بنویس:

«فقط scholarly literature با peer review تأییدشده اجازه ورود به این گزارش را دارد. Preprintها و مقاله‌های دارای وضعیت داوری نامعلوم پیش از scoring حذف می‌شوند.»

اگر شمارش دقیق در همان اجرا مستقیماً مشاهده شد، می‌توان اضافه کرد:

`Non-peer-reviewed literature excluded: N`

این عدد را تخمین نزن.

## 9. سلامت GitHub / Repository

فقط برای پروژه‌های مهم انتخاب‌شده. شواهد تأییدشده درباره release/activity/tests/CI/container/license را بیاور. تعداد star را به‌تنهایی شاخص کیفیت ندان.

اگر metadata ناقص است، نتیجه‌گیری کیفی نکن.

## 10. رادار بازتولیدپذیری

فقط وقتی معیارهای کافی تأیید شده‌اند امتیاز /10 بده؛ در غیر این صورت بنویس «شواهد ناکافی».

مشخص کن کدام مؤلفه‌ها واقعاً بررسی شدند: code، data، environment/container، tests/CI، version pinning، documentation، benchmark reproducibility یا موارد دیگر.

## 11. ادعاهای Benchmark

ادعاهای بزرگ سرعت/دقت/حافظه را فهرست کن و مشخص کن آیا تأیید مستقل وجود دارد یا نه.

برای scholarly benchmark papers فقط peer-reviewed literature مجاز است.

برای هر claim بیاور:
- ادعای دقیق
- منبع claim
- comparator/baseline
- dataset و hardware context در صورت موجود بودن
- وضعیت تأیید مستقل: YES/NO/UNKNOWN
- محدودیت یا red flag

اگر تأیید مستقل پیدا نشد، `AUTHOR_REPORTED` را حفظ کن و نتیجه را به‌صورت واقعیت مستقل بازنویسی نکن.

## 12. سیگنال امروز

1 تا 3 سیگنال با شواهد و سطح اطمینان ارائه کن.

هر scholarly paper که به‌عنوان evidence یک Signal استفاده می‌شود باید peer-review-verified باشد. Non-peer-reviewed literature نمی‌تواند برای ساخت trend یا Signal استفاده شود.

قالب هر سیگنال:

### [بیان دقیق سیگنال]
شواهد: [چند مشاهده مرتبط، ترجیحاً مستقل]
برداشت تحلیلی: ...
چرا مهم است: ...
سطح اطمینان: LOW/MEDIUM/HIGH
چه چیزی را باید بعداً رصد کرد: ...

یک مقاله منفرد را معمولاً trend معرفی نکن.

## 13. کاندیدهای سوشال

3 تا 5 مورد عمومی و دقیق ارائه کن.

هر scholarly Social Candidate باید peer-review-verified باشد. Preprint یا مقاله با وضعیت داوری نامعلوم را حتی با social score بالا انتخاب نکن.

قالب:

### [عنوان جذاب اما دقیق]
هوک: ...
چرا برای مخاطب عمومی مهم است: ...
فرمت پیشنهادی: ...
امتیاز سوشال: X/30
ریسک اغراق: LOW/MEDIUM/HIGH — [دلیل]

لحن پیش‌فرض داخلی: `CURIOSITY_BRIDGE`. تمام evidence modifiers آیتم اصلی را حفظ کن.

## 14. کاندیدهای Deep-Dive

در صورت امکان دقیقاً 3 مورد.

Scholarly Deep-Diveها باید فقط از peer-reviewed literature انتخاب شوند. Software/database/infrastructure/dataset deep dives طبق منبع رسمی خود مجازند.

برای هر مورد:
- مسئله یا سیگنال
- چرا ارزش deep dive دارد
- چه evidence gap یا technical question باقی مانده است
- قدم بعدی برای آزمون
- نتیجه‌ای که فعلاً نباید گرفت

## 15. Watchlist

Watchlist می‌تواند شامل software releaseهای experimental، migrations درحال تکمیل، API changes، database transitions و رویدادهای رسمی دیگر باشد.

Non-peer-reviewed scholarly papers را در Watchlist نام نبر یا خلاصه نکن. اگر مقاله‌ای هنوز peer reviewed نشده است، آن را خارج از گزارش نگه دار تا peer-reviewed publication آن تأیید شود.

صریح بگو برای آیتم‌های مجاز چه چیزی هنوز معلوم نیست و چه event یا evidence باعث خروج آن از Watchlist می‌شود.

## 16. آمار رادار

فقط شمارش‌هایی را گزارش کن که واقعاً مشاهده شده‌اند.

- Candidates retrieved: [N یا «از رابط جست‌وجو قابل اندازه‌گیری نیست»]
- Items reviewed: [N، اگر واقعاً ثبت شد]
- Shortlisted: [N]
- High priority: [N]
- Social candidates: [N]
- Deep-dive candidates: [N]
- Non-peer-reviewed literature excluded: [N، فقط اگر مستقیم مشاهده شد]

## رفتار در روزهای کم‌خبر

اگر بازه کم‌خبر بود، گزارش را با خبرهای ضعیف یا preprintها پر نکن. صریحاً بگو روز کم‌خبر است و برای context از fallback هفت‌روزه استفاده کن. فقط آیتم‌های واجد شرایط را وارد کن.

کمبود peer-reviewed news یک نتیجه معتبر رادار است.

## انتقال به Telegram Editor

اگر یک مرحله تحریریه Telegram بخشی از همان workflow است، پس از تکمیل گزارش یک `Telegram Handoff v1` مطابق `references/telegram-handoff.md` به صورت داخلی بساز.

Handoff فقط باید از Social Candidateهای واجد شرایط ساخته شود. اگر candidate یک scholarly paper است، peer-review verification باید قبل از handoff انجام شده باشد.

Radar نباید خودش Editor را به‌عنوان tool یا Skill فراخوانی یا جست‌وجو کند. JSON خام را در گزارش کاربر نمایش نده مگر اینکه کاربر صریحاً درخواست کند.

## Final output gate

پیش از پاسخ نهایی تأیید کن:

- هیچ preprint-only یا scholarly paper با وضعیت peer review نامعلوم در متن دیده نمی‌شود.
- هیچ عنوان یا claim از مقاله حذف‌شده در Watchlist یا بخش کنترل وضعیت داوری افشا نشده است.
- Social Candidates، Signals، Deep Dives، Benchmark Claims و Telegram Handoff همان peer-review gate را رعایت می‌کنند.
- نسخه peer-reviewed بر نسخه preprint همان مطالعه ترجیح داده شده است.
- Software/database/dataset/infrastructure events به‌اشتباه به peer-review gate مقاله‌ها محدود نشده‌اند.
