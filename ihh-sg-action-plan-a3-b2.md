# IHH Singapore アクションプラン精緻化 — A3(専門医へのASC持分)・B2-i(入院系への特化)・B2-ii(非入院科のACC JV)

**作成日**: 2026年10月20日
**位置づけ**: ihh-sg-hypotheses-verification.md 補遺5(§16-2)・補遺6(§17-3)で評価した3つのアクションを、**IHH Healthcare(Parkway Hospitals Singapore)が主体として実行する前提**で、目的・対象・設計・手順・KPI・規制整合・リスク・未確認事項まで落とし込んだ実行計画。三井物産は資本の出し手の選択肢としてのみ言及し、主体には置かない。
**前提(ご確認いただいた4点)**: (1) B2-iiのACCは**IHHキャンパス内・隣接**に置く(IHH経済圏の外には出さない)。(2) JV相手の「グループ」は**IHH入居医で新設する医師グループ**とする(既存グループとのJVは本書の対象外)。(3) B2-iは検証文書§17-3の判定(「増やす余地は小さい」)を踏まえ、**承継主導の修正版**で設計する。(4) 成果物は本ファイル(新規)。
**表記ルール**: 検証文書と同じ。【確認】=出典原文で裏付けた事実、【算出】=一次データ(`data/ihh-sg-specialists-directory-2026-10.csv`、IHH 4病院ディレクトリ1,295人、2026年10月8日取得)または出典数値から計算した値、【推定】=出典の数値を前提に置いた概算、【未検証】=公開情報で確認できなかった事項、【分析】=確認済み事実から導いた本書の判断。出典は姉妹文書で原文確認済みのもの(A)と検索エンジン経由(B)を巻末に区分。既存レポートの引用は「(文書名 §節)」で示す。

---

## 調査手順(Step-by-Step)

1. **判定の継承**: 検証文書§16-2(A3=合理性◎・実現可能性○、B2=△→×)と§17-3(B2の修正版=○)を出発点とし、「×」とされた形(IHH経済圏の外への外出し、医師頭数を増やす採用)を採らず、「○」とされた形(IHH内ASC/ACCへの移動+承継+設備+支払者)に沿って設計した。
2. **対象母数の確定**: 一次データ(1,295人)を、(a) 日帰り手技を持つ外科系(A3の持分対象)、(b) 入院依存科の独立医で卒後35年超(B2-iの承継対象)、(c) 非入院10科(B2-iiのACC移転対象)の3つに再集計し、拠点(ビル)別・独立/グループ別・保険者接続別に分けた。
3. **設計要素の抽出**: 姉妹文書で原文確認済みの先行例(Novena Surgery、HC Surgical 51/49、Foundation 60/40・MP2、Tamarind Leaver条項、米ASCセーフハーバー、USPIの買取義務)と規制(SMC ECEG 2016 H3、HCSA ASC規則2023、CCCS 2010年決定、HCSA広告規則、Health Information法)から、各施策の標準装備と禁止事項を抽出した。
4. **手順化**: 3施策を0〜36か月の4フェーズに置き、相互依存(支払者修復が先行、ACCは持分設計とパネル接続の後)を明示した。
5. **未確認事項の明示**: 社内データ・契約・保険者の意思に依存する項目は【未検証】とし、推測で埋めなかった(§⑦)。

---

## ① 総括

### 1-1. 3施策の関係【分析】

3施策は独立した選択肢ではなく、**同じ1,295人の認定医を、症例の性質(日帰り/入院)と医師のライフサイクル(現役/引退)で振り分ける1つの設計**である。

```
                    認定医1,295人(独立989・グループ306)
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
  日帰り手技を持つ医師      入院依存科の医師        非入院10科の医師
  (外科系+眼科・消化器等)   (666人、51%)           (401人、31%)
        │                     │                     │
   [A3] ASC持分で            [B2-i] 引退・退去で     [B2-ii] 新設グループ×IHHの
   日帰り部分をIHH内ASCへ    空くスイート・入院権限を  ACC JVへ診療所ごと移転
   (施設料をIHHに残す)       入院依存の後継者へ      (キャンパス内・隣接)
        │                     ▲                     │
        │   同じ医師の入院部分は病院へ(入院の選別装置)  │  空いた分譲スイートが
        └─────────────────────┘                     │  B2-iの受け皿になる
                                                    └─────────────────────┘
```

- **A3**は「同じ外科医の日帰り部分がグループのASCへ、入院部分が保険者の都合で他院へ」という二重流出(検証文書§12-4)の前半を止める。医師がIHHのASCに持分を持てば、その医師の入院もIHHに置かれやすい(ihh-sg-growth-strategy.md §A6: 「資本で結ばれた医師の入院の約8割が当該病院へ」〔B〕)。
- **B2-ii**は、A3の対象にならない非入院科(眼科・皮膚科・ENT等)を、診療所ごとIHH保有のACCへ移す。IHHが失うものは何もなく(施設料はACCに残る)、空いた分譲スイートがB2-iの受け皿になる。
- **B2-i**は、病院本館の手術室・病床を「入院を要する症例」に集中させる。頭数を増やすのではなく、引退(卒後35年超が全体の24〜28%【算出】)とB2-iiの移転で空く枠を、入院依存のサブスペシャリティの後継者に配分する。

### 1-2. 各施策の目的とKPIの要約

| 施策 | 効く駆動力(検証文書§16-1) | 目的(1行) | 主KPI | 時間軸 |
|---|---|---|---|---|
| **A3** | (b)請求額、(c)医師の施設料取り込み | 日帰り症例のグループ内捕捉率を上げ、施設料をIHHに残す | 日帰り症例のIHH施設捕捉率、ASC稼働率、持分医師の入院ロイヤルティ | 0〜24か月(Royal Square SPC化→2〜3拠点) |
| **B2-i** | (d)民間入院の需要縮小、(c) | 入院件数×ケースミックス(ALOS・重症度)を上げる | 入院依存科の入院ロイヤルティ、承継件数、ハイブリッド手術室・ICU稼働 | 0〜36か月(承継は10年スパン) |
| **B2-ii** | (b)(c) | 非入院科をACCに集約し、本館を入院に空けつつ施設料と入口(内視鏡→外科)を守る | ACC移転医師数、ACCの全保険者パネル接続、スイート再配分件数 | 6〜36か月 |

### 1-3. 前提条件(3施策に共通)【分析】

1. **支払者修復(検証文書A1・A2)が先行する**。GEのPAC再開とPrudentialのHI-led参加が直らないままA3・B2-iを進めると、「保険者に誘導されて他院に入院する医師」に持分を渡すことになる(Foundationの「hospital-agnostic」【確認】)。ただしASC/ACCはPrudentialの「日帰り手術センター」区分で個別にパネル接続できる(Royal Squareは2026年8月に接続済【確認】)ため、A3・B2-iiは病院側の修復を待たずに着手できる。
2. **SMC倫理規程H3の線**: 施設持分は時価(FMV)で割り当て、分配は持分比例のみ、紹介・症例数連動の対価は一切置かず、患者に利害を開示する【確認】(SMC ECEG 2016 pp.61〜62)。
3. **CCCS第34条の線**: 医師グループ・JVが医師の料金を共同で決める、または病院が独立医の料金をまとめて交渉する行為は、SMA料金ガイドラインを違反とした2010年決定と同型のリスクがある【確認】。本書の設計は料金交渉を含まない。
4. **分譲スイートはIHHの所有物ではない**(MEMC 232戸、Novena 250戸超【確認】)。移転・承継は強制できず、認定(入院権限)・Annexe/病院保有区画・手術枠・持分・立上げ支援という「IHHが配分できるもの」で誘導する。
5. **三井物産はIHHの筆頭株主(32.8%)**であり、三井が資本を出す形はBursaの関連当事者取引になる【確認】。本書はIHH単独資本を基本形とし、三井の関与は§⑥で選択肢として扱う。

---

## ② 共通の設計部品: 施設SPCと持分の標準装備

A3・B2-iiの両方で使う「医師持分付き施設SPC」の標準仕様。先行例と規制から逆算した【分析】。

### 2-1. 構造

