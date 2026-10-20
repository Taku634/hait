# IHH提携専門医支援(A4-i〜iv)の精緻化とTPA連携の検証 — IHH×三井物産の協働を前提とした設計要件

**作成日**: 2026年10月20日
**位置づけ**: `ihh-sg-hypotheses-verification.md` 補遺5(§16-2)のアクション **A4-i(非診療業務の解放)・A4-ii(電カル連携とデータ取得)・A4-iii(Payor交渉代行)・A4-iv(グループ内患者リファラル)** を、IHHと三井物産が協働して実行する前提で設計要件レベルまで精緻化する。あわせて、同書補遺6(§17-1)が提案した「三井によるTPA(iXchange等)への出資」について、**三井がiXchange等に出資することでIHH専門医がSinglife以外の保険パネルへのアクセスを獲得できるか**を一次資料で検証する。
**想定読者**: 三井物産の投資・事業部門。三井が何を出し何を得るか、IHHとの合意が要る論点を中心に書く。
**粒度**: 設計要件(目的・提供内容・法的線引き・前提条件・成功条件)まで。スケジュール・担当割り・費用概算は書かない。
**表記ルール**: 【確認】=出典原文で裏付けた事実、【算出】=出典の数値から計算した値、【未検証】=公開情報で確認できなかった事項(推測で埋めない)、【分析】=確認済み事実から導いた本書の評価。出典は「A=原文を取得して本文確認」「B=検索エンジン経由で要旨を確認(原文サイトが本環境から取得不可)」に区分し巻末に記載。既存レポートからの引用は「(文書名 §節)」で示す。
**本書の範囲外**: A4-v(立上げ期の給料保証)・A4-vi(クリニックのEquity取得)は対象外(補遺5の評価を維持)。

---

## 調査手順(Step-by-Step)

1. **対象の確定**: 補遺5 §16-2のA4-i〜ivの4行と、補遺6 §17-1(支払者対応・TPA・データ基盤への三井投資)、10月14日文書 `ihh-sg-inpatient-loyalty-asc-payor-strategy.md` §7(提携専門医プログラムの原型)・§8 層D(D1〜D7)を再読し、既に確定している制約(SMC倫理規程H3、CCCS第34条、HCSA、PDPA/Health Information法)を引き継いだ。
2. **TPA連携の一次資料の再取得**: LIA(生命保険協会)の7社比較表2025年2月25日版PDFをローカルでテキスト化して**各社の申請窓口の原文**を確認した。Singlife×IHHの2023年8月14日プレスリリース(SGX掲載PDF)、IHHの2026年7月10日発表、MOHのIPパネル統計ページ、MOHの国会答弁(2021年5月10日・5月11日、2025年9月24日・10月6日・11月26日)、CCCSのExtended Panelに関するMOHへの助言(2022年8月24日)、PrudentialのPRUPanel Connect(PPC)およびExtended Panelの公式ページ、HSBC Lifeのパネルページ、Foundation Healthcareの2026年上期決算説明会スクリプト(SGX掲載PDF、ローカルでテキスト化)、三菱商事のFullerton Health出資(2025年8月)、Health Information法のgov.sg解説、iXchange CEOのプロフィール(BMJ国際フォーラム)を原文で確認した(A区分)。
3. **取得できなかった資料の扱い**: iXchange公式サイト、Singlife公式サイト、三井物産公式サイト(中期経営計画2029)、The Edge Malaysia、AIA・Great Eastern公式サイトは本環境のネットワーク制限で取得できず、検索エンジン経由の要旨(B区分)に依拠した。該当箇所には(B)を付す。
4. **検証の論理**: 「TPAへの出資がパネルアクセスを生むか」は、(a) パネル採否の決定主体は誰か、(b) 各保険者の申請窓口でTPAがどの役割を担うか、(c) 実際にIHH以外で「一括でパネルが開いた」事例は何によって開いたか、の3点で判定した。
5. **設計要件の整理**: A4-i〜ivそれぞれについて「目的と効く駆動力」「提供内容」「対象」「提供主体と三井の寄与」「対価と法的線引き」「前提条件・依存関係」「成功条件(KPI定義)」「競合ベンチマーク」「リスク」を揃え、三井の関与形態(共同事業体 vs 株主としての支援)を比較した。

---

## ① Executive Summary

1. **三井がiXchange等のTPAに出資しても、それ自体ではIHH専門医のSinglife以外のパネルアクセスは得られない**【確認→分析】。パネルへの採否は各保険者が独立に決める(MOH 2021年5月10日答弁)。LIA比較表2025年版の原文では、申請窓口は AIA=社内Provider Engagementチーム、GE=Doctor Anywhereドメイン、HSBC Life=Fullerton Health(「当社はFullerton Healthをパネル管理のTPAに任命」「Fullertonと共同で選定」)、Income=社内、Prudential=提携医療機関(HI)主導で個人申請不可、RHI=社内、Singlife=iXchangeドメインまたはSinglife社内Provider Network、と7社すべて異なる【確認】。iXchangeが申請窓口を担うのはSinglifeだけであり、AIA・GE・IncomeとのIHHの提携はiXchangeが「入院前から請求までを接続する」運用上の役割であって、パネル採否の窓口ではない【確認/分析】。
2. **「出資すれば窓口を持てる」が成り立つのはHSBC Life(Fullerton)とSinglife(iXchange)の2社に限られ、前者は三菱商事が2025年8月に少数出資済み、後者は既にIHH 100%子会社である**【確認】。GEの窓口Doctor AnywhereにはIHHが2020年から少数株主として入っているが、GEのパネル採否はGEが決める【確認/分析】。Prudentialは施設単位(HI-led)で、IHH系で提携済みはMount Elizabeth Royal Square(2026年8月1日、IHH初の施設)のみ、4病院は提携外【確認】。
3. **実際にパネルが「一括で開いた」事例は、すべてTPA資本ではなく保険者と医療機関の直接合意による**【確認】: AIA×Raffles Hospital(2025年1月、90人超を一括追加、MOH料金ベンチマークに沿った請求の共同管理を含む)、Prudential×Thomson(2025年4月、約100人)、Prudential×Royal Square(2026年8月)、Foundation Healthcare(「6社中3社と直接の取り決めがあり、所属医の加入経路が簡素化」)。共通項は**料金・請求管理を施設側が保険者に約束すること**であり、これがIHHにとっての本当の鍵である【分析】。
4. **A4-iii(Payor交渉代行)の設計は「交渉」を外し、「保険者別の加入経路支援+Extended Panel(EP)の活性化+e-filing/事前承認+成果データ」に置き換える**【分析】。CCCSは2022年8月のEP助言で「EP医は料金・条件という商業上機微な情報を各保険者から**個別に**取得すべき」と条件を付けており、病院や共同事業体が医師間で料金情報を集約・中継する行為は第34条の問題になる【確認】。EPは「1社の主パネルに入れば他社のEP医として認められる」仕組みで、Prudentialは申請不要・事前承認必須、HSBC Lifeは契約ベースでFullerton経由【確認】。Singlifeの主パネル(2025年705人)に入っているIHH独立医にとって、EPは**今すぐ使える**他社給付への経路である【分析】。
5. **A4-i(非診療業務)・A4-ii(電カル)・A4-iv(リファラル)は三井の資本がなくてもIHHが実行でき、三井の寄与は「中立な器」と「データ事業の受け皿」に限られる**【分析】。A4-iiはHealth Information法(2026年1月12日可決、2027年初施行、全ライセンス事業者にNEHR寄与を義務化、保険・雇用目的のアクセスを禁止)が契機だが、競合のAVA(Foundation)は「全私立・公立病院に導入済み」と主張し、「地域の私立病院運営者と入院モジュールのUATを完了」している。IHH病院内でのAVAの稼働範囲を確認してから、自前(C+外来モジュール)か提携かを決めるのが先決である【確認/分析】。
6. **三井の関与形態は「段階的」が整合的**【分析】。(b) 筆頭株主としてIHH取締役会経由で支援し、A4-i・ii・ivとA4-iiiの基礎層をIHH(iXchange・4病院管理部門・Parkway Shenton)の内部で先に立ち上げ、(a) 共同事業体(iXchangeの現物出資+三井過半+保険者または政府系の参加)は、「保険者の共同出資意思」「IHH病院内のAVAの位置」「IHH取締役会の関連当事者取引の承認」の3条件が確認できた場合に限って進める。共同事業体の根拠は「アクセスの購入」ではなく、**中立性(保険者の警戒を解く)、全私立医への開放、症例の行き先データと定額商品の原価データ**にある。
7. **両社の合意が要る論点**は、(i) 料金・請求管理の保険者への約束(A1・A2)を提携専門医プログラムの前提に置くこと、(ii) 医師から取る対価を固定事務手数料に限ること、(iii) 全認定医への同一条件と入院量非連動を文書化すること、(iv) iXchangeの現物出資と支配権、(v) NEHRデータと保険者向けデータの経路分離、(vi) 非参加テナント・既存グループ所属医の公平な扱い、である(§⑥)。

