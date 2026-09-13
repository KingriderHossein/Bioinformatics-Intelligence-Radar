# Newsroom Engine

Protocol component: Radar 3.0+

Use this reference after an eligible Evidence Card exists and before user-visible writing or Telegram handoff construction.

The Newsroom Engine converts verified events into stories. It does not change scientific eligibility, claim strength, publication status, or evidence quality. Evidence is a gate; newsroom judgment decides whether an eligible item is worth the reader's attention and how to frame it.

## Product principle

Radar is not a paper digest.

Its job is to:

1. find what changed;
2. verify what is true;
3. decide what deserves attention;
4. find the strongest evidence-safe story angle;
5. write the news in clear Persian.

An eligible paper, release, dataset, or service update is not automatically a story.

## Design provenance

The newsroom model was informed by a qualitative review of technology/science/health publishing patterns across Digiato, Zoomit, Peivast, Euronews Persian, Interesting Engineering, ScienceAlert, Science in Telegram, and Gadget News.

Use those publications only as evidence sources for abstract editorial behaviors. Do not imitate the distinctive style of any publication or create a publication-named style profile.

The retained cross-publication behaviors are:

- result-first or consequence-first leads;
- short paragraphs;
- a concrete number only when it clarifies scale or consequence;
- rapid explanation of why the event matters;
- limited prerequisite explanation;
- visible but concise uncertainty;
- clear attribution for risky claims;
- separation between a short channel brief and a longer article treatment;
- editorial selection rather than exhaustive publication listing.

Reject clickbait, unsupported causal framing, exaggerated AI capability, miracle/cure language, and novelty inflation even when they are common engagement tactics elsewhere.

## Story gate

For each final Evidence Card, write an internal one-sentence `news_statement_fa`:

`چه چیزی تغییر کرده یا کشف شده + چرا امروز برای مخاطب BioInsight مهم است`

The item passes the Story Gate only if this sentence is both evidence-safe and meaningful without relying on the journal name, paper title, or generic words such as «جدید»، «نوآورانه»، or «مهم».

Strong story triggers include one or more of:

- a workflow can materially change;
- a common assumption is challenged;
- a new capability becomes practically available;
- a meaningful limitation or failure mode is revealed;
- a large or unusually reusable dataset/resource becomes available;
- an independent validation changes confidence;
- a correction, retraction, security issue, migration, or deprecation matters;
- a result has a clear scientific, technical, translational, or community consequence;
- an unexpected contrast, trade-off, or negative result changes interpretation.

Weak story signals by themselves:

- publication in a prestigious journal;
- a fashionable AI label;
- large parameter count;
- repository stars;
- a high benchmark number without consequence;
- incremental method variation without workflow or conceptual impact;
- a routine paper that is merely recent.

If no defensible story angle exists, omit the item from normal newsroom output even if it is scientifically valid.

## News Value Score /30

Score only items that already passed scientific eligibility.

Rate each dimension 0-5:

1. `impact` — does something meaningfully change?
2. `audience_relevance` — does it matter to BioInsight/bioinformatics readers?
3. `novelty` — is the event genuinely new, surprising, or assumption-changing?
4. `consequence` — is there a clear practical/scientific implication?
5. `storyability` — can the core news be explained clearly without distorting it?
6. `timeliness` — why does this deserve attention now?

Evidence quality is **not** a News Value dimension. Evidence already determines eligibility and wording boundaries.

Default interpretation:

- 25-30: lead-story candidate
- 21-24: strong follow-up story
- 17-20: newsroom watch / include only if the day is quiet or the domain is strategically important
- <17: normally omit from visible daily coverage

A CRITICAL operational alert may bypass the numerical threshold because urgency itself is the story.

Do not lower the threshold just to fill the report.

## Angle generation

Before writing, generate at least three materially different internal angles when the story supports them. Choose the angle that maximizes reader relevance while preserving the Evidence Card.

Preferred angle types:

- `RESULT` — what was found or released?
- `TENSION` — what assumption, trade-off, or apparent contradiction makes the story interesting?
- `CONSEQUENCE` — what changes for researchers, workflows, interpretation, or downstream use?
- `WORKFLOW_IMPACT` — what should a practitioner check or do now?
- `SCALE` — does an unusual dataset/sample/compute scale materially change what is possible?
- `LIMITATION` — did the work expose where a popular method fails?
- `EXPLAINER` — is one concept required before the result becomes meaningful?

Do not choose an angle merely because it sounds dramatic.

## Story Card

Derive one internal Story Card from the Evidence Card for each selected newsroom item.

Recommended fields:

