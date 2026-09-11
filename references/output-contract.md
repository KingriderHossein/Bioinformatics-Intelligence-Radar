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

پیش از نوشتن متن، `peer-review-policy.md`، `evidence-card.md` و سپس `editorial-tone-engine.md` را اعمال کن.

قاعده غیرقابل‌مذاکره: هیچ مقاله‌ای بدون peer review تأییدشده نباید در هیچ بخش قابل مشاهده رادار، Watchlist، Signal، Social Candidate، Deep Dive، Benchmark Claims یا Telegram Handoff ظاهر شود. اگر وضعیت داوری مقاله نامعلوم است، آن را حذف کن.

تمام سطوح خروجی یک story باید از همان Evidence Card مشتق شوند. اگر یک fact، عدد، تاریخ، benchmark status یا limitation تغییر کرد، ابتدا Evidence Card را اصلاح کن و سپس متن را بازتولید کن.

# رادار هوشمندی بیوانفورماتیک — [تاریخ دقیق]

بازه رصد: [شروع] تا [پایان]

اگر cross-run state در دسترس بود و diagnostics یا آمار مرتبط هستند، می‌توان state availability را نیز گزارش کرد. هرگز prior state را حدس نزن.

## 1. خلاصه مدیریتی

حداکثر پنج مورد. برای هر مورد: عنوان، اهمیت در یک خط، نوع، اولویت، منبع.

برای scholarly literature فقط مقالات peer-reviewed تأییدشده مجازند. Software/database/dataset/infrastructure events طبق منبع رسمی خود قابل گزارش‌اند.

لحن پیش‌فرض داخلی: `ANALYTICAL_NEWS`، اما قوی‌ترین محدودیت شواهد هر آیتم را از Evidence Card به ارث ببر.

## 2. هشدارهای حیاتی

فقط تغییرات زمان‌حساس یا مواردی که می‌توانند workflow را مختل کنند. اگر موردی وجود ندارد، بنویس: «در این بازه هشدار حیاتی تأییدشده‌ای پیدا نشد.»

برای هر هشدار بیاور:
- چه چیزی تغییر کرده است
- تاریخ اثرگذاری
- چه کسانی تحت تأثیرند
- اقدام لازم
- اولویت
- منبع رسمی

لحن پیش‌فرض داخلی: `TECHNICAL_ALERT` با `WORKFLOW_IMPACT` و در صورت واقعی بودن فوریت، `BREAKING_URGENCY`.

## 3. رادار اصلی

هیچ حداقل تعداد اجباری وجود ندارد.

فقط آیتم‌هایی را وارد کن که eligibility و relevance threshold را رد کرده‌اند. به‌طور پیش‌فرض بیش از 20 مورد وارد نکن مگر اینکه حجم واقعی خبر و درخواست کاربر پوشش گسترده‌تر را توجیه کند.

اگر فقط 6 یا 8 مورد قوی وجود دارد، همان تعداد صحیح است. برای رسیدن به quota خبر ضعیف، تکراری یا کم‌اهمیت اضافه نکن.

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

اگر prior state موجود است، release تکراری بدون material change را دوباره به‌عنوان خبر جدید وارد نکن.

لحن پیش‌فرض داخلی: `NEUTRAL_TECHNICAL`. اگر release یا deprecation می‌تواند workflow را بشکند، به `TECHNICAL_ALERT` ارتقا بده.

## 5. رادار دیتابیس و زیرساخت

releaseها، تغییرات schema/API، migration، authentication، به‌روزرسانی annotation/reference و deprecationها را پوشش بده.

تغییر reference/annotation را صرفاً یک release معمولی معرفی نکن اگر می‌تواند نتیجه تحلیل را تغییر دهد. event date، announcement date و effective date را در صورت تفاوت جدا نگه دار.

## 6. رادار Dataset

برای هر dataset مهم این موارد را در صورت تأیید ثبت کن: modality، species/disease، scale، دسترسی raw/processed، license و کاربرد محتمل.

Standalone official dataset releases می‌توانند بدون مقاله peer-reviewed وارد این بخش شوند، به شرط اینکه خود رویداد dataset از منبع رسمی تأیید شود. اگر فقط یک preprint dataset را توصیف می‌کند، preprint را به‌عنوان مقاله یا authority علمی وارد گزارش نکن.

## 7. رادار مقالات داوری‌شده

فقط مقالاتی را وارد کن که peer review آن‌ها طبق `peer-review-policy.md` تأیید شده باشد.

