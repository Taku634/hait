# 米国急性期病院の Out of Hospital 戦略 v2 — HCA・Tenet・AMC×Regent・Mayo の事例と「高難度症例のASC/ACC化」

**作成日**: 2026年9月11日(v1同日作成の「us-out-of-hospital-strategy-cases.md」を統合・拡張)
**位置づけ**: 「bor-decline-countermeasures.md」(BOR低下対応策)および「ihh-sg-growth-strategy.md」の補完資料。第I部は米国の急性期病院グループが「病院の外(Out of Hospital)」へ症例と収益を移す戦略を4類型(営利チェーンHCA・Tenet、非営利AMC3系統×ASC運営会社Regent、Mayo Clinic)で整理する(v1の内容を収録)。第II部は、**各グループがASC(日帰り手術センター)・ACC(外来医療センター)・在宅で扱う疾患領域・症例の幅・難易度をどこまで広げているか**を、その目的と制度的背景とともに整理する。第III部はIHH SGへの示唆、第IV部は調査に用いたドメイン一覧と未検証事項。

**調査方法と信頼性の注記**: 英語Web調査に基づく。本セッションの実行環境では企業IR・ニュースルーム・SEC EDGAR・業界メディア・学会サイトの大半がネットワーク遮断(egress proxy)されており、原典本文を直接取得できたのは**CMS(cms.gov)のファクトシート**と**PMC掲載論文の一部**に限られる。それ以外の数値は検索エンジン経由で得た記事・プレスリリースの要約に依拠している。出典URLは各項目に併記したが、原典本文で照合できていない項目は引用前に再確認されたい(第IV部)。推測は書かず、根拠のない項目は記載していない。

---

## 総括

1. **共通の背景**は、待機的手術・処置の入院→外来(ASC等)への移行と、保険者(CMS・民間)による低コストサイトへの誘導である。病院外来の手術料金はASC比で平均101〜167%高いとされ(Cleveland Clinic発表を伝えるHealthcare Finance News)、ASCが誘導の着地先になっている。
2. **HCA(営利・病院中心)**は「病院1つに外来拠点15→18〜20」の**市場密度モデル**。2025年末で病院190・外来拠点約2,500、外来収益比率38.4%(2025年通年)、2025年に外来拠点約100増。緊急ケア(Urgent care)・独立型ER(Freestanding ER)を病院への送客網として優先し、ASC(Surgery Ventures、約150施設・医師パートナー3,400人超)は自社開発(greenfield)を軸にする。
3. **Tenet(営利・ASC中心へ転換)**は「病院を売ってASCを買う」。2024年に病院14を約$5bnで売却し、病院は50(2025年末)。USPIはASC 533+外科病院26(2025年末、37州)、2025年売上$5.2bn・調整EBITDA約$2.0bn(全社$4.6bnの約44%)。2025年もASC 34施設を追加($339m)。
4. **AMC×Regent(非営利AMCの「持たない/共同保有」型)**。Regent Surgical(2001年設立、ASC 26施設・13州超、TowerBrookとAscension Capitalが2021年に出資)は、AMCが**過半数を持ちブランドを冠する**JVでASCを開発・運営する。Ascension(2021年、全国独占パートナー)、MGB(2025年2月、MGB 70%、第1号は内視鏡ASC。**医師持分ゼロ**が特徴)、Cleveland Clinic(2025年5月、CC過半数、全米展開)。AscensionはさらにAmSurgを$3.9bnで買収(2025年6月合意、2026年8月FTC同意命令を経て完了、ASC約300施設)し、病院は売却(2025年第1四半期だけで13病院)する「病院縮小・外来拡大」を明確化した。
5. **Mayo Clinic(デスティネーション型AMC)**は「病院を家へ」。2020年7月にMedically Homeと組み高急性度の**在宅入院(Advanced Care at Home)**を開始、2021年にKaiser Permanenteと共同で同社へ$100m出資。2020年以降3,300人超に提供(2024年8月時点)、再入院率15%低、NPS 94。並行してロチェスター本院を「入院・外来・バーチャルを融合し部屋を相互転換できる」設計で再構築(Bold. Forward. Unbound.、約$5bn、2030年まで)。
6. **高難度症例のOut of Hospital化(第II部)**は、(a) **制度**がまず動いた——CMSはCY2026最終規則で「入院限定(IPO)リスト」の3年廃止を開始(初年度は筋骨格系中心の285手技を除外)し、ASC対象手技リストに289+271手技を追加、心臓カテーテルアブレーションを初めてASCで償還(2026年1月1日〜)。CY2027提案規則では第2年として消化器・泌尿器・呼吸器等の638サービスを除外予定。(b) **営利チェーン**は整形(人工関節・脊椎)→泌尿器・ロボット→心臓の順に難度を上げるが、Tenet CEOは心臓について「変革的にはならない」と慎重(循環器医の病院雇用、設備コスト、Medicare比率の高さ)。(c) **AMC**はASCでは内視鏡・整形・眼科・小手術という「待機リストの解消」に軸足を置き、高難度は**在宅入院**(MGB Home Hospital 1日50〜60人・術後・腫瘍へ拡大、Cleveland Clinic 4,000人超・術後大腸手術を含む、Mayo ACH 骨髄移植・腎移植後・透析・在宅化学療法)で扱う。(d) 学会(HRS/ACC、2025年11月)は「適切に選択された症例」に限りASCでのアブレーションを支持し、患者選択・搬送体制・品質保証を条件とした。

---

# 第I部 4類型の Out of Hospital 戦略(v1収録)

## 1. 比較表

