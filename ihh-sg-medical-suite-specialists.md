# IHH Singapore 医療スイート（分譲クリニック棟）入居専門医の実態調査 — 年齢・専門領域・専門医グループ所属

**作成日**: 2026年10月8日
**位置づけ**: IHH Singapore戦略シリーズ（parkwayshenton-divestment-strategy.md、sg-specialist-group-typology.md、ihh-mitsui-specialist-network-acquisition.md）の姉妹文書。前文書が「IHH SGは約1,500〜1,800人の認定独立専門医を擁する」と二次情報で記述していた部分を、IHH SG 4病院の公式「Find a Doctor」ディレクトリに掲載された全専門医プロファイル（1,295人）を悉皆収集して一次データで裏付け、年齢（卒業年からの推計）・専門領域・診療所所在ビル・専門医グループ所属の4軸で集計した。
**表記ルール**: 【確認】＝出典で裏付けた事実、【推定】＝本書がデータから推計した事項、【分析】＝本書の解釈、【未確認】＝公開情報で確認できなかった事項。出典は「A＝原文を取得して本文確認」「B＝検索エンジン経由で要旨のみ確認（原文サイトがネットワーク制限で取得不可）」に区分し巻末に記載。
**データファイル**: `data/ihh-sg-specialists-directory-2026-10.csv`（1,295人×26項目）、`data/ihh-sg-specialists-summary-2026-10.json`（集計値）、`data/sg-specialist-group-doctor-lists-2026-10.json`（主要グループ35社の公開医師名簿1,183名）、`data/scripts/`（収集・集計スクリプト）。

---

## 調査手順（Step-by-Step）

1. **母数の定義**: 「メディカルスイートに入居する専門医約1,800名」の出所を確認した。IHH自身の公表値は2系統あり、Mount Elizabethサイトの「IHH in Numbers」が **1,800+ Medical / Surgical Specialists**、IHH Healthcare Singaporeの会社概要が **1,500+ Accredited Specialists** である【確認・A】。
2. **一次データの収集**: Mount Elizabeth（Orchard・Novenaの2病院を1サイトで掲載）、Gleneagles、Parkway Eastの3公式サイトの専門医ディレクトリを、頭文字×診療科×性別×病院×氏名トークンで検索結果が10件以下になるまで分割し、全プロファイルURLを列挙した（各頭文字の件数と収集数が全て一致、取りこぼしゼロ）。病院別の認定数はMount Elizabeth（Orchard）689、Mount Elizabeth Novena 580、Gleneagles 485、Parkway East 195で、重複を除いた固有の医師は **1,295人**【確認・A】。
3. **プロファイルの取得**: 1,295人のプロファイルページを取得し（1,289人成功、6人はサイト側エラー）、専門領域・性別・使用言語・保険パネル・経歴文・資格取得年・診療所名と住所を構造化した。
4. **年齢の推計**: 資格欄の基礎医学学位（MBBS等）取得年、経歴文中の卒業年、「臨床経験N年超」の記述の順に採用し、医学部卒業年を特定できた651人（50%）について「卒後年数」を算出。年齢は卒業時25歳の仮定で帯域化した（§3に限界を明記）。
5. **診療所所在ビルの判定**: 住所から、Mount Elizabeth Medical Centre（3 Mount Elizabeth）、Mount Elizabeth Novena Specialist Centre（38 Irrawaddy Rd）、Gleneagles Medical Centre（6 Napier Rd）、Gleneagles Hospital Annexe（6A Napier Rd）、Parkway East Medical Centre（319 Joo Chiat Pl）と、IHH外のParagon・Royal Square・Lucky Plaza等を判別した。
6. **グループ所属の判定**: (a) 診療所名のブランド照合（Foundation Healthcare傘下27ブランド、Tamarind、HMI、SMG、OUE/Healthway/Nobel/O2、Icon、gutCARE、HC Surgical等）と、(b) 主要グループ公式サイトの医師名簿（35社・1,183名を別途収集）との氏名照合（3トークン以上一致）の和集合で判定した。
7. **外部ベンチマーク**: SMC（Singapore Medical Council）Annual Report 2025の「専門科別・民間部門専門医数」（2025年12月末、民間2,426人）と照合し、IHH認定医のシンガポール民間専門医に占める比率（浸透率）を算出した【確認・A】。

---

## ① Executive Summary