برای قوی‌ترین مقالات، فقط فیلدهای مادی را از Evidence Card باز کن:
- مسئله
- ادعا
- روش یا طراحی کلیدی
- شواهد/benchmark
- code/data در صورت مرتبط بودن
- validation
- محدودیت اصلی
- ارزش عملی

لحن پیش‌فرض داخلی: `PAPER_SPOTLIGHT`.

برای benchmark بزرگ، clinical implication، causal claim یا ادعای AI پرریسک، محدودیت‌های `EVIDENCE_CRITICAL` را اعمال کن.

## 8. کنترل وضعیت داوری

این بخش فقط compliance را گزارش می‌کند و نباید عنوان یا claim مقاله‌های حذف‌شده را نشان دهد.

بنویس:

«فقط scholarly literature با peer review تأییدشده اجازه ورود به این گزارش را دارد. Preprintها و مقاله‌های دارای وضعیت داوری نامعلوم پیش از scoring حذف می‌شوند.»

اگر شمارش `excluded_ineligible_scholarly` در telemetry همان اجرا واقعاً ثبت شده بود، می‌توان عدد آن را اضافه کرد. این عدد را تخمین یا از روی نتایج نهایی بازسازی نکن.

## 9. سلامت GitHub / Repository

فقط برای پروژه‌های مهم انتخاب‌شده و فقط در حد evidence مادی بررسی‌شده.

شواهد ممکن: release/activity، tests، CI، container، license، environment، documentation و example data.

تعداد star را به‌تنهایی شاخص کیفیت ندان. اگر metadata ناقص است، نتیجه‌گیری کیفی نکن.

## 10. رادار بازتولیدپذیری

از فیلدهای verified در Evidence Card استفاده کن.

فقط وقتی معیارهای کافی واقعاً بررسی شده‌اند امتیاز /10 بده؛ در غیر این صورت بنویس «شواهد ناکافی» و مواردی را که واقعاً تأیید شدند نام ببر.

unknown را صفر فرض نکن.

## 11. ادعاهای Benchmark

ادعاهای بزرگ سرعت/دقت/حافظه/برتری را فهرست کن و مشخص کن آیا تأیید مستقل وجود دارد یا نه.

برای هر claim در صورت موجود بودن بیاور:
- ادعای دقیق
- منبع claim
- comparator/baseline
- dataset و hardware context
- وضعیت تأیید مستقل: YES/NO/UNKNOWN
- محدودیت یا red flag

اگر تأیید مستقل پیدا نشد، `AUTHOR_REPORTED` را حفظ کن و نتیجه را به‌صورت واقعیت مستقل بازنویسی نکن.

## 12. سیگنال امروز

1 تا 3 مورد ارائه کن، اما فقط وقتی evidence graph کافی وجود دارد.

طبقه‌بندی داخلی:

- `OBSERVATION`: یک event قوی یا مجموعه‌ای بسیار نزدیک که هنوز برای trend language کافی نیست.
- `EMERGING_SIGNAL`: حداقل دو observation واجد شرایط و مستقل از پروژه‌ها/منشأهای متفاوت که یک جهت مشترک را پشتیبانی می‌کنند.
- `ESTABLISHED_TREND`: به‌ندرت استفاده شود؛ به evidence گسترده‌تر در چند زمان/منبع مستقل نیاز دارد و معمولاً از یک اجرای روزانه به‌تنهایی حاصل نمی‌شود.

هر scholarly evidence node باید peer-review-verified باشد. duplicate publicationها، preprint/journal pair یک مطالعه، یا چند خبر از یک project را به‌عنوان observation مستقل نشمار.

قالب:

### [بیان دقیق سیگنال]
نوع: OBSERVATION / EMERGING_SIGNAL / ESTABLISHED_TREND
شواهد: [مشاهدات مستقل]
برداشت تحلیلی: ...
چرا مهم است: ...
سطح اطمینان: LOW/MEDIUM/HIGH
چه چیزی را باید بعداً رصد کرد: ...

## 13. کاندیدهای سوشال

به‌طور معمول 3 تا 5 مورد، ولی quota اجباری نیست. اگر تعداد storyهای واجد شرایط کمتر است، همان تعداد را ارائه کن.

هر scholarly Social Candidate باید peer-review-verified باشد.

قالب:

### [عنوان جذاب اما دقیق]
هوک: ...
چرا برای مخاطب عمومی مهم است: ...
فرمت پیشنهادی: ...
امتیاز سوشال: X/30
اولویت تحریریه: [editorial_priority_score]
ریسک اغراق: LOW/MEDIUM/HIGH — [دلیل]