| 項目 | 仕様 | 根拠 |
|---|---|---|
| 器 | 施設ごとに特別目的会社(SPC)。HCSAのASCライセンス(および外来・放射線等の束)はSPCが保有。ライセンス保有者は法人で可、医師保有要件なし、Clinical Governance Officer(SMC登録専門医)の設置が要件 | HCSA Ambulatory Surgical Centre Service Regulations 2023【確認】(ihh-sg-growth-strategy.md §A9) |
| 持分 | IHH 51〜70%、施術医30〜49%。IHHが過半を持ち連結する | 前例: HC Surgical 51/49(+11年コミットメント)、Foundation 60/40、Novena Surgery(医師シンジケート)【確認】 |
| 割当価格 | 時価(FMV)。割安付与は「紹介誘引」と看做されるリスク。SPCも IHHも取得資金を医師に貸し付けない・保証しない | SMC H3、米ASCセーフハーバー42 CFR 1001.952(r)の設計参照【確認】 |
| 対象医師の選定基準 | 当該施設を自分の診療の延長として使う医師。米セーフハーバーの「診療収入の3分の1以上が手技から」「手技の3分の1以上を当該ASCで」を社内基準として採用(法的義務ではなく、紹介誘引でないことの実務的証拠) | 同上【確認】。OIG FAQ「この基準を満たす医師はASCを診療所の延長として使う蓋然性が高い」 |
| 分配 | 持分比例の配当・キャピタルゲインのみ。症例数・紹介数・入院数に連動する分配は禁止 | SMC H3(fee splitting禁止)【確認】 |
| ベスティング | 時間ベスティング(例: 3〜5年)と、法人業績(SPCの売上・PAT)連動の解除。紹介量連動は不可 | Tamarind 7年、Foundation 1〜10年【確認】(sg-four-specialist-groups-incentives-growth.md §4) |
| 退任・離脱 | 定式価格(PAT倍率または純資産)による**法人経由の強制買戻し**、分割払いで資金負担を平準化。Good/Bad Leaverを区分 | Medical Economics型、USPIの買取義務(償還可能非支配持分)、Tamarind Leaver条項【確認】(sg-specialist-groups-succession-design.md §4.6・§5) |
| 後継者プール | 買戻した持分を留保し、公的部門から移籍する40〜50歳の中堅に勤務年数と業績で段階配分 | 4大グループのいずれも完成形を持たない(同§4.7)【確認】 |
| 後継採用連動 | 創業医の未確定分の一部を「後継者の採用・定着」で解除(Foundation MP2型)。条件は売上・PAT・採用人数等の法人指標に限定 | Foundation目論見書【確認】 |
| 利害開示 | 持分を持つ医師は、当該施設への紹介時に患者へ利害を開示 | SMC H3【確認】 |
| ガバナンス | 経営は取締役会(IHH過半)、臨床はCGOと医師評議会。手術枠の配分ルールは公開・一律 | テナント政治のリスク管理(検証文書§16-2 A4-vi) |
| 第三者医師 | 非持分医・非認定医の利用も受け入れ、稼働を優先 | Foundationの論理(1H26: 第三者専門医の症例を保険者経由でFACへ)【確認】 |

### 2-2. 保険者・公的財源への接続(施設単位で必須)

| 保険者・制度 | 接続の単位 | 施設側の要件 | 根拠 |
|---|---|---|---|
| Prudential(PRUPanel Connect) | **施設単位**(機関主導)。日帰り手術センター区分、eLOG上限S$15,000(病院はS$30,000) | PPCの日帰り手術センターとしての参加。Royal Squareは2026年8月に参加済 | Prudential PPC施設一覧、IHH×Prudential 2026年8月17日【確認】 |
| Great Eastern | 医師単位(パネル)+事前承認(PAC)。Mount Elizabeth 2病院の入院PACは2025年6月から停止、**日帰り手術センターへの事前承認は継続** | 施設がDSCとして認識されること | Mothership 2025年6月〔B〕、GE Health Connect【確認】 |
| AIA・Income・HSBC Life・Singlife | 医師単位。HSBC Life(Fullerton経由)・Singlife(iXchange経由)はe-filing設備が加入要件 | e-filing・事前承認のシステム対応 | LIA「Insurance Panel of IP Insurers」2025年2月版【確認】 |
| 新ライダー(2026年4月〜) | 自己負担上限(年S$6,000)は**パネル医または事前承認の請求のみ**に適用 | 施設・医師の双方がパネル/事前承認の対象であること | MOH 2025年11月26日【確認】 |
| MediSave/MediShield Life | TOSP収載術式なら私立ASCでもMediSave利用可。MediSave認定が集患の必須条件 | MediSave認定の取得 | MOH「MediSave and MediShield Coverage for Surgical Procedures」【確認】 |

---

## ③ A3. 専門医にASCの株式(Royal Square・新規ASC)

### 3-1. 目的と機構【分析】

- **目的**: 認定医の日帰り手技(内視鏡・白内障・ヘルニア・関節鏡・手外科・ENT・婦人科日帰り・泌尿器内視鏡)のうちIHH施設で実施される比率(グループ内捕捉率)を上げ、施設料(民間請求額の約60%、MOH 2026年5月答弁【確認】)をIHHに残す。同時に、持分を持つ外科医の入院をIHH病院に結び付ける。
- **なぜ持分か**: 医師の手技料はMOHベンチマークで施設によらず横並びであり、医師が施設を移す動機は「施設の利益の取り分」にしかない(検証文書§13-3)。Foundationは「報酬は自社医療センター利用を促す設計」「第三者施設の施設料を取り込む」と明言しており【確認】、IHHが同じ装置を持たなければ日帰り症例はFAC等へ流れ続ける。
- **なぜ今か**: FAC Novena(手術室4+内視鏡室2、2026年2月)、Mount Alvernia新DSC(手術室4、段階開設)、Cura(手術室5)、Novena Surgery(手術室3)に対し、Royal Squareは手術室2+内視鏡室4【確認】。Foundationは「2H26に第三者専門医の症例を保険者経由でFACへ」と述べている【確認】。医師がどの施設に慣れ、どこで持分を持つかは一度固定されると動かない。

### 3-2. 対象施設と容量計画

| 拠点 | 現状【確認】 | 計画【分析】 | 備考 |
|---|---|---|---|
| **Royal Square(Novena)** | 手術室2+内視鏡室4。Hoi Hup–Sunway JVの建物(2013年6月起算99年リース、医療スイート171戸)をIHHが賃借。IHH認定医22人が診療所を置く(眼科5・小児3・一般外科3・形成2・消化器2・整形1・O&G 1・ENT 1・循環器1・泌尿器1・精神科1・内分泌1)【算出】。Luma(Tamarind)・Eagle Eye(HMI)・Royal Healthcare(双日)も入居 | **第1号SPC**。追加フロアのリースで手術室を4へ拡張。内視鏡はgutCARE/HC Surgical型JVの接続先 | 建物の支配権はなく、拡張はリース交渉次第【未検証】 |
| **Orchard(Mount Elizabeth Orchard周辺)** | 認定医653人がMEMCに診療所、Paragon Medicalに64人(眼科13・一般外科8・皮膚7・O&G 7・形成5)【算出】。MEMC入居医のうち日帰り手技を持つ科は一般外科76・整形72・泌尿器25・眼科40・消化器41・ENT 29・形成10・手外科15【算出】 | **第2号SPC**。手術室4+内視鏡室2〜4を標準。MEH改装後の院内日帰り手術室との役割分担(院内=入院に転換し得る症例、ASC=完結症例)を先に決める | 候補物件はMEMC・Paragon・近隣商業ビル【未検証】 |
| **East(Parkway East)** | PEMCに178人(一般外科31・整形24・眼科18・消化器17・泌尿器12・ENT 10)【算出】。Aptus(Alfa Medicus)が先行 | **第3号SPC**。地域の内視鏡・眼科・整形日帰りの受け皿 | 規模は手術室2〜3 |
| **Napier(Gleneagles)** | GMCに352人、Annexe(賃貸)に120人(整形18・循環器18・腫瘍内科9・眼科9・O&G 9・一般外科8・消化器7)【算出】 | Annexeは病院保有の賃貸区画であり、B2-iの承継の受け皿として優先。ASCは第2期 | — |