1. **「約1,800名」は固有の医師数ではなく、病院単位の認定（accreditation）の延べ数に近い**【分析】。公式ディレクトリで固有の専門医は1,295人、4病院の認定延べ数は1,949件（MEH 689＋MNH 580＋GEH 485＋PEH 195）であり、IHHが公表する「1,800+」はこの延べ数に、「1,500+」は固有数（ディレクトリ非掲載の認定医を含む）に対応すると解釈するのが整合的である。67%（871人）は1病院のみの認定で、4病院全てに認定された医師は38人（3%）にとどまる。
2. **IHHの認定専門医は、シンガポール民間専門医（SMC登録2,426人、2025年末）の実に半分以上を占め、外科系では7〜9割に達する**【確認／推定】。消化器内科93%、整形外科89%、心臓胸部外科90%、手外科90%、脳神経外科96%、腫瘍内科84%、泌尿器77%、ENT 76%、一般外科72%、循環器72%、眼科70%。一方、産婦人科39%、小児科26%、麻酔科23%、精神科22%、画像診断26%は低く、これらの科は他病院（Thomson、Mount Alvernia、Raffles）や病院外で完結する科である。
3. **専門領域は外科系に偏る**【確認】。上位は一般外科147、整形外科144、眼科98、産婦人科95、循環器79、消化器68、ENT 65、麻酔科50、腫瘍内科48、小児科46、泌尿器43。歯科専門医（口腔外科・補綴・矯正等）も50人含まれる。女性は26%（330人）で、整形外科2%・脳神経外科0%・循環器8%に対し、産婦人科59%・皮膚科57%・小児科57%・眼科41%と科で二極化している。
4. **年齢構成は「卒後15〜34年（推定40代〜50代）」が7割の中核で、卒後35年超（推定60代以上）が26%、卒後15年未満が3%しかいない**【推定】。卒業年が判明した651人の中央値は卒後27年（推定52歳）。病院別ではMount Elizabeth Orchardが最も高齢（中央値28年、卒後35年超が28%）、Novena・Parkway East・Gleneaglesは中央値25〜26年。グループ所属医（中央値25年）は独立開業医（27.5年）より若い。**今後10年で約4分の1が引退年齢に達する一方、若手の流入が細い**ことが、スイートの世代交代とグループ化（持分の受け皿）を同時に進める構造要因である。
5. **診療所の93%はIHHキャンパス内の分譲／賃貸メディカルスイートにある**【確認】。Mount Elizabeth Medical Centre（232戸の分譲ユニット）に653人、Mount Elizabeth Novena Specialist Centre（250戸超の医師スイート）に468人、Gleneagles Medical Centreに352人、Parkway East Medical Centreに178人、Gleneagles Annexeに120人が診療所を置き、複数キャンパスに診療所を持つ医師が392人（30%）いる。IHH外のビル（Paragon 64人、Royal Square 22人、Lucky Plaza 13人等）だけで診療する認定医は88人（7%）にすぎない。
6. **企業型・PE系の専門医グループに属する医師は306人（24%）で、独立開業医が依然4分の3を占める**【推定】。最大はFoundation Healthcare 89人（SGX上場、傘下27ブランド）、Tamarind Health 45人（Parkway Cancer Centre/TalkMed・OncoCare・Solis）、HMI Medical 30人（Eagle Eye・Advanced Urology・Harley Street）、OUE Healthcare系25人（Nobel・O2・Urohealth）、SMG 13人、HC Surgical 13人、Orthopaedics International 12人、Eye & Retina Surgeons 12人、Icon 10人、Specialist Dental Group 10人、gutCARE 8人。グループ化率は科で大差があり、**腫瘍内科90%、泌尿器47%、眼科39%、循環器37%、整形外科27%、一般外科22%、消化器22%、産婦人科9%、皮膚科・形成外科・精神科・画像診断0%**である。
7. **ただし「独立」医師の約半数は同名の共同診療所（グループ診療）に属する**【推定】。単独診療所のみの医師は575人（44%）、3人以上の同名診療所に属する医師は559人（43%）、5人以上は390人（30%）。企業資本の入っていない5人以上の大型診療グループとして、Asian Heart & Vascular Centre（10人）、Synergy Orthopaedic（9）、Kinder Clinic（8）、Island Orthopaedic（7）、Fem Surgery（7）、Anaesthesia Unlimited（7）、Ascent ENT（6）、SportsIN（6）、The Gastroenterology Group（5）、Ten Surgery Group（5）等が確認でき、これらが次のグループ化・買収の候補群である。
8. **保険パネル接続率はPrudentialが73%で突出し、他社は40〜50%**【確認】。Prudential 941人、HSBC Life 652、Singlife 635、Great Eastern 597、Income 554、AIA 523。また氏名照合で249人（19%）がThomson Medical Centreの専門医ディレクトリにも掲載されており、IHH認定医の2割はThomsonと兼任する。
9. **IHHへの含意**【分析】: (a) 「1,800名」の囲い込み効果は、実態としては1,295人の固有医師、うち1病院のみ認定の871人に依存する。(b) 外科系民間専門医の7〜9割を既に認定しているため、新規獲得余地は小さく、争点は**既存認定医の世代交代（卒後35年超の26%）とグループ化（残り76%）の受け皿を誰が持つか**に移っている。(c) グループ化が進んだ科（腫瘍内科・眼科・泌尿器・循環器）はTamarind・HMI・Foundationが既に押さえており、未グループ化で大型の独立診療グループが残る科（整形外科・一般外科・消化器・産婦人科・ENT・麻酔科）が、姉妹文書で推奨した専門医JV／マイノリティ出資の現実的な対象である。