---

## ② 前提の整理(既存文書から引き継ぐ事実)

| 項目 | 事実【確認/算出】 | 出典 |
|---|---|---|
| 対象となる医師 | IHH 4病院の認定医1,295人のうち独立開業医989人(76%)。グループ所属306人(24%: Foundation 89・Tamarind 45・HMI 30・OUE 25等) | 10月14日文書 §4-1、`ihh-sg-medical-suite-specialists.md` |
| 独立医の支払者接続の弱さ | 平均パネル数: 独立医2.6社 vs グループ医4.4社。6社全てに在籍: 9% vs 43%。入院依存「高」の科ではGE接続41% vs 83%、Prudential 76% vs 95% | 10月14日文書 §2 表、§7-2 |
| グループが医師に与える8つのメリット | ①支払者接続 ②患者の流入 ③事務 ④施設と施設料 ⑤流動性・承継 ⑥立上げ支援 ⑦臨床・キャリア ⑧統治・持分。A4-i〜ivは①②③(と⑥の一部)の非資本代替 | 10月14日文書 §7-2、§7-3 |
| 流出の駆動力 | (a) 保険の給付条件がIHH施設を外す、(b) IHH施設の請求額が高い、(c) 医師・グループが施設料を取り込む持分設計を持つ、(d) 民間入院需要の縮小 | 検証文書 §16-1 |
| 法的な線引き | SMC倫理規程H3(紹介対価の禁止、TPA等への手数料は実際の事務作業に見合う額に限定、報酬比例の禁止)、CCCS第34条(料金の推奨・共同交渉の禁止: 2010年SMA料金ガイドライン決定)、HCSA(TPA手数料を明細に独立表示、広告規則)、PDPA/Health Information法(保険目的のNEHRアクセス禁止) | 検証文書 §8-2、§17-1(2)、本書 §③-1 |
| IHHの既存部品 | iXchange(TPA)、Singlife CareCollab(事前承認なし直接アクセス)、Royal Square×PPC、C+(4病院でNEHR完全寄与)、Parkway Shenton GP約50クリニック、Healthspan、4病院UCC/A&E、国際患者オフィス、法人2,000社超 | 検証文書 §8-1、§17-1(1) |
| 三井の立場 | IHH筆頭株主(MBK Healthcare Management経由で約32.8%、2025年3月28日時点32.76%〔B〕)。共同投資は関連当事者取引。中期経営計画2029(2026年5月1日)で「Wellness Ecosystem Creation 2.0」を重点施策とし、IHHの臨床データを使う事業(Oncoshot/MSK iHubとの腫瘍データ連携、2026年9月)を開始 | 検証文書 §16-1、出典M1〜M3 |

---

## ③ TPA連携の検証: 三井がiXchange等に出資すれば、IHH専門医はSinglife以外のパネルにアクセスできるか

### 3-1. 制度上の事実: パネル採否は保険者が独立に決める【確認】

- MOHは2021年5月10日の国会答弁で、保険者は医師と合意した条件のもとで**各社が独立に**パネル採否を決めており、これは競争法に反しない、と整理した。MOHは選定基準の透明化を保険者に奨励し、LIAは「Panel Good Practice Guide」で支える(出典1)。
- MOHのIPパネル統計ページは「各保険者は望ましいパネル規模について異なる考慮を持ち得る」と明記し、2025年の主パネル私立専門医数をPrudential 957、HSBC Life 894、GE 814、Singlife 705、AIA 684、Income 648、RHI 198と公表する。脚注は「**Singlifeは2023年9月にTPAを変更し、専門医の入替が増えた**」(同年離脱78人・加入121人)、「GEの2024年の高い離脱(126人)は計画的パネル見直しによる」と記す(出典2)。
- 2025年9月24日の答弁でMOHは「ほとんどの保険者は600人以上」「専門科レベルで十分なカバレッジを確保するよう保険者と協働」「EPにより大半の保険者は他社パネル医の受診を(審査を条件に)認める」とし、専門科別最低人数や契約期間の規制は採らなかった(出典3)。2025年10月6日の回答では「パネル料金レンジを大幅に上回る、または不適切な請求をする医師を保険者が外すことはシグナルとしてあり得る」「過度な入替は避けるべき」「MHIC(多者間医療保険委員会)の下にパネル問題の作業部会を設置」と述べた(出典4)。

**読み取り**【分析】: TPAは保険者から委託された事務の実行者であり、採否の決定権は持たない。ただしSinglifeの2023年の例が示すとおり、**保険者がTPAを替えるとパネル構成が動く**(78人離脱)。TPAは「誰が窓口に座り、誰の請求実績データで評価するか」を通じて採否に影響する。影響と決定は別である。

### 3-2. 7社の申請窓口とTPAの役割(LIA比較表2025年2月25日版の原文)【確認】

| 保険者 | 申請窓口(原文の要旨) | TPAの役割 | 採否の決定 | IHH専門医の現在の位置 |
|---|---|---|---|---|
| **AIA** | 「専任のProvider Engagementチーム」が対応。sg-provider@AIA.com | **なし**(社内) | AIA(請求パターン・顧客基盤・サブ専門科と施設レベルでの必要キャパで定員算定。待機リストあり。公立から開業しても自動移行なし) | AIAはIHHのIPパートナー(2026年7月)。Mount Elizabethでの事前承認は継続(2025年6月時点〔B〕) |
| **Great Eastern** | provider-sp@**doctoranywhere.com** へメール→フォーム送付 | 窓口はDoctor Anywhere(IHHが2020年から少数株主〔B〕) | GE(商品カバレッジとの整合、専門科別人数、**当社パネル料金への同意**) | GEはIHHのIPパートナーだが、Mount Elizabeth 2病院へのPAC(事前承認証明)は2025年6月17日から停止、再開は2026年10月時点で未確認〔B〕 |
| **HSBC Life** | 「**Fullerton HealthをTPAとしてパネル管理に任命**」。Fullerton Network Servicing Team(fhn3@fullertonhealth.com)が料金・契約条件を説明し、「**Fullerton Healthと共同で**パネル医を選定」。EPは契約ベースで、他社パネル医のEP加入もFullerton窓口 | Fullerton(RRJ Capital・Far East Drug過半+**三菱商事が2025年8月22日に少数出資**) | HSBC Life(Fullertonと共同。財務的質=ベンチマークに見合う価格、サービスの質、臨床の質。日帰り手術を自院で行う医師はe-filing設備必須) | 医師単位で申請可能。IHH病院との施設提携は確認できず |
| **Income** | incomeproviders@income.com.sg | **なし**(社内) | Income(専門科の必要性、性別・人種・診療場所の多様性、記録上の診療パターン、**臨床アウトカムの提出**、**医療機関との戦略的提携**。待機リストあり、処理は申請順でない) | IncomeはIHHのIPパートナー(2026年7月) |
| **Prudential** | 「**HI主導の提携モデルで専門医と直接は提携しない**」。PPC提携HIに認定され、HIが推薦・オンボードを調整。申請フォームなし | **なし**(保険者と施設の直接契約) | Prudential(HIの推薦が前提。コンサルタント級以上、合意済み料金ベンチマークの遵守。請求は**HIの事務所からe-file**) | 提携私立病院はMount Alvernia・Raffles・Thomsonの3院。IHH系はMount Elizabeth Royal Square(日帰り手術センター、2026年8月1日〜、**IHH初の施設**〔B〕)のみ。4病院は提携外 |
| **RHI** | sp-panel-enquiries@raffleshealthinsurance.com | **なし**(社内。Raffles MedicalのMedical Directorと協議) | RHI | 新規受入は2024年0人・2025年3人で実質停止【算出】 |
| **Singlife** | medixchangeshield@**ixchange.com.sg** **または** medicalprovider_engagement@singlife.com。担当者(Provider Network)の連絡先もixchangeドメイン | **iXchange**(IHH 100%子会社)。ただしSinglife社内窓口も併記 | Singlife(専門科分布が加入者ニーズを満たすか。**CPF e-file設備**が要件) | 2023年9月9日からSinglife Shield加入者は「iXchangeが管理する500人超の認定専門医網」へ事前承認なしで直接アクセス |