- **容量の目安**【推定】: FAC Novena(手術室4)は1日36〜40件、FAC Orchardは14〜16件〔B〕(Growbeansprout)。Royal Square+2拠点で手術室計10〜12・内視鏡室8〜10なら、年間2万〜3万件規模の日帰り症例を受けられる(稼働率・診療日数の仮定次第であり、社内の術式別件数で検証を要する【未検証】)。
- **投資規模**【推定】: FAC Novena(手術室4)の設備投資はS$2.5百万、画像センターS$5.4百万【確認】(sg-specialist-group-typology.md)。不動産を持たないASC 2拠点の内装・設備はS$5〜10百万程度のオーダーであり、病院のPLife REIT賃料(S$97.2百万/年【確認】)と比べて軽い。土地・建物を持つ場合は別途。

### 3-3. 対象医師の選定【算出・分析】

| 層 | 母数【算出】 | 持分割当の優先順位 | 理由 |
|---|---|---|---|
| ① Royal Square現入居医 | 22人(グループ所属はHMI Eagle Eye 1人・Royal Healthcare 1人のみ) | 第1号シンジケートの核 | 既に施設を使っている |
| ② Novena・Orchardの日帰り手技を持つ独立医 | 一般外科114・整形105・泌尿器23・消化器53・眼科60・ENT 47・形成32・手外科11・口腔外科16(いずれも独立医のみ) | 術式・件数で選定。「手技の3分の1以上をASCで」の基準で、ASCを実際に使う医師に限る | 紹介誘引でないことの実務的根拠 |
| ③ Mount Elizabethにしか認定を持たない医師 | 702人(54%)。うち一般外科76・整形61・眼科58・消化器36・ENT 36・泌尿器20 | ロイヤルティ上の最優先 | GEのPAC停止・Prudential提携外の影響を直接受ける層 |
| ④ Thomson兼任 | 249人(19%)。入院依存科の独立医では126人、うちMount Elizabethのみ認定は62人 | ③と重なる層を先に | 流出が既に始まっている |
| ⑤ グループ所属医 | 306人(Foundation 89・Tamarind 45・HMI 30・OUE 25・HC Surgical 13等) | 原則対象外。ただしgutCARE(8)・HC Surgical(13)は内視鏡JVの相手として別枠 | 自社施設への誘導契約を持つ |

- **パネル接続の差**【算出】: 独立医の平均パネル数はグループ医より少ない(消化器3.5 vs 5.2社、ENT 2.8 vs 4.2、一般外科3.6 vs 5.1、整形3.8 vs 4.6、眼科3.1 vs 3.7)。ASC持分の提案は、施設のPPC接続と層D(加入経路支援)を**セット**にして初めてグループの提案と同等になる。

### 3-4. 術式単位のデカント・プロトコル【分析】

| 科 | ASCへ(完結症例) | 病院へ(入院・転換可能性) | 根拠 |
|---|---|---|---|
| 一般外科 | 大腸内視鏡・ポリープ切除、ヘルニア、痔、乳腺良性腫瘍 | 大腸切除・胃切除・肝胆膵 | 検証文書§12-4 |
| 整形 | 関節鏡、手の手術、足部 | 人工関節、脊椎固定 | 同 |
| 泌尿器 | 膀胱鏡、結石砕石 | 前立腺全摘 | 同 |
| 眼科 | 白内障、硝子体の一部 | 複雑網膜 | 価格帯: 公立補助S$974/眼 vs 私立S$4,500〜10,000【確認】 |
| 消化器 | 上下部内視鏡 | 治療内視鏡の一部・出血 | 外来S$1,000〜3,000 vs 入院S$5,000〜8,000超【確認】 |
| ENT・手外科・形成 | 大半の日帰り手技 | 頭頸部腫瘍等 | — |

- プロトコルは医師評議会(§2-1)で合意し公開する。**臨床判断は医師に残し、IHHは場所を提供する**(ECEG H3との整合)。
- 内視鏡はがん(大腸・胃)の入口であり、「内視鏡→外科→腫瘍内科→入院」の連鎖をIHH内で完結させる設計にする(検証文書§12-5)。

### 3-5. 実行ステップ

| フェーズ | 期間 | ステップ | 成果物 |
|---|---|---|---|
| 0. 準備 | 0〜3か月 | (a) 社内データで認定医別の日帰り件数・施設別配分を確定(【未検証】の最優先項目)。(b) Royal Squareのリース条件・拡張余地の確認。(c) SMC H3・CCCS・HCSAに関する法的助言と、必要ならMOH/SMCへの事前相談。(d) 持分設計の標準契約(§2-1)の作成。(e) FMV評価者の選任 | 対象医師リスト、標準株主間契約、評価報告 |
| 1. 第1号SPC | 3〜9か月 | (a) Royal SquareをSPC化(IHH 51〜70%)。(b) 現入居医22人+Novena高頻度利用医に時価で30〜49%を割当(初回は20〜30人規模)。(c) PPC接続(済)に加え、GE DSC事前承認・HSBC Life/Singlife e-filing・MediSave認定を整備。(d) デカント・プロトコル公開。(e) 手術枠の配分ルール公開 | SPC設立、第1回割当、パネル接続一覧 |
| 2. 面展開 | 9〜24か月 | (a) Orchard第2号(手術室4+内視鏡室2〜4)の物件確定・HCSA申請・内装。(b) East第3号。(c) 各拠点で同じ持分設計・パネル接続。(d) gutCARE/HC Surgical型の内視鏡JVを接続。(e) 第三者医師の受入れ開始 | 2拠点開業、持分医師累計60〜100人【推定】 |
| 3. 循環 | 24〜36か月〜 | (a) 退任時買戻し・後継者プールの初回運用。(b) 持分医師の入院ロイヤルティの測定と、病院側サービス(B2-i)との接続。(c) 稼働と第三者比率に応じた増床 | 承継装置の実装率、ロイヤルティ指標 |

### 3-6. KPI【分析】

| KPI | 定義 | 参照値 |
|---|---|---|
| 日帰り症例のグループ内捕捉率 | 認定医の日帰り手技のうちIHH施設(病院+ASC)で実施された比率 | 【未検証】(社内データ) |
| ASC稼働率・回転 | 手術室・内視鏡室の1日件数 | FAC Novena 36〜40件/日〔B〕 |
| 持分医師の入院ロイヤルティ | 持分医師の入院症例のうちIHH 4病院に置かれた比率(非持分医と比較) | 【未検証】 |
| パネル接続 | 各施設が6保険者のパネル/事前承認対象である比率 | Royal Square: Prudential接続済 |
| 第三者医師比率 | 非認定医の症例比率 | Foundationの論理 |
| 承継装置の実装率 | SPCのうち買戻し・後継者プール・後継採用連動を備える比率 | — |
| ASCマージン | SPCのEBITDAマージン | 米USPI約40%、HC Surgical純利益率約19%【確認】 |

### 3-7. 規制整合とリスク【分析】

| リスク | 内容 | 対応 |
|---|---|---|
| SMC H3 | 割安付与・症例連動分配・紹介対価と看做される | FMV、持分比例分配、開示、紹介量非連動の文書化、融資・保証の禁止 |
| CCCS第34条 | 同一科の多数の医師を束ね料金を決める形 | SPCは施設料のみを決め、医師の手技料には関与しない。同一科で多数の医師を束ねる場合は事前審査 |
| テナント政治 | 持分を得られない医師の離反 | 選定基準(利用実績)の公開、第三者利用の受入れ、新規キャパシティへの配置 |
| カニバリゼーション | 病院内日帰り手術室の稼働低下 | 院内はMEH改装後の高acuity・転換可能症例に特化し、ASCと役割分担。入院単価の対保険者説明力が上がる(ihh-sg-growth-strategy.md §A6) |
| 容量競争 | FAC・Mount Alvernia・Cura・HMIが先に医師の行動を固定する | 第1号SPCを9か月以内、2〜3拠点を24か月以内 |
| 資本・組織 | 複数拠点の同時進行 | アウト・オブ・ホスピタル専任の責任者(検証文書§16-4 IHH 7) |

---

## ④ B2-i. 専門医mixの変更: 入院系への特化(承継主導の修正版)