---

## ② 母数の確定：「約1,800名」の正体

| 指標 | 値 | 出典・備考 |
|---|---|---|
| IHH公表「Medical / Surgical Specialists」 | **1,800+** | Mount Elizabeth公式「IHH in Numbers」（看護師2,150+、コメディカル332、認可病床1,000+、手術室45、内視鏡室25と併記）【A】 |
| IHH公表「Accredited Specialists」 | **1,500+** | IHH Healthcare Singapore会社概要（4病院・793稼働病床・プライマリケア30+拠点・従業員5,000+と併記）【A】 |
| IHH 2024年次報告 | over 1,500 clinical specialists | 【B】 |
| 公式ディレクトリ掲載の固有専門医 | **1,295人** | 本調査（2026年10月8日時点）。1,289人はプロファイル取得、6人はページエラー【A】 |
| 病院別認定数（延べ） | MEH 689 / MNH 580 / GEH 485 / PEH 195 ＝ **1,949** | 同上。Mount Elizabethサイト全体で1,048人、うちOrchard・Novena両方認定221人 |
| 認定病院数の分布 | 1病院 871人（67%）／2病院 232人（18%）／3病院 154人（12%）／4病院 38人（3%） | 同上 |
| 性別 | 男性959人（74%）／女性330人（26%） | 同上 |

**解釈**【分析】: 「1,800+」は病院別認定の延べ数（1,949）に、「1,500+」は固有数（ディレクトリ非掲載の認定医、例えば病院雇用の救急医・麻酔医・病理医等を含む）に対応する。本調査の1,295人は「患者向けに公開され、スイートで外来を持つ認定専門医」の母集団として最も実態に近い。なお本文書の分析単位は、ユーザー前提の「約1,800名」ではなく、この1,295人である。

---

## ③ 医療スイート（分譲クリニック棟）の概要と入居分布

### 3-1. IHH SG 4キャンパスのメディカルスイート

| ビル | 所在地 | 戸数・形態 | 出典 |
|---|---|---|---|
| Mount Elizabeth Medical Centre（MEMC） | 3 Mount Elizabeth | 17階建、医療センター＋商業区画で**分譲（strata）232ユニット**。SMC認定専門医のみが診療可能な「private medical specialists only」の建物 | memc.com.sg【B】、Wikipedia【A】 |
| Mount Elizabeth Novena Specialist Centre | 38 Irrawaddy Road | 病院併設で**250超の専門医スイート**（公式）。開発時計画は259スイート、2010年前後の第1期分譲100戸は2週間で完売、452〜1,431平方フィート、S$3,588〜3,828 psf | Mount Elizabeth公式【A】、The Edge【B】 |
| Gleneagles Medical Centre | 6 Napier Road | 分譲（freehold strata）スイート。2026年の売り出し例は603平方フィートでS$9.08百万（約S$15,000 psf） | 不動産仲介サイト【B】 |
| Gleneagles Hospital Annexe | 6A Napier Road | 病院付属棟（賃貸）。本調査では120人が診療所を置く | 本調査【A】 |
| Parkway East Medical Centre | 319 Joo Chiat Place | 病院併設の医療センター。本調査では178人が診療所を置く | 本調査【A】 |

### 3-2. 1,295人の診療所所在ビル（複数拠点は重複計上）