出典: LIA比較表2025年2月25日版(出典5、原文PDF)。Prudential PPCページ(出典6、2025年10月14日時点)。Singlife×IHHプレスリリース(出典7)。三菱商事×Fullerton(出典8)。IHH 2026年7月10日(出典9)。

### 3-3. iXchangeが実際に担っている機能【確認】

- **Singlifeとの関係**: 2023年8月14日のプレスリリースは「iXchange——IHHSGのTPA——が管理する500人超の認定専門医網」「パネルネットワーク管理と請求審査(claims adjudication)の専門性でiXchangeが支える」「IHHSGがSinglifeを**Shield加入者向けの戦略的保険パートナーとして選んだ**」と記す(出典7)。LIA表ではSinglifeの申請窓口がiXchangeドメインであり、iXchangeがSinglifeのIP専門医パネルの事務を担っていることと整合する(出典5)。
- **AIA・GE・Incomeとの関係**: IHHは2026年7月10日、AIA・GE・Income・SinglifeをIPパートナーと公表し、iXchangeが「入院前から請求まで、IHHの病院・医師・保険者を接続」し、保険者に在院日数・手術の複雑さ・ケア設定といったコスト要因の可視性を与え、管理プログラムの平均請求額上昇率を7〜10%から「極めて低い一桁%」に抑え、循環器で費用とプロトコルを事前に定めた構造化パッケージを運用していると説明した(出典9)。**この発表に「IHH専門医のパネル加入」への言及はない**【確認】。
- **規模と資格**: iXchange CEO(Loh Chek Chai氏)のプロフィールは「2023年に**2つのShield TPAプログラムを管理する初のTPA**になった」(保険者名は非記載)、「2022年に新TPAシステムを導入」「OSPAR認証・ISO 27001」と記す(出典10)。International Assistance Groupの2025年4月の発表は、法人顧客2,000社超、GPパネル600超、専門医800人超、歯科280超、中医20超と伝える〔B〕(出典11)。Cigna Healthcare Singaporeは2025年末にiXchangeと価値ベース契約を開始したと2026年3月に発表した〔B〕(出典12)。
- **「2つ目のShieldプログラム」の保険者名**は公開情報で確認できない【未検証】。IHHのIPパートナー4社のうちSinglife以外のいずれかである可能性はあるが、LIA表の申請窓口にiXchangeが現れるのはSinglifeのみである【確認】。

### 3-4. 判定: 出資 ≠ アクセス【分析】

**判定: ×(iXchange等への出資のみではSinglife以外のパネルアクセスは得られない)。△(窓口を持つTPAへの出資は「申請の通りやすさ」に影響し得るが、採否と料金条件は保険者が決める)。**

根拠を保険者別に示す。

| 保険者 | iXchangeに三井が出資した場合 | 他のTPA等に出資した場合 | 実際にアクセスを開く手段 |
|---|---|---|---|
| Singlife | 既にIHHが窓口を持つ。出資で変わるのは所有者であって機能ではない。中立化すればSinglifeの警戒は下がるが、Singlifeは「IHHが戦略的パートナーに選んだ」側であり現状で機能している | — | 現状維持。CPF e-file設備の整備支援(加入要件) |
| HSBC Life | 効果なし(窓口はFullerton) | Fullertonは三菱商事が少数出資済み(2025年8月)。追加出資の余地・条件は【未検証】。出資しても「HSBC Lifeと共同で選定」であり、HSBC Lifeが決める | 医師単位の申請支援+EP(契約ベース、Fullerton窓口)。価格=「国家ベンチマークに見合う価格」が選定基準の第一 |
| Great Eastern | 効果なし(窓口はDoctor Anywhere) | IHHは既にDoctor Anywhereの少数株主(2020年〜)だが、GEのパネル採否・PAC停止には影響していない事実が、「資本≠アクセス」の実証である | **施設の価格**(他院比20〜30%高とGEが主張する請求額)の是正。Foundationは「3社と直接取り決め」でGE接続83%(入院依存科のグループ医) |
| Prudential | 効果なし(TPAを使わないHI-led) | 効果なし | **施設単位の提携**。Royal Squareで開いた経路をGleneagles・Parkway Eastに広げる(検証文書 §16-4 IHH-1)。医師は提携HIで開業していれば推薦対象 |
| AIA・Income | 効果なし(社内窓口) | 効果なし | 医師単位の申請支援。AIA×Raffles(90人超一括)型の**病院単位MoU**(品質指標の共有+MOHベンチマークに沿った請求の共同管理) |
| RHI | 効果なし | 効果なし | 実質閉鎖。EPで代替 |

**補強する事実**【確認】:
- **一括でパネルが開いた事例の共通項は料金管理の約束**: AIA×Raffles(2025年1月23日MoU)は「90人超をAQHPに追加」と同時に「品質指標・アウトカムの共有」「**MOH料金ベンチマークに沿った入院請求の共同管理**」を約束した〔B〕(出典13)。Prudential×Thomson(2025年4月1日)は約100人を一括追加し、医師は「HIと合意した料金」を守る(出典14)。Foundationは「6社中3社と直接の取り決めがあり、所属医はより簡素な加入経路を得る」「保険者は当社の医療センターがコストを管理していることを評価する」と説明する(出典15)。
- **TPA側の収益構造は医師ではなく保険者・法人から取る形に制約される**: SMC倫理規程H3は医師がTPAに払う手数料を「実際の事務作業に見合う額」に限り、報酬比例を禁じる(MOH 2021年5月11日)。TPAはMOHの免許対象外だが、HCSAでTPA手数料は明細に独立表示される(出典16)。したがってTPAへの出資で「医師から取る手数料」を事業にすることはできず、価値は保険者・法人契約とデータにある【分析】。
- **MHICの作業部会は「窓口の価値」を下げる方向に働き得る**: 2025年10月設置の作業部会が加入手続きの標準化や入替制限に進めば、TPAが窓口を握ることの戦略的価値は相対的に下がる(出典4)【分析】。

### 3-5. Singlife以外への「現実の経路」: Extended Panelと施設提携【確認】

**Extended Panel(EP)**は、三井の出資を要さずに、Singlife主パネルに入っているIHH独立医が他社の給付に接続する経路である。
- 2022年4月導入。MHICの勧告に基づき、7社すべてが合意。「1社の主パネルに入っている医師は、他社のEP医として認められ得る」。加入者は自己負担上限等の主要なパネル給付を受ける(当初S$3,000、総額S$60,000超の場合)。医師は患者の保険者の条件(料金を含む)に従う。IncomeとSinglifeは2022年4月以降の契約更新時から適用(出典17)。
- **CCCSの助言(2022年8月24日)**: EPは「より大きな医師プールで競争を促進し得る」としつつ、競争を守るために「**EP医候補は料金・条件という商業上機微な情報を、共有チャネルではなく各保険者から個別に取得すべき**」と条件を付けた(出典18)。
- **Prudentialの運用**: EP医への「申請」は不要。(i) 他社の主パネルに在籍、(ii) Prudentialの事前承認を取得、(iii) Prudentialの料金表に従う、(iv) 事前承認条件を満たす、の4条件を満たせばEP医として扱う。**EP請求は事前承認が必須**。給付は施設で変わり、PPC提携HIでは完全な給付(キャッシュレス・高いLOG上限)、非PPC施設では付帯サービスなし、一部プランでは私立病院・「No Access」施設が除外される(出典19)。
- **HSBC Lifeの運用**: 「EPは契約ベース。他社パネル医で当社パネルへの加入を希望する場合はFullerton窓口へ」(出典5)。
- **新ライダー(2026年4月1日〜)との関係**: MOHは「自己負担上限(最低S$6,000)はパネルまたは事前承認済みの請求といった適格な請求にのみ適用」と定めた(出典20)。EP請求は事前承認が必須であるため、事前承認済み請求として上限の対象になると読めるが、MOHの発表はEPを明示しておらず、各社の商品約款で確認が要る【未検証】。