### 4-1. 目的の再定義【分析】

病院の収益は病床・手術室・ICUの稼働で決まる。達成すべきは**入院件数とケースミックス(ALOS・重症度)**であり、医師の科別構成比は手段にすぎない(検証文書§17-3)。認定医の頭数では既に入院依存科が過半(666人、51%)であり、問題は構成比ではなく、**入院依存科の医師1人当たりの入院件数がIHHの外へ出ていること**である。したがって本施策は「がん・循環器の医師を増やす」ではなく、次の4つに読み替える。

1. **承継**: 引退・退去で空くスイートと入院権限を、入院依存のサブスペシャリティの後継者へ配分する(本節の中核)。
2. **ロイヤルティ**: 既存の入院依存科医師の入院をIHHに置かせる(支払者修復+病院側サービス)。
3. **設備**: 入院を生む設備(ハイブリッド手術室・カテ室・ICU/HDU)を先に置く。
4. **外部需要**: 国際患者・公立の待機手術の受入れで高acuity症例を連れてくる。

### 4-2. 現状の一次データ【算出】

**入院依存科の独立医476人のうち、年齢推計が可能な260人中、卒後35年超は61人(23%)**。全1,295人では卒後35年超が154人/651人(24%)で、姉妹文書の算出(26〜28%、閾値の違い)と概ね一致する。

| 科 | 独立医で卒後35年超 | 主な拠点 | 備考 |
|---|---|---|---|
| 一般外科 | 15 | MEH中心 | 大腸・肝胆膵の後継が必要 |
| 整形外科 | 10 | — | 脊椎・人工関節 |
| 循環器 | 10 | — | カテ室依存。独立グループAsian Heart & Vascular(10人)は別枠 |
| 産婦人科 | 8 | — | Thomson兼任47%・GE接続17%の科(ihh-sg-inpatient-loyalty-asc-payor-strategy.md §4-1) |
| 泌尿器 | 5 | — | — |
| 脳神経外科・心臓胸部外科・小児外科・集中治療 | 各2〜3 | — | 民間専門医の90〜96%を既に認定 |
| **合計** | **61** | MEH 32・GEH 19・PEH 9・MNH 9(重複計上) | 53人は診療所1か所のみ(=引退で1戸が空く) |

- 年齢不明の216人を同率で外挿すると、入院依存科の独立医で引退期にある医師は**約110人**と推定される【推定】。これが今後5〜10年で空く入院権限・スイートの母数である。
- 供給側: 民間部門への新規専門医登録は2025年に35人(SMC年次報告2025【確認】)。供給は公的部門の上級コンサルタント(定年64歳・再雇用69歳)の移籍に依存する(sg-specialist-groups-succession-design.md)。
- 入院依存科の独立医の保険者接続: Prudential 373人(78%)、GE 195人(41%)、Mount Elizabethのみ認定269人(57%)、Thomson兼任126人(26%)【算出】。GE接続が低いのは、GEのパネルがMount Elizabethの入院PACを出さない状況と整合する。

### 4-3. 設計

#### (a) 承継プログラム(中核)【分析】

| 要素 | 内容 | 根拠・前例 |
|---|---|---|
| 対象 | 入院依存科の独立医で引退期にある約110人【推定】と、その診療所(スイート)・症例簿・入院権限 | §4-2 |
| 後継者の供給源 | 公的部門の上級コンサルタント(心臓外科・脳外科・脊椎・肝胆膵・移植・複雑がん外科・婦人科腫瘍)、海外からの帰国医、IHHマレーシア・インド拠点の上級医 | Foundationは「採用組」40人を同じ論理で獲得【確認】 |
| IHHが配分できるもの | (i) 認定(入院権限)の新規付与で入院依存のサブスペシャリティを優先、(ii) Gleneagles Annexe(賃貸120人分)・病院保有区画の市場賃料内でのフェーズイン、(iii) 立上げ期1〜2年の事務・パネル加入・紹介調整支援(層D)、(iv) 手術枠・ICU・ハイブリッド手術室の優先枠(公開ルール内)、(v) MDT・当直・国際患者割当への参加 | 検証文書§16-2 A4-v、ihh-sg-inpatient-loyalty-asc-payor-strategy.md 層A5 |
| 引退医への提案 | 後継者マッチング(IHHが候補を紹介)、症例簿の段階的引継ぎ(半引退期間4〜5年の設計)、SPC持分(A3)の後継移転、スイートの売却・賃貸の仲介 | Medical Economics・AAFP FPM(半引退期間)【確認】 |
| 立上げの経済 | Foundation開示: 既存医の平均売上S$2.7百万に対し新規医の初年度は約48%(S$1.3百万)【確認】。IHHは雇用モデルを持たないため、給料保証ではなく「賃料フェーズイン+事務・パネル・紹介支援」で立上げ曲線を埋める(入院量連動の保証は紹介誘因と看做される) | 検証文書§16-2 A4-v |
| 承継の動機づけ | A3のSPC持分で「後継採用連動(MP2型)」の解除条件を置く。引退医のスイートを後継者が市場価格で取得する際の仲介・つなぎ(IHHの融資・保証はSMC整合上避ける) | Foundation MP2【確認】 |
| スイートの受け皿(選択肢) | 分譲スイートの売却は医師の判断だが、IHH(または不動産保有主体)が市場価格で取得・賃貸し後継者へ転貸する「スイート流動化」を限定的に持てば、承継の時間差を埋められる。資本負担とFMV規律が条件 | ihh-sg-inpatient-loyalty-asc-payor-strategy.md §5-2(iii)【分析】 |

#### (b) 認定(入院権限)の運用【分析】

- 現行の認定基準・審査体制は【未検証】。新規認定の優先順位に「入院依存のサブスペシャリティ」「IHH施設での入院比率のコミットメント(契約ではなく臨床統治上の期待値)」を置く。
- 認定は希少資源ではなくなっている(外科系民間専門医の72〜96%を既に認定【確認】)ため、認定単体では誘導力が弱い。Annexe・持分・立上げ支援と束ねて初めて効く。

#### (c) 入院を生む設備・サービス【分析】

| 設備・サービス | 内容 | 根拠 |
|---|---|---|
| ハイブリッド手術室・ロボット | 心臓血管・脊椎・泌尿器の複雑手術を独立外科医が自院に置く理由を作る | 検証文書§17-3(3) |
| カテ室・EP室 | 循環器のリテンションJV(Asian Heart & Vascular 10人、Orchard Heart 4人、The Heart Specialist 4人)の共同投資対象。持分はA3と同じ規律 | ihh-sg-inpatient-loyalty-asc-payor-strategy.md 層C |
| ICU/HDU | Mount Alverniaは16室へ倍増【確認】。MEH改装後の容量と、Integrative Critical Care(ICU 10人・麻酔5人)等の院内グループとの体制 | 同 |
| ホスピタリスト・麻酔・術後管理 | 病院が提供し、独立外科医の入院管理負担を下げる | 公立のGIMホスピタリスト〔B〕 |
| MDT・腫瘍登録・キャンサーボード | IHHが主催し全テナントの腫瘍医に同一条件で開く | 検証文書§12-5(5) |

#### (d) がん・循環器の個別設計【分析】

ご提示の「がん・循環器の医師を増やす」は、両科とも**頭数ではなく運営主体と設備の問題**である。

| 科 | 現状【確認】 | B2-iでの打ち手 |
|---|---|---|
| がん | 腫瘍内科48人の90%がグループ所属。PCCの運営者TalkMedは2025年9月からTamarind傘下、売上の約9割がPCC向け。Consultancy Restatement Agreement(2013年、2016年に2021年まで更新、以後非公開)。IconはIHH医療センター内7センターでPrudentialの外来腫瘍をキャッシュレス化。CDLで薬剤ごとの請求上限 | (1) PCC契約の精査と後継条項(創業医65〜69歳、非創業医9人)。(2) 放射線治療・入院化学療法・複雑手術・合併症管理を病院キャンパスに集中し、装置はPCC・Icon・OncoCare・Curieの医師に同一条件で開放。(3) 外科腫瘍(大腸・乳腺・肝胆膵・婦人科)の後継者を承継プログラムで優先。(4) デイ・オンコロジーはB2-iiのACC(腫瘍内科医の持分30〜49%付き)へ。(5) がんのエピソード定額を保険者に提示 |
| 循環器 | 79人、グループ所属37%、卒後35年超30%(年齢判明47人中)。Novena Heart→Tamarind、Harley Street→HMIで買収可能なスケール資産は消滅 | (1) カテ室・EP室・ハイブリッド手術室のリテンションJV。(2) 循環器の定額パッケージ(開始済)の拡充。(3) 心臓外科(19人、卒後35年超33%)の後継者を承継プログラムで最優先(民間の90%を既に認定、後継以外に増やす余地なし) |