| ビル | 診療所を置く医師数 | 1,295人に占める比率 |
|---|---|---|
| Mount Elizabeth Medical Centre | 653 | 50% |
| Mount Elizabeth Novena Specialist Centre | 468 | 36% |
| Gleneagles Medical Centre | 352 | 27% |
| Parkway East Medical Centre | 178 | 14% |
| Gleneagles Hospital Annexe | 120 | 9% |
| （IHH外）Paragon Medical | 64 | 5% |
| （IHH外）Royal Square at Novena | 22 | 2% |
| （IHH外）Parkway MediCentre（IHHのコミュニティ外来） | 16 | 1% |
| （IHH外）Lucky Plaza | 13 | 1% |
| （IHH外）Novena Medical Center／Novena Specialist Center／Camden等 | 13 | 1% |

- **IHHキャンパス内に少なくとも1診療所を持つ医師は1,207人（93%）**、IHH外のみは88人（7%、Paragon 49人が中心）【確認】。
- **キャンパス数**: 1キャンパス813人（63%）、2キャンパス245人（19%）、3キャンパス119人（9%）、4キャンパス28人（2%）。診療所数は1か所847人、2か所251人、3か所135人、4か所以上56人【確認】。
- **含意**【分析】: 前文書の「スイートに入居する専門医は隣の病院に入院させるのがデフォルト」という構造は定量的に裏付けられる。一方で、認定医の37%が複数キャンパスに診療所を持ち、19%がThomsonにも掲載される（§5-4）ことから、個々の医師の症例は単一病院に固定されていない。

---

## ④ 年齢構成（卒業年からの推計）

### 4-1. 方法と限界

- プロファイルの「Fellowship and accreditation」欄に年付きで記載された基礎医学学位（MBBS、MB BCh、MD等）の取得年を第一優先（233人）、経歴文中の「graduated from NUS in 1998」等の記述を第二優先（262人）、「more than 20 years of experience」等の年数記述を第三優先（147人、下限値のため若年側に偏る）、その他9人とし、**651人（50%）で卒業年を特定**した【推定】。残り644人は資格欄に年の記載がない。
- 年齢換算は「卒業時25歳」を仮定（NUS医学部5年制、男性は兵役により27歳前後の卒業が多いため、男性74%の母集団では**実年齢は推計より1〜2歳高い**方向に偏る）。SMC年次報告は年齢分布を公表していないため、公的ベンチマークとの突合はできない【未確認】。

### 4-2. 分布

| 卒後年数 | 推定年齢帯 | 人数 | 比率（n=651） |
|---|---|---|---|
| 15年未満 | 〜39歳 | 18 | 3% |
| 15〜24年 | 40〜49歳 | 242 | 37% |
| 25〜34年 | 50〜59歳 | 219 | 34% |
| 35〜44年 | 60〜69歳 | 127 | 20% |
| 45年以上 | 70歳以上 | 45 | 7% |

- 中央値は卒後27年（推定52歳）、平均28.5年、四分位は20〜35年。医学部卒業年の分布は1970年代31人、80年代98人、90年代197人、2000年代244人、2010年代73人【推定】。
- **病院別**: Mount Elizabeth Orchard 中央値28年（卒後35年超28%）、Gleneagles 26年（22%）、Novena 25年（18%）、Parkway East 25年（20%）。ビル別でもMEMC 27年、Novena Specialist Centre 26年、Gleneagles Medical Centre 25年、Parkway East Medical Centre 25年【推定】。
- **科別中央値（n≥20）**: 麻酔科33年、内分泌32年、泌尿器30年、循環器29年、ENT 29年、小児科29年、消化器28年、一般外科26年、腫瘍内科26年、脳神経外科26年、産婦人科25.5年、整形外科25年、眼科25年、皮膚科25年、形成外科23年【推定】。
- **グループ所属と年齢**: グループ所属医の中央値25年に対し、独立開業医は27.5年。若い世代ほどグループに属して開業する傾向が読み取れる【推定】。

### 4-3. 含意【分析】

卒後35年超（推定60代以上）が26%、卒後15年未満（40歳未満）が3%という形は、**上が厚く下が極端に細い**構造である。民間専門医の新規登録は年間35人（2025年、SMC）にすぎず、公的部門からの移籍（卒後15〜25年）が供給の主経路であるため、今後10年で引退する約4分の1のスイートと症例を誰が引き継ぐかが、IHH・グループ・不動産（分譲スイートの流通）の三者にとって共通の論点になる。

---

## ⑤ 専門領域の分布とシンガポール民間専門医に占める比率

### 5-1. 科別人数と浸透率