| 項目 | HCA Healthcare | Tenet / USPI | AMC × Regent (Ascension・MGB・Cleveland Clinic) | Mayo Clinic |
|---|---|---|---|---|
| 主体の性格 | 営利・最大手病院チェーン | 営利・ASC最大手を内包 | 非営利AMC/大規模非営利+JV特化のASC運営会社 | 非営利・デスティネーションAMC |
| Out of Hospitalの主戦場 | Urgent care・独立型ER・ASC・医師クリニック | ASC(USPI) | ASC(AMCブランド、AMC過半数JV)+在宅入院 | 在宅入院(hospital at home)+本院の入院・外来融合 |
| 規模(最新) | 病院190、外来拠点約2,500(2025年末)、うち独立型外科センター121 | ASC 533+外科病院26(2025年末)、病院50 | Regent: ASC 26(13州超)。Ascension: AmSurg買収でASC約300 | ACH: 3,300人超(2020〜2024年8月) |
| 財務指標 | 外来収益比率38.4%(2025年)、Q4 2025は39.7% | USPI売上$5.2bn、調整EBITDA約$2.0bn=全社の約44%(2025年) | 公表なし(MGBのCambridge ASCは約$7.4m投資) | 再入院率▲15%、NPS 94(Mayo Magazine) |
| 資本配分 | 2025年に外来拠点約100追加、2026年Q1に約$260m買収(主に独立型ER・Urgent care)、2028年までの開発案件$7bn承認済 | 2024年に病院14売却(約$5bn)、2025年ASC M&A $339m、2026年も年$250m規模(Q1で$125m・7施設) | Ascension: AmSurg $3.9bn+病院売却。CC/MGB: Regentと共同投資 | Medically Homeへ$100m(Kaiserと共同、2021年)、本院再開発約$5bn |
| 医師との関係 | 病院雇用+ASC持分(Surgery Ventures 医師パートナー3,400人超) | 施設単位のUSPI+医師+医療システムの3者持分 | Ascension: 医師持分あり(例: Austin整形ASC、AmSurgは医師主導JV)。MGB: **医師持分ゼロ** | 雇用医師(Mayoモデル) |
| 目標・KPI | 病院1つあたり外来拠点18〜20(2020年代末) | 2026年USPI売上$5.5〜5.7bn、EBITDA $2.13〜2.23bn | MGB: 内視鏡待機26,500人超の解消 | 2030年までにロチェスター再構築完了 |

## 2. HCA Healthcare — 「病院1つに外来拠点18〜20」の市場密度モデル

- **規模**: 2025年12月31日時点で病院190、外来拠点約2,500(ASC・独立型ER・Urgent care・医師クリニック)、19州+英国。2025年末の独立型外科センターは121。年間4,700万件の患者接点(CEO Hazenの下院歳入委員会証言、2026年4月)。
  - 出典: HCA Q4 2025決算発表 https://investor.hcahealthcare.com/news/news-details/2026/HCA-Healthcare-Reports-Fourth-Quarter-2025-Results-and-Provides-2026-Guidance/default.aspx / Becker's ASC https://www.beckersasc.com/asc-transactions-and-valuation-issues/hcas-2025-revenue-surpassed-75b-10-things-to-know/ / 下院歳入委員会 証言PDF https://waysandmeans.house.gov/wp-content/uploads/2026/04/Hazen-HCA-Testimony-1.pdf
- **外来収益比率**は緩やかに上昇: 36.5%(2020)→37.6%(2021)→37.9%(2022)→37.5%(2023)→**38.4%(2025年通年)、Q4 2025は39.7%**。
  - 出典: HCA 8-K(FY2023) https://www.sec.gov/Archives/edgar/data/860730/000119312523016833/d268135dex991.htm / Becker's ASC(上記)
- **拠点密度の目標**: 現在は病院1つあたり外来拠点約15。**2020年代末までに18〜20**へ。2025年に外来拠点約100を追加し、2026〜27年も「相当な資本がパイプラインにある」(Hazen)。2028年までの開発案件として$7bnを承認済み。
  - 出典: ASC News(2026年1月) https://ascnews.com/2026/01/hca-accelerates-outpatient-strategy-as-growth-shifts-beyond-hospitals/ / Becker's https://www.beckershospitalreview.com/finance/hcas-outpatient-boom-reshapes-its-care-network/ / Q4 2025決算説明会(The Motley Fool書き起こし) https://www.fool.com/earnings/call-transcripts/2026/01/27/hca-healthcare-hca-q4-2025-earnings-transcript/
- **優先順位**: 2026年Q1の買収約$260mは「主に独立型ERとUrgent care、次いでASC」。Urgent careは340拠点超・年420万件(2026年初)。ASCは長期戦略の中核だが、直近はUrgent care・医師クリニック・独立型ERへ傾斜。ASCは買収より自社開発(greenfield)を重視。
  - 出典: Fierce Healthcare https://www.fiercehealthcare.com/providers/freestanding-eds-urgent-care-acquisition-opportunities-abound-hca-healthcare / ASC News(2025年3月) http://ascnews.com/2025/03/ambulatory-surgery-centers-remain-key-to-hcas-market-strategy-ceo-says/ / Becker's ASC https://www.beckersasc.com/asc-transactions-and-valuation-issues/hcas-greenfield-asc-development-strategy/
- **含意**: HCAのOut of Hospitalは「病院を守るための外来」であり、入院を減らす発想ではない。Urgent care・独立型ERは救急・入院への送客口、ASCは待機症例の受け皿として、同一都市圏で面を取る。

## 3. Tenet / USPI — 「病院を売ってASCを買う」