#### (e) 入院依存科のロイヤルティ(支払者側)【分析】

- GEのPAC再開(Mount Elizabeth 2病院の標準的入院術式の定額化)、PrudentialのHI-led参加(Gleneagles・Parkway Eastを先に)、定額パッケージの整形・一般外科・泌尿器・産科への拡大。これは検証文書A1・A2であり本書の前提条件(§1-3)。
- 患者に対する合法で規模の出る「入院インセンティブ」は、IHH病院がパネル・事前承認の対象施設であることそのもの(ihh-sg-inpatient-loyalty-asc-payor-strategy.md §4-3)。

#### (f) 外部需要【分析】

- 国際患者の非伝統市場(がん・心臓・移植)はIHHの2026年重点【確認】(IHH 2Q26プレスリリース)。
- 公立の稼働率95%超・2025〜30年に13,600床増の中で、待機手術・逼迫時の受入れ契約(Raffles ECC・CGH–Parkway East提携・TCFの前例)。それでも空く病床はステップダウン・リハ・緩和へ転換(bor-decline-countermeasures.md §5)。

### 4-4. 実行ステップ

| フェーズ | 期間 | ステップ |
|---|---|---|
| 0. 把握 | 0〜6か月 | (a) 認定医ごとの入院症例のIHH配分比率(ロイヤルティ)を社内データで確定。(b) 入院依存科の独立医の引退予定・後継の有無を面談で把握(SMA型調査)。(c) 分譲スイートの所有者・年齢・空室動向をSLA/URAの区分所有記録で把握。(d) 認定基準の見直し案 |
| 1. 装置 | 3〜12か月 | (a) 承継プログラム(マッチング・Annexeフェーズイン・立上げ支援)の制度化と公開。(b) 後継者の供給源(公的部門上級コンサルタント)との接点づくり(MDT・教育・治験)。(c) ハイブリッド手術室・カテ室・ICUの投資判断。(d) 循環器リテンションJVの交渉 |
| 2. 運用 | 12〜36か月 | (a) 年10〜20件の承継を目標に運用【推定】。(b) A3のSPC持分に後継採用連動を実装。(c) スイート流動化(選択肢)の限定運用。(d) がんはPCC契約更改とデイ・オンコロジーACC(B2-ii)へ接続 |
| 3. 構造転換 | 36か月〜 | 空く病床の機能転換、高acuity特化のKPIへの移行 |

### 4-5. KPI【分析】

| KPI | 定義 | 参照値 |
|---|---|---|
| 入院ロイヤルティ | 入院依存科の認定医ごとの入院症例のうちIHH 4病院に置かれた比率 | 【未検証】 |
| 承継件数 | 引退医のスイート・入院権限が入院依存の後継者へ引き継がれた件数/年 | 引退期の独立医約110人【推定】 |
| 後継者の立上げ | 後継者の加入後12か月売上の既存医比 | Foundation 48%【確認】 |
| ケースミックス | ALOS・重症度・ICU利用率、ハイブリッド手術室・カテ室の稼働 | — |
| 入院件数 | SG入院件数の前年比 | 2Q26 ▲6%〔B〕 |
| 稼働率 | 4病院の病床稼働率 | 2Q26 51%〔B〕 |

### 4-6. リスク【分析】

1. **後継者の供給不足**: 民間新規専門医35人/年。公的部門が定年延長・処遇改善で引き留めれば、移籍は細る。
2. **スイート価格の下落**: B2-iiの移転とB2-iの承継でスイートの需要が減れば、現所有者(入院依存科の医師を含む)の資産価値を毀損し反発を招く。後継者の参入コストは下がる両面性。
3. **保険者が応じない**: 支払者修復なしでは、後継者もhospital-agnosticに振る舞う。
4. **公立の容量**: SGH Elective Care Centre(2027年、300床)等が待機手術を吸収し、民間入院のパイがさらに縮む。
5. **紹介誘因と看做される運用**: 入院量連動の保証・優先枠は不可。すべて公開ルール・FMV・法人指標で設計する。

---

## ⑤ B2-ii. 非入院科のグループ化とACC JV(キャンパス内・隣接)

### 5-1. 目的と「なぜキャンパス内か」【分析】

- **目的**: 眼科・皮膚科・ENT・形成・手外科・口腔外科・内分泌・精神科等の**非入院科を診療所ごとACCへ集約**し、(i) 本館のスイート・手術室を入院依存科に空け(B2-iの受け皿)、(ii) 日帰り手技の施設料と内視鏡→外科の入口をIHHに残し、(iii) 保険者の「日帰り手術センター」区分と自己負担上限に接続して症例を失わない。
- **なぜIHH経済圏の内側か**: 外に出せば施設料と入口を同時に失い、本館の入院は増えない(検証文書§17-3「算術・所有・収益・供給」)。キャンパス内・隣接なら、病院の画像・検査・薬局・麻酔・緊急時のバックアップを共有でき、HCSAライセンスの束(ASC+外来+放射線)をIHHが保有できる。
- **なぜIHH入居医の新設グループか**: 既存グループ(Foundation・Tamarind・HMI)は自社施設への誘導契約を持ち、JVにしてもhospital-agnosticの立場を崩さない。入居医で新設するグループは、IHHが「場所と保険者接続」を差し出す代わりに医師が「症例と臨床統治」を差し出す対等の取引になり、Hirslanden原則(テナントと競合する資産を持たない)はテナント自身をパートナーにすれば満たされる(ihh-sg-growth-strategy.md §A9)。

### 5-2. 対象科と母数【算出】

| 科 | 認定医 | 独立医 | 主な所在(ビル別、重複計上) | ACCでの機能 |
|---|---|---|---|---|
| 眼科 | 98 | 60 | MEMC 40・Novena 30・GMC 13・PEMC 18・Paragon 13・Annexe 9 | 白内障・硝子体の日帰り手術室+外来 |
| 消化器 | 68 | 53 | MEMC 41・GMC 23・Novena 21・PEMC 17 | 内視鏡室(がんの入口) |
| ENT | 65 | 47 | MEMC 29・Novena 24・GMC 13・PEMC 10 | 日帰り手術+外来 |
| 皮膚科 | 37 | 37 | MEMC 13・GMC 12・Novena 10・Paragon 7 | 外来・レーザー(診察室型) |
| 形成外科 | 32 | 32 | GMC 13・MEMC 10 | 日帰り手術 |
| 口腔外科 | 23 | 16 | — | 日帰り手術 |
| 手外科 | 18 | 11 | MEMC 15 | 日帰り手術 |
| 内分泌・精神科・リウマチ | 60 | 58 | — | 外来(診察室型) |
| **合計(10科)** | **401** | **314** | IHHキャンパス内に診療所を持つ医師359人 | — |

- グループ所属は87人(Foundation 27・HMI 16・Eye & Retina Surgeons 12・OUE 8・gutCARE 8・Fullerton 5・ISEC 3等)。Eye & Retina Surgeons(12人)とgutCARE(8人)は独立系の共同診療であり、新設グループの中核候補になり得る【分析】。
- 卒後35年超は44人/198人(22%)で、引退で空く診療所も相当数ある。
- **ビル別のACC型需要**【算出】(日帰り手術室を要する眼科・消化器・ENT・形成・手外科・口腔外科の入居医): MEMC 143人、Novena 93人、GMC 75人、PEMC 56人、Annexe 24人、Paragon 24人。診察室型(皮膚・内分泌・精神・リウマチ)はMEMC 41・GMC 37・Novena 29。

### 5-3. グループの組成【分析】