浸透率＝IHH認定医数÷SMC登録の民間専門医数（2025年12月末、第1専門科ベース）。IHH側には歯科専門医（SMC非管轄）と複数科登録が含まれるため、100%近傍の値は上振れを含む。

| 専門科 | IHH認定医 | 女性比率 | SG民間専門医（SMC 2025） | 浸透率 | グループ所属（人・比率） |
|---|---|---|---|---|---|
| 一般外科 | 147 | 20% | 204 | 72% | 33（22%） |
| 整形外科 | 144 | 2% | 161 | 89% | 39（27%） |
| 眼科 | 98 | 41% | 140 | 70% | 38（39%） |
| 産婦人科 | 95 | 59% | 241 | 39% | 9（9%） |
| 循環器 | 79 | 8% | 110 | 72% | 29（37%） |
| 消化器 | 68 | 13% | 73 | 93% | 15（22%） |
| ENT | 65 | 17% | 86 | 76% | 18（28%） |
| 麻酔科 | 50 | 38% | 222 | 23% | 6（12%） |
| 腫瘍内科 | 48 | 38% | 57 | 84% | 43（90%） |
| 小児科 | 46 | 57% | 177 | 26% | 3（7%） |
| 泌尿器 | 43 | 12% | 56 | 77% | 20（47%） |
| 皮膚科 | 37 | 57% | 82 | 45% | 0 |
| 集中治療 | 33 | 12% | （副専門科） | — | 6 |
| 形成外科 | 32 | 31% | 49 | 65% | 0 |
| 画像診断 | 31 | 26% | 121 | 26% | 0（26人はIHH放射線科部門） |
| 内分泌 | 25 | 28% | 36 | 69% | 2 |
| 口腔外科 | 23 | 22% | （歯科） | — | 7 |
| 脳神経外科 | 23 | 0% | 24 | 96% | 3 |
| 精神科 | 22 | 32% | 99 | 22% | 0 |
| 呼吸器 | 21 | 29% | 36 | 58% | 4 |
| 腎臓 | 20 | 15% | 36 | 56% | 0 |
| 心臓胸部外科 | 19 | — | 21 | 90% | 1 |
| 神経内科 | 19 | — | 31 | 61% | 1 |
| 手外科 | 18 | — | 20 | 90% | 7 |
| リウマチ | 13 | — | 19 | 68% | 0 |
| 血液 | 12 | — | 19 | 63% | 5 |
| 感染症 | 10 | — | 19 | 53% | 0 |
| 放射線腫瘍 | 9 | — | 22 | 41% | 4 |
| 歯科（補綴7・矯正7・歯内5・小児歯科4・歯周2・公衆歯科2） | 27 | — | — | — | 10（Specialist Dental Group） |
| その他（小児外科4・内科4・核医学3・老年2・スポーツ2・リハ1・病理1・緩和1） | 18 | — | — | — | — |
| **合計** | **1,295** | **26%** | **2,426** | **（医科のみ約51%）** | **306（24%）** |

### 5-2. 含意【分析】

- **IHHは外科・インターベンション系の民間専門医をほぼ独占的に認定している**（脳外96%、消化器93%、心臓胸部外科90%、手外科90%、整形89%、腫瘍内科84%）。ここでの競争は「新規認定の獲得」ではなく、認定医の症例をどの施設に置くか（病院 vs 自前ASC）の争いである。
- **浸透率が低い科（産婦人科39%、小児科26%、麻酔科23%、精神科22%、画像診断26%）**は、Thomson・Mount Alvernia（産科・小児）や病院外診療（精神科・皮膚科）で完結する科であり、IHHの病院型モデルの外側にある。
- 前文書（sg-specialist-group-typology.md）の「病院外シフト圧力が強い科＝消化器内視鏡・眼科・日帰り外科・皮膚科」のうち、消化器（93%）と眼科（70%）はIHHの認定医が大半を占めるため、これらの科の自前ASC化はIHH施設収入への直接の圧力になる。

---

## ⑥ 専門医グループへの所属

### 6-1. 判定方法