**施設提携**: Prudentialの提携施設一覧(2025年10月14日時点)には私立病院3院のほか、日帰り手術センター11(Foundation Ambulatory Centre Novena/Orchard、HC Surgical、HMI Medical Centre、Luma、Novena Surgery、Mount Elizabeth〔Royal Square〕等)、外来腫瘍センター9(Icon各拠点、Mount ElizabethやGleneagles館内のIconを含む)が並ぶ(出典6)。**Iconの館内拠点がPPC提携施設に入っている一方でIHH病院自体は入っていない**事実は、提携の単位が「施設の運営主体と価格」であることを示す【確認/分析】。

### 3-6. TPA検証の含意(A4-iiiと三井の関与形態への接続)【分析】

1. **三井のTPA出資の根拠を「アクセスの購入」から「中立性・開放・データ」に書き換える**。補遺6 §17-1(3)の論理(中立な株主が持てば保険者の警戒が解ける、全私立医に開ける、症例の行き先と定額商品の原価データが得られる)は維持できるが、「IHH専門医のパネルアクセスが広がる」という期待は、保険者ごとの窓口と採否の構造から外す。
2. **アクセスを広げる実効策は3つ**: (i) 施設の価格・請求管理の約束(A1・A2)を伴う病院単位の提携(Gleneagles・Parkway Eastを先に)、(ii) 保険者別の窓口に沿った加入支援(定員・請求実績・e-file設備・アウトカム提出という各社の評価項目を医師ごとに整える)、(iii) Singlife主パネル在籍を足場にしたEPの活性化(事前承認の運用を支援する)。
3. **「等」に含まれる候補の評価**: Fullerton(HSBC Life窓口)は三菱商事が先行し、提供者系(Far East Drug)の資本が入っているため中立性の訴求に使えない。Doctor Anywhere(GE窓口)は既にIHHが株主で、追加出資がGEの採否に効く根拠はない。MHC(HMI)は競合プラットフォームの中核で対象外。AVA(Foundation)は上場企業の中核資産で、出資より「IHH病院内での利用の有無の確認」が先。したがって、三井が出資対象として検討する意味があるのは**iXchangeを母体とする新会社**に限られ、その目的は上記1である。

### 3-7. 本節で確認できなかった事項【未検証】

- iXchangeが2023年に管理を始めた「2つのShield TPAプログラム」の保険者名、およびSinglifeが2023年9月に切り替える前のTPA名。
- IHHとAIA・GE・Incomeの契約でiXchangeが担う機能の範囲(事前承認・請求の代行か、単なるデータ接続か)。
- GEのMount Elizabeth 2病院に対するPAC停止の2026年10月時点の状況(再開を報じる資料は確認できず)。
- 各保険者のEP運用の詳細(Prudential以外の申請要否、新ライダー下でEP請求が自己負担上限の対象になるか)。
- Fullerton Healthへの三菱商事の出資比率と、他の株主との取り決め。
- Doctor Anywhereに対するIHHの現在の持分比率。

---

## ④ A4-i〜ivの精緻化(設計要件)

共通の設計原則【分析】(10月14日文書 §7-4・§7-6、検証文書 §8-2から引き継ぐ):
- **P1 同一条件**: 全認定医(独立医・グループ所属医を問わず)に同一条件で提供し、入院数・施設利用量・紹介量と連動させない(SMC H3「紹介の対価としての現物補償」の回避)。
- **P2 固定対価**: 医師から取る対価はクリニック単位の固定サブスクリプションまたは固定事務手数料に限る。診療報酬・請求額の比率は用いない(SMC H3、MOH 2021年5月11日)。
- **P3 料金に触れない**: 料金の推奨・集約・共同交渉を行わず、料金・条件は医師が各保険者から個別に取得する(CCCS 2010年決定、CCCS 2022年EP助言)。
- **P4 データ経路の分離**: NEHRデータは診療目的に限り、保険者向けの請求・成果データは患者同意に基づく別経路で扱う(Health Information法)。
- **P5 患者の選択の保持と配分基準の公開**: 紹介・当直・国際患者の配分は公開基準で運用し、提携医以外を希望する患者には応じる。
- **P6 テナント中立**: 非参加の認定医・既存グループ所属医が不利益を受けない(Hirslanden原則)。

### A4-i. 非診療業務の解放(財務・調達・賃貸・管理のサービス化)

| 要件 | 内容 |
|---|---|
| **目的と効く駆動力** | 駆動力(c)の動機を弱める。グループのメリット③(事務)と⑥(立上げ支援)の非資本代替。「買われる前にホスト病院が本社機能を提供すれば、買われる動機が弱まる」(10月14日文書 §7-1)【分析】 |
| **提供内容** | (1) 会計・税務・給与・人事・MOH許認可(HCSA)更新の代行、(2) 消耗品・薬剤・医療賠償保険の団体条件(共同購買)、(3) Parkway Laboratory/Radiologyの優先接続、(4) 開業支援(立地・内装・IT・許認可: Medinexが月次課金で提供してきた役務の同型)、(5) 法務・契約の定型支援。**電カル・請求事務はA4-ii・iiiに分ける** |
| **対象** | 全認定医。優先コホートは開業直後(民間5年未満)と中堅独立医。グループ所属医にも同一条件で開放(P6) |
| **提供主体と三井の寄与** | 主体はIHH(4病院の購買・人事・財務・法務を再編した専任組織)。三井の寄与は小さく、(a) 共同事業体を選ぶ場合はサービス会社(ServiceCo)への出資と商社の調達機能の提供、(b) 株主支援の場合は取締役会での専任組織・KPI設定の後押しに限られる【分析】 |
| **対価と法的線引き** | P1・P2。基礎層(許認可・団体条件の案内)は無償、上位層(会計・人事・開業支援)は有償の月次課金。費用の一部を医師が負担する設計は、米国のEHR寄付セーフハーバー(受領者15%負担、紹介量非考慮)〔B〕を参照 |
| **前提条件・依存関係** | 専任組織(Mount Elizabeth病院CEOとParkway Shenton CEOの兼務解消は既往提言)。Foundationは専門医108人に本社71人を置いており、認定医1,000人規模への提供は人員と費用を要する(10月14日文書 §7-9) |
| **成功条件(KPI定義)** | 加入率(独立医989人のうち基礎層・有償層それぞれ)、サブスクリプション継続率、グループへの年間流出数(2026年10月時点の306人を基準)、医師1人当たり事務コストの低減(医師側の申告ベース) |
| **競合ベンチマーク** | Foundation(集中購買を買収後シナジーの運営優先課題と明言、本社71人)、Medinex(月次課金、利益率7割超だが売上横ばい)、HMI(OneCare・MHC・StarMedを束ねたプラットフォーム) |
| **リスク** | 便益が紹介の対価と見られる運用(非参加医の排除、入院量連動)。非参加テナントの離反。収益事業として自立しない(Medinexの前例)ため、防衛投資として位置づける |

### A4-ii. 電カル連携とデータ取得