```
   医師(個人)                                IHH(Parkway Hospitals Singapore)
      │ 100%                                         │
      ▼                                              │
 [診療グループ](医師所有の診療法人/LLP、仮称)          │
  ・各医師の診療・手技料は医師/グループに帰属            │
  ・IHHは出資しない(雇用もしない)                       │
  ・共通機能: 予約・請求・e-filing・採用・品質・CGO      │
      │ 30〜49%(個人またはグループ持株会社経由)         │ 51〜70%
      ▼                                              ▼
 [ACC運営SPC](施設SPC: HCSAライセンス群・設備・賃借・人員)
  ・施設料・設備使用料・日帰り手術室/内視鏡室/画像の収入
  ・IHH連結、医師へは持分比例の配当のみ
  ・全6保険者のパネル接続、MediSave認定
  ・IHHから購買・検査・画像・C+外来モジュール・NEHR対応を固定サブスクで受ける
```

| 論点 | 設計 | 理由 |
|---|---|---|
| 二層にする理由 | 診療(医師の手技料)と施設(施設料)を法的に分ける | SMC H3のfee splitting禁止、CCCS(IHHが医師の料金に関与しない)、医師の「雇われ感」の回避 |
| 診療グループへのIHH出資 | **しない**(または最大でも少数・無議決権)。グループは医師所有 | 雇用型(Healthscope・Ramsay心理クリニックの失敗)を避ける。IHHの中核能力は場所貸しと施設運営 |
| 施設SPCの持分 | §2-1の標準装備(FMV、ベスティング、買戻し、後継者プール、後継採用連動、持分比例分配、開示) | — |
| グループの共通機能 | 予約・請求・e-filing・パネル加入事務・採用・品質指標・CGO。料金の共同決定は行わない(各医師がMOHベンチマーク内で個別に設定) | CCCS 2010年決定【確認】 |
| 医師の拒否権 | 臨床統治・施設の手術枠ルール・CGO選任にグループの同意を要する事項を置く | Tamarind型の拒否権(sg-four-specialist-groups-incentives-growth.md §6.2) |
| 規模 | 第1号は眼科・消化器・ENTの高頻度利用医20〜40人から開始し、科を追加 | 同一科で多数を束ねる場合はCCCS審査の見通しを先に取る |

### 5-4. 立地候補(キャンパス内・隣接)【分析】

| 候補 | 内容 | 利点 | 制約 |
|---|---|---|---|
| **Novena: Royal Squareの追加フロア** | A3の第1号SPCと同一建物に外来診察室を併設し、ACC化 | 既にPPC接続、病院から徒歩5分【確認】、Novena Specialist Centreの入居医(眼科30・消化器21・ENT 24)が至近 | 第三者ビルの賃借で拡張余地はリース次第【未検証】 |
| **Orchard: MEMC周辺の商業ビル/Paragon** | MEMC入居医(眼科40・消化器41・ENT 29・皮膚13・手外科15)とParagon(眼科13・皮膚7)の受け皿 | 最大の母数。A3第2号SPCと同一施設にできる | 物件の確保、MEMCとの距離 |
| **Napier: Gleneagles Annexeの一部転用** | 病院保有の賃貸区画をACC型(外来+日帰り)に再編 | IHHが支配する唯一の区画。B2-iの承継用区画と分けて設計 | 既存入居120人(整形18・循環器18等)との調整 |
| **East: Parkway East Medical Centre** | 地域型の眼科・消化器・整形日帰り | PEMC入居56人のACC型需要 | 規模は小さい |

- 新築・取得で建物を持つ場合は、IHHのアセットライト方針(PLife REIT)と整合させ、医療特化型の建物を第三者(REIT・三井物産等)が保有しIHH・医師JVがオペレーターとして入る形が選択肢になる(検証文書§16-4 三井4)。

### 5-5. 医師が診療所を移すインセンティブ【分析】

分譲スイートの所有者に「移転」を提案するには、金銭的誘因(紹介対価)ではなく、**診療上・経済上の合理性**を揃える必要がある。

| インセンティブ | 内容 | 根拠 |
|---|---|---|
| (i) 症例を失わない | ACCがPrudentialの日帰り手術センター区分・eLOG S$15,000・自己負担上限の対象になり、GEのDSC事前承認、HSBC Life/Singlifeのe-filingに接続。本館のスイートに残るより保険患者を失いにくい | Prudential PPC、MOH 2026年4月ライダー【確認】 |
| (ii) 専用手術枠と回転 | ACC内の日帰り手術室・内視鏡室の枠を、病院の緊急・入院手術に割り込まれない形で確保 | ASCの回転率が病院より高い構造(sg-asc-acc-market-report.md §6) |
| (iii) 施設利益の持分比例配当 | 施設SPCの30〜49% | §2-1 |
| (iv) 承継装置 | 退任時の定式価格買戻し、後継者プール、後継採用連動。4大グループが持たない装置 | sg-specialist-groups-succession-design.md §5 |
| (v) 診療所のコスト | 分譲スイートの保有コスト(S$15,000 psfの売り出し例【確認】)より軽い賃料。診察室ごと移転でき、分譲スイートは売却・賃貸して現金化できる | ihh-sg-medical-suite-specialists.md §3-1 |
| (vi) 事務・ITの肩代わり | C+外来モジュール・NEHR対応(2027年初施行予定のHealth Information法【確認】)、請求・e-filing・採用をグループ共通機能とIHHサブスクで提供 | 層D(ihh-sg-inpatient-loyalty-asc-payor-strategy.md §7) |
| (vii) キャリア | サブスペシャリティ化、MDT、教育・治験、ブランド(Mount Elizabeth/Gleneaglesの名を冠する) | Tamarindの「サブスペシャリティ化」訴求 |

- **スイートの流動化**: 移転医の分譲スイートは医師の資産であり、IHHは買い手を指定できない。B2-iの承継プログラムで後継者(入院依存科)をマッチングし、必要なら限定的なスイート流動化(§4-3(a))でつなぐ。

### 5-6. 実行ステップ

| フェーズ | 期間 | ステップ |
|---|---|---|
| 0. 組成 | 0〜6か月 | (a) 眼科・消化器・ENTの高頻度利用医(Eye & Retina Surgeons・gutCARE等の独立共同診療を含む)への打診と意向確認。(b) 診療グループの法形態・定款・共通機能の設計。(c) 施設SPCの標準契約(§2-1)。(d) CCCS事業者間協力ガイダンスに沿った内部審査と、SMC H3運用ルールの文書化。(e) 立地の確定(Novena追加フロアを第1候補) |
| 1. 第1号ACC | 6〜18か月 | (a) Royal SquareのSPC(A3第1号)に外来診察室を併設しACC化、またはNovena追加フロア。(b) 第1陣20〜40人が診療所を移転。(c) PPC日帰り手術センター・GE DSC・e-filing・MediSave認定。(d) C+外来モジュール・NEHR接続。(e) 空いたスイートをB2-iの承継プログラムへ |
| 2. 面展開 | 18〜36か月 | (a) Orchard第2号ACC(A3第2号SPCと同一施設)。(b) 皮膚・内分泌・精神等の診察室型を追加。(c) デイ・オンコロジー(腫瘍内科医の持分30〜49%)をACC内に置き、Prudentialの外来腫瘍センター区分・CDL上限内の定額サイクル価格に接続(検証文書§12-5(3))。(d) East・Napier |
| 3. 循環 | 36か月〜 | 退任時買戻し・後継者プールの運用、第三者医師の受入れ拡大 |

### 5-7. KPI【分析】

| KPI | 定義 | 参照値 |
|---|---|---|
| 移転医師数 | 非入院10科(401人)のうちACCへ診療所を移した医師数 | 母数: 独立医314人、キャンパス内359人 |
| スイート再配分 | 移転・引退で空いたスイートのうち入院依存科の後継者が入った件数 | — |
| ACCのパネル接続 | 6保険者のパネル/事前承認対象の比率、MediSave認定 | Royal Square: Prudential接続済 |
| ACC稼働 | 日帰り手術室・内視鏡室の1日件数、診察室稼働 | FAC Novena 36〜40件/日〔B〕 |
| 症例捕捉率 | 移転医の日帰り手技のうちACCで実施された比率 | 【未検証】 |
| 入口の転換率 | 内視鏡→外科手術・腫瘍内科への転換のうちIHH内で完結した比率 | 【未検証】 |
| グループ流出 | 対象10科の医師が他グループへ移った数 | 2026年10月時点のグループ所属87人が基準 |