- **診療所名によるブランド照合**【確認】: プロファイルに記載された診療所名を、各グループの公式ブランド一覧（Foundation傘下のPanAsia Surgery・Pinnacle Orthopaedic・Lang Eye・Colorectal Clinic Associates・Nexus Surgical・Hand Surgery Holdings・Orchard Surgery Center・Orthopaedic Associates Medical Group等27ブランド、Tamarind傘下のParkway Cancer Centre・OncoCare・Solis、HMI傘下のEagle Eye・Advanced Urology・Harley Street、OUE系のNobel・O2・Urohealth、Icon、gutCARE、HC Surgical傘下16診療所、SMG傘下18ブランド等）と照合。
- **氏名照合**【推定】: 35グループの公式サイトから収集した医師名簿1,183名と、3トークン以上の氏名一致で照合（Foundationは名簿112名のうち上場目論見書の108名と整合）。Thomson Medical（614名、受入専門医の名簿）とRaffles（255名）は「グループ所属」ではなく「他院ディレクトリにも掲載」として別集計した。
- **未判定の限界**【未確認】: Novena Heart Centre（Tamarind）、Advanced Urology（HMI）、StarMed、SOG、O2 Healthcare、Orthopaedics International、Asian Healthcare Specialists等は公式サイトがネットワーク制限で取得できず、診療所名照合のみで判定した。したがって所属率24%は下限値である。

### 6-2. グループ別の所属医師数（1,295人中）

| グループ（資本） | 所属医師数 | 主な科 | 主なブランド・備考 |
|---|---|---|---|
| **Foundation Healthcare**（SGX上場2026年7月、SeaTown/Temasek系） | **89** | 一般外科21、整形13、循環器11、ENT 8、手外科6、口腔外科6 | PanAsia Surgery、Pinnacle Orthopaedic、Lang Eye、Colorectal Clinic Associates、Nexus Surgical、Orthopaedic Associates、Winston Tan OMS等。公式名簿112人のうち73人（65%）がIHH認定医 |
| **Tamarind Health**（Templewater＋65 Equity Partners） | **45** | 腫瘍内科26、循環器6、一般外科5、血液4 | Parkway Cancer Centre/TalkMed（15）、OncoCare（16＋女性がんクリニック4）、Solis Breast Care（5）。Novena Heart Centreは名簿未取得のため過小 |
| **HMI Medical**（EQT＋Apollo） | **30** | 眼科16、泌尿器8、循環器4 | Eagle Eye Centre（17）、Advanced Urology Associates（8）、Harley Street Heart & Vascular（5） |
| **OUE Healthcare／Healthway**（OUE） | **25** | 呼吸器・ENT・泌尿器・循環器 | O2 Lung Centre／The Respiratory Practice（9）、Nobel ENT/Heart/Paediatric Surgery、Urohealth |
| **Singapore Medical Group**（CHA Healthcare） | 13 | 産婦人科5、眼科2、腫瘍2 | Astra Women's Specialists、The Cancer Centre、LSC Eye等。SMG名簿53人の多くはIHH外の拠点で診療 |
| **HC Surgical Specialists**（Catalist） | 13 | 一般外科・大腸・整形 | 医師名を冠した子会社診療所（Lai Endoscopy、Heah Colorectal、LS Lee Surgery等） |
| Orthopaedics International | 12 | 整形外科 | 独立系の整形外科グループ |
| Eye & Retina Surgeons | 12 | 眼科 | Camden・Novena拠点の眼科グループ |
| **Icon Group**（EQT） | 10 | 腫瘍内科10 | Icon Cancer Centre Mount Elizabeth／Gleneagles／Novena／Orchard |
| Specialist Dental Group | 10 | 歯科 | MEMC・Gleneagles Medical Centre |
| gutCARE | 8 | 消化器8 | 全8人がIHH認定医 |
| Doctor Anywhere／Asian Healthcare Specialists | 8 | 整形・泌尿器 | 旧AHS（整形外科・泌尿器） |
| Curie Oncology | 7 | 腫瘍内科 | Gleneagles・Novena |
| Beyond Medical Group、Fullerton Health（The ENT Clinic）、Alfa Medicus（ICG） | 各5 | — | — |
| ISEC（Aier）、Cardiac Care Partners、Singapore Paincare、Royal Healthcare（Sojitz）、AARO | 1〜4 | — | — |
| **企業型グループ所属 合計** | **306（24%）** | | |
| （参考）IHH病院部門（放射線科26人等） | 31 | 画像診断 | 独立開業医ではなくIHH雇用・部門契約 |
| （参考）Parkway MediCentreでも診療 | 16 | — | IHHのコミュニティ外来を第2拠点とする独立医 |

- **病院別の所属率**: Mount Elizabeth Novena 39%（225/580）、Parkway East 41%（79/195）、Gleneagles 32%（157/485）、Mount Elizabeth Orchard 30%（207/689）。新しいキャンパスほどグループ所属率が高い【推定】。
- **科別の所属率**（§5-1表）: 腫瘍内科90%（Tamarind・Icon・Curie・OncoCareでほぼ全員）、泌尿器47%、眼科39%、循環器37%、ENT 28%、整形27%、一般外科22%、消化器22%、産婦人科9%、皮膚科・形成外科・精神科・画像診断・腎臓0%。