| 要件 | 内容 |
|---|---|
| **目的と効く駆動力** | 駆動力(c)。グループのメリット③と①(支払者接続の基盤)。IHHにとっての価値は「症例の可視化(どの医師のどの症例がどこへ行ったか)」と「定額商品の原価データ」【分析】 |
| **制度の契機【確認】** | Health Information法: 2026年1月12日可決、2027年初施行予定。全ライセンス医療事業者にアレルギー・予防接種・診断・投薬・検査・画像・退院サマリー等のNEHR寄与を義務化。**雇用・保険目的のアクセスは厳格に禁止**。「break glass」緊急アクセスは監査対象(出典21) |
| **提供内容** | (1) C+の外来・クリニックモジュール、または認定クリニック管理システム(CMS)のNEHR対応版を全認定医に提供、(2) 病院C+と患者単位で接続(紹介・入院・退院サマリーの往復)、(3) e-filing・事前承認・定額パッケージ運用・紹介ワークフロー・PROM/PREM収集を同じ基盤に載せる(A4-iii・ivの基盤)、(4) サイバーセキュリティ・データ保護の法令要件(MOHへのインシデント通知義務)を含めた運用 |
| **対象** | 全認定医。未接続の私立専門医クリニックは法案審議で「残る層」として名指しされており(検証文書 §8-2 9)、法令対応が加入動機になる |
| **提供主体と三井の寄与** | 主体はIHH(C+の所有者)。三井の寄与は「データ事業の受け皿」: 中期経営計画2029の「Wellness Ecosystem Creation 2.0」はIHHの臨床データを薬剤開発支援等に使う方針で、2026年9月にOncoshot(MSK iHub参加)と腫瘍データの標準化・匿名化で提携した(出典M2)。**ただしこの経路は研究・創薬目的であり、保険目的のNEHRデータ利用は法で禁止される**ため、保険者向けデータ(請求・成果)は患者同意に基づく別経路(P4)に限る【確認/分析】 |
| **対価と法的線引き** | P1・P2・P4。医師が費用の一部を負担し、紹介量を考慮しないことを文書化。保険者向けのデータ提供は、個々の請求・事前承認の範囲(保険者が「ケースバイケースで医療機関に情報を請求できる」範囲〔B〕)と、集計・匿名化された成果指標に限る |
| **前提条件・依存関係** | **IHH病院内でのAVAの稼働範囲の確認が先決**。Foundationは「AVAは全私立・公立病院に導入済み」「地域の私立病院運営者と入院モジュールのUATを完了」「新モジュールのロードマップあり」と説明する(出典15)。IHH病院がAVAの入院モジュールの相手方であれば、独立医のクリニック側はAVAに接続している可能性があり、自前基盤との二重投資か、AVAとの相互接続かを決める必要がある【未検証】 |
| **成功条件(KPI定義)** | NEHR接続した認定医クリニック数(2027年初の施行前)、病院C+との患者単位接続率、e-filing経由の請求比率、PROM/PREMの収集率、「症例の行き先」データの網羅率(認定医の日帰り・入院症例のうち基盤上で把握できる比率) |
| **競合ベンチマーク** | AVA(保険者との電子契約、事前承認、予約、入院モジュール。GEと2025年4月に「取引の自動化のための先進デジタルソリューションの採用を探索」(出典22))、MHC(HMI)、Fullerton(HSBC Life)。 |
| **リスク** | AVAとの先行差。NEHRデータの保険目的利用と見られる運用(制裁)。サイバーセキュリティ事故(通知義務)。医師が「病院に症例を監視される」と受け取る心理的抵抗(配分基準・データ利用目的の公開で緩和) |

### A4-iii. Payor交渉代行 → 「支払者対応センター」(交渉を含まない)

| 要件 | 内容 |
|---|---|
| **目的と効く駆動力** | 駆動力(a)。グループのメリット①(支払者接続)の非資本代替。独立医の痛点は「申請したが不成功または待機リスト」(SMA 2020年調査で保険者別10〜34%)と「患者の1/4超がパネル外のため他院へ流出」(53%)(`sg-insurer-panel-accessibility.md` §6) |
| **名称と範囲の修正** | 「交渉代行」は採らない。**料金の推奨・集約・共同交渉を行わず**(P3)、料金・条件は医師が各保険者から個別に取得する。CCCSの2022年EP助言はこの点を明示する(出典18)。センターが行うのは**手続・資格・請求・事前承認・データ**の支援である |
| **提供内容** | (1) **保険者別の加入経路テーブル**(§3-2)に沿った申請支援: AIA(社内窓口、請求パターン評価→IHH加入者の診療実績の整理)、GE(Doctor Anywhere窓口、料金同意)、HSBC Life(Fullerton窓口、e-filing設備)、Income(社内窓口、臨床アウトカム提出・医療機関との戦略的提携が評価項目)、Prudential(提携施設で開業する医師のHI推薦: Royal Square、将来はGleneagles・Parkway East)、Singlife(iXchange窓口、CPF e-file設備)。(2) **資格・信用情報の一元管理**(SMC登録、専門医認定、懲戒・訴訟歴、賠償保険、入院権限)。(3) **CPF e-file設備・e-filing・請求代行・支払追跡**(HSBC Life・Singlifeの加入要件。Prudentialは提携HIの事務所からのe-fileが条件)。(4) **事前承認・eLOGの標準化と提出**(各社フォーム)。(5) **EP活性化**: Singlife主パネル在籍医に対し、他社の事前承認を前提としたEP請求の運用支援(Prudentialは申請不要、HSBC LifeはFullerton経由の契約)。(6) **料金ベンチマーク遵守の自己点検ツール**(MOH公表の2,800超のベンチマークに対する自院請求の位置を医師自身が確認する。センターは数値を推奨しない)。(7) **成果データ**(PROM/PREM、合併症、再入院: Incomeが評価項目とする)。(8) **CCRP(臨床請求紛争解決)対応**。(9) 国際PMI・法人チャネル(iXchangeの法人2,000社、Cigna等) |
| **対象** | 全認定医。特に独立医989人(平均2.6社)。Singlife主パネル在籍医はEPの足場を持つ |
| **提供主体と三井の寄与** | **基礎層はiXchangeの内部拡張で立ち上がる**(IHH単独で可能)。三井の寄与が意味を持つのは、(a) 共同事業体として**IHH以外の私立医にも開放し、保険者の参加を得る**場合で、根拠は中立性と全市場データ(§3-6)。(b) 株主支援の場合は、保険商品の共同開発(検証文書 §16-4 三井-7、Swiss Medical Network×Visana型)や保険者との関係構築で側面支援する。三井のBowtie(香港のデジタル保険会社、2021年10月に三井がリード投資〔B〕)は保険者側の知見の接点になり得るが、シンガポールのIP保険者との直接の接点は確認できない【未検証】 |
| **対価と法的線引き** | P2・P3。医師からは固定事務手数料(SMC H3)。保険者・法人からは加入者当たり・請求当たりの固定料金。TPA手数料はHCSA下で患者明細に独立表示(出典16)。SMAは2023年にTPAへの不満(2015年調査で56%が不満、手数料控除後の報酬水準)を再提起しており〔B〕(出典23)、**評判が参入条件**になる |
| **前提条件・依存関係** | **A1(保険者との契約修復)・A2(定額パッケージ)が前提**。施設の価格が是正されなければ、医師の加入支援を尽くしてもGE・Prudentialの給付はIHH病院で使えない(§3-4)。Royal SquareのPPC提携はこの前提が部分的に満たされた例 |
| **成功条件(KPI定義)** | 独立認定医の平均パネル数(目標: グループ医並みの4.4社)、6社全て在籍率(現状9%)、申請から採否までの日数、待機リスト解消数、EP経由の事前承認件数、IHH施設がパネル/事前承認の対象となる症例の比率(現状: Prudential=病院0院・ASC 1施設、GE=Mount Elizabeth 2病院PAC停止)、請求差戻し率 |
| **競合ベンチマーク** | Foundation(3社と直接取り決め、92%が3社以上、Patient Assistance Centre)、Thomson(PPCで約100人一括)、Raffles(AIAで90人超一括)、Fullerton(HSBC Lifeのパネル管理)、AVA(保険者との電子契約) |
| **リスク** | 「交渉代行」に踏み込んだ場合のCCCS審査。保険者が「病院が自院へ誘導する基盤」と見て協力しない(中立性)。MHIC作業部会による手続標準化で窓口の価値が低下。保険者のTPA切替(Singlife 2023年の78人離脱)がIHH独立医に及ぶ |

### A4-iv. グループ内患者リファラル(紹介・配分の調整)