- **ポートフォリオ転換**: 2024年に病院14を売却(総額約$5bn。Becker'sは合計$4.8bnと報道)。2025年末の病院数は50。CEO Sutaria「USPIへの投資加速が社内で最も価値増加に寄与する(single most accretive)」。
  - 出典: Healthcare Finance News https://www.healthcarefinancenews.com/news/ambulatory-surgery-centers-drive-tenets-strong-q4-results / Becker's https://www.beckershospitalreview.com/hospital-transactions-and-valuation/how-hca-tenet-and-chs-hospital-portfolios-shifted-in-2025/ / Healthcare Dive https://www.healthcaredive.com/news/tenet-healthcare-earnings-fourth-quarter-2024/740033/
- **USPIの規模と収益**: 2025年12月31日時点でASC 533(連結401)+外科病院26、37州。2025年売上$5.2bn(+14.1%)、調整EBITDA約$2.0bn(2024年$1.81bn)。全社調整EBITDA $4.6bnの約44%。同一施設の症例単価は+7.1%、外科症例数は+0.3%(単価主導の成長)。
  - 出典: Tenet Q4/FY2025決算発表 https://investor.tenethealth.com/press-releases/press-release-details/2026/Tenet-Reports-Strong-Fourth-Quarter-and-FY-2025-Results-Provides-2026-Financial-Outlook/default.aspx / Becker's ASC https://www.beckersasc.com/asc-transactions-and-valuation-issues/uspi-revenue-climbs-to-5-2b-10-things-to-know/
- **投資ペース**: 2025年にASC 34+外科病院1を追加(新設6、支配持分取得28)、M&A約$339m。2026年見通しはUSPI売上$5.5〜5.7bn、EBITDA $2.13〜2.23bn。2026年Q1にASC 7施設を$125mで取得。
  - 出典: Becker's ASC https://www.beckersasc.com/asc-transactions-and-valuation-issues/uspi-splashed-350m-added-35-facilities-in-2025/ / https://www.beckersasc.com/asc-transactions-and-valuation-issues/where-uspi-wants-to-win-next/
- **含意**: 保険者誘導の着地先(ASC)を自社資産にし、入院で失う症例をASCのマージンで取り返す。病院は「予測可能で資本効率の高い」少数のコア市場に絞る(Sutaria)。

## 4. AMC × Regent Surgical — 「AMCが過半数を持ち、運営はRegent」

**Regent Surgical(旧Regent Surgical Health)**: 2001年設立、医療システム・医師グループとのJVでASCを開発・保有・運営。2021年3月4日にTowerBrook Capital PartnersとAscension Capital(Ascensionの投資部門)が出資(当時ASC 21施設)。2026年1月時点でASC 26施設・13州超。CEOはTravis Messina(在宅入院企業Contessa Healthの創業者)。
- 出典: PR Newswire https://www.prnewswire.com/news-releases/regent-surgical-health-announces-strategic-investment-from-towerbrook-and-ascension-capital-301240926.html / PESP報告書(2025年10月) https://pestakeholder.org/wp-content/uploads/2025/10/PESP_Report_Ambulatory-Surgical-Centers_2025-compressed.pdf / Becker's ASC https://www.beckersasc.com/asc-transactions-and-valuation-issues/run-toward-areas-others-avoid-regents-new-asc-playbook-in-a-turbulent-market/

### 4-1. Ascension(全米最大の非営利・カトリック系)
- 2021年3月、Regentを**ASC開発の全国独占パートナー**に選定。Ascensionの各地域で共同開発・買収・運営。例: Orthopedic Surgery Center of Central Texas(Austin、Regent+Ascension Texas+医師のJV)、Birmingham消化器ASC(約$7.7m、2022年)。
  - 出典: Ascension https://about.ascension.org/news/2021/03/ascension-chooses-regent-surgical-health-as-exclusive-national-ambulatory-surgery-center-partner / Regent https://regentsurgicalhealth.com/regent-surgical-health-and-ascension-texas-joint-venture-on-the-orthopedic-surgery-center-of-central-texas/ / Becker's ASC https://www.beckersasc.com/new-asc-development/regent-ascension-to-open-joint-7-7m-asc-in-alabama/
- **病院縮小と外来拡大の同時進行**: Illinoisの9病院をPrime Healthcareへ売却(2025年Q1完了)。2025年の最初の3か月で13病院を売却し、ASC・医師診療・在宅/バーチャル・画像・薬局へ投資を振り向けた。
  - 出典: Healthcare Dive https://www.healthcaredive.com/news/ascension-prime-healthcare-midwestern-deal/722489/ / Hospitalogy https://hospitalogy.com/articles/2025-06-24/ascension-seals-the-deal/
- **AmSurg買収**: 2025年6月に$3.9bnで合意。FTCは7施設(Nashville、Panama City、Tulsa、Waco、Wichita)の売却を条件に2026年6月に同意命令、8月に最終承認し完了。AscensionのASC網は約300施設へ。CEO Conradoは「25の新市場に入り、独立医師・他システムとの提携の入口になる」と説明(JPM 2026)。
  - 出典: Ascension https://about.ascension.org/news/2025/06/ascension-enters-into-an-agreement-to-acquire-amsurg / https://about.ascension.org/news/2026/06/ascension-and-amsurg-come-together-to-serve-more-communities / FTC https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-requires-divestiture-ambulatory-surgery-centers-protect-patients-anticompetitive-effects / https://www.ftc.gov/news-events/news/press-releases/2026/08/ftc-approves-final-consent-order-ascension-health-amsurg-deal / Fierce Healthcare https://www.fiercehealthcare.com/providers/jpm26-ascension-ceo-says-asc-megadeal-opens-new-markets-partnership-opportunities

### 4-2. Mass General Brigham(MGB)
- 2025年2月25日発表。New England Surgery Center Holdings, LLC(MGB 70%)を通じ、New Englandで整形・小手術・眼科・内視鏡のASCを新設。狙いは待機時間短縮・アクセス改善・コスト低減。
  - 出典: Business Wire https://www.businesswire.com/news/home/20250225612382/en/Mass-General-Brigham-Announces-Collaboration-with-Regent-Surgical / Boston Globe https://www.bostonglobe.com/2026/02/11/business/boston-endoscopy-procedures/
- **第1号はCambridgeの内視鏡ASC**: 処置室3・前後回復ベイ10・6,095平方フィート・約$7.4m。2025年9月15日にDetermination of Need申請、2026年2月に州Public Health Councilが承認。MGBは規制当局に「AMCで内視鏡待機が26,500人超」と説明。
  - 出典: Becker's ASC https://www.beckersasc.com/new-asc-development/mass-general-brigham-earns-con-approval-for-endoscopy-asc/ / Boston Globe(上記)
- **医師持分ゼロ**: Regentは「医師がASCの持分を持たないと関与が得られない、というのは思い込み」とし、部屋の回転・スケジューリング・予測可能な臨床体験で医師を引き付ける設計をMGBで採用。
  - 出典: Regent Surgical(Hospitalogy対談の要約) https://regentsh.com/25k-patients-deep-and-zero-physician-equity-inside-mgb-and-regents-site-of-service-bet-and-their-new-asc-ownership-playbook/

### 4-3. Cleveland Clinic
- 2025年5月7日発表。Cleveland ClinicがJVの**過半数を保有し全ASCにブランドを冠する**。米国内の各市場で今後のASCを共同開発。CEO Mihaljevic「ASCは医療システムが手術へのアクセスを広げ、提供を効率化する重要な場。Regentの運営能力により、我々は最高品質のケアに集中し、より多くの患者へ提供できる」。
  - 出典: Cleveland Clinic Newsroom https://newsroom.clevelandclinic.org/2025/05/07/cleveland-clinic-to-partner-with-regent-surgical-for-ambulatory-surgery-centers / Healthcare Finance News https://www.healthcarefinancenews.com/news/cleveland-clinic-partners-regent-surgical-ambulatory-surgery-centers / Modern Healthcare https://www.modernhealthcare.com/providers/cleveland-clinic-regent-surgical-joint-venture/

**AMC×Regent型の含意**: AMCは(a)ASC運営のノウハウと開発資本を外部化し、(b)過半数持分とブランドで症例と患者関係を手放さず、(c)病院の手術室・病床を高acuity症例へ解放する。Regentの立場では「ASCを買わずにスケールする」PE型モデル。

## 5. Mayo Clinic — 「病院を家へ」と「入院・外来の境界をなくす本院」

- **Advanced Care at Home(ACH)**: 2020年7月にJacksonville(FL)とEau Claire(WI)で開始、2021年9月にPhoenix(AZ)へ拡大。Medically Homeの技術基盤と指令センター、在宅での点滴・看護・検査・画像・リハを組み合わせる「バーチャル・ハイブリッド型」の在宅入院。
  - 出典: Mayo Clinic News Network https://newsnetwork.mayoclinic.org/discussion/mayo-clinic-launches-advanced-care-at-home-model-of-care/ / BMC Health Services Research(2023) https://pmc.ncbi.nlm.nih.gov/articles/PMC10041490/
- **資本・政策**: 2021年5月、Kaiser Permanenteと共同でMedically Homeへ計$100mを出資し、Advanced Care at Home Coalition(Geisinger、Johns Hopkins、UNC等)を結成してCMSの在宅入院ウェイバー延長を働きかけ。Medically Homeは2025年にDispatchHealthと統合。
  - 出典: Healthcare IT News https://www.healthcareitnews.com/news/mayo-clinic-kaiser-put-100m-toward-hospital-home-care / Fierce Healthcare https://www.fiercehealthcare.com/hospitals/mayo-clinic-kaiser-permanente-recruit-11-health-system-partners-for-new-hospital-at-home / Healthcare Dive https://www.healthcaredive.com/news/dispatchhealth-medically-home-merge-hospital-at-home/742834/
- **実績**: 2020年以降3,300人超に提供(2024年8月時点)。再入院率はACHで15%低く、NPSは94。研究では退院923人の平均年齢70.9歳、APR-DRG重症度2.89、平均在宅入院日数4.10日と、対象は高急性度。
  - 出典: Mayo Magazine(2024年8月) https://mayomagazine.mayoclinic.org/2024/08/at-home-healthcare-programs/ / BMC HSR(上記)
- **Bold. Forward. Unbound. in Rochester**: 約$5bn・6年(2030年完了)、新築5棟・約240万平方フィート。入院・外来・バーチャルを一体化し、検査・画像・診察・処置を同じ「ケア・ネイバーフッド」に集約。「フレキシブル・グリッド」で病室⇔手術室などの相互転換を可能にする。
  - 出典: Mayo Clinic News Network https://newsnetwork.mayoclinic.org/discussion/mayo-clinic-board-of-trustees-approves-plans-to-transform-healthcare-improve-experience-for-staff-and-patients-redesign-rochester-campus/ / Post Bulletin https://www.postbulletin.com/health/mayo-clinic-to-invest-5-billion-in-rochester-including-5-new-buildings-downtown
- **含意**: Mayoは外来拠点を面で増やすのではなく、(a)入院そのものを家へ移す、(b)本院の病床を固定資産ではなく可変資産として設計する、という2方向で「病院に縛られない(Unbound)」を実装している。

---

# 第II部 高難度症例の ASC・ACC・在宅への拡大 — 疾患領域・症例の幅・難易度と目的

## 6. 制度的背景 — CMSが「難度の上限」を引き上げた(原典確認済み)

| 年 | 措置 | 内容 | 出典 |
|---|---|---|---|
| 2020/2021 | ASC対象手技リスト(ASC CPL)へ人工膝関節(2020)・人工股関節(2021)を追加 | Medicareの人工関節置換がASCで償還可能に | NY州のTHA/TKA外来化研究(PMC) https://pmc.ncbi.nlm.nih.gov/articles/PMC12099752/ |
| CY2026最終規則(2025年11月21日) | **入院限定(IPO)リストの3年廃止を開始**。初年度は「主に筋骨格系」の**285手技**を除外 | 「医療の進歩により、より多くの手技を短い回復期間で外来実施できる」(CMS)。除外手技はTwo-Midnightルールの審査免除を継続 | CMSファクトシート(原典確認) https://www.cms.gov/newsroom/fact-sheets/calendar-year-2026-hospital-outpatient-prospective-payment-system-opps-ambulatory-surgical-center |
| 同上 | **ASC CPLの基準改定**: 5つの一般除外基準を撤廃し「拘束力のない医師向け安全考慮事項」へ移行。結果として**289手技**を追加。さらにIPOリストから除外した**271コード**をASC CPLへ追加 | 「医師が医学的判断を行使し、患者が手術のより多くの提供場所から選べるようにする」(CMS) | 同上 |
| 同上 | **心臓カテーテルアブレーションを初めてASC CPLへ追加**(2026年1月1日〜)。CPT 93650/93653/93654/93656等 | CY2025規則では「処置当日深夜に能動的な医療監視を要する入院を伴う」として見送られていたが、CY2026で転換。ACC/HRSは「大きな勝利」と評価 | ACC https://www.acc.org/latest-in-cardiology/articles/2025/11/21/22/22/cms-releases-2026-hospital-opps-final-rule / MedTech Dive https://www.medtechdive.com/news/CMS-Medicare-cardiac-ablation-ASCs/806548/ / Heart Rhythm Advocates https://www.heartrhythmadvocates.org/ep-asc-covered-procedures |
| CY2027提案規則(2026年7月2日) | IPO廃止の第2年として**638サービス**(聴覚・消化器・内分泌・女性/男性生殖器・血液リンパ・皮膚・産科・縦隔横隔膜・呼吸器・泌尿器)を除外提案 | 筋骨格系に続き、消化器・泌尿器・呼吸器など内臓外科へ拡大 | CMSファクトシート(原典確認) https://www.cms.gov/newsroom/fact-sheets/calendar-year-2027-hospital-outpatient-prospective-payment-system-opps-ambulatory-surgical-center |
| 2025年11月 | **HRS/ACC共同声明**「ASCにおける心内アブレーション実施の指針」 | 「技術的・手技的進歩と同日退院プロトコルを活用すれば、適切に選択された心臓EP手技(アブレーション、デバイス植込み)はASCへ移行し得る」。ただし臨床医・政策当局・保険者の協働、安全性検証、支払政策の調和、公平なアクセス、厳格な品質保証枠組みを条件 | HRS https://www.hrsonline.org/news/hrs-acc-joint-statement-ablation-asc/ / JACC https://www.jacc.org/doi/10.1016/j.jacc.2025.10.044 |
| 在宅入院 | CMS Acute Hospital Care at Homeウェイバー(2020年11月〜) | 2026年歳出法で2030年まで延長との報道【要確認】 | AHA https://www.aha.org/fact-sheets/2024-08-06-fact-sheet-extending-hospital-home-program |

**要点**: 米国では「どこまで難しい手技をASCで行えるか」の上限を、まずMedicareの償還ルールが定義している。CY2026規則は(1)筋骨格系の入院限定を解除、(2)ASCの除外基準を「拘束力のない考慮事項」に緩め、(3)心臓EPを解禁、という三段の引き上げであり、各グループの高難度化はこの上に乗っている。

## 7. 安全性・アウトカムのエビデンス(高難度症例のASC化を支える根拠)

- **人工関節(TJA)**: 病院外来(HOS)とASCで外来TJAを比較した前向き研究(123例、THA 77・TKA 46、1年追跡)では、ASC群は**59例中59例(100%)が同日退院**、病院群は64例中55例(86%)が同日退院。**両群とも術後90日の再入院はゼロ**、1年時の患者報告アウトカムに有意差なし。「同日退院の外来人工関節手術は病院・ASCのいずれでも安全かつ有効に実施できる」と結論(原典確認)。
  - 出典: PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC11754168/
- **人工関節のASC移行の規模**: 米国人工関節レジストリ(AJRR)2025年報告では、ASCから報告された症例が**前年比+70%、2021年報告比で約+300%**。登録ASCは93(2023)→107(2024)。
  - 出典: Arthroplasty Today(AJRR 2024/2025ハイライト) https://www.arthroplastytoday.org/article/S2352-3441(25)00114-1/fulltext / PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC13524717/
- **TKAのコスト**: ASCでのTKAは病院外来(HOPD)より90日間の総コスト・入院・ED受診が低いとする観察研究。
  - 出典: PubMed https://pubmed.ncbi.nlm.nih.gov/38870530/
- **心臓EP**: ASCでのEP手技の安全性・実行可能性を報告する研究(Heart Rhythm 2024)と、上記HRS/ACC声明(2025年11月)。
  - 出典: Heart Rhythm https://www.heartrhythmjournal.com/article/S1547-5271(24)03106-0/abstract
- **在宅入院**: Mayo ACHの退院923例はAPR-DRG重症度(SOI)平均2.89・死亡リスク(ROM)2.73、平均在宅入院4.10日。COVID-19群(162例)はSOI 3.41・ROM 3.35と非COVID群より有意に高い(p<0.001)。
  - 出典: BMC Health Services Research(2023) https://pmc.ncbi.nlm.nih.gov/articles/PMC10041490/

## 8. グループ別 — どの領域・どの難度まで病院外へ出しているか、その目的

### 8-1. HCA — 多専門ASCで「軽症〜中等度」を面で取り、高難度は病院に残す

- **ASCの領域**: Surgery Ventures(HCAのASC事業体)は約150の手術・内視鏡センター(16州・40市場)、医師パートナー3,400人超、2023年に患者80万人超。対象専門領域は**大腸肛門外科、消化器、産婦人科、整形外科、耳鼻咽喉科、疼痛管理、足病、手の外科、形成再建、泌尿器、一般外科**。HCA内で**最初のASC人工関節置換プログラム**を立ち上げたのもSurgery Ventures。
  - 出典: HCA Healthcare https://www.hcahealthcare.com/for-physicians/surgery-ventures / Becker's ASC https://www.beckersasc.com/asc-news/150-hca-ascs-by-state/ / Healthcare Dive https://www.healthcaredive.com/news/hca-healthcare-surgery-ventures-texas-surgery-center-acquisition/705397/
- **難度の位置づけ**: 高難度の外来化(人工関節・脊椎・心血管)を認識しつつ、HCAのASC展開は「病院網と地理的に密着した市場単位の配置」で、独立型の大規模展開ではない(VMG Health)。Q4 2025決算説明会では、同一施設の外来手術は▲0.5%、ASC症例は▲1.5%、要因は「Medicaidを中心とする支払者構成」と「耳鼻咽喉科など**低強度症例の減少**」であり、外来手術全体では収益・利益は増加。
  - 出典: VMG Health https://vmghealth.com/insights/published-article/ascs-in-2025-a-year-in-review/ / HCA Q4 2025決算説明会(The Motley Fool) https://www.fool.com/earnings/call-transcripts/2026/01/27/hca-healthcare-hca-q4-2025-earnings-transcript/
- **在宅入院**: HCAの在宅入院プログラムに関する公表情報は本調査では確認できなかった(未確認)。
- **目的**: (a)同一都市圏の救急・待機症例を病院へ集める送客網(Urgent care・独立型ER)、(b)ASCで待機的・軽症〜中等度手術の症例と医師を囲い込む、(c)高acuity(救急入院、複雑手術)は病院に残す。外来収益比率が緩やかに上昇(36.5%→38.4%)する一方、入院手術は横ばいで、HCAは「病院を守るための外来」を貫いている。

### 8-2. Tenet / USPI — 整形(人工関節・脊椎)→泌尿器・ロボット→心臓、の順に難度を上げる

- **整形が第一の成長軸**: CEO Sutariaは整形外科を「今後5〜10年のこのセグメントの**第1の成長ベクトル**」と位置づけ。USPIのASCで人工関節置換は前年比+19%(2024年)、2025年も**同一施設で二桁の症例増**。2025年Q3にはSan DiegoのSynergy Orthopedicsと組み「同地域最大の筋骨格系専門ASC」を新設。
  - 出典: Becker's ASC https://www.beckersasc.com/asc-transactions-and-valuation-issues/uspi-bets-big-on-high-acuity-procedures/ / https://www.beckersasc.com/orthopedics-tjr/why-uspi-is-doubling-down-on-ortho-heavy-ascs/ / Becker's Spine https://www.beckersspine.com/spine/uspi-to-capitalize-on-high-acuity-spine/
- **次の領域**: 「高acuityの脊椎と泌尿器」に早期の機会。USPIは**150超のロボット手術プログラム**をASCに持ち(一般外科・泌尿器に集中)、泌尿器プラットフォームを継続拡張、ロボットは「新たな拡張の道」と説明。
  - 出典: Becker's ASC https://www.beckersasc.com/asc-transactions-and-valuation-issues/where-uspi-wants-to-win-next/ / ASC News https://ascnews.com/2026/03/tenet-ceo-saum-sutaria-on-higher-acuity-care-asc-opportunities/
- **低acuityは外へ出す**: Sutariaは「**低acuity・高ボリュームの活動をASCの外へ移す**」機会を検討中と発言。減少しているのは高ボリューム・低acuity領域のみ。すなわちASCの症例構成を意図的に高難度側へシフト。
  - 出典: Becker's ASC(上記「bets big」) / ASC News https://ascnews.com/2026/02/tenet-continues-to-elevate-uspi-amid-inpatient-to-outpatient-migration/
- **心臓(EP・カテーテル)には慎重**: CMSの2026年解禁を受けてもSutariaは「**変革的(transformative)にはならないと思う**」と表明。理由は(1)循環器医の多くが医療システムに雇用されている、(2)ASCに高価な設備投資が要る、(3)対象患者はMedicare比率が高く、ASCが狙う商業保険患者より償還が低い。「幅広い心血管手技に機会はあるが、患者安全と支払者構成の観点から想定より緩やかに進む」。
  - 出典: ASC News(2026年5月) https://ascnews.com/2026/05/i-dont-think-this-is-going-to-be-transformative-tenet-ceo-tempers-expectations-around-cardiovascular-shift/
- **難度の受け皿としての外科病院**: USPIはASC 533に加えて**外科病院26**を保有し、ASCでは扱えない一泊〜短期入院を要する高難度手術の受け皿とする(施設数はTenet決算発表)。
  - 出典: Tenet Q4/FY2025決算発表(上記)
- **目的**: ASCの症例単価と施設マージン(USPI EBITDAマージン約40%、既存文書参照)を引き上げるため、症例構成を「高ボリューム低単価」から「高acuity高単価」へ移す。心臓は制度上可能でも医師雇用・設備・支払者構成の3条件が揃う市場に限定する、という**収益性基準の選別**が特徴。

### 8-3. AMC × Regent — ASCは「待機リストの解消」、高難度は「在宅入院」で

**Regent Surgical(運営会社側の動き)**
- **心臓EPへの参入**: CMSの2026年解禁を受け、Phoenix郊外Avondaleの多専門ASC(Integrated Surgical Center of Arizona)をネットワークに加え、「ASC対象となったカテーテルアブレーションを軸に組成した最初期のパートナーシップ」と位置づけ。「保険者は低コストのASCでより多くの手技が行われることを望む」。ArizonaとTexasはASCに有利な規制環境から心血管ASC開発の先行州(Banner HealthはMedAtlasとEP対応心血管ASC 3施設を開発)。
  - 出典: Regent https://regentsh.com/regent-surgical-embraces-outpatient-ep-ablation-services-after-cms-policy-change/ / Cardiovascular Business https://cardiovascularbusiness.com/topics/cardiac-imaging/ep-lab/asc-operator-regent-surgical-embraces-outpatient-ep-ablation-services-after-cms-policy-change
- **小児外科**: 2025年9月、小児専門のPatches Kids Careと提携し小児手術ASCへ。
  - 出典: Business Wire https://www.businesswire.com/news/home/20250903250699/en/Patches-Kids-Care-Joins-Forces-with-Regent-Surgical-to-Deliver-Cutting-Edge-Pediatric-Surgery
- **戦略の骨子**: 「他社が避ける領域へ走る」。医療システムによる医師雇用の進展とMedicare Advantageの急増で独立医師グループのJV案件が減ったため、医療システムJV・支払者関係・IT/分析への投資へ軸足を移す。
  - 出典: Becker's ASC https://www.beckersasc.com/asc-transactions-and-valuation-issues/run-toward-areas-others-avoid-regents-new-asc-playbook-in-a-turbulent-market/

**Ascension(+AmSurg)**
- **ASCの領域**: AmSurgの250超施設は**消化器・眼科・整形・多専門**。Ascensionは「AmSurgの医師主導JVとガバナンスのモデルを継続」。
- **目的**: 「地域の低コストな手術選択肢を増やし、**病院の資源をより複雑な急性期医療に最適化する**」。既存市場では「低acuity手技を病院から移し、病院が高acuityサービスに集中できるようにする」。加えて25の新市場への入口。
  - 出典: Ascension https://about.ascension.org/news/2026/06/ascension-and-amsurg-come-together-to-serve-more-communities / Becker's ASC https://www.beckersasc.com/asc-transactions-and-valuation-issues/why-ascension-is-acquiring-amsurg/ / Fierce Healthcare(JPM26) https://www.fiercehealthcare.com/providers/jpm26-ascension-ceo-says-asc-megadeal-opens-new-markets-partnership-opportunities

**Mass General Brigham**
- **ASCの領域**: 整形・小手術・眼科・内視鏡。第1号は内視鏡専門(処置室3)で、目的は「AMCで26,500人超の内視鏡待機」の解消、待機時間短縮、低コスト化。すなわちASCは**高難度化ではなく、病院の処置室を圧迫する高ボリューム待機症例の切り出し**。
  - 出典: Boston Globe https://www.bostonglobe.com/2026/02/11/business/boston-endoscopy-procedures/ / Business Wire(上記)
- **高難度は在宅入院(Home Hospital)で**: MGBは全米最大級の在宅入院プログラムを持ち、**1日平均50〜60人**に入院レベルのケアを在宅で提供。15か月で200%成長、累計**25,000床日超を節減**、再入院は平均以下、予期せぬ死亡ゼロ。2025年は**術後患者と腫瘍(oncology)へ拡大**し、「エピソード型からシームレスな在宅ケア連続体へ」。
  - 出典: Becker's https://www.beckershospitalreview.com/telehealth/mass-general-brighams-2025-hospital-at-home-plans.html / Becker's Oncology https://www.beckersoncology.com/oncology/mass-general-brigham-home-hospital-expands-to-oncology/ / Current Health事例 https://currenthealth.com/insights/studies/mass-general-brigham-case-study/ / MGB https://www.massgeneralbrigham.org/en/patient-care/services-and-specialties/healthcare-at-home/home-hospital
- **目的**: 病床・処置室の**容量危機**への対応。ASCで待機処置を外へ、在宅入院で内科的急性期・術後を外へ出し、AMCの病床を複雑症例に充てる。

**Cleveland Clinic**
- **ASC**: 2025年5月のRegentとのJVは「手術へのアクセス拡大と提供の効率化」が目的で、対象手技の詳細は未公表(本調査で確認できず)。
- **在宅入院(Hospital Care at Home)**: 2022年5月にMedically Homeと提携、2023年にFlorida 5病院で実装。**4,000人超**が利用し再入院を低減。対象は**COPD、敗血症、蜂窩織炎、肺炎、喘息、および選択された大腸手術の術後**。慢性疾患(COPD・心不全)では病院と同等以上のアウトカム傾向。2025年後半にOhioへ拡大。Mayoと共同で在宅ケアの研究コンソーシアム(レジストリ)を設立。
  - 出典: Cleveland Clinic Newsroom https://newsroom.clevelandclinic.org/2022/05/05/cleveland-clinic-collaborates-with-medically-home-group-inc-to-bring-hospital-level-care-to-patients-homes / Consult QD https://consultqd.clevelandclinic.org/early-success-leads-to-hospital-care-at-home-expansion / Healthcare Finance News https://www.healthcarefinancenews.com/news/cleveland-clinic-expands-hospital-home-ohio / AJMC https://www.ajmc.com/view/bridging-boundaries-a-research-consortium-to-advance-hospital-at-home-care-delivery

### 8-4. Mayo Clinic — 手術は本院、内科的急性期・移植後・化学療法は家へ

- **ACHの対象疾患**: 「入院レベルのケアを要するが在宅治療が可能な程度に安定した患者」。主な対象は**心不全、肺炎、気管支炎、血流感染**。加えて**骨髄移植後、腎移植後、その他の術後管理**を扱い、在宅サービスは**腎透析、静脈栄養、気道吸引、小腸閉塞の治療**などへ拡大。**手術やCT/MRI等の高度画像を要する患者は対象外**。
  - 出典: Mayo Clinic Health System https://www.mayoclinichealthsystem.org/services-and-treatments/advanced-care-at-home / Mayo Clinic https://www.mayoclinic.org/departments-centers/hospital-at-home/sections/overview/ovc-20551797 / Mayo Magazine(2024年8月) https://mayomagazine.mayoclinic.org/2024/08/at-home-healthcare-programs/
- **重症度**: 上記研究のとおりAPR-DRG SOI平均2.89(4段階中「major」相当)で、通常の病棟患者と同等の重症度層を在宅で扱っている。
- **在宅化学療法(Cancer Care Beyond Walls)**: 2023年4月にJacksonvilleで開始。ACHと同じタブレット・24時間指令センターを用い、化学療法ユニットの代わりに自宅で投与。専任腫瘍看護師3名+オンコール腫瘍医。
  - 出典: Mayo Magazine(2025年5月) https://mayomagazine.mayoclinic.org/2025/05/healing-at-home/
- **Care Hotel**: 遠方から手術・処置に来る患者が近隣ホテルで回復し、指令センターの看護師が夜間モニタリング。手術後の病床使用を外す仕組み。
  - 出典: Mayo Magazine(2024年8月、上記)
- **目的**: デスティネーション病院として本院の病床を高度手術・複雑診断に集中させ、内科的急性期・移植後・化学療法・術後回復を「家またはホテル」に移す。Bold. Forward. Unbound.の「部屋を相互転換できる本院」はその裏面である。

## 9. 難度別マトリクス — 誰が何をどこまで病院外へ出しているか

| 領域/難度 | 病院外の場 | 実施主体(本調査で確認) | 目的 | 制度・エビデンス上の前提 |
|---|---|---|---|---|
| 内視鏡・眼科・小手術(低〜中) | ASC | HCA(Surgery Ventures)、AmSurg/Ascension、MGB(第1号ASC) | 待機リスト解消、病院処置室の解放、低コスト化 | 従来からASC CPL対象 |
| 人工関節(中〜高) | ASC | USPI(二桁成長、MSK専門ASC)、HCA(初のASC TJRプログラム)、AJRR登録ASC 107 | 高単価症例の獲得、整形医の囲い込み | TKA 2020・THA 2021にASC CPL追加。ASCで同日退院100%・90日再入院ゼロの研究 |
| 脊椎・泌尿器・ロボット(高) | ASC | USPI(ロボット150超、泌尿器プラットフォーム、高acuity脊椎) | 単価向上、ASC症例構成の高度化 | CY2026 IPOリスト285手技(筋骨格系)除外、CY2027提案で泌尿器等638除外 |
| 心臓EP(アブレーション)(高) | ASC(心血管専門ASC) | Regent(Avondale)、Banner/MedAtlas。USPIは慎重 | 保険者の低コスト志向に応える。ただし医師雇用・設備・Medicare比率がボトルネック | CY2026でASC CPL追加。HRS/ACC声明(患者選択・品質保証を条件) |
| 内科的急性期(心不全・肺炎・感染・COPD)(高) | 在宅入院 | Mayo ACH、MGB Home Hospital、Cleveland Clinic | 病床容量の解放、再入院低減 | CMS在宅入院ウェイバー。SOI 2.89の重症度層で運用 |
| 術後管理・移植後・化学療法(高) | 在宅入院・Care Hotel | Mayo(骨髄移植・腎移植後、在宅化学療法、Care Hotel)、Cleveland Clinic(大腸手術術後)、MGB(2025年に術後・腫瘍へ拡大) | 手術は病院、回復は家。病床回転の改善 | 同上 |
| 小児外科 | ASC | Regent×Patches Kids Care | 専門特化ASC | — |

---

# 第III部 IHH Singapore への示唆

1. **「高難度症例もASC/ACCで」は米国では制度→整形→泌尿器・ロボット→心臓の順で進んでいる**。シンガポールで同じ道を進むなら、(a)HCSAのASC定義(「12時間を超える収容を要しない」——bor-decline-countermeasures.md 第1章)の下で同日退院プロトコルが組める術式から始め、(b)保険者(IP)と定額パッケージで合意できる術式(人工関節・脊椎・泌尿器ロボット)を優先し、(c)心臓EPはHRS/ACC声明に相当する患者選択・搬送体制・品質保証の枠組みが前提になる。
2. **USPIの「低acuityをASCの外へ出す」発想**は、IHH SGのASC/ACCが高ボリューム低単価(GP的処置)に埋まらないための設計指針。ASC/ACCを「病院の外来の延長」ではなく「高単価・同日退院の手術プラットフォーム」として定義し、症例構成をKPI化する。
3. **AMC型の「ASCは待機解消、高難度は在宅」の二層構造**は、病床稼働率が低下しているIHH SGでは順序が逆になる。IHHには埋めるべき病床があるため、在宅入院は「病床を空けるため」ではなく「保険者に対する低コスト・高満足の商品」(bor-decline-countermeasures.md 選択肢(6))として位置づけるのが整合的。
4. **Tenet CEOの心臓に関する3条件**(医師の雇用形態、設備投資、支払者構成)は、IHH SGでも高難度ASCの採算を左右する。シンガポールでは専門医が独立開業で持分JVに乗りやすい一方、設備投資と保険者の償還水準が制約となる。
5. **医師持分ゼロ(MGB/Regent)**は、医師紹介規制や利益相反規制が厳しい場合の代替設計として検討余地がある。

---

# 第IV部 調査ドメイン一覧と未検証事項

## 10. 信頼性があり必要情報を含むドメイン(アクセス許可リスト用)

本セッションで到達できたのは cms.gov、pmc.ncbi.nlm.nih.gov(一部)、ecfr.gov、law.cornell.edu のみ。以下は今回の調査で出典として参照し、今後の原典照合のために許可を推奨するドメイン。

**A. 政府・規制当局・議会(最優先)**
- cms.gov(OPPS/ASC規則ファクトシート、在宅入院ウェイバー)
- federalregister.gov(規則本文)
- ecfr.gov / law.cornell.edu(CFR条文)
- ftc.gov(Ascension–AmSurg同意命令)
- sec.gov(HCA・Tenetの8-K/10-K/決算エキシビット)
- medpac.gov(ASC統計)
- waysandmeans.house.gov / congress.gov(CEO証言)
- mass.gov(MGBのDetermination of Need資料)
- oregon.gov(Ascension–AmSurgの州審査)
- hhs.gov

**B. 学術誌・データベース**
- pmc.ncbi.nlm.nih.gov / pubmed.ncbi.nlm.nih.gov / ncbi.nlm.nih.gov
- jacc.org(HRS/ACC声明)
- heartrhythmjournal.com / sciencedirect.com
- arthroplastyjournal.org / arthroplastytoday.org(AJRR)
- link.springer.com(BMC Health Services Research)
- academic.oup.com
- jamanetwork.com / healthaffairs.org / ajmc.com

**C. 学会・業界団体**
- hrsonline.org / acc.org(心臓EP)
- aaos.org(AJRR年次報告)
- ascassociation.org(ASCA)
- aha.org(在宅入院ファクトシート)
- heartrhythmadvocates.org

**D. 企業IR・ニュースルーム(一次情報)**
- investor.hcahealthcare.com / hcahealthcare.com
- investor.tenethealth.com / tenethealth.com / uspi.com
- about.ascension.org / amsurg.com
- newsroom.clevelandclinic.org / consultqd.clevelandclinic.org
- massgeneralbrigham.org
- newsnetwork.mayoclinic.org / mayomagazine.mayoclinic.org / mayoclinic.org / mayoclinichealthsystem.org
- regentsh.com / regentsurgicalhealth.com
- towerbrook.com

**E. プレスリリース配信**
- businesswire.com / prnewswire.com / globenewswire.com

**F. 医療業界メディア(二次情報、速報性が高い)**
- beckershospitalreview.com / beckersasc.com / beckersspine.com / beckersoncology.com
- fiercehealthcare.com
- healthcaredive.com / medtechdive.com
- healthcarefinancenews.com
- modernhealthcare.com
- ascnews.com
- hospitalogy.com
- cardiovascularbusiness.com
- healthcareitnews.com
- vmghealth.com(ASC年次レビュー)
- fool.com(決算説明会の書き起こし)

**G. 地域紙・監視団体(補助)**
- bostonglobe.com / postbulletin.com
- pestakeholder.org(PEのASC投資に関する報告)
- mcdermottplus.com / hklaw.com / hallrender.com(規則の法律事務所サマリー)

## 11. 未検証事項(原典未到達)

以下は本環境で原典に到達できず、検索エンジン経由の記事要約に依拠している。引用前に原典で確認されたい。
- HCA: 「Urgent care 340拠点超・年420万件」(Becker's記事の要約)。「外来拠点約2,700」とする記事もあり、HCA公式の「約2,500」と定義が異なる可能性。HCAの在宅入院プログラムは未確認。
- Tenet: 2024年の病院売却総額($5bn/$4.8bn)は媒体で異なる。2025年通年のAmbulatory Care調整EBITDA約$2.0bnは四半期値の合算(Q1 456+Q2 498+Q3 492+Q4 580=約$2.03bn)で、原典の通年表記は未確認。「ロボット手術プログラム150超」はBecker's経由。
- Regent: ASC「26施設」はRegent自社サイト・PESP報告書の記載。Ascension–Regent JVの累計施設数は公表資料が見当たらない。
- Cleveland Clinic: RegentとのJVで対象とする手技・第1号施設は未公表(確認できず)。
- MGB Home Hospital: 「1日50〜60人」「25,000床日超」は Becker's/Current Health事例の要約。
- Mayo: 再入院率の低下幅は媒体により「15%」(Mayo Magazine 2024)と「65%」(Healthcare IT News 2021)が併存。本文は新しい方を採用。ACHの直近(2025〜26年)累計患者数は未確認。
- CMS: CY2026最終規則のIPO 285手技・ASC CPL 289+271手技、CY2027提案の638サービスはcms.govファクトシートで**原典確認済み**。心臓アブレーションのASC CPL追加はACC/HRS/MedTech Dive経由(ファクトシート本文には個別記載なし)。
- 在宅入院のCMSウェイバー延長(2030年まで)は検索要約のみで法文未確認【要確認】。