### 6-3. 「独立」医師の内訳：共同診療所（グループ診療）の規模

診療所名を正規化して同名診療所に属する医師を数えると、企業資本の有無とは別に「グループ診療」の実態が見える【推定】。

| 診療形態 | 医師数 | 比率 |
|---|---|---|
| 単独診療所のみ（同名診療所に他の医師がいない） | 575 | 44% |
| 3人以上の同名診療所に所属 | 559 | 43% |
| うち5人以上 | 390 | 30% |

企業資本の入っていない5人以上の診療グループ（延べ人数）: Asian Heart & Vascular Centre 10、Synergy Orthopaedic Group 9、Kinder Clinic 8、Island Orthopaedic 7、Fem Surgery 7、Anaesthesia Unlimited 7、Eye Surgeons 7、The Dermatology Practice 7、Ascent ENT 6、SportsIN Orthopaedic 6、Specialist Anaesthesia Services 6、International Eye Cataract Retina Centre 5、OrthoSports 5、Respiratory Medical Associates 5、The Gastroenterology Group 5、Singapore Eye & Vision 5、Orthopaedic and Hand Surgery Partners 5、The Children's Eye & ENT Centre 5、Ten Surgery Group 5。**これらは、姉妹文書のT1（病院テナント型コンサルトグループ）に相当し、IHHが専門医JV・マイノリティ出資の相手として検討すべき「未上場・未PE化の受け皿」である**【分析】。

### 6-4. 保険パネルとThomson兼任

| 保険者パネル | 掲載医師数 | 比率 |
|---|---|---|
| Prudential（Extended Panel含む） | 941 | 73% |
| HSBC Life | 652 | 50% |
| Singlife | 635 | 49% |
| Great Eastern | 597 | 46% |
| Income | 554 | 43% |
| AIA | 523 | 40% |

- Prudentialの突出は、同社がIHH 4病院の専門医をExtended Panelとして広く接続している制度設計による【確認】。前文書で触れた「GEによるMount Elizabeth事前承認停止」の文脈では、GEパネル46%という数字が交渉の基礎になる。
- **Thomson Medical Centreの専門医ディレクトリにも掲載される医師は249人（19%）**、Raffles 12人。IHH認定医の2割はThomsonの病床にも入院させられる立場にあり、「囲い込み」は排他的ではない【推定】。

---

## ⑦ 限界と留意点

1. **母集団**: 公式ディレクトリ掲載医のみ（1,295人）。病院雇用医（救急・麻酔の一部・病理等）や掲載を希望しない認定医は含まない。6人はプロファイル未取得。
2. **年齢**: 直接の年齢データはなく、卒業年からの推計（651人、50%）。年数記述に基づく147人は下限値で若年側に偏る。性別による卒業年齢差（兵役）で男性は1〜2歳の過小推計。
3. **グループ所属**: 公式サイトを取得できなかったグループ（Novena Heart、Advanced Urology、StarMed、SOG、O2、OI、AHS、Royal等）は診療所名のみで判定しており、所属率24%は下限。氏名照合は3トークン以上一致のため、同姓同名の誤判定はごく少数ながら排除できない。
4. **浸透率**: 分母のSMC統計は第1専門科ベース（2025年12月末）、分子のIHHディレクトリは2026年10月時点で歯科・複数科を含むため、100%近傍の科は上振れを含む。
5. **ビル判定**: 住所文字列の照合による。Gleneagles Annexe（6A）とGleneagles Medical Centre（6）は住所表記に揺れがある。

---

## ⑧ 出典