| 要件 | 内容 |
|---|---|
| **目的と効く駆動力** | 駆動力(c)。グループのメリット②(患者の流入)の非資本代替。医師にとって最も直接的な価値であり、最も規律が要る(10月14日文書 §7-4) |
| **法的線引き【確認】** | SMC倫理規程H3: 紹介に対する支払い・贈与・現物補償の授受を禁止、紹介は患者の最善の利益に基づき、紹介先への利害を開示。HCSA広告規則(割引・特典・勧誘的表現の禁止)。PDPA/Health Information法(紹介に伴う情報共有は同意に基づく) |
| **提供内容** | IHHが保有する入口を、紹介対価なしに、臨床的適切性と患者の選択に基づいて提携医に開く: (a) 保険者・TPA向けの提携医ディレクトリ(パネル別、A4-iiiと一体)、(b) GP・健診・Healthspanからの紹介調整(FoundationのHealth Connectiveの同型。Hirslanden型でGPのP&Lを移管しても紹介パスは契約で残す)、(c) 4病院のUCC/A&E当直ローテーションの公平・透明な開放、(d) 国際患者オフィスからの割当(手数料は病院負担。医師の%手数料は不可)、(e) 法人プログラム(iXchange法人2,000社: 健診→専門医、産業医→専門医)、(f) インスティテュート(がん・心臓・脊椎/整形・消化器・脳神経)のMDTと紹介ワークフロー、(g) Find a Doctor・予約・費用案内の強化 |
| **対象** | 全認定医。配分基準は科・サブスペシャリティ・空き枠・認定・技能要件・患者の保険とし、入院数・施設利用量を基準にしない(P5) |
| **提供主体と三井の寄与** | 主体はIHH。三井の寄与は限定的で、(a) 共同事業体を選ぶ場合は(a)(e)のチャネルを事業体に載せる、(b) 株主支援の場合は配分基準の公開・評議会による監査というガバナンスを取締役会で担保する【分析】。三井の既存事業が新たな患者チャネルになる事実は確認できない【未検証】 |
| **対価と法的線引き** | 双方向で紹介対価なし。センターの役務対価は固定(P2)。当直・国際患者の対価は当該業務に対するもので、入院量に連動させない |
| **前提条件・依存関係** | A4-ii(紹介ワークフローの基盤)とA4-iii(パネル別ディレクトリ)。提携専門医評議会(手術枠・ICU・当直・パッケージ設計・品質指標・デカント基準を協議)の設置 |
| **成功条件(KPI定義)** | 入口別の紹介仲介件数とIHH施設での手技・入院への転換率、当直・国際患者配分の公開基準の遵守率(評議会監査)、提携医の新患数の変化(医師側の申告)、患者の代替提供者希望への対応件数 |
| **競合ベンチマーク【確認】** | FoundationのHealth Connective: GP 340人超・専門医350人超、7,800件超の予約仲介(2026年3月末まで、目論見書。10月14日文書 §7-2)、**2026年上期に大手保険者2社がエコシステムパートナーとして参加し、加入者を所属医へ誘導する「管理された紹介経路」を構築**(出典15)。IHHの独立認定医の一部がHealth Connective会員である可能性は高い【未検証: 会員の重複】 |
| **リスク** | 便益が紹介の対価と見られる運用。CCCSが「市場分割」と読む余地(患者の選択を保持することで回避)。非参加医・既存グループ所属医の離反(P6)。Foundationが保険者2社を取り込んだことで、保険者経由の入口でIHHが後手に回る |

---

## ⑤ 三井の関与形態の比較: 共同事業体(a) vs 株主としての支援(b)

### 5-1. 2つの形態の定義【分析】

- **(a) 共同事業体**: 補遺6 §17-1(4)の現実的な形。IHHがiXchangeを現物出資して少数株主となり、三井が過半、保険者または政府系(Temasek系)が参加する新会社が、A4-iii(支払者対応センター)とA4-ii(クリニック基盤)を全私立医向けに運営し、A4-i(事務)とA4-iv(紹介調整の基盤部分)をサービスとして載せる。
- **(b) 株主としての支援**: 三井は新たな資本を出さず(またはIHHレベルの資本に限り)、筆頭株主としてIHH取締役会で専任組織・KPI・規律(P1〜P6)の設定を後押しし、三井側の資産(保険者との関係、データ事業の受け皿、保険商品の共同開発)を提供する。A4-i〜ivはIHH(iXchange・4病院管理部門・Parkway Shenton)が内部で実行する。

### 5-2. 比較表【分析】

| 評価軸 | (a) 共同事業体 | (b) 株主としての支援 |
|---|---|---|
| 効く駆動力 | (a)(c)。中立化により保険者の参加を得やすく、全私立医に開放できる | (c)が中心。(a)はA1・A2(IHH自身の価格・提携)に依存 |
| **パネルアクセスへの効果** | §③の判定どおり、**出資自体はアクセスを生まない**。効くのは保険者の共同参加が得られた場合の「窓口の共有」と、全市場データによる保険者への訴求 | 同左。IHHの施設提携(Royal Square型)と加入支援で同じ効果を得られる |
| 中立性 | 高い(病院でも専門医グループでもない株主)。ただし三井はIHH筆頭株主のため完全中立とは見なされず、保険者・政府系の共同出資が担保 | 低い(IHHが自ら運営)。Prudentialの機関主導、GEのPAC停止のような警戒は残る |
| 保険者の受容 | 既存TPAからの切替に消極的(Singlife 2023年の前例)。Singlife(iXchange)とGE(Doctor Anywhere=IHH出資先)が起点 | IHH×保険者の既存提携(AIA・GE・Income・Singlife、Cigna)の延長で進む |
| 規制・ガバナンス | IHH取締役会の関連当事者取引の承認(Bursa規則)、CCCSの垂直的審査の可能性、SMC H3・HCSAの線引きは同じ | 関連当事者取引なし。CCCS・SMCの線引きは同じ |
| 資本・時間 | 新会社の設立、IHHの現物出資の評価、保険者との交渉。HIA施行(2027年初)前の12〜24か月が窓(補遺6) | 既存資産の組み替えで基礎層6〜12か月、C+外来モジュール12〜18か月(10月14日文書 §7-8) |
| データ | 全私立医の症例の行き先・定額商品の原価データが事業体に集まる(保険目的のNEHR利用は不可) | IHH内部のデータに限る。三井のデータ事業(Oncoshot等)は研究目的で別経路 |
| 競合との位置 | AVA(全病院に導入済みと主張)・Fullerton(三菱商事)・MHC(HMI)と正面競合 | AVAとの相互接続または棲み分けを選べる |
| IHHの他株主との関係 | IHHから支払者接点の支配が外れる構図。Khazanah・少数株主の同意が要る | 問題なし |
| 出口 | IHHへの売却、上場、保険者への持分売却(Columbia Asiaの前例どおり出口を先に置く: 検証文書 §16-4 三井-8) | — |
| A4-i〜ivとの適合 | A4-iii・iiは事業体の中核。A4-i・ivはサービスとして載せられるが、IHHの入口(GP・救急・国際)はIHH側に残る | A4-i〜ivすべてIHH内部で完結 |
| 主要リスク | 保険者が参加しない、AVAに先行される、IHH取締役会が支配権を手放さない、単体の収益性が薄い(Fullerton・Medinex・AVAの前例) | IHHの実行力(専任組織)、中立性の限界、Foundation等の対抗 |

### 5-3. 推奨【分析】

**段階的に進める。**
1. **まず(b)で基礎層を立ち上げる**: A4-i(事務の基礎層)、A4-iii(保険者別の加入支援・e-filing・事前承認・EP活性化)、A4-iv(ディレクトリ・当直ローテーション・紹介調整)は、iXchangeと病院管理部門の内部拡張で実行でき、三井の資本を要しない。三井は取締役会で専任組織・KPI・規律(P1〜P6)の文書化と、A1・A2(価格・施設提携)の先行を求める。
2. **A4-iiはAVAの位置を確認してから**: IHH病院内でのAVAの稼働範囲、独立医クリニックのAVA接続状況、C+外来モジュールの開発状況を確認し、自前・相互接続・提携のいずれかを決める。
3. **(a)は3条件が揃った場合に限って進める**: (i) 保険者または政府系の共同出資意思、(ii) IHH取締役会がiXchangeの現物出資と少数化を承認する見込み、(iii) 事業体の価値を「アクセス」ではなく「中立性・開放・データ」で説明できること(§3-6)。3条件のいずれかが欠ければ、(b)の延長として「iXchangeの保険者向け機能の拡張+全私立医への有償開放」に留める。
4. **(a)を進める場合でも、A4-ivの入口(GP・救急・国際患者・法人)はIHH側に残す**。これらはIHHの施設と不可分であり、事業体に移すと紹介対価の外形(事業体が医師に患者を売る)を作りかねない。

---

## ⑥ 両社の合意が要る論点と、三井がIHHに確認すべき事項【分析】

### 6-1. 合意事項(設計要件として文書化するもの)

1. **A1・A2の先行**: 提携専門医プログラムは、施設の価格・請求管理の保険者への約束(Royal Square型のPPC提携、GEとの請求額是正、定額パッケージ)と同時に進める。これなしに加入支援だけを行っても、GE・Prudentialの給付はIHH病院で使えない。
2. **対価の原則**: 医師から取る対価は固定(サブスクリプション・事務手数料)に限り、報酬・請求額比例を用いない。TPA手数料は明細に独立表示する。
3. **同一条件と非連動**: 全認定医に同一条件、入院量・施設利用量・紹介量と非連動、資格要件の公開、提携専門医評議会による監査。
4. **料金に触れない**: センター・事業体は料金を推奨・集約・交渉せず、医師は各保険者から個別に料金・条件を取得する。内部規程と研修で担保し、必要に応じCCCSに相談する。
5. **データ経路**: NEHRデータは診療目的に限定。保険者向けデータは患者同意に基づく別経路。三井のデータ事業(研究・創薬)は匿名化・施設内処理(Oncoshot型)に限る。
6. **テナント中立**: 非参加医・既存グループ所属医に同じ施設・当直・ディレクトリの基準を適用する。
7. **(a)を選ぶ場合**: iXchangeの現物出資の評価、IHHの持分とROFR、保険者・政府系の参加条件、IHH以外の私立医への開放条件、出口の設計。