### 5-8. リスク【分析】

| リスク | 内容 | 対応 |
|---|---|---|
| CCCS | 同一科の多数の医師を1グループに束ね料金に関与する形 | グループは料金を決めない。科ごとの人数が大きい場合は事前審査 |
| SMC H3 | 移転インセンティブが「紹介対価」と看做される | 金銭的誘因を置かず、(i)〜(vii)の診療上・経済上の合理性のみ。持分はFMV |
| テナント政治 | 本館に残る医師とACCへ移る医師の間の不公平感、分譲スイート価格への影響 | 公開ルール、段階実施、承継プログラムとの接続 |
| 容量競争 | FAC・HMI・Cura・Mount Alverniaが眼科・消化器・ENTの医師を先に固定する | 第1号を18か月以内に |
| 建物の支配権 | Royal Squareは第三者ビルの賃借 | 追加フロアのリース、Annexe転用、将来の自社・REIT保有の選択肢 |
| 既存グループの反応 | Foundation(27人)・HMI(16人)の所属医は移転の対象外。自社施設への誘導契約が強まる可能性 | 独立医314人に集中 |
| 組織 | ASC・ACC・承継・EMRの同時進行 | アウト・オブ・ホスピタル専任の責任者、KPIを「症例のグループ内捕捉率×回転×原価」に置く |

---

## ⑥ 3施策の統合: 順序・資本・組織

### 6-1. 順序と相互依存【分析】

```
0〜6か月   データ確定(日帰り件数・入院ロイヤルティ・引退予定) ── 法的助言(SMC/CCCS/HCSA) ── 標準契約
             │
6〜12か月  [A3-1] Royal Square SPC化 ──▶ [B2-ii-1] 同一建物にACC(外来併設) ──▶ 空くスイート
             │                                                                    │
             │          [支払者修復 A1/A2: GE PAC・Prudential HI-led・定額]            ▼
             │                              │                               [B2-i-1] 承継プログラム
12〜24か月 [A3-2] Orchard SPC ──▶ [B2-ii-2] Orchard ACC                     ハイブリッド手術室・カテ室・ICU
             │
24〜36か月 [A3-3] East ──▶ 循環(買戻し・後継者プール) ──▶ [B2-i-2] 年10〜20件の承継、がん・循環器の個別設計
```

1. **A3→B2-ii→B2-iの順**。ASC持分(A3)が先に動けば、同じ施設に外来を併設するだけでACC(B2-ii)になり、空いたスイートが承継(B2-i)の受け皿になる。
2. **支払者修復は並行**。ASC/ACCは施設単位でPPCに入れるため病院の修復を待たないが、B2-iの入院ロイヤルティは病院の修復なしに戻らない。
3. **層D(加入経路・EMR・事務)はA3・B2-iiの提案に同梱**する。独立医のパネル数はグループ医より少なく(§3-3)、持分だけではグループの提案に負ける。

### 6-2. 資本配分の目安【推定】

| 項目 | 規模の目安 | 根拠 |
|---|---|---|
| ASC/ACC 2〜3拠点の内装・設備(不動産を持たない場合) | 拠点あたりS$3〜8百万、合計S$10〜20百万程度 | FAC Novena(手術室4)S$2.5百万、画像S$5.4百万【確認】。外来併設・画像を含めば上振れ |
| 施設SPCの医師持分 | IHHの持分売却(30〜49%)で資本の一部を回収 | FMV割当 |
| ハイブリッド手術室・カテ室・ICU | 病院側の設備投資(別途) | 【未検証】 |
| スイート流動化(選択肢) | 1戸あたりS$数百万〜(GMCの売り出し例S$9.08百万/603平方フィート【確認】)で資本集約的。限定運用に留める | ihh-sg-medical-suite-specialists.md §3-1 |
| 組織 | アウト・オブ・ホスピタル専任組織。Foundationは本社71人で108人を支える【確認】 | 認定医1,000人規模への提供には専任組織が要る |

- 比較対象: 病院のPLife REIT賃料S$97.2百万/年【確認】、IHH SGの2Q26 EBITDAマージン29%・稼働率51%〔B〕。ASC/ACCは病院に比べて桁違いに軽い投資で、症例の配分を決める立場を取り戻す手段である。

### 6-3. 三井物産の関与(選択肢)【分析】

主体はIHHだが、資本の出し手として三井物産が入る形は検証文書M3(三井が建物・過半を持ちIHHが少数+運営)と同じ施策になる。利点は IHHのアセットライト維持と「病院そのものではない」外形、欠点はBursaの関連当事者取引とIHHの他株主(Khazanah等)との関係。本書ではIHH単独資本を基本形とし、不動産(ACC建物)の保有のみ三井または REITの選択肢とする。

### 6-4. 組織とKPI【分析】

- Mount Elizabeth病院CEOとParkway Shenton CEOの兼務を解消し、ASC・ACC・承継・提携プログラムを一体で持つアウト・オブ・ホスピタル専任の責任者を置く(既往レポートの提言と同じ)。
- 全体KPIは単価ではなく「症例のグループ内捕捉率×回転×原価」。入院単価は保険者とベンチマークが抑える前提に立つ。

---

## ⑦ 未確認事項(実行前に埋めるべきDD項目)【未検証】

| 区分 | 事項 | 本書のどこに効くか |
|---|---|---|
| 社内データ | 認定医ごとの日帰り件数の施設別配分、入院症例のIHH配分比率(ロイヤルティ)の推移 | A3の対象選定、B2-iのKPI基準値 |
| 社内データ | 病院内日帰り手術室・Royal Squareの稼働率、術式別件数、第三者医師比率 | A3の容量計画 |
| 契約 | Royal Squareのリース条件・追加フロアの可否、Annexeの賃貸条件 | A3・B2-iiの立地 |
| 契約 | PCC(TalkMed)のConsultancy Restatement Agreementの期限・専属・支配権変更条項 | B2-i(がん) |
| 医師 | 入院依存科の独立医の引退予定・後継の有無、非入院科の移転意向、競合ASC・グループへの持分保有 | B2-i・B2-iiの対象母数 |
| 不動産 | 分譲スイートの所有者・年齢・空室・売却動向(SLA/URA区分所有記録) | B2-iの受け皿 |
| 保険者 | GEとの協議状況(PAC再開条件)、PrudentialのIHH病院HI-led参加の可否、各ASC/ACCのPPC・DSC認定の手続と所要期間 | 前提条件、A3・B2-iiのパネル接続 |
| 規制 | SMCの施設持分配当の解釈、CCCSの医師グループ・JVに対する見解、HCSAのASC/ACCライセンス要件(複数ライセンスの束)と申請所要期間、MediSave認定の要件 | §2の標準装備 |
| 認定 | 現行の認定(入院権限)基準・審査体制 | B2-i(b) |
| 競合 | Foundationの2H26買収対象、FAC・Mount Alvernia・Curaの稼働、Eye & Retina Surgeons・gutCAREの意向 | A3・B2-iiの時間軸 |
| 株主 | 三井物産の関与意向、IHH取締役会の関連当事者取引の扱い | §6-3 |

---

## ⑧ 主要出典

**A = 姉妹文書で原文を取得して本文確認(本書はその事実を引用)**