### 一次データ（本調査が取得・A）
- IHH SG公式専門医ディレクトリ: [Mount Elizabeth（Orchard・Novena）](https://www.mountelizabeth.com.sg/patient-services/specialists)、[Gleneagles](https://www.gleneagles.com.sg/patient-services/specialists)、[Parkway East](https://www.parkwayeast.com.sg/patient-services/specialists)（各医師プロファイル `/patient-services/specialists/profile/<slug>`、2026年10月8日取得）。収集方法は `data/scripts/crawl_list.py`、`crawl_profiles.py`、集計は `analyze.py`、ビル・ブランド対応表は `maps.py`。
- IHH公表値: [IHH Healthcare Singapore — 会社概要（1,500+ Accredited Specialists、793稼働病床、4病院、30+プライマリケア）](https://www.ihhhealthcare.com/our-reach/singapore)、[Mount Elizabeth「IHH in Numbers」（1800+ Medical / Surgical Specialists、2150+ Nurses、332 AHP、45手術室、25内視鏡室）](https://www.mountelizabeth.com.sg/aoe/)。
- メディカルスイート: [Mount Elizabeth Novena Hospital（「more than 250 specialist physician suites」）](https://www.mountelizabeth.com.sg/why-choose-us/mount-elizabeth-novena-hospital)、[Mount Elizabeth Hospital（278床）](https://www.mountelizabeth.com.sg/why-choose-us/mount-elizabeth-hospital)、[Gleneagles Hospital（221床）](https://www.gleneagles.com.sg/why-choose-us)、[Wikipedia: Mount Elizabeth Hospital（MEMCは民間専門医のみ、SMC認定専門医に限る、31専門科）](https://en.wikipedia.org/wiki/Mount_Elizabeth_Hospital)。
- SMC: [Singapore Medical Council Annual Report 2025（go.gov.sg/smc-annual-report-2025）](https://file.go.gov.sg/smc-annual-report-2025.pdf) — 2025年12月末の専門医7,634人、民間2,426人（32.3%）、Table 3-2 専門科別・部門別人数、新規専門医登録479人（民間35人）。[SMC年次報告一覧](https://www.healthprofessionals.gov.sg/smc/publications-newsroom/smc-annual-reports)。
- 専門医グループ公式名簿（`data/sg-specialist-group-doctor-lists-2026-10.json`）: [Foundation Healthcare](https://www.foundationhealthcare.sg/specialists/)、[SMG](https://smg.sg/specialists-and-partners/)、[OncoCare](https://oncocare.sg/specialists/)、[Tamarind Health拠点一覧](https://tamarindhealth.com/our-network/our-centres/)、[Eagle Eye Centre](https://eagleeyecentre.com.sg/doctors/)、[Harley Street Heart](https://www.harleystreet.sg/heart/)、[Icon Cancer Centre Singapore](https://iconcancercentre.sg/doctors/)、[gutCARE](https://www.gutcare.com.sg/doctors/)、[HC Surgical Specialists](https://www.hcsurgicalspecialists.com/en/our-specialist-surgeons-and-general-practitioners/specialist-surgeons)、[Beyond Medical Group](https://beyondmedical.com.sg/our-doctors/)、[Curie Oncology](https://curieoncology.com.sg/our-team/)、[PanAsia Surgery](https://www.panasiasurg.com/our-doctors-and-general-surgeons-in-singapore/)、[Cardiac Care Partners](https://www.cardiaccarepartners.com/our-doctors/)、[Alfa Medicus](https://www.alfamedicus.com/care/)、[Thomson Medical（サイトマップ経由）](https://www.thomsonmedical.com/find-an-expert)、[Raffles Medical Group](https://www.rafflesmedicalgroup.com/doctor/)、[AARO](https://aaro.sg/)。

### 二次情報（検索エンジン経由で要旨確認・B）
- [Mount Elizabeth Medical Centre「Our History」（17階建、分譲232ユニット）](https://www.memc.com.sg/our-history/)
- [The Edge Malaysia「Corporate: Hot demand for medical suites in Novena」（259スイート計画、第1期100戸が2週間で完売、452〜1,431 sq ft、S$3,588〜3,828 psf）](https://theedgemalaysia.com/article/corporate-hot-demand-medical-suites-novena)
- [Gleneagles Medical Centre分譲スイート売り出し（603 sq ft、S$9.08百万、freehold strata）](https://www.commercialguru.com.sg/listing/for-sale-gleneagles-hospital-500194414)
- [IHH Annual Report 2024（Singapore: over 1,500 clinical specialists）](https://www.insage.com.my/interactiveAR/IHH/interactiveAR2024/41/)
- Parkway Pantai求人票（4病院に入院させられる認定専門医1,400人超、年次不明）: [JobStreet](https://id.jobstreet.com/id/companies/parkway-pantai-168554722228304)

### 本シリーズの姉妹文書
- `parkwayshenton-divestment-strategy.md`（第5章「約1,500人の認定独立専門医」の記述を本書で更新）
- `sg-specialist-group-typology.md`（T0〜T5類型、Frost & Sullivanの主要グループ5社）
- `ihh-mitsui-specialist-network-acquisition.md`