### 6-2. 三井がIHHに確認すべき事項(社内情報)

| 事項 | 目的 |
|---|---|
| iXchangeの契約: AIA・GE・Income・Singlife・Cignaそれぞれで担う機能(パネル事務、事前承認、請求審査、データ接続)、手数料体系、「2つのShieldプログラム」の相手先 | A4-iiiの基礎層の起点と、(a)の事業価値の把握 |
| 認定医ごとのパネル在籍状況(保険者別)と、申請して不成功・待機中の医師数 | A4-iiiの対象と優先順位 |
| 認定医ごとの入院・日帰り症例の施設別配分(ロイヤルティ) | プログラム全体の効果測定の基準値 |
| IHH病院内でのAVAの稼働範囲、独立医クリニックのAVA・NEHR接続状況、C+外来モジュールの開発状況 | A4-iiの自前・相互接続・提携の判断 |
| GEとの協議状況(PAC再開の条件)、PrudentialのHI-led参加条件(Gleneagles・Parkway East) | A1の見通し=A4-iiiの前提 |
| 4病院のUCC/A&E当直配分ルール、国際患者オフィスの割当基準、GP紹介の現行フロー | A4-ivの配分基準の公開に向けた現状把握 |
| Mount Elizabeth病院CEOとParkway Shenton CEOの兼務解消と、アウト・オブ・ホスピタル専任組織の設置意向 | 実行体制 |
| Health Connective会員となっているIHH独立認定医の人数(Foundation側の公開情報では確認不可) | A4-ivの競合度 |

---

## ⑦ 本書で確認できなかった事項【未検証】(再掲と追加)

- §3-7の各項目(iXchangeの2つ目のShieldプログラム、Singlifeの旧TPA、GE PACの現状、EPの各社運用と新ライダー下の扱い、Fullertonの出資比率、Doctor AnywhereのIHH持分)。
- 三井のシンガポールIP保険者との直接の接点(Bowtieは香港)。三井の「保険会社・製薬会社とのデータ新事業」発言(2020年10月16日のNikkei Asiaインタビュー、Insurance Business Asia経由で確認)以降の、保険者側の具体的な提携の有無。
- 三井の中期経営計画2029の原文(本環境から取得不可。Wellness Ecosystem Creation 2.0の記述は2026年9月10日の三井×Oncoshot発表〔A〕と検索要旨〔B〕に依拠)。
- IHH病院内でのAVAの稼働範囲、独立医クリニックのAVA接続状況。
- 三井が過去にシンガポールで法人向け健康保険・福利厚生チャネルを持つか(確認できず。A4-ivの三井寄与は限定的と評価)。

---

## ⑧ 出典

### A = 原文を取得して本文確認

1. MOH「Criteria for Inclusion of Medical Specialists into Insurer's Panel for Integrated Shield Plans」(国会答弁、2021年5月10日) — https://www.moh.gov.sg/newsroom/criteria-for-inclusion-of-medical-specialists-into-insurer's-panel-for-integrated-shield/ (保険者が独立に採否を決定、競争法に反しない、選定基準の透明化を奨励、MHICの4ワークストリーム)
2. MOH「About Integrated Shield Plans」(IPパネル統計、2026年4月30日更新) — https://www.moh.gov.sg/managing-expenses/schemes-and-subsidies/integrated-shield-plans/about-integrated-shield-plans/ (7社の主パネル人数2023〜2025、Singlife 2023年9月TPA変更の脚注、GE 2024年の計画的見直し、「各保険者は望ましいパネル規模について異なる考慮を持ち得る」)
3. MOH「Ensuring the Sustainability of Private Healthcare Insurance」(国会答弁、2025年9月24日) — https://www.moh.gov.sg/newsroom/ensuring-the-sustainability-of-private-healthcare-insurance/ (600人以上、専門科レベルのカバレッジ、EP、2,800超の料金ベンチマーク、私立病院の料金設定の指針を検討)
4. MOH「Collaborative and Multi-stakeholder Approach Needed to Address Deeper Insurance Issues」(Lydia Loh氏のフォーラム回答、2025年10月6日) — https://www.moh.gov.sg/newsroom/collaborative-and-multi-stakeholder-approach-needed-to-address-deeper-insurance-issues (料金超過・不適切請求による除外の容認、過度な入替の回避、MHIC下のパネル作業部会)
5. LIA「Insurance Panel of IP Insurers: Application Process, Requirements and Considerations」(2025年2月25日版、PDF原文をローカルでテキスト化) — https://www.lia.org.sg/media/4476/insurance-panel-of-ip-insurers_application-process-requirements-and-consideration_20250225.pdf (7社の申請窓口・要件・考慮事項の原文。HSBC Life「Fullerton HealthをTPAとしてパネル管理に任命」「Fullerton Healthと共同で選定」、GE=doctoranywhere.comドメイン、Singlife=ixchange.com.sgドメインまたは社内、Prudential=HI主導で個人申請不可)
6. Prudential Singapore「PRUPanel Connect」(2025年10月14日時点の情報) — https://www.prudential.com.sg/ppc (病院主導モデル、1,700人超、提携私立病院3院、日帰り手術センター11、外来腫瘍センター9、HI事務所からのe-file)
7. Singlife「Singlife Partners IHH Healthcare Singapore to Enhance Healthcare Coverage Solutions」(2023年8月14日、SGX掲載PDFをローカルでテキスト化) — https://links.sgx.com/1.0.0/corporate-announcements/O4B45I4D3Q5M19OC/768939_News%20Release%20-%20Singlife%20Partners%20IHH%20Healthcare%20Singapore%20to%20Enhance%20Healthcare%20Coverage%20Solutions.pdf (2023年9月9日から入院の事前承認不要、iXchangeが管理する500人超、「パネルネットワーク管理と請求審査」、IHHSGがSinglifeを戦略的保険パートナーに選定、iXchange=IHH SGのTPA部門)
8. Mitsubishi Corporation「Mitsubishi Corporation Invests in Fullerton Health」(2025年8月26日、ACN Newswire配信版) — https://www.acnnewswire.com/press-release/english/102094/mitsubishi-corporation-invests-in-fullerton-health ／ Fullerton Health プレスリリース(2025年8月26日) — https://www.fullertonhealth.com/?p=11496 (2025年8月22日完了、戦略的少数持分、TPA・HMO・クリニック・画像・健診を保有、9市場)
9. IHH Healthcare「IHH Singapore Collaborates with Insurers to Improve Affordability of Private Hospital Care」(2026年7月10日) — https://www.ihhhealthcare.com/newsroom/care-in-action/ihh-singapore-collaborates-with-insurers-to-improve-affordability-of-private-hospital-care (AIA・GE・Income・Singlife、iXchangeが入院前から請求までを接続、請求額上昇率7〜10%→低一桁%、循環器パッケージ)
10. BMJ International Forum on Quality and Safety in Healthcare (Singapore)「Loh Chek Chai」プロフィール — https://healthcareimprovementforum.bmj.com/singapore/?p=618 (iXchange CEO、2023年に2つのShield TPAプログラムを管理する初のTPA、2022年新TPAシステム、OSPAR・ISO 27001)
14. Thomson Medical「Thomson Medical Partners with Prudential to Enhance Healthcare Access for Patients」(2025年4月1日) — https://www.thomsonmedical.com/news/thomson-medical-partners-with-prudential-to-enhance-healthcare-access-for-patients (約100人を一括追加、1,700人超、eLOG S$30,000)
15. Foundation Healthcare Holdings「1H2026 Earnings Call Script」(2026年8月13日、SGX掲載PDFをローカルでテキスト化) — https://links.sgx.com/1.0.0/corporate-announcements/W24OZ7ZOF8FK4CPV/901088_FHH%201H26%20Earnings%20Call%20Script.pdf (「6社中3社と直接の取り決め」「92%が3社以上のパネル」「AVAは全私立・公立病院に導入済み」「地域の私立病院運営者と入院モジュールのUAT完了」「Health Connectiveに大手保険者2社がエコシステムパートナーとして参加」「hospital-agnostic」「新規専門医の初年度売上平均S$1.3百万」)
16. MOH「Regulation of Third Party Administrators」(国会答弁、2021年5月11日) — https://www.moh.gov.sg/newsroom/regulation-of-third-party-administrators/ (TPAは免許対象外、HCSAで明細にTPA手数料を独立表示、SMC規程: TPAへの手数料は提供サービス・徴収料金に基づかない、fee splittingに当たる高額は不可)
17. Asia Advisers Network「Singapore: Insured patients with IP riders now potentially have choice of more than 1,000 specialists」(2022年7月11日) — https://www.asiaadvisersnetwork.com/Article?aid=80989 (EPの7社合意、自己負担上限S$3,000、Income・Singlifeは契約更新時から、事前承認による医療必要性・料金の審査、約1,080人=私立専門医1,287人の84%)
18. CCCS「Advice to MOH on the Extended Panel initiative」(2022年8月24日) — https://www.ccs.gov.sg/case-register/public-register/government-advisories/advice-to-moh-on-the-extended-panel-initiative (EP医候補は料金・条件を各保険者から個別に取得すべき)
19. Prudential Singapore「Extended Panel」 — https://www.prudential.com.sg/ppc-ep (他社主パネル在籍・事前承認必須・料金表遵守、申請不要、施設種別で給付が異なる)
20. MOH「New Requirements for Integrated Shield Plan Riders…」(2025年11月26日) — https://www.moh.gov.sg/newsroom/new-requirements-for-integrated-shield-plan-riders-to-strengthen-sustainability-of-private-health-insurance-and-address-rising-healthcare-costs/ (2026年4月1日〜、自己負担上限最低S$6,000は「パネルまたは事前承認済みの請求といった適格な請求にのみ適用」)
21. gov.sg「What is the Health Information Bill?」(2026年1月) — https://www.gov.sg/explainers/parliament-jan2026/ (2026年1月12日可決、2027年初施行、全ライセンス事業者にNEHR寄与を義務化、雇用・保険目的のアクセスを厳格に禁止、break glassの監査、インシデント通知義務)
22. BioSpectrum Asia「Foundation Healthcare collaborates with Great Eastern to enhance value for policyholders in Singapore」(2025年4月7日) — https://www.biospectrumasia.com/news/30/25834/foundation-healthcare-collaborates-with-great-eastern-to-enhance-value-for-policyholders-in-singapore.html (取引自動化のデジタルソリューションの採用を探索、費用の共同管理)
24. HSBC Life「Panel and Letter of Guarantee」 — https://www.insurance.hsbc.com.sg/health/products/shield/panel-and-letter-of-guarantee/ (選定基準3項目、700超の専門医クリニック、LOG上限)
25. Insurance Business Asia「Japan's Mitsui and Co. eager to work with Warren Buffett's Berkshire」(2020年10月16日) — https://www.insurancebusinessmag.com/asia/news/breaking-news/japans-mitsui-and-co--eager-to-work-with-warren-buffetts-berkshire-236441.aspx (安永CEO「保険会社・製薬会社とデータを使った新事業を作りたい」、IHH外来600万人・入院60万人)
- M2. MarketScreener「Mitsui: Asia–US Clinical Data Collaboration Built on IHH's Clinical Data」(2026年9月10日) — https://www.marketscreener.com/news/mitsui-asiaa-us-clinical-data-collaboration-built-on-ihh-s-clinical-data-ce785bdfd88af62d (中期経営計画2029「Wellness Ecosystem Creation 2.0」、Oncoshot/MSK iHub、施設内での構造化・匿名化、IHH 89病院・10か国)