`editorial_priority_score` فقط ابزار ranking است؛ آن را با scientific evidence score یکی ندان.

لحن پیش‌فرض داخلی: `CURIOSITY_BRIDGE`. تمام evidence modifiers، limitationها و `do_not_say_fa` از Evidence Card حفظ شوند.

## 14. کاندیدهای Deep-Dive

در صورت وجود evidence کافی، تا 3 مورد. دقیقاً سه مورد اجباری نیست.

برای هر مورد:
- مسئله یا سیگنال
- چرا ارزش deep dive دارد
- چه evidence gap یا technical question باقی مانده است
- قدم بعدی برای آزمون
- نتیجه‌ای که فعلاً نباید گرفت

## 15. Watchlist

Watchlist می‌تواند شامل software releaseهای experimental، migrations درحال تکمیل، API changes، database transitions و رویدادهای رسمی دیگر باشد.

Non-peer-reviewed scholarly papers را در Watchlist نام نبر یا خلاصه نکن.

برای هر آیتم بگو چه چیزی هنوز معلوم نیست و چه material event یا evidence باعث update/خروج آن از Watchlist می‌شود.

اگر run state موجود است، item قدیمی بدون material change را فقط برای continuity لازم نگه دار؛ آن را خبر تازه معرفی نکن.

## 16. آمار رادار

فقط telemetryهایی را گزارش کن که در همان اجرا واقعاً نگه‌داری شدند.

فیلدهای ترجیحی از `run-state.md`:

- Discovered unique
- Identity resolved
- Peer review verified
- Ineligible scholarly excluded
- Official events verified
- Cross-run duplicates suppressed
- Material updates detected
- Primary claims verified
- Shortlisted
- High priority
- Social candidates
- Deep-dive candidates
- Telegram handoff candidates

اگر یک counter در طول اجرا maintain نشده است، بنویس «اندازه‌گیری نشد» یا آن ردیف را حذف کن. بعداً از روی search interface یا final shortlist آن را حدس نزن.

## رفتار در روزهای کم‌خبر

اگر بازه کم‌خبر بود، گزارش را با خبرهای ضعیف، duplicate یا preprintها پر نکن. صریحاً بگو روز کم‌خبر است و فقط در صورت نیاز از fallback هفت‌روزه استفاده کن.

کمبود خبر واجد شرایط یک نتیجه معتبر رادار است.

Adaptive stop rule در `search-playbook.md` را رعایت کن تا low-news day به broad search نامحدود تبدیل نشود.

## انتقال به Telegram Editor

اگر یک مرحله تحریریه Telegram بخشی از همان workflow است، پس از تکمیل Radar quality gate یک `Telegram Handoff v1` مطابق `references/telegram-handoff.md` به صورت داخلی بساز.

Handoff فقط از Social Candidateهای واجد شرایط و از همان Evidence Cardهای نهایی ساخته شود. Editor نباید مجبور شود facts را دوباره از source استخراج کند.

Radar نباید خودش Editor را به‌عنوان tool یا Skill فراخوانی یا جست‌وجو کند. JSON خام را در گزارش کاربر نمایش نده مگر اینکه کاربر صریحاً درخواست کند.

## Final output gate

پیش از پاسخ نهایی تأیید کن:

- هیچ preprint-only یا scholarly paper با وضعیت peer review نامعلوم در متن دیده نمی‌شود.
- هیچ عنوان یا claim از مقاله حذف‌شده در Watchlist یا بخش کنترل وضعیت داوری افشا نشده است.
- تمام اعداد، تاریخ‌ها و benchmark qualifierهای تکرارشونده با Evidence Card یکسان‌اند.
- Social Candidates، Signals، Deep Dives، Benchmark Claims و Telegram Handoff همان peer-review gate را رعایت می‌کنند.
- نسخه peer-reviewed بر نسخه preprint همان مطالعه ترجیح داده شده است.
- Software/database/dataset/infrastructure events به‌اشتباه به peer-review gate مقاله‌ها محدود نشده‌اند.
- duplicateهای cross-run فقط در صورت وجود state معتبر suppress شده‌اند.
- material update به‌اشتباه به‌عنوان duplicate حذف نشده است.
- هیچ minimum quota باعث ورود filler نشده است.
- author-reported، clinical، causal و AI-capability limitations در کوتاه‌سازی از بین نرفته‌اند.
