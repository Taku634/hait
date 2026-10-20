# IHH入居専門医の「グループ加入インセンティブ」を削ぐ提携専門医プログラム — A4-i〜ivの設計要件(IHH×三井物産の協働前提)

**作成日**: 2026年10月20日(同日改訂: 初版の「iXchange等への三井出資によるパネルアクセス獲得」の検証は、出資がアクセスを生まないという結論で確定したため付録Aに要旨のみ残し、本文を**「IHHに入居する専門医が専門医グループへ加入するインセンティブを削ぐ」**設計に絞って全面改訂した)
**位置づけ**: `ihh-sg-hypotheses-verification.md` 補遺5(§16-2)のアクション **A4-i(非診療業務の解放)・A4-ii(電カル連携とデータ取得)・A4-iii(Payor対応)・A4-iv(グループ内患者リファラル)** を、「グループが医師に与えているものを、グループに入らずにIHHから得られるようにする」という一点に絞って設計要件レベルまで精緻化する。10月14日文書 `ihh-sg-inpatient-loyalty-asc-payor-strategy.md` §7(提携専門医プログラムの原型)・§8 層Dを継承し、グループ4社の取引条件(`sg-four-specialist-groups-incentives-growth.md`)と照らして「医師の損得」の形に落とす。
**想定読者**: 三井物産の投資・事業部門。三井の関与は筆頭株主としての支援に限定し、新規の資本投下(TPA出資等)は前提にしない。
**粒度**: 設計要件(目的・提供内容・対象・対価・法的線引き・前提条件・成功条件・リスク)まで。スケジュール・担当割り・費用概算は書かない。
**表記ルール**: 【確認】=出典原文で裏付けた事実、【算出】=出典の数値から計算した値、【推定】=複数事実から同定した事項、【未検証】=公開情報で確認できなかった事項(推測で埋めない)、【分析】=確認済み事実から導いた本書の評価。出典は「A=原文を取得して本文確認」「B=検索エンジン経由で要旨を確認」に区分し巻末に記載。既存レポートからの引用は「(文書名 §節)」で示す。
**本書の範囲外**: A4-v(給料保証)・A4-vi(クリニックのEquity取得)、A3(ASC持分)、層C(入院依存科への資本参加)。ただし本プログラムで埋められない「施設料の持分」「現金化」の2つのメリットは、A3・層Cへの接続点として§⑤で明示する。

---

## 調査手順(Step-by-Step)

1. **問いの再定義**: 「IHH入居医がグループへ加入するインセンティブ」を、グループ側の開示(Foundation目論見書・1H26決算説明会、TalkMed Composite Document、OUE公告、HMI発表)から**医師が受け取るもの**と**医師が差し出すもの**に分解し、IHH認定医1,295人の一次データ(独立医989人、グループ所属306人)でコホート別の重みを付けた。
2. **既存文書の継承**: 10月14日文書 §7-2(8つのメリット)・§7-3(代替可能性)・§7-7(コホート別提案)と、検証文書 §8-2(条件・制約)・§16-2(A4-i〜vi)を再読し、A4-i〜ivに該当する部分を抜き出した。
3. **一次資料の再確認**: Foundation Healthcareの2026年上期決算説明会スクリプト(SGX、2026年8月13日)をローカルでテキスト化し、「保険者3社と直接取り決め」「92%が3社以上のパネル」「Health Connectiveに大手保険者2社が参加」「hospital-agnostic」「新規専門医の初年度売上S$1.3百万」を原文で確認した。LIAの7社比較表2025年2月25日版(申請窓口の原文)、CCCSのExtended Panel助言(2022年8月24日)、MOHのTPA規制答弁(2021年5月11日)、Health Information法のgov.sg解説、MOHの2025年9〜11月の発表を原文で確認した(A区分)。
4. **設計の整理**: グループの8つのメリットごとに「A4のどれで、どこまで埋められるか」「残る差分は何か」を判定し、A4-i〜ivの設計要件を「グループに入った場合との損得比較」の形で記述した。
5. **制約の明示**: SMC倫理規程H3(紹介対価・報酬比例手数料の禁止)、CCCS第34条(料金の推奨・集約・共同交渉の禁止)、HCSA(TPA手数料の明細表示・広告規則)、PDPA/Health Information法(保険目的のNEHRアクセス禁止)を各施策の設計に織り込んだ。

---

## ① Executive Summary