- `story_id`
- `evidence_card_id`
- `news_statement_fa`
- `news_value_score`
- `angle_candidates`
- `selected_angle_type`
- `selected_angle_fa`
- `headline_options_fa`: 2-4 materially different evidence-safe options
- `selected_headline_fa`
- `lead_fa`
- `essential_facts`: only facts needed to understand the story
- `why_it_matters_fa`
- `visible_boundary_fa`: the most important limitation or non-conclusion
- `source_line`
- `recommended_formats`
- `article_worthy`: true/false
- `telegram_worthy`: true/false
- `visual_worthy`: true/false
- `overhype_risk`
- `do_not_say_fa`

Do not copy the full Evidence Card into the Story Card. Keep only what the reader needs.

## Headline rules

Prefer headlines built around result, consequence, tension, or a precise question.

Good headline behavior:

- foreground the news, not the framework name;
- use a number only when the number itself makes the story concrete;
- avoid starting with jargon if plain language can carry the meaning;
- preserve association/causality and prediction/measurement boundaries;
- make the reader curious without withholding the actual news.

Avoid:

- «مقاله جدیدی نشان داد...» as a default headline;
- empty novelty words such as «انقلابی»، «شگفت‌انگیز»، «بی‌سابقه»;
- universal claims from narrow benchmarks;
- personifying AI as understanding, discovering, deciding, or proving unless the evidence supports that interpretation;
- causal verbs for observational evidence;
- clinical wording for research-only results.

## Lead rules

The first 1-2 sentences should answer most of these immediately:

- what happened?
- what is the surprising or useful part?
- who should care?

Do not open with methodology unless the method itself is the news.

Do not start with long scene-setting, publication metadata, or a list of technologies.

## Narrative sequence

Default short-news sequence:

`event/result -> context needed to understand it -> key evidence -> consequence -> visible boundary`

Default article sequence:

`headline -> deck -> lead -> nut graf -> context -> what they did -> key result -> interpretation -> limitation -> what next`

The visible text should read as continuous journalism. Do not expose these labels unless they genuinely improve clarity.

## Persian newsroom style

Use natural modern Persian with technical precision.

- Keep paragraphs short, usually 1-3 sentences.
- Prefer active, direct verbs.
- Use English technical terms when translation would reduce precision.
- Explain one unfamiliar prerequisite at most before returning to the story.
- Integrate «چرا مهم است؟» into the narrative instead of mechanically labeling it in every item.
- Put the strongest caveat where a reader could otherwise overinterpret the story; do not bury it at the end.
- Use emojis sparingly and functionally in channel-ready surfaces.
- Avoid academic abstract style, excessive headings, and method-first summaries.

## Channel brief vs article

### Telegram / channel brief

Default target: roughly 100-220 Persian words depending on complexity.

The brief must be independently understandable without opening the source. It should contain the result, enough context, consequence, and the most important boundary.

Use `FLASH` only when the story is simple and low-risk. Use `STANDARD` for ordinary stories. Use `DEEP` when evidence boundaries, causality, clinical implications, AI-capability claims, or benchmark context require space.

### BioInsight article candidate

Recommend article treatment when at least one is true:

- the story needs prerequisite explanation;
- multiple evidence layers materially change interpretation;
- the finding has broader field consequences;
- benchmark/clinical/causal nuance cannot fit responsibly in a short post;
- there is a useful practical decision framework for readers.

Do not write a full article unless requested by the user or the workflow explicitly includes article production.

## Signal of the Day

A Signal is optional, not a quota.

Use a Signal only when at least two independent eligible observations support the same directional interpretation and the synthesis adds information beyond repeating the individual stories.

If no defensible signal exists, say concisely that no cross-source signal was strong enough today.

Never manufacture a trend to make the report feel complete.

## Editorial selection

At the end of newsroom selection, choose the strongest 2-5 Story Cards for downstream editorial work when available.

For each, recommend one or more of:

- Telegram
- article
- infographic/carousel
- technical explainer
- alert

Selection should reflect News Value, audience fit, and evidence-safe storyability. High overhype risk does not make a story less newsworthy; it changes how much context and caution the final treatment requires.

## Newsroom release gate

Before any visible story is released, confirm:

- the Story Card matches the Evidence Card;
- the selected angle does not change claim strength;
- the headline contains the actual news rather than only the paper/tool name;
- the lead reaches the result quickly;
- the consequence is explicit or naturally inferable;
- at least one material limitation is visible when needed;
- author-reported benchmarks remain attributed;
- high-risk AI, clinical, causal, and observational claims retain their boundaries;
- no item is included merely to increase count;
- the story would still be worth reading if the journal name were removed.