### B = 検索エンジン経由で要旨を確認(原文サイトが本環境から取得不可)

11. International Assistance Group「Welcome iXchange」(2025年4月) — https://www.international-assistance-group.com/welcome-ixchange-international-assistance-group-expands-asia-presence-with-new-singapore-core-partner/ (法人2,000社超、GP 600超、専門医800人超、歯科280超、中医20超)
12. Cigna Healthcare Singapore「Celebrating Cigna Healthcare Singapore's 15 years」(2026年3月31日、Malay Mail配信版) — https://www.malaymail.com/news/money/mediaoutreach/2026/03/31/celebrating-cigna-healthcare-singapores-15-years-of-connected-world-class-healthcare/457556 (2025年末にiXchangeと価値ベース契約を開始)
13. AIA Singapore「AIA Singapore partnering with Raffles Hospital to boost accessibility of quality healthcare in Singapore」(2025年1月23日) — https://aia.com.sg/en/about-aia/media-centre/press-releases/2025/aia-singapore-partnering-with-raffles-hospital-to-boost-accessibility-of-quality-healthcare-in-singapore (90人超をAQHPに追加、私立パネル約700人、品質指標の共有、MOHベンチマークに沿った請求の共同管理)
23. SMA News「Third-Party Administrators: A Call for Feedback」(2023年11月) — https://sma.org.sg/news/2023/November/Third-Party-Administrators-A-Call-for-Feedback (2015年調査で56%が不満、手数料控除後の報酬水準)
26. IHH Healthcare「IHH Healthcare and Prudential partner to offer policyholders more day surgery care options at Mount Elizabeth Royal Square」(2026年8月17日、Malay Mail配信版) — https://www.malaymail.com/news/money/mediaoutreach/2026/08/17/ihh-healthcare-and-prudential-partner-to-offer-policyholders-more-day-surgery-care-options-at-mount-elizabeth-royal-square/481308 (2026年8月1日からPPCに参加、IHH SG初の施設)
27. Square Peg「Investment Notes: Doctor Anywhere」／The Edge Markets「IHH Healthcare invests in Doctor Anywhere」(2020年3月) — https://www.theedgemarkets.com/article/ihh-healthcare-invests-doctor-anywhere (IHHがSeries B US$27百万を共同リード、少数持分)
28. Singapore Law Watch / Straits Times「Insurer Great Eastern pauses pre-authorisation certificates for Mount Elizabeth admissions」(2025年6月) — https://www.singaporelawwatch.sg/Headlines/insurer-great-eastern-pauses-pre-authorisation-certificates-for-mount-elizabeth-admissions (2025年6月17日〜、他院比20〜30%高、Prudential・AIAは事前承認を継続。2026年10月時点で再開を報じる資料は確認できず)
- M1. IHH Healthcare Annual Report 2024(2025年3月28日時点の大株主: MBK Healthcare Management経由で三井32.76%、Khazanah 25.91%、EPF 10.55%) — https://www.insage.com.my/interactiveAR/IHH/interactiveAR2024/239 ／ Business Today(2024年9月30日、32.8%) — https://www.businesstoday.com.my/2024/09/30/mitsuis-eyes-bigger-stake-in-ihh-as-valuation-remains-low/
- M3. Mitsui & Co.「Medium-term Management Plan 2029」(2026年5月1日) — https://www.mitsui.com/jp/en/ir/library/meeting/pdf/en_263_4q_chukei.pdf (Wellness Ecosystem Creation 2.0を重点施策として継続、病院事業を中心にデータを活用し創薬支援等へ拡張)／Bowtie「Series B1 round」(2021年10月、三井がリード、MBK Healthcare「初の健康保険会社投資」) — https://www.bowtie.com.hk/blog/en/press-release/bowtie-series-b1-round/
- SMC倫理規程H3(7)の要旨(SMA「The Basics of Fee-Splitting」2017年9月、SMA「Joint Advisory on Fees Paid to Managed Care and TPA Companies」2017年5月) — https://sma.org.sg/news/2017/September/the-basics-of-fee-splitting (TPAへの手数料は実際の業務を反映、%手数料はfee splittingと見なされ得る、執行は2017年7月1日に延期)

### 既存文書(本リポジトリ)
- `ihh-sg-hypotheses-verification.md` §8-2、§16-1〜16-5、§17-1
- `ihh-sg-inpatient-loyalty-asc-payor-strategy.md` §7-1〜7-9、§8 層D、KPI、主要リスク
- `sg-insurer-panel-accessibility.md` §3〜§6、§10〜§11
- `ihh-sg-medical-suite-specialists.md`(認定医1,295人の一次データ)、`parkwayshenton-divestment-strategy.md` §2(iXchangeの法人上の位置)