1. **医師がグループに入る「価格」は高い。IHHの提携プログラムはこの価格差を訴求の中心に置く**【確認→分析】。Foundationに入る医師は診療法人の60%を現金で売り、残り40%を親会社株と交換し(1〜10年の売却禁止、半分は自クリニック業績・半分は自分が採用した新規医の売上目標で解除)、フルタイム雇用(基本給+クリニック群業績連動の変動給)になる。Tamarindは対価の67.2%を非上場株で再投資し、40.3%は7年ベスティング、退職時は強制譲渡。OUE/O2は60/40の二層JV。HMIは過半数取得(条件非開示)(出典1〜3)。IHH提携医は**診療法人の100%を保持し、固定の役務対価と施設の利用料だけを払う**。
2. **グループが与える8つのメリットのうち、A4-i〜ivで埋められるのは「支払者接続」「患者の流入」「事務」と「立上げ支援」の非資本部分であり、「施設料の持分」と「現金化・承継」は埋められない**【分析】。前者4つはグループ側の開示で最も強調されるもの(Foundation目論見書「保険者のパネル採用が専門医を引き付け維持する主要因」、1H26「規模・事務支援・保険者提携・患者ファネルが民間参入直後の医師にとっての魅力」)であり、ここを先回りすれば**開業直後と中堅の独立医**に対する加入動機の大半を削げる。後者2つはシニア医の動機であり、A3(ASC持分)・層C(少数持分)・承継サービスに接続する(§⑤)。
3. **A4-iii(支払者対応)は「交渉」を外し、保険者7社それぞれの窓口に沿った加入支援・e-filing・事前承認・Extended Panel(EP)活性化・成果データに置き換える**【確認→分析】。パネル採否は各保険者が独立に決め(MOH 2021年5月10日)、窓口は7社で全て異なる(LIA 2025年版原文)。CCCSは2022年のEP助言で「料金・条件は各保険者から個別に取得すべき」と条件を付けており、センターが医師間で料金情報を集約・中継してはならない(出典5・6・8)。Foundationが「3社と直接取り決めがあり所属医の加入経路が簡素化」と語る機能は、料金に触れない範囲で病院も提供できる(出典4)。
4. **A4-iv(患者の流入)が最も効き、最も規律が要る**【分析】。IHHはグループが持たない入口(4病院のUCC/A&E当直、国際患者オフィス、法人2,000社、GP約50クリニック、健診・Healthspan、Find a Doctor)を持つ。これを紹介対価なし・配分基準公開・患者の選択保持の条件で提携医に開く。Foundationは2026年上期にHealth Connectiveへ大手保険者2社を参加させ「加入者を所属医へ誘導する管理された紹介経路」を作っており(出典4)、IHHが後手に回ると独立医の流出は加速する。
5. **A4-ii(電カル)はHealth Information法(2027年初施行、全ライセンス事業者にNEHR寄与を義務化)が契機だが、IHH病院内でのAVA(Foundation)の稼働範囲を確認してから自前・相互接続・提携を決める**【確認→分析】。Foundationは「AVAは全私立・公立病院に導入済み」「地域の私立病院運営者と入院モジュールのUATを完了」と説明する(出典4)。
6. **コホート別の設計**【分析】: (a) 開業直後(民間5年未満。卒後15年未満は認定医の3%、民間新規専門医は年35人)には「Emerging Specialist Package」(Annexe・病院保有スイート、1〜2年の事務・パネル加入・紹介調整支援、市場賃料内のフェーズイン)、(b) 中堅独立医(主力。卒後15〜34年が7割)には支払者対応+事務+患者融通の基礎層無償・上位層有償、(c) シニア(卒後35年超26〜28%)には承継サービス(後継者マッチング、SPC持分の後継移転)とA3への接続、(d) 既グループ所属306人は対象外だが施設・パネルは同一条件で開放する。
7. **粘着性の窓は今**【確認→分析】。米国の査読研究(JAMA Health Forum 2025)はPE出口後2年の医師残留率44%(対照60%)を示し、グループの囲い込みが契約上の「甘味料」に依存することを示す(出典9)。Foundationの売却医師のモラトリアムは1〜10年、Tamarindのベスティングは2031年まで。Foundationは上場資金S$55百万で2026年下期に国内買収を再開すると明言しており(出典1・4)、白地(整形27%、一般外科22%、消化器22%、ENT 28%、産婦人科9%、麻酔12%のグループ所属率)の独立医に対して「入らなくても得られる」選択肢を先に提示できるかが勝負である。
8. **三井の役割は筆頭株主としての支援に限る**【分析】。(i) 取締役会で専任組織(アウト・オブ・ホスピタル担当、Mount Elizabeth病院CEOとParkway Shenton CEOの兼務解消)とKPI(グループ流出数・独立医のパネル数・症例捕捉率)を設定させる、(ii) 規律(P1〜P6)の文書化を求める、(iii) A1(保険者との契約修復)・A2(定額パッケージ)を本プログラムの前提として先行させる。TPAへの出資はアクセスを生まないため採らない(付録A)。

---

## ② 問題の定義: 誰が、何を得るためにグループへ入り、何を差し出しているか

### 2-1. グループに入る医師が受け取るもの(グループ側の開示)【確認】

| # | メリット | グループ側の証拠 | 出典 |
|---|---|---|---|
| 1 | **支払者接続(パネル)** | Foundation目論見書「保険者のパネル採用が専門医を引き付け維持する主要因」。1H26説明会「6社中3社と直接の取り決めがあり、所属医はより簡素な加入経路を得る」「92%が3社以上のパネルに在籍」。Frost & Sullivan「ソロ・小規模開業医が複数パネルの要件を維持するのは重い運用負担」 | 出典1・4、10月14日文書 §7-2 |
| 2 | **患者の流入** | Foundation: Health Connective(GP 340人超・専門医350人超、7,800件超の予約仲介、2026年3月末)、**2026年上期に大手保険者2社がエコシステムパートナーとして参加し「加入者を所属医へ誘導する管理された紹介経路」**、Patient Assistance Centre、「AVAは当社プラットフォームへの自然な患者ファネル」。HMI: OneCare GP約40・MHC法人会員80万人 | 出典1・4 |
| 3 | **事務・バックオフィス** | Foundation: 本社人員43人(2024年末)→71人(2026年3月)、調達・マーケ・財務・人事・IT・法務を集約。1H26「強い事務支援」。Medinex: 開業支援・会計・人事・薬剤調達を月次課金 | 出典1・4、`sg-specialist-group-typology.md` §7.2 |
| 4 | **施設と施設料** | Foundation「医療センターを増やすことで第三者施設が得ていた施設料・診断料を取り込む」「報酬は自社医療センター利用を促す設計」。HC Surgical 51/49、OUE 60/40 | 出典1・3 |
| 5 | **流動性・承継** | Foundation: 診療法人の60%を現金化(2023年だけでS$337.2百万)、残り40%は上場株。Tamarind: Leaver時に後継者へ持分移転可。OUE: アーンアウトS$9.3百万支払済 | 出典1〜3 |
| 6 | **立上げ支援** | Foundation 1H26「新規専門医は初年度平均S$1.3百万を貢献」(既存医S$2.7百万の約48%)、「規模・強い事務支援・保険者提携・成長する患者ファネルが、民間参入直後の医師にとっての魅力」、採用組37人(2026年下期見込み) | 出典4、10月14日文書 §7-2 |
| 7 | **臨床・キャリア** | Tamarind「サブスペシャリティ化とキャリア進展」。Foundation: 11領域の品質運営委員会、2027年からPROM/PREM | 出典1・2 |
| 8 | **統治・持分** | Tamarind: 重要事項に医師取締役半数以上の承認。Foundation: 上場後1年以内にPSP 1.0%を採用組に付与、全医師向けESOPを検討 | 出典1・2・4 |

### 2-2. グループに入る医師が差し出すもの(取引条件)【確認】

| グループ | 差し出すもの | 出典 |
|---|---|---|
| **Foundation** | 診療法人の**60%を現金で売却**→残り40%を**親会社株(上場後35.9%)と交換**し100%子会社化→株式は**1〜10年の売却禁止**(半分MP1=自クリニック業績目標、半分MP2=自分が採用した新規専門医の売上目標で解除。未達分はエスクロー代理人が市場売却しShortfallを会社に支払う)→**フルタイム雇用**(基本給および/またはクリニック群の財務業績連動の変動給) | 出典1(目論見書pp.157-160, 231-233, 195) |
| **Tamarind** | 対価の**67.2%を非上場株で再投資**(現金32.8%)、うち40.3%は**7年ベスティング**(2025〜2031年)、退職時は**強制譲渡**、譲渡同意制 | 出典2 |
| **OUE / O2** | 持株会社を60:40、各法人の60%を持株会社が保有する二層。対価の40%は持株会社株式 | 出典3 |
| **HMI** | 過半数(「最大51%」等)を譲渡し、創業医は医療経営トップに残留。持分比率・ベスティング・退出条項は【非公開】 | 出典3 |
| **IHH提携医(本書の設計)** | **診療法人の100%を保持**。固定の役務対価(サブスクリプション・事務手数料)と、使った施設の市場水準の利用料・賃料のみ | 本書 §④ |