1. Singapore Medical Council「2016 Ethical Code and Ethical Guidelines」(H3 Financial conflicts of interest pp.61〜62、広告の金銭的誘因禁止p.55) — https://isomer-user-content.by.gov.sg/77/775548fb-11df-4393-89c5-33717769ccf6/2016-smc-ethical-code-and-ethical-guidelines---(13sep16).pdf
2. HCSA「Ambulatory Surgical Centre Service」 — https://www.hcsa.gov.sg/outpatient-services/ambulatory-surgical-centre-service/ ／ Healthcare Services (Ambulatory Surgical Centre Service) Regulations 2023 — https://sso.agc.gov.sg/SL/HSA2020-S411-2023
3. Competition Commission of Singapore「CCS Decides against SMA Guidelines on Fees」(2010年8月19日) — https://www.ccs.gov.sg/media-and-consultation/newsroom/media-releases/ccs-decides-against-singapore-medical-association-sma-guidelines-on-fees ／ Allen & Gledhill「CCCS issues Business Collaboration Guidance Note」(2022年1月) — https://www.allenandgledhill.com/sg/publication/articles/20008/cccs-issues-business-collaboration-guidance-note-to-enable-businesses-to-collaborate-with-greater-confidence
4. MOH「New Requirements for Integrated Shield Plan Riders…」(2025年11月26日。自己負担上限はパネル/事前承認のみ) — https://www.moh.gov.sg/newsroom/new-requirements-for-integrated-shield-plan-riders-to-strengthen-sustainability-of-private-health-insurance-and-address-rising-healthcare-costs/
5. MOH「MediSave and MediShield Coverage for Surgical Procedures」 — https://www.moh.gov.sg/newsroom/medisave-and-medishield-coverage-for-surgical-procedures/
6. Prudential Singapore「PRUPanel Connect — Participating Healthcare Institutions」(2025年10月14日時点。eLOG病院S$30,000・日帰り手術センターS$15,000) — https://www.prudential.com.sg/ppc
7. IHH Healthcare×Prudential「IHH Healthcare and Prudential partner to offer policyholders more day surgery care options at Mount Elizabeth Royal Square」(2026年8月17日) — https://www.media-outreach.com/news/singapore/2026/08/17/481308/ihh-healthcare-and-prudential-partner-to-offer-policyholders-more-day-surgery-care-options-at-mount-elizabeth-royal-square/
8. IHH Healthcare「Mount Elizabeth Royal Square: Specialised Day Care, All in a Day」(2025年11月4日。手術室2・内視鏡室4、Novena病院から徒歩5分) — https://www.ihhhealthcare.com/newsroom/care-in-action/mount-elizabeth-royal-square-specialised-day-care-all-in-a-day
9. IHH Healthcare「IHH Singapore Collaborates with Insurers to Improve Affordability of Private Hospital Care」(2026年7月10日) — https://www.ihhhealthcare.com/newsroom/care-in-action/ihh-singapore-collaborates-with-insurers-to-improve-affordability-of-private-hospital-care
10. IHH Healthcare「IHH Healthcare delivers double-digit growth in Q2 2026」(2026年8月27日、SGX) — https://links.sgx.com/1.0.0/corporate-announcements/C041XU6YZZFQH0CK/902593_IHH%20Q2%202026_Press%20Release%2027.08.2026.pdf
11. Foundation Healthcare Holdings「1H2026 Earnings Call Script」(2026年8月13日、SGX。hospital-agnostic、FAC Novena手術室4・内視鏡室2、第三者専門医の症例、新規医の初年度売上、2H26買収再開) — https://links.sgx.com/1.0.0/corporate-announcements/W24OZ7ZOF8FK4CPV/901088_FHH%201H26%20Earnings%20Call%20Script.pdf
12. Foundation Healthcare Holdings 目論見書(60/40、モラトリアム1〜10年、MP1/MP2、本社71人) — sg-four-specialist-groups-incentives-growth.md 出典参照
13. HC Surgical Specialists: NYK Endoscopy 51%取得(2026年6月、医師49%+11年コミットメント) — https://www.theedgesingapore.com/news/ma/hc-surgical-acquires-51-stake-nyk-endoscopy-and-digestive-centre-750000 ／ AR2025 — https://www.hcsurgicalspecialists.com/files/090925-HC-Surgical-AR2025-Full%20Set.pdf
14. Novena Surgery(2008年〜、Alfa Medicus) — https://novenasurgery.com.sg/about/
15. 42 CFR 1001.952(r) ASCセーフハーバー、Tenet 10-K FY2024(USPIの買取義務)、Medical Economics(2012)・AAFP FPM(2004)の買入れ・買戻し契約 — sg-specialist-groups-succession-design.md 出典参照
16. Allen & Gledhill「Health Information Bill passed…」(2026年1月12日可決、2027年初施行予定) — https://www.allenandgledhill.com/sg/publication/articles/32164/health-information-bill-passed-to-establish-framework-for-the-safe-collection-and-sharing-of-health-information
17. LIA「Insurance Panel of IP Insurers」2025年2月版(HSBC Life=Fullerton、Singlife=iXchange) — https://www.lia.org.sg/media/4476/insurance-panel-of-ip-insurers_application-process-requirements-and-consideration_20250225.pdf
18. 本リポジトリ一次データ: `data/ihh-sg-specialists-directory-2026-10.csv`(1,295人、2026年10月8日取得)、`data/ihh-sg-specialists-summary-2026-10.json`。本書の【算出】は同CSVの再集計(Python標準ライブラリ)。入院依存度の区分はihh-sg-inpatient-loyalty-asc-payor-strategy.md §4-1の定義に従い、非入院10科は眼科・消化器・ENT・皮膚科・形成外科・手外科・口腔外科・内分泌・精神科・リウマチとした

**B = 検索エンジン経由で要旨を確認**

19. Mothership「Great Eastern suspends pre-authorisation certificates for Mount Elizabeth admissions…」(2025年6月。日帰り手術センターへの事前承認は継続) — https://mothership.sg/2025/06/great-eastern-suspends-pre-authorisation-certificates-for-mount-elizabeth-admissions-due-to-higher-costs-than-other-private-hospitals/
20. Growbeansprout「Foundation Healthcare Initiation Report」(FAC Novena 1日36〜40件、FAC Orchard 14〜16件) — https://cdn.growbeansprout.com/strapi-uploads/Foundation_Healthcare_Initiation_Report_983e54796a.pdf
21. Vatican News「Singapore Catholic non-profit hospital expands services」(2026年5月。Mount Alvernia新DSC手術室4、ICU/HDU 16室) — https://www.vaticannews.va/en/church/news/2026-05/singapore-catholic-non-profit-hospital-expands-services.html
22. The Edge Singapore(EdgeProp)「Three F&B strata units at Royal Square mall for sale」(Hoi Hup–Sunway JV、99年リース、医療スイート171戸) — https://www.edgeprop.sg/amp/property-news/three-fb-strata-units-royal-square-mall-sale-198-mil
23. The Star「IHH Healthcare remains confident on growth trajectory」(2026年8月27日。SG入院▲6%・稼働率51%・マージン29%) — https://www.thestar.com.my/business/business-news/2026/08/27/ihh-healthcare-remains-confident-on-growth-trajectory
24. Cura Day Surgery — https://curadaysurgery.com/ ／ HMI StarMed — https://www.hmi.com.sg/starmed-specialist-centre-provides-one-stop-ambulatory-care/
25. 価格: Curasia(外来vs入院の内視鏡費用) — https://www.curasia.com/outpatient-vs-inpatient-endoscopy-cost-explained/ ／ health365(白内障費用、2025年8月) — https://www.health365.sg/cataract-surgery-cost-singapore/
26. The Hospitalist「Adoption of Hospitalist Care in Asia」 — https://mdedge.com/content/adoption-hospitalist-care-asia-experiences-singapore-taiwan-korea-and-japan

**姉妹文書(本リポジトリ)**: ihh-sg-hypotheses-verification.md(§12-4・§12-5・§13-3・§16・§17-3)、ihh-sg-inpatient-loyalty-asc-payor-strategy.md(§4〜§8)、ihh-sg-growth-strategy.md(§A6・§A9)、sg-asc-acc-market-report.md(§2・§5・§6)、sg-specialist-groups-succession-design.md(§4.6・§5)、sg-four-specialist-groups-incentives-growth.md(§4・§6)、ihh-sg-medical-suite-specialists.md(§3・§6)、sg-specialist-group-typology.md、ihh-mitsui-specialist-network-acquisition.md、parkwayshenton-divestment-strategy.md、bor-decline-countermeasures.md

---

*本書の【分析】【推定】は上記出典と一次データからの筆者の整理であり、実行判断には社内データ(日帰り件数・入院配分)、契約(Royal Squareリース・PCC)、保険者の意思、SMC・CCCS・HCSAに関する法的助言を要する。*