### 2-3. コホート別の重み(IHH認定医1,295人の一次データ)【算出/推定】

| コホート | 規模 | 主な動機(§2-1の#) | 現状の支払者接続 | 出典 |
|---|---|---|---|---|
| 開業直後(民間5年未満) | 卒後15年未満は3%(18人)。民間新規専門医は年35人、供給は公的部門からの中堅移籍 | 1・2・3・6(SMA会長2023「開業直後の若い世代は主パネルに入れない」) | 不利(AIA「公立からの開業時に自動移行なし」、請求実績が乏しい) | `ihh-sg-medical-suite-specialists.md` §4、`sg-insurer-panel-accessibility.md` §6・§11 |
| 中堅独立医(主力) | 独立医989人の中核。卒後15〜34年が認定医の7割 | 1・2・3(・4) | 平均パネル2.6社(グループ医4.4社)、6社全て9%(同43%)。入院依存「高」の科でGE接続41%(同83%)、Prudential 76%(同95%) | 10月14日文書 §2・§7-2 |
| シニア(卒後35年超) | 26%(Mount Elizabeth Orchardは28%)。中央値は卒後27年 | 5・4(現金化と施設料) | — | `ihh-sg-medical-suite-specialists.md` §4 |
| 既グループ所属 | 306人(24%): Foundation 89・Tamarind 45・HMI 30・OUE 25等。科別では腫瘍内科90%、泌尿器47%、眼科39%、循環器37%が既にグループ化 | — | グループは「hospital-agnostic」(Foundation 1H26) | 同 §5-1・§6、出典4 |
| 次のグループ化候補 | 企業資本の入っていない5人以上の共同診療所(Asian Heart & Vascular 10人、Synergy Orthopaedic 9人、Orthopaedics International 8〜9人等)。白地は整形27%・一般外科22%・消化器22%・ENT 28%・産婦人科9%・麻酔12% | 1・2・4・5 | Orthopaedics Internationalは平均パネル4.75社と既に高い | 検証文書 §8-2・§9-2 |

**読み取り**【分析】: A4-i〜ivが効くのは**開業直後と中堅独立医**であり、ここが独立医989人の大半を占める。シニアと共同診療所の動機(現金化・施設料)はA3・層Cでしか埋まらない。したがってA4-i〜ivの目標は「989人の流出を止める」ことであり、「306人を取り戻す」ことではない。

---

## ③ インセンティブ分解: 8つのメリットのどれを、A4のどれで、どこまで埋めるか【分析】

| # | メリット | 埋める施策 | 埋まる程度 | 残る差分とその受け皿 |
|---|---|---|---|---|
| 1 | 支払者接続 | **A4-iii** 支払者対応センター | 高(料金を除く全て) | 料金はグループでも保険者が設定。Prudentialは施設単位のためIHH病院の提携(A1)が前提 |
| 2 | 患者の流入 | **A4-iv** 紹介・配分調整 | 高(IHHの入口はグループより多い) | 保険者経由の入口はFoundationが先行(保険者2社)。A4-iiiと一体で追う |
| 3 | 事務 | **A4-i** 非診療業務のサービス化 | 高 | なし(Medinex型の役務を病院が提供) |
| 4 | 施設と施設料 | (A3・層B: SPC持分) | 本書の範囲外 | **埋まらない**。A3のRoyal Square型SPC持分(30〜49%)に接続 |
| 5 | 流動性・承継 | (層C・承継サービス) | 部分(A4-iの延長で承継マッチングは可能) | **60%現金化は埋まらない**。「売らずに引き継ぐ」選択肢を示す |
| 6 | 立上げ支援 | **A4-i+iii+iv**の束ね(Emerging Specialist Package) | 高(給与保証を除く) | 給与保証(A4-v)は紹介誘因と見られるため採らない。市場賃料内のフェーズインまで |
| 7 | 臨床・キャリア | **A4-ii**(C+接続・MDT)+インスティテュート | 中〜高 | 4病院の症例・設備はグループにない強み |
| 8 | 統治・持分 | 提携専門医評議会(非持分) | 中 | 株式のアップサイドは埋まらない |

**設計上の帰結**: A4-i〜ivは「1・2・3・6・7・8」を束ねて**一つのパッケージ**として提示し、「4・5」はA3・層Cへの**接続点**として同じ窓口から案内する。医師に見せる比較は「Foundation: 60%売却+雇用+1〜10年ロック」対「IHH提携: 100%保持+固定対価」である。

---

## ④ A4-i〜ivの設計要件

### 共通の規律(P1〜P6)【確認→分析】

| 規律 | 内容 | 根拠 |
|---|---|---|
| **P1 同一条件** | 全認定医(独立医・グループ所属医を問わず)に同一条件で提供し、入院数・施設利用量・紹介量と連動させない | SMC倫理規程H3(紹介の対価としての現物補償の禁止)。10月14日文書 §7-6 |
| **P2 固定対価** | 医師から取る対価はクリニック単位の固定サブスクリプションまたは固定事務手数料に限る。診療報酬・請求額の比率は用いない | SMC H3(TPA等への手数料は実際の事務作業に見合う額、報酬比例の禁止)、MOH 2021年5月11日(出典7) |
| **P3 料金に触れない** | 料金の推奨・集約・共同交渉を行わず、料金・条件は医師が各保険者から個別に取得する | CCCS 2010年SMA料金ガイドライン決定、CCCS 2022年EP助言(出典8) |
| **P4 データ経路の分離** | NEHRデータは診療目的に限り、保険者向けの請求・成果データは患者同意に基づく別経路で扱う | Health Information法(保険・雇用目的のアクセスを厳格に禁止)(出典10) |
| **P5 配分基準の公開と患者の選択** | 紹介・当直・国際患者の配分は公開基準で運用し、提携医以外を希望する患者には応じる | SMC H3、CCCS(市場分割と読まれない) |
| **P6 テナント中立** | 非参加の認定医・既存グループ所属医が不利益を受けない(手術枠・当直・ディレクトリの基準は共通) | Hirslanden原則(`ihh-sg-growth-strategy.md` §3) |

### A4-i. 非診療業務の解放 — 「本社機能を、買われる前に病院が提供する」

| 要件 | 内容 |
|---|---|
| **削ぐインセンティブ** | #3 事務、#6 立上げ支援の事務部分。Medinexの教訓は「顧客クリニックがプラットフォームに買われると本社機能がプラットフォーム側に吸収される」(2026年3月期に最大顧客の売却でのれん減損)であり、裏返せば**買われる前にホスト病院が本社機能を提供すれば買われる動機が弱まる**(`sg-specialist-group-typology.md` §7.2、10月14日文書 §7-1)【確認→分析】 |
| **提供内容** | (1) 会計・税務・給与・人事・MOH許認可(HCSA)更新の代行、(2) 消耗品・薬剤・医療賠償保険の団体条件(共同購買。Foundationは集中購買を「買収後シナジーの運営優先課題」と明言)、(3) Parkway Laboratory/Radiologyの優先接続、(4) 開業支援(立地・内装・IT・許認可)、(5) 法務・契約の定型支援、(6) 承継の事務(後継者への診療法人の譲渡手続)。電カル・請求はA4-ii・iiiに分ける |
| **医師の損得(グループ比)** | Foundation: 本社71人の事務を得る対価は診療法人の60%売却と雇用化。IHH提携: 同種の事務を月次課金で得て診療法人は100%保持【分析】 |
| **対象と階層** | 全認定医(P1)。基礎層(許認可案内・団体条件・開業相談)は無償、上位層(会計・人事・開業支援・承継事務)は有償 |
| **対価と法的線引き** | P1・P2。医師が費用の一部を負担し紹介量を考慮しないことを文書化(米国EHR寄付セーフハーバー〔受領者15%負担、紹介量非考慮〕を設計参照〔B〕) |
| **前提条件** | 4病院の購買・人事・財務・法務を再編した専任組織。Foundationは専門医108人に本社71人、認定医1,000人規模には相応の人員が要る(10月14日文書 §7-9) |
| **成功条件(KPI定義)** | 加入率(独立医989人の基礎層・有償層別)、継続率、医師1人当たり事務コストの低減(医師の申告)、年間のグループ流出数(2026年10月の306人を基準) |
| **リスク** | 便益が紹介の対価と見られる運用。非参加テナントの離反。収益事業として自立しない(Medinex: 利益率7割超でも売上横ばい)ため、防衛投資として位置づける |

### A4-ii. 電カル連携とデータ取得 — 「2027年の法令対応を、グループではなく病院が肩代わりする」

| 要件 | 内容 |
|---|---|
| **削ぐインセンティブ** | #3 事務(IT)、#7 臨床(病院との患者単位の接続)、#1 支払者接続の基盤(e-filing・事前承認・PROM) |
| **制度の契機【確認】** | Health Information法: 2026年1月12日可決、2027年初施行予定。全ライセンス医療事業者にアレルギー・予防接種・診断・投薬・検査・画像・退院サマリーのNEHR寄与を義務化。雇用・保険目的のアクセスは厳格に禁止。緊急アクセスは監査、サイバー事故はMOHへ通知義務(出典10)。私立専門医クリニックは未接続が残る層として名指しされた(検証文書 §8-2 9) |
| **提供内容** | (1) C+の外来・クリニックモジュール、または認定クリニック管理システムのNEHR対応版を全認定医に提供、(2) 病院C+と患者単位で接続(紹介・入院・退院サマリーの往復)、(3) e-filing・事前承認・定額パッケージ運用・紹介ワークフロー・PROM/PREM収集を同じ基盤に載せる(A4-iii・ivの基盤)、(4) サイバーセキュリティ・データ保護の法令要件を含めた運用 |
| **医師の損得(グループ比)** | Foundation: AVAと本社ITを得る対価は売却・雇用化。IHH提携: 法令対応と病院接続を費用の一部負担で得る。IHHにとっての価値は「症例の行き先(どの医師のどの症例がどこへ行ったか)」と定額商品の原価データ【分析】 |
| **対価と法的線引き** | P1・P2・P4。保険者向けデータは個々の請求・事前承認の範囲と、集計・匿名化された成果指標に限る |
| **前提条件(先決)** | **IHH病院内でのAVAの稼働範囲の確認**。Foundationは「AVAは全私立・公立病院に導入済み」「地域の私立病院運営者と入院モジュールのUATを完了」「新モジュールのロードマップあり」と説明する(出典4)。IHH病院がその相手方なら、独立医クリニック側もAVAに接続している可能性があり、自前基盤との二重投資か、相互接続かを決める【未検証】 |
| **成功条件(KPI定義)** | 2027年初までにNEHR接続した認定医クリニック数、病院C+との患者単位接続率、e-filing経由の請求比率、PROM/PREM収集率、症例の行き先データの網羅率 |
| **リスク** | AVAとの先行差。NEHRデータの保険目的利用と見られる運用(制裁)。医師の「病院に監視される」という抵抗(データ利用目的と配分基準の公開で緩和) |

### A4-iii. Payor対応 — 「交渉代行」ではなく「支払者対応センター」

| 要件 | 内容 |
|---|---|
| **削ぐインセンティブ** | #1 支払者接続(グループ側が最も強調するメリット)。独立医の痛点は「申請したが不成功または待機リスト」(SMA 2020年調査で保険者別10〜34%)と「患者の1/4超がパネル外のため他院へ流出」(53%)(`sg-insurer-panel-accessibility.md` §6) |
| **名称と範囲の修正【確認→分析】** | パネル採否は各保険者が独立に決める(MOH 2021年5月10日、出典5)。**料金の推奨・集約・共同交渉は行わない**(P3)。CCCSはEP助言で「EP医候補は料金・条件という商業上機微な情報を共有チャネルではなく各保険者から個別に取得すべき」と条件を付けた(出典8)。センターが行うのは**手続・資格・請求・事前承認・データ**の支援である。Foundationの「3社と直接取り決めで加入経路が簡素化」も、料金は保険者が設定し医師が個別に受諾する枠内にある |
| **提供内容(1) 保険者別の加入経路支援【確認】** | LIA比較表2025年2月25日版の原文に沿って、7社の窓口と評価項目ごとに医師の申請書類・請求実績・設備要件を整える(出典6): **AIA**=社内Provider Engagementチーム(請求パターン・顧客基盤・サブ専門科と施設レベルの必要キャパで定員算定。待機リスト。公立からの開業で自動移行なし)、**GE**=doctoranywhere.comドメイン(商品カバレッジとの整合、専門科別人数、当社パネル料金への同意)、**HSBC Life**=Fullerton Health(TPA)窓口でHSBC Lifeと共同選定(国家ベンチマークに見合う価格、自院で日帰り手術を行う医師はe-filing設備必須)、**Income**=社内(専門科の必要性、性別・人種・診療場所の多様性、記録上の診療パターン、**臨床アウトカムの提出**、**医療機関との戦略的提携**)、**Prudential**=提携医療機関主導で個人申請不可(提携施設で開業・雇用され、施設が推薦。請求は施設の事務所からe-file)、**RHI**=社内(新規受入は2024年0人・2025年3人)、**Singlife**=ixchange.com.sgドメインまたはSinglife社内(CPF e-file設備が要件) |
| **提供内容(2)〜(8)** | (2) 資格・信用情報の一元管理(SMC登録・専門医認定・懲戒歴・賠償保険・入院権限)、(3) CPF e-file設備・e-filing・請求代行・支払追跡、(4) 事前承認・eLOGの各社フォーム標準化と提出、(5) **EP活性化**: 1社の主パネルに在籍する医師を他社のEP医として機能させる(Prudentialは申請不要・事前承認必須・料金表遵守、HSBC LifeはFullerton経由の契約。EP請求は事前承認が必須のため、2026年4月以降の新ライダーの自己負担上限〔パネルまたは事前承認済み請求に適用〕の対象になり得るが各社約款で要確認【未検証】)(出典8・11・12)、(6) 料金ベンチマーク遵守の自己点検ツール(MOH公表の2,800超のベンチマークに対する自院請求の位置を医師自身が確認。センターは数値を推奨しない)、(7) 成果データ(PROM/PREM・合併症・再入院: Incomeの評価項目)、(8) CCRP(臨床請求紛争解決)対応、国際PMI・法人チャネル(iXchange法人2,000社) |
| **医師の損得(グループ比)** | Foundation: 92%が3社以上のパネル、3社と直接取り決め。IHH提携: 7社の窓口ごとの申請支援+EP+e-filing+成果データを固定事務手数料で得る。料金はいずれでも保険者が設定【分析】 |
| **対価と法的線引き** | P2・P3。医師からは固定事務手数料(SMC H3)。TPA手数料はHCSA下で患者明細に独立表示(出典7)。SMAは2023年にTPAへの不満(2015年調査で56%)を再提起しており〔B〕、評判が条件(出典13) |
| **前提条件** | **A1(保険者との契約修復)・A2(定額パッケージ)が前提**。施設の価格が是正されなければ、医師の加入支援を尽くしてもGE(Mount Elizabeth 2病院のPAC停止、2025年6月17日〜、再開未確認〔B〕)・Prudential(提携私立病院はMount Alvernia・Raffles・Thomsonの3院、IHH系はRoyal Squareのみ〔2026年8月1日〜〕)の給付はIHH病院で使えない(出典11・14)。一括でパネルが開いた事例(AIA×Raffles 90人超、Prudential×Thomson約100人、Prudential×Royal Square)はいずれも施設側の料金・請求管理の約束を伴う(付録A) |
| **成功条件(KPI定義)** | 独立認定医の平均パネル数(現状2.6社→目標はグループ医並み4.4社)、6社全て在籍率(現状9%)、申請から採否までの日数、待機リスト解消数、EP経由の事前承認件数、IHH施設がパネル/事前承認の対象となる症例の比率、請求差戻し率 |
| **リスク** | 「交渉代行」に踏み込んだ場合のCCCS審査。保険者が「病院が自院へ誘導する基盤」と見て協力しない。MHIC作業部会(2025年10月設置、出典15)による手続標準化で窓口支援の価値が低下。保険者のTPA切替(Singlife 2023年9月の78人離脱)がIHH独立医に及ぶ(出典16) |

### A4-iv. 患者リファラル — 「IHHにしかない入口を、対価なしに開く」

| 要件 | 内容 |
|---|---|
| **削ぐインセンティブ** | #2 患者の流入。医師にとって最も直接的な価値であり、Foundationは「より多くの患者がプラットフォームにいれば、より多くの専門医が加入する」と明言する(出典4) |
| **法的線引き【確認】** | SMC倫理規程H3: 紹介に対する支払い・贈与・現物補償の授受を禁止、紹介は患者の最善の利益に基づき、紹介先への利害を開示。HCSA広告規則(割引・特典・勧誘的表現の禁止)。PDPA/Health Information法(紹介に伴う情報共有は同意に基づく) |
| **提供内容(IHHの入口別)** | (a) **保険者・TPA向けの提携医ディレクトリ**(パネル別。A4-iiiと一体。Singlife CareCollabの500人超の専門医網はその原型)、(b) **GP・健診・Healthspanからの紹介調整**(Parkway Shenton約50クリニック、Executive Health Screeners。FoundationのHealth Connectiveの同型。Hirslanden型でGPのP&Lを移管しても紹介パスは契約で残す)、(c) **4病院のUCC/A&E当直ローテーションの公平・透明な開放**(科別、認定・技能要件を満たす医師を順番で)、(d) **国際患者オフィス(海外20都市超)からの割当**(サブスペシャリティ・言語・空き枠・国際PMI。手数料は病院負担。医師の%手数料は不可)、(e) **法人プログラム**(iXchange法人2,000社: 健診→専門医、産業医→専門医)、(f) **インスティテュート**(がん・心臓・脊椎/整形・消化器・脳神経)のMDTと紹介ワークフロー(館内の腫瘍・心臓・整形・消化器の連鎖をC+上に実装)、(g) **Find a Doctor(1,295人掲載)・予約・費用案内の強化**(Patient Assistance Centre相当をiXchangeで) |
| **医師の損得(グループ比)** | Foundation: Health Connective(GP 340人超、保険者2社)とAVAのファネルを得る対価は売却・雇用化。IHH提携: グループが持たない救急・国際・法人・4病院の館内連鎖を、対価なし・配分基準公開で得る【分析】 |
| **配分の5条件【分析】** | (1) 双方向で紹介対価なし(固定の役務対価のみ)、(2) 配分基準の公開(臨床的適切性、患者の選択・保険、サブスペシャリティ、空き枠、認定・技能要件。入院数・施設利用量は基準にしない)、(3) 透明なローテーション(当直・国際患者・GP紹介は科ごとの公開ルールで運用し評議会が監査)、(4) 患者同意とデータ(PDPA、NEHRは診療目的に限る)、(5) 患者の選択の保持(提携医以外を希望する患者には応じる) |
| **前提条件** | A4-ii(紹介ワークフローの基盤)、A4-iii(パネル別ディレクトリ)、提携専門医評議会(手術枠・ICU・当直・パッケージ設計・品質指標・デカント基準を協議) |
| **成功条件(KPI定義)** | 入口別の紹介仲介件数とIHH施設での手技・入院への転換率(参照値: Health Connective 7,800件超)、当直・国際患者配分の公開基準の遵守率(評議会監査)、提携医の新患数の変化(医師の申告)、患者の代替提供者希望への対応件数 |
| **競合の先行【確認/未検証】** | FoundationはHealth Connectiveに非所属のGP・専門医も会員として取り込んでおり、IHHの独立認定医の一部が既に会員である可能性が高い【未検証: 会員の重複】。IHHの紹介調整はこれと同等以上でなければ流出抑止にならない |
| **リスク** | 便益が紹介の対価と見られる運用。CCCSが市場分割と読む余地(患者の選択の保持で回避)。非参加医・既存グループ所属医の離反(P6)。保険者経由の入口でFoundationに後れを取る |

---

## ⑤ コホート別パッケージと「埋まらない差分」の受け皿【分析】

| コホート | パッケージ(A4-i〜ivの束ね方) | 医師に示す比較 | 埋まらない差分と受け皿 |
|---|---|---|---|
| **開業直後(民間5年未満)** | **Emerging Specialist Package**: Gleneagles Annexe(賃貸、120人分の区画)・病院保有スイートの市場賃料内でのフェーズイン、1〜2年の事務(A4-i)・パネル加入(A4-iii)・紹介調整(A4-iv: GP・救急当直・国際)の支援、C+接続(A4-ii)、MDT参加。層A5(公的部門の上級コンサルタントの受入れ)と同じ入口 | Foundation: 基本給+変動給と採用組向けPSP 1.0%(3年ベスティング)の代わりに、診療法人を持たず雇用される。IHH: 診療法人を100%保有したまま同じ支援を固定対価で得る | 給与保証(紹介誘因と見られるため不可)。初年度売上がFoundation平均S$1.3百万に届くかは本人次第 |
| **中堅独立医(主力)** | 基礎層(ディレクトリ・加入経路支援・当直・紹介調整・団体条件)は無償、上位層(会計・人事・C+外来モジュール・請求代行)は有償。インスティテュートの共同管理と評議会への参加 | Foundation: 60%現金+40%株式(1〜10年ロック、MP1/MP2)+雇用。IHH: 100%保持+固定対価 | **施設料の持分**(#4)→A3のSPC持分(時価、ベスティング、退任時定式価格買戻し)。**株式のアップサイド**(#8)→SPC持分で部分的に |
| **シニア(卒後35年超、26〜28%)** | **承継サービス**: 引退予定医と公的部門出身の後継者のマッチング、診療法人の後継者への譲渡の事務(A4-i)、スイートの後継者への引継ぎ(入院依存科の後継者を優先)、半引退期の役務契約(教育・MDT・品質) | Foundation: 60%現金化+MP2(自分が採用した後継者の売上目標で株式解除)。IHH: 「売らずに引き継ぐ」+層Cの少数持分による部分現金化 | **60%現金化**(#5)は埋まらない。層C(少数持分・リテンションJV)で部分対応 |
| **既グループ所属(306人)** | 対象外。ただし施設・パネル・当直・ディレクトリは同一条件で開放(P6) | — | グループは「hospital-agnostic」で、IHHが接点を保てるのは施設の価格競争力とパネル施設化(A1・A2)のみ |
| **次のグループ化候補(5人以上の共同診療所)** | 中堅パッケージに加え、A3(施設SPC)・層C(少数持分)を同じ窓口から案内する | Foundationは2026年下期に買収を再開し上場株とS$55百万を対価に使える(出典1・4)。IHHは倍率競争に入らず「場所と保険者接続」で差別化 | 現金化(#5)。Foundationの提示額には届かない前提で、「売らない選択肢」の価値を示す |

**価格設計**【分析】(10月14日文書 §7-7を継承): (1) 医師から徴収する対価はクリニック単位の固定サブスクリプション(階層別、月次・四半期)に限る。(2) 基礎層は無償で全認定医に提供し、費用は施設収入(捕捉した日帰り症例と入院)で回収する。(3) 上位層は有償とし、Medinex型の月次課金を参照する。(4) 施設持分(A3)は時価で割り当て、プログラムの対価と混同しない。

---

## ⑥ ガバナンスと組織【分析】

| 項目 | 設計 |
|---|---|
| **提携専門医評議会** | 科別代表(独立医を含む)で構成。手術枠・ICU・当直・国際患者配分・パッケージ設計・品質指標・デカント基準を協議し、配分基準の遵守を監査する。経営権は持たないが、Tamarindの「重要事項に医師取締役の承認」に相当する**手続上の拒否権**を配分基準の変更に限って与える(#8 統治の非持分代替) |
| **専任組織** | アウト・オブ・ホスピタル担当の専任CEO。Mount Elizabeth病院CEOとParkway Shenton CEOの兼務解消(既往提言)。iXchange・4病院管理部門・Parkway Shentonの機能を再編し、A4-i(事務)・ii(IT)・iii(支払者)・iv(紹介調整)を一つの窓口に束ねる |
| **規律の文書化** | P1〜P6を内部規程にし、SMC H3・CCCS・HCSA・PDPA/HIAの観点で年次に外部レビュー。必要に応じCCCSに事前相談 |
| **KPI(単価ではなく捕捉率)** | 独立認定医のグループ流出数(年)、独立医の平均パネル数、症例のグループ内捕捉率(入院+ASC)、紹介仲介件数と転換率、プログラム加入率(基礎層・有償層)、NEHR接続クリニック数。入院単価は保険者とベンチマークが抑える前提(`ihh-sg-growth-strategy.md` §4) |
| **三井の関与** | 筆頭株主として、(i) 専任組織とKPIの設定、(ii) 規律の文書化、(iii) A1・A2の先行、(iv) A3・層Cとの接続(資本が要る部分)の取締役会での後押し。新規の資本投下(TPA出資)は採らない(付録A)。三井のデータ事業(中期経営計画2029「Wellness Ecosystem Creation 2.0」、Oncoshot/MSK iHubとの腫瘍データ連携〔2026年9月〕)は研究・創薬目的で、保険目的のNEHR利用禁止の範囲外に置く(出典17) |

---

## ⑦ 競合の対抗と時間軸【確認→分析】

- **Foundation**: 2026年下期に国内買収を再開(上場資金S$100百万のうち55%を国内買収に充当)、Health Connectiveに大手保険者2社を参加させ、AVAを病院内に展開、採用組37人、全医師向けESOPを検討(出典1・4)。IHHの独立認定医に**既に接触している**可能性が高い。
- **HMI**(OneCare GP・MHC TPA・StarMed・Lifescan画像7拠点)、**Thomson**(Prudential PPCのHI-ledで約100人を一括加入)、**Healthway/Cura**も同型の価値を提供する。
- **粘着性の窓**: JAMA Health Forum 2025はPE出口後2年の残留率44%(対照60%)を示し、グループの囲い込みが契約上の甘味料に依存することを示す(出典9)。Foundationのモラトリアムは1〜10年、Tamarindのベスティングは2031年まで続く。**この期間中に「入らなくても得られる」選択肢を提示できるか**が次の統合波を左右する。
- **制度の変数**: MHICのパネル作業部会(2025年10月設置)が加入手続きの標準化・入替制限に進めば、A4-iiiの「窓口支援」の価値は下がり、A4-iv・A4-iの相対的な重みが上がる(出典15)。Health Information法の2027年初施行はA4-iiの期限を規定する。
- **立上げの目安**(10月14日文書 §7-8): 基礎層(加入経路・ディレクトリ・当直ローテーション・紹介調整)は既存資産の組み替えで6〜12か月、C+外来モジュールとバックオフィスは12〜18か月(2027年初の施行に間に合わせる)。

---

## ⑧ 主要リスク【分析】

1. **SMC H3**: 便益が「紹介の対価」と見られる運用(入院量連動、非参加医の排除)。対策はP1・P2・P5・P6と評議会監査。
2. **CCCS第34条**: 料金の共同交渉・推奨・集約。対策はP3と、EP助言に沿った「各保険者から個別に取得」の運用。
3. **保険者が応じない**: GEのPAC停止が続き、PrudentialがIHH病院のHI-led参加を認めない場合、A4-iiiの効果は医師単位の保険者(AIA・HSBC Life・Income・Singlife)とRoyal Square型施設に限られる。
4. **AVAとの関係**: IHH病院内で稼働しているなら、自前基盤との二重投資か、提携による依存かの選択を迫られる。
5. **テナント政治**: 特定の医師群への優遇が他テナントの離反を招く。公開・一律の配分ルールで緩和。
6. **費用と組織**: Foundationは108人に本社71人。認定医1,000人規模への提供には専任組織と費用を要し、収益事業として自立しない前提で防衛投資と位置づける。
7. **グループの対抗**: Foundation・HMIがESOP・現金化でさらに有利な条件を提示する可能性。IHHの差別化は「病院・ASC・救急・国際患者という入口の実物」と「100%保持」にある。
8. **シニアと共同診療所の流出**: A4-i〜ivでは現金化・施設料の動機は埋まらない。A3・層Cが遅れれば、この層の流出は続く。

---

## ⑨ 本書で確認できなかった事項【未検証】

- IHH病院内でのFoundation AVAの稼働範囲と、独立認定医クリニックのAVA・NEHR接続状況。
- IHHの独立認定医のうちHealth Connective会員の人数。
- 認定医ごとのパネル在籍状況(保険者別)、申請して不成功・待機中の医師数、入院・日帰り症例の施設別配分(ロイヤルティ)。いずれも社内データでしか検証できない。
- GEのMount Elizabeth 2病院に対するPAC停止の2026年10月時点の状況。
- 各保険者のEP運用の詳細と、新ライダー下でEP請求が自己負担上限の対象になるか。
- 4病院のUCC/A&E当直配分、国際患者オフィスの割当基準、GP紹介の現行フロー。
- C+外来モジュールの開発状況。

---

## 付録A. 三井によるTPA(iXchange等)出資とパネルアクセスの検証(要旨)【確認→分析】

**判定: ×(出資のみではSinglife以外のパネルアクセスは得られない)**。根拠: (1) パネル採否は各保険者が独立に決める(MOH 2021年5月10日、出典5)。(2) LIA比較表2025年版の原文で、iXchangeが申請窓口を担うのはSinglifeのみ。AIA・Income・RHIは社内、GEはDoctor Anywhere(IHHが2020年から少数株主〔B〕だがGEのPAC停止に影響していない)、HSBC LifeはFullerton Health(三菱商事が2025年8月22日に少数出資済み)、Prudentialは提携施設主導で個人申請不可(出典6・18・19)。(3) IHHとAIA・GE・Income・Singlifeの提携でiXchangeが担うのは「入院前から請求までの接続」であり、2026年7月の発表にパネル加入への言及はない(出典20)。(4) 一括でパネルが開いた事例(AIA×Raffles 2025年1月90人超、Prudential×Thomson 2025年4月約100人、Prudential×Royal Square 2026年8月、Foundationの3社直接取り決め)はすべて保険者と医療機関の直接合意で、共通項は**施設側の料金・請求管理の約束**である(出典4・14・21〔B〕)。(5) TPAが医師から取れる対価はSMC H3で固定事務手数料に限られ、出資の価値は保険者・法人契約とデータにあってアクセスにはない(出典7)。

**含意**: アクセスを広げる実効策は、(i) 施設の価格・請求管理の約束を伴う病院単位の提携(A1・A2)、(ii) 保険者別の窓口に沿った加入支援(A4-iii)、(iii) 1社の主パネル在籍を足場にしたEP活性化(A4-iii)、の3つであり、いずれも三井の新規資本を要しない。

---

## 付録B. 主要出典

### A = 原文を取得して本文確認
1. Foundation Healthcare Holdings 最終目論見書(2026年7月1日、SGX) — https://links.sgx.com/FileOpen/Foundation_Healthcare_Holdings_Limited_-_Final_Prospectus_dated_1_July_2026.ashx?App=IPO&FileID=6749 (60%現金取得・40%株式交換・1〜10年モラトリアム・MP1/MP2・雇用形態・PSP 1.0%・Health Connective・AVA・「保険者のパネル採用が専門医を引き付け維持する主要因」。`sg-four-specialist-groups-incentives-growth.md` §4.1で原文確認)
2. TalkMed Composite Document(2025年6月30日、SGX) — https://links.sgx.com/1.0.0/corporate-announcements/55PEO68YLXWC6SCL/850256_TalkMed%20-%20Composite%20Document.pdf (現金32.8%・再投資67.2%・B株7年ベスティング・Leaver強制譲渡・医師取締役の承認。同 §4.2)
3. OUE Healthcare 公告(2022年5月)・年次報告2024・FY2025決算、HMI Medical プレスリリース(Eagle Eye 2022年、Harley Street 2023年、Advanced Urology 2024年) — `sg-four-specialist-groups-incentives-growth.md` §4.3・§4.4・§8で原文確認
4. Foundation Healthcare Holdings「1H2026 Earnings Call Script」(2026年8月13日、SGX。本書でローカルにテキスト化) — https://links.sgx.com/1.0.0/corporate-announcements/W24OZ7ZOF8FK4CPV/901088_FHH%201H26%20Earnings%20Call%20Script.pdf (「6社中3社と直接の取り決め」「92%が3社以上」「Health Connectiveに大手保険者2社が参加」「AVAは全私立・公立病院に導入済み」「入院モジュールのUAT完了」「hospital-agnostic」「新規専門医の初年度S$1.3百万」「規模・事務支援・保険者提携・患者ファネルが民間参入直後の医師の魅力」「採用組37人」「全医師向けESOPを検討」「2H26に買収再開」)
5. MOH「Criteria for Inclusion of Medical Specialists into Insurer's Panel for Integrated Shield Plans」(2021年5月10日) — https://www.moh.gov.sg/newsroom/criteria-for-inclusion-of-medical-specialists-into-insurer's-panel-for-integrated-shield/
6. LIA「Insurance Panel of IP Insurers: Application Process, Requirements and Considerations」(2025年2月25日版、PDF原文をローカルでテキスト化) — https://www.lia.org.sg/media/4476/insurance-panel-of-ip-insurers_application-process-requirements-and-consideration_20250225.pdf
7. MOH「Regulation of Third Party Administrators」(2021年5月11日) — https://www.moh.gov.sg/newsroom/regulation-of-third-party-administrators/
8. CCCS「Advice to MOH on the Extended Panel initiative」(2022年8月24日) — https://www.ccs.gov.sg/case-register/public-register/government-advisories/advice-to-moh-on-the-extended-panel-initiative
9. JAMA Health Forum 2025(Berquist・Klarnet・Dafny。PE出口後2年の残留率44% vs 60%) — `sg-specialist-groups-succession-design.md` §4-6で原文確認
10. gov.sg「What is the Health Information Bill?」(2026年1月) — https://www.gov.sg/explainers/parliament-jan2026/
11. Prudential Singapore「PRUPanel Connect」(2025年10月14日時点) — https://www.prudential.com.sg/ppc ／「Extended Panel」 — https://www.prudential.com.sg/ppc-ep
12. MOH「New Requirements for Integrated Shield Plan Riders…」(2025年11月26日) — https://www.moh.gov.sg/newsroom/new-requirements-for-integrated-shield-plan-riders-to-strengthen-sustainability-of-private-health-insurance-and-address-rising-healthcare-costs/ (自己負担上限は「パネルまたは事前承認済みの請求といった適格な請求にのみ適用」)
14. Thomson Medical「Thomson Medical Partners with Prudential…」(2025年4月1日) — https://www.thomsonmedical.com/news/thomson-medical-partners-with-prudential-to-enhance-healthcare-access-for-patients
15. MOH「Collaborative and Multi-stakeholder Approach Needed to Address Deeper Insurance Issues」(2025年10月6日) — https://www.moh.gov.sg/newsroom/collaborative-and-multi-stakeholder-approach-needed-to-address-deeper-insurance-issues ／「Ensuring the Sustainability of Private Healthcare Insurance」(2025年9月24日) — https://www.moh.gov.sg/newsroom/ensuring-the-sustainability-of-private-healthcare-insurance/
16. MOH「About Integrated Shield Plans」(IPパネル統計、2026年4月30日更新) — https://www.moh.gov.sg/managing-expenses/schemes-and-subsidies/integrated-shield-plans/about-integrated-shield-plans/
17. MarketScreener「Mitsui: Asia–US Clinical Data Collaboration Built on IHH's Clinical Data」(2026年9月10日) — https://www.marketscreener.com/news/mitsui-asiaa-us-clinical-data-collaboration-built-on-ihh-s-clinical-data-ce785bdfd88af62d
18. Mitsubishi Corporation「Mitsubishi Corporation Invests in Fullerton Health」(2025年8月26日、ACN Newswire配信版) — https://www.acnnewswire.com/press-release/english/102094/mitsubishi-corporation-invests-in-fullerton-health
20. IHH Healthcare「IHH Singapore Collaborates with Insurers to Improve Affordability of Private Hospital Care」(2026年7月10日) — https://www.ihhhealthcare.com/newsroom/care-in-action/ihh-singapore-collaborates-with-insurers-to-improve-affordability-of-private-hospital-care
22. Singlife「Singlife Partners IHH Healthcare Singapore…」(2023年8月14日、SGX掲載PDFをローカルでテキスト化) — https://links.sgx.com/1.0.0/corporate-announcements/O4B45I4D3Q5M19OC/768939_News%20Release%20-%20Singlife%20Partners%20IHH%20Healthcare%20Singapore%20to%20Enhance%20Healthcare%20Coverage%20Solutions.pdf (iXchangeが管理する500人超の専門医網、事前承認不要)

### B = 検索エンジン経由で要旨を確認
13. SMA News「Third-Party Administrators: A Call for Feedback」(2023年11月) — https://sma.org.sg/news/2023/November/Third-Party-Administrators-A-Call-for-Feedback
19. The Edge Markets「IHH Healthcare invests in Doctor Anywhere」(2020年3月) — https://www.theedgemarkets.com/article/ihh-healthcare-invests-doctor-anywhere
21. AIA Singapore「AIA Singapore partnering with Raffles Hospital…」(2025年1月23日) — https://aia.com.sg/en/about-aia/media-centre/press-releases/2025/aia-singapore-partnering-with-raffles-hospital-to-boost-accessibility-of-quality-healthcare-in-singapore ／ IHH×Prudential「…Mount Elizabeth Royal Square」(2026年8月17日、Malay Mail配信版) — https://www.malaymail.com/news/money/mediaoutreach/2026/08/17/ihh-healthcare-and-prudential-partner-to-offer-policyholders-more-day-surgery-care-options-at-mount-elizabeth-royal-square/481308 ／ Singapore Law Watch「Insurer Great Eastern pauses pre-authorisation certificates for Mount Elizabeth admissions」(2025年6月) — https://www.singaporelawwatch.sg/Headlines/insurer-great-eastern-pauses-pre-authorisation-certificates-for-mount-elizabeth-admissions
- 米国EHR寄付セーフハーバー(42 CFR 1001.952(y)) — 10月14日文書 §7-3で参照

### 既存文書(本リポジトリ)
- `ihh-sg-hypotheses-verification.md` §8-2、§9-2、§16-1〜16-5、§17-1
- `ihh-sg-inpatient-loyalty-asc-payor-strategy.md` §2、§7-1〜7-9、§8 層A5・層D、KPI、主要リスク
- `sg-four-specialist-groups-incentives-growth.md` §3〜§6
- `sg-specialist-groups-succession-design.md` §4-6、§5
- `sg-specialist-group-typology.md` §7.2(Medinex)
- `sg-insurer-panel-accessibility.md` §3〜§6、§11
- `ihh-sg-medical-suite-specialists.md` §3〜§6(認定医1,295人の一次データ)
