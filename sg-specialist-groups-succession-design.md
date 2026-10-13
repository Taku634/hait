# シンガポール専門医グループの医師構成と世代交代耐性 — Foundation・Tamarind・HMI・OUE/Healthwayの専門科・年齢分析と、米国モデルを参照した「持分の循環」設計の評価

**作成日**: 2026年10月13日(同日、一次資料の原文確認を追加して改訂)
**位置づけ**: sg-four-specialist-groups-incentives-growth.md(4社のビジネスモデル・医師インセンティブ・成長戦略)の続編。本書は、各グループの**所属医師を専門科・年齢(卒業年からの推計)で分析**し、「著名医師(診療法人を売却した創業医)」と「創業医らが採用したキャリアの浅い専門医」への二分が実際に起きているかを確認したうえで、**著名医師が引退・離脱したときに持分が次世代に回る設計になっているか**(ご指摘の「著名医師が株式を売却しないと、新規採用医師に渡せる株式が細る」問題)を、米国の医師グループの承継設計と比較して評価する。
**表記ルール**: 【確認】=出典原文で裏付けた事実、【算出】=出典の数値から本書が計算した値、【推定】=卒業年等からの推計、【非公開】=公開情報で確認できなかった事項、【分析】=本書の解釈。出典は「A=原文を取得して本文確認」「B=検索エンジン経由で要旨確認」に区分。

---

## 調査手順(Step-by-Step)

1. **母集団データの構築**: Foundation Healthcare公式サイトの専門医112人全員のプロフィール(専門科・学位取得年・経歴)を取得した(A)。Tamarind・HMI・OUE/Healthwayは、本リポジトリのIHH認定専門医ディレクトリ(1,295人、2026年10月、`data/ihh-sg-specialists-directory-2026-10.csv`)のグループ所属タグ(Foundation 89・Tamarind 45・HMI 30・OUE/Healthway 25)を用い、Eagle Eye(21人)・Solis(11人)・Harley Street Vascularの公式名簿で補完した(A)。
2. **年齢の推計**: 基礎医学学位(MBBS等)の取得年を「卒業時25歳」と仮定して推定年齢に換算した(姉妹文書ihh-sg-medical-suite-specialists.mdと同じ方法。男性は兵役により実年齢が1〜2歳高い方向に偏る)。Foundationは112人中90人、Tamarind 24人、HMI 15人、OUE 15人で年齢を推計できた。
3. **目論見書・公的統計との突合**: Foundation目論見書の「平均年齢約52歳」「Shareholder Specialists 68人/Recruited Specialists 40人」「Emerging Specialists 34人」、SMC(Singapore Medical Council)2025年次報告の専門医数・新規登録数と照合した(A)。
4. **持分の循環メカニズムの抽出**: Foundation目論見書(Share Swap・Moratorium・PSP/ESOS規則・Share Purchase Mandate)、TalkMed Composite Document(Leaver・強制譲渡条項)、OUE公告(二層60/40・アーンアウト・90%配当)から、「医師が離脱した際に持分がどこへ行くか」「新規医師に持分を渡す経路は何か」を抽出した(A)。
5. **米国比較**: 伝統的パートナーシップの買入れ・買戻し契約(Medical Economics 2012、AAFP Family Practice Management 2004)、ASC(外来手術センター)セーフハーバー(42 CFR 1001.952(r)条文、OIG FAQ、Tenet Healthcare 10-K)、PE主導MSOロールアップの契約実務(Morgan Lewis「A Friendly Guide to Private Equity Acquisitions of Physician Practices」Thomson Reuters Health Law Handbook 2023、Foley & Lardner 2025、Nixon Peabody 2026)、PE売却後の医師離職に関する査読研究(JAMA Health Forum 2025本文、HBS Working Knowledge解説)を**原文で確認**した(A)。初版でB区分だったこれらは、ネットワーク許可ドメイン追加後に原文を取得して格上げした。Permanente(permanente.org)、FTC訴状、Health Affairs本文、The Edge Singapore記事、Tamarind Health自社サイトは改訂時点でも取得できず(ポリシー拒否またはサイト側のボット遮断)、B区分のまま残した。

---

## ① Executive Summary

1. **「著名医師と若手の二分」は、年齢分布としては半分だけ正しい**【推定/分析】。Foundationの推定年齢分布(n=90)は<45歳16%、45〜54歳42%、55〜64歳28%、65歳以上14%で、中央値53歳。谷のある二峰分布ではなく、**45〜64歳の厚い中核に、細い若手の裾(16%)と厚い高齢の裾(42%が55歳以上)**が付いた形である。目論見書の「Shareholder 68人/Recruited 40人」「Emerging(民間開業5年未満)34人」という区分は実在するが、Recruited/Emergingの多くは公的病院の部長級(例: 元KTPH上部消化管外科部長、推定40歳)であり、**「キャリアの浅い専門医」ではなく「民間経験の浅い中堅」**である。
2. **専門科で年齢構造が極端に違う**【推定】。Foundationの産婦人科15人は中央値66歳(15人中11人が55歳以上、最高齢は推定85歳・80歳)で、承継リスクが最も高い。対照的に麻酔科16人は中央値49.5歳(55歳以上ゼロ)、口腔外科6人は46歳で、若手の受け皿として機能している。一般外科19人は中央値55歳。
3. **4社の中で高齢度が最も高いのはHMI、最も低いのはOUE/Healthway**【推定】。IHH認定医に限った推定中央値はHMI 58歳(60%が55歳以上、眼科20人の中核)、Tamarind 53歳(TalkMed創業医3名は65〜69歳)、Foundation 53歳、OUE/O2 48歳(55歳以上7%)。参照値のIHH認定医全体は中央値53歳・55歳以上44%。
4. **供給側の制約は公的統計で裏付けられる**【確認】。SMC 2025年次報告では、専門医7,634人のうち民間は2,426人(31.8%)。2025年に新規登録された専門医479人のうち**民間部門はわずか35人**(国内訓練30人・海外訓練5人)で、民間専門医の供給は公的部門からの移籍に依存している。
5. **持分の「循環」を明文化しているのはTamarindだけ**【確認】。TalkMed創業医のTamarind株は「雇用終了(Leaver)時に、Tamarindまたは**その地位を引き継ぐ者**へ全部まで強制譲渡」でき、持分が後継医師に回る経路が契約上存在する。一方、Foundationの売却医師が持つ35.9%(Swap Shares)は、モラトリアム解除後は**退職しても売却義務のない普通株**であり、新規医師への持分は①PSP/ESOS(全制度合計で発行済株式の15%が上限、初回は採用組40人に1.0%)、②自己株買い(Share Purchase Mandate)で取得した株式のPSP充当、③買収時の新株交換、の**新規発行または買戻しによってしか供給できない**。ご懸念は、Foundationについては構造的に正しい。
6. **ただしFoundationには「承継を強制する」条件がある**【確認→分析】。Swap Sharesの半分(MP2)は「自分が採用した新規専門医の売上目標」の達成で解除され、期限は8〜10年。推定66歳の医師でもMP2期限は2034〜36年(74〜76歳)に当たるため、**引退前に後継を採用して売上を立てなければ株式が市場売却され不足額を返還する**。これは米国にも例の少ない承継強制装置だが、「若手が売上を上げると**先輩の**株式が解除される」構造でもある。米国のFoley & Lardnerは「高齢医師は最も高い報酬を得ており、売却対価とロールオーバー持分のより大きな割合を享受する一方、若手医師はキャリアの大半をPEの下で働くことになり得る」と、同型の世代間緊張を指摘している【確認】。
7. **数字で見た非対称**【算出】。IPO価格S$0.76で評価すると、売却医師1人当たりのSwap Sharesは平均約S$5.3百万(4億7,710万株÷68人)、Employee Specialistsを含む受領者92人で割っても約S$3.9百万。これに対し採用組40人向けPSP初回枠は1人当たり約33万株=約S$25万で、**約15〜20倍の差**がある。採用組にとっての経済的中心は株式ではなく「基本給+クリニック群業績連動の変動給」と「立ち上げ支援(初年度売上は既存医の48%)」である。
8. **OUE/O2は循環設計がなく、しかし人口動態上の切迫度は最も低い**【確認/推定】。創業医の40%は個人持株会社(RMA Med Holdings・TRP Holdings・Witty Hearty Lungs)が保有し、傘下法人は税引後利益の90%を四半期配当する。アーンアウトS$9.3百万は2024年に支払済みで、残る拘束は持分と雇用のみ。創業医の推定年齢は45〜50歳で、承継は10〜15年先の課題である。
9. **HMIは条件非開示だが、最も早く承継問題に直面する**【推定/非公開】。Eagle Eye会長Dr Julian Thengは推定59歳、HMI系IHH認定医の60%が55歳以上。Eagle Eyeの公式サイトは21人全員を「Senior Consultant Ophthalmologist」と表示し、常勤眼科医は買収時17人→21人に増えた。Harley Streetには推定32歳(2019年卒)の循環器医が在籍し、若手採用は進んでいる。少数持分の回収・再配分条件は【非公開】。
10. **米国の教訓は3点**【確認(A)】。(a)伝統的パートナーシップとASCセーフハーバーは「診療を続ける医師だけが持分を持つ」ことを強制し、退職時の買戻し・新規加入時の買入れで持分が自動的に循環する。42 CFR 1001.952(r)は「各外科医投資家の診療収入の3分の1以上が手技から得られていること」「投資条件が紹介量と無関係であること」を求め、OIGはこの基準の目的を「医師がASCを自分の診療所の延長として使う蓋然性を高めるため」と説明する。(b)PE主導MSOでは、Morgan Lewisが「買い手は雇用終了時に理由を問わず発動する買戻し権を求め、売り手はロールオーバー持分を対価と見て抵抗する」緊張を記し、Nixon Peabodyは「Good Leaverは公正価値だが約束手形で出口まで未払いのことがあり、Bad Leaverは取得原価」「再ロール時にベスティングがゼロから再開することがある」と記す。PE売却(出口)後2年の医師残留率は44%対対照60%で、16.5ポイント低い(JAMA Health Forum 2025)。(c)USAPのように入社後に持分を得られるプラットフォームでは、スポンサー持分が設立時50.2%から2017年に約23%へ低下した(B)。**若手に持分を渡し続けるには、スポンサーが希薄化を受け入れるか、退職者から強制回収するかのどちらかが必要**である。
11. **結論**: 4社のうち世代交代に「耐えうる」完成形はない。Tamarindは回収条項を持つが若手への配分が未開示、Foundationは承継強制条項を持つが回収条項がなく、新規医師への持分供給は15%枯渇枠と自己株買いの資金力に依存する。HMI・OUEは開示がない。IHHが医師JVを設計する場合、「退職時の定式価格による強制買戻し」「後継者向けに留保した持分プール」「MP2型の後継採用連動」の3点を組み合わせることが、4社の弱点を埋める最短経路である【分析】。

---

## ② データと方法

| データ | 内容 | 区分 |
|---|---|---|
| Foundation公式サイト | 専門医112人(2026年10月13日取得)。各プロフィールの専門科、学位取得年(「obtained his MBBS from NUS in 2000」等)、経歴 | A |
| 目論見書 | Shareholder/Recruited、Established/Emergingの人数推移、平均年齢約52歳・平均経験25年超、Swap Shares・PSP・ESOS・Share Purchase Mandateの規則、名前が挙がる主要専門医23人 | A |
| IHH認定専門医ディレクトリ | 1,295人。姉妹文書で構築。グループ所属タグと卒業年(651人で特定) | A(本リポジトリ) |
| 各社公式名簿 | Eagle Eye Centre(21人、全員Senior Consultant)、Solis Breast Care(乳腺外科医7人・放射線科3人・病理1人)、Harley Street Vascular(血管外科医1人) | A |
| SMC Annual Report 2025 | 専門医7,634人(民間2,426人)、新規専門医登録479人(民間35人) | A |
| TalkMed Composite Document | Leaver・強制譲渡、Tamarind株主構成(取引前後) | A |
| OUE公告(2022年5月) | 創業医の持株会社名、二層60/40、アーンアウト | A |
| 65 Equity Partnersポートフォリオ | Tamarind投資(2023年12月・2025年9月)、「創業医と提携して設立」 | A |

**限界**: (1)年齢は卒業年からの推計で、個人単位では±2〜3歳の誤差がある。(2)Tamarind・HMI・OUEはIHH認定医に限った部分集合で、年齢が判明した人数は15〜24人と少ない。Eagle Eye・Solisの公式名簿は学位取得年を掲載していない。(3)Foundationでも22人は卒業年が特定できず、「more than 20 years」等の年数表記6人は下限値(若年側に偏る)。(4)Shareholder/Recruitedの個人別区分は非開示のため、年齢と目論見書の集計から推論した。

---

## ③ 医師構成の分析

### 3.1 Foundation Healthcare(112人、年齢推計90人)【A: 公式サイト・目論見書】

**専門科別の人数と年齢**

| 専門科 | 人数 | 年齢判明 | 推定中央値 | 最小〜最大 | <45歳 | 55歳以上 |
|---|---|---|---|---|---|---|
| 一般外科(大腸・上部消化管・肝胆膵含む) | 19 | 14 | 55 | 40〜68 | 2 | 7 |
| 麻酔科 | 16 | 8 | 49.5 | 40〜53 | 3 | 0 |
| 産婦人科 | 15 | 15 | **66** | 43〜85 | 2 | **11** |
| 整形外科 | 12 | 11 | 51 | 45〜66 | 0 | 4 |
| 循環器 | 11 | 7 | 53 | 45〜61 | 0 | 3 |
| 耳鼻咽喉科 | 9 | 7 | 53 | 43〜61 | 1 | 2 |
| 手外科 | 7 | 7 | 54 | 48〜62 | 0 | 3 |
| 口腔外科 | 6 | 5 | 46 | 40〜50 | 2 | 0 |
| 小児科 | 4 | 4 | 54.5 | 50〜68 | 0 | 2 |
| 消化器内科 | 4 | 4 | 50.5 | 43〜56 | 1 | 2 |
| 眼科・脳神経外科・泌尿器(各2)、内分泌・放射線・神経内科(各1) | 9 | 8 | — | 40〜62 | 3 | 4 |
| **合計** | **112** | **90** | **53** | **40〜85** | **14(16%)** | **38(42%)** |

- 公式サイトの112人は目論見書の108人(2026年3月末)より4人多く、2026年7月に迎え入れた口腔外科医2名(公式サイト「welcomes」記事)等の増員と整合する【確認】。
- 推定年齢の分布: <45歳14人(16%)、45〜54歳38人(42%)、55〜64歳25人(28%)、65歳以上13人(14%)。四分位は46〜60歳。平均53.9歳(男性比率を考慮すると実年齢は1〜2歳上)は、目論見書の「平均約52歳」と概ね整合する【推定/確認】。
- 卒業年コホート: 1980年代16人、1990年代31人、2000年代35人、2010年代6人。2010年以降卒業(専門医として民間に出て間もない層)は6人にすぎない【推定】。
- **目論見書の区分との対応**【確認→分析】: Shareholder Specialists 68人(自分の診療法人を売却した医師)、Recruited Specialists 40人(37%)、Emerging Specialists 34人(31.5%、民間開業5年未満)。年齢で<45歳は14人しかいないので、**Emergingの大半は45歳以上**である。目論見書が「Recruited Specialistsは民間・公的双方から採用」と述べ、経歴で名前を挙げる医師の中にも推定40歳の元公立病院部長(上部消化管・肥満外科)がいることから、採用組の典型像は「公的病院で部長・上級コンサルタントを務めた40〜50歳の中堅が民間へ転じた」人材であり、ご指摘の「キャリアの浅い専門医」は**民間でのキャリアが浅い**という意味で正しい。
- **著名医師層の年齢**: 目論見書が「元部長・元学会長」等として名前を挙げた23人のうち年齢が推計できた20人の中央値は54歳、55歳以上10人、<45歳3人。Foundation Imaging JV(画像診断センター)に出資した医師18人のうち12人の中央値は53歳。「著名医師=高齢」ではなく、**50代前半の中核層が著名医師の主体**である【推定】。
- **産婦人科の特異性**: 15人全員の年齢が判明し、中央値66歳、70歳以上が6人、最高齢は推定85歳・80歳。買収した産婦人科グループが高齢医師を多く含むことを示し、**今後5〜10年で最も多くの引退が出る科**である。一方、麻酔科(16人、中央値49.5歳)はFoundationのASC(FAC Novena・Orchard)運営に直結する科であり、若手採用の受け皿になっている【推定/分析】。
- **収益面の非対称**【確認】: 既存専門医(民間5年超)の2025年平均売上は約S$2.7百万、新規専門医の加入後12カ月の売上はその約48%。人件費率は39.5%(2023年)→42.7%(2025年)に上昇し、会社はEmerging比率の上昇(20.9%→33.3%)を要因と説明している。

### 3.2 Tamarind Health(IHH認定医45人、年齢推計24人)【A: ディレクトリ・Composite Document・Solis公式サイト・65EP】

- 専門科: 腫瘍内科26、循環器6(Novena Heart)、一般外科5(Solis乳腺)、血液4、放射線腫瘍2ほか。推定年齢の中央値53歳、<45歳12%、55歳以上42%【推定】。
- **TalkMed創業医の年齢**: Dr Ang Peng Tiam推定69歳(1982年卒)、Dr Lim Hong Liang推定65歳(1986年卒)、Dr Teo Cheng Peng推定67歳(1984年卒)、Dr Khoo Kei Siongは不明。Parkway Cancer Centre(PCC)の13人のうち創業医4人を除く9人は非創業の腫瘍医・血液医である【推定/確認】。
- **OncoCare**: 16人(腫瘍内科15・緩和1)。創業医Dr Tay Miah Hiang・Dr Peter Angの年齢は不明、Dr Wong Nan Soonは推定45歳【推定】。
- **Solis Breast Care & Surgery Centre**: 公式サイトは乳腺外科医7人(全員「Senior Consultant & Breast Surgeon」)、放射線科医3人、病理医1人(Prof Tan Puay Hoon)を掲載。学位年の記載はない【確認】。
- **持分の所在**【確認】: Tamarindの「doctor shareholders」はTalkMed取引前に議決権40.3%、取引後30.5%。すなわち**TalkMed買収は既存の医師株主(OncoCare等の創業医)を約10ポイント希薄化し、TalkMed創業医に新たに持分を配った**。65 Equity Partnersは「創業医(founding doctors)と提携してTamarind Healthグループを設立した」と説明し、投資時期を2023年12月と2025年9月の2回としている。買収のたびに「新しい著名医師」に持分が渡る一方、PCCやOncoCareの非創業医に持分が渡ったことを示す開示はない【非公開】。

### 3.3 HMI Medical(IHH認定医30人、年齢推計15人)【A: ディレクトリ・HMI発表・Eagle Eye/Harley Street公式サイト・Apollo発表】

- 専門科: 眼科16(Eagle Eye)、泌尿器8(Advanced Urology)、循環器4(Harley Street)ほか。推定年齢の中央値58歳、<45歳7%、**55歳以上60%**。4社で最も高齢【推定】。
- Eagle Eye: 買収時(2022年1月)の常勤眼科医17人→公式サイト21人(2026年、全員「Senior Consultant Ophthalmologist」表示)。会長Dr Julian Thengは推定59歳(1992年卒)。公式サイトは個人の学位年を掲載せず、センターとして「25年超の臨床経験」と記す【確認/推定】。
- Harley Street: 公式サイトの循環器医4人のうち1人は推定32歳(2019年卒)で、買収後に採用された若手と考えられる。血管外科医Dr Sriram Narayananは「15年超の血管外科経験」、2010年に英国でコンサルタント就任【確認/推定】。
- Apollo Hybrid Valueの出資(2023年6月)に際し、HMI Group CEO Chin Wei Jiaは「統合型ヘルスケア・プラットフォーム」の構築を掲げた【確認】。医師持分の条件は【非公開】(前編参照)。

### 3.4 OUE Healthcare / Healthway(IHH認定医25人、年齢推計15人)【A: ディレクトリ・OUE公告】

- 専門科: 呼吸器・集中治療8(O2: The Respiratory Practice、O2 Lung Centre/RMA)、耳鼻科3・循環器3(Nobel)、泌尿器3(Urohealth)、消化器2、眼科2ほか。推定年齢の中央値48歳、<45歳13%、**55歳以上7%**。4社で最も若い【推定】。
- O2創業医の年齢: Dr Chew Huck Chin(RMA、集中治療)推定45歳、Dr Kang Ning(心臓胸部外科)推定50歳【推定】。
- 持分は創業医の**個人持株会社**(RMA Med Holdings、TRP Holdings、Witty Hearty Lungs)が、持株会社Echo Healthcare Servicesの40%と各医療法人の40%を保有する【確認】。

### 3.5 4社比較と参照値

| 指標 | Foundation | Tamarind | HMI | OUE/O2・Healthway | 参照: IHH認定医全体 |
|---|---|---|---|---|---|
| 分析対象(年齢判明) | 112(90) | 45(24) | 30(15) | 25(15) | 1,295(485〜651) |
| 推定中央値 | 53 | 53 | **58** | **48** | 53 |
| <45歳 | 16% | 12% | 7% | 13% | 17% |
| 55歳以上 | 42% | 42% | **60%** | **7%** | 44% |
| 創業医・中核医師の年齢 | 名指し23人の中央値54(70歳も) | TalkMed創業医65〜69 | Eagle Eye会長59 | O2創業医45〜50 | — |
| 若手の受け皿となる科 | 麻酔・口腔外科(中央値46〜50) | 腫瘍内科の非創業医 | Harley Street(32歳在籍) | 呼吸器・集中治療 | — |
| 最も承継が切迫する科 | **産婦人科(中央値66、70歳以上6人)** | **TalkMed創業医(腫瘍内科)** | **眼科** | 当面なし | 麻酔(中央値33年卒後)・内分泌・泌尿器 |

【分析】ご指摘の「二分」は、**年齢軸では「創業医(50代中心、一部60〜80代)」と「民間経験5年未満の40〜50代中堅」の二分**として現れており、「若手=30代」は各社とも数人にとどまる。これはシンガポールの民間専門医の供給構造に由来する。SMC 2025年次報告では新規専門医登録479人のうち民間部門は35人(7%)にすぎず【確認】、どのグループも**公的部門からの中堅移籍を主要な供給源**にしている。目論見書付録のFrost & Sullivanも、公的部門の定年(2026年7月から64歳、再雇用69歳)到達者が「定年のない民間へ移る」ことを民間専門医供給の要因に挙げている【確認】。

---

## ④ 世代交代ストレステスト: 著名医師が離脱したとき、持分はどこへ行くか

### 4.1 評価の枠組み【分析】

世代交代に耐える医師グループは、次の4つの装置を持つ必要がある。
- **(A)回収**: 引退・離脱する医師から持分を取り戻す契約(強制譲渡・買戻し)。
- **(B)供給**: 新規・若手医師に持分を渡す経路(回収した持分の再配分、留保プール、新株発行)と、その上限。
- **(C)承継の動機づけ**: 現役の著名医師が後継を採用・育成することに経済的利益を持つ条件。
- **(D)若手の経済**: 持分以外で若手を引き付ける給与・立ち上げ支援・キャッシュ還元。

### 4.2 Foundation Healthcare【A: 目論見書】

| 装置 | 設計の有無と内容 | 評価 |
|---|---|---|
| (A)回収 | **なし**。Swap Shares(4億7,710万株=35.9%)はモラトリアム解除後、退職・引退しても売却義務のない普通株。解除前の未達分のみ「市場で売却し不足額(Shortfall)を会社へ支払う」が、売却先は市場であり後継医師ではない。経営陣のロックアップもSeaTownの売却に比例して解除される。目論見書のリスク要因も「ロックアップ期間の満了後、Shareholder Specialistsを維持できる保証はない」と明記 | ご懸念どおり、**著名医師が引退後も株式を保有し続けることを妨げる条項はない** |
| (B)供給 | ①PSP/ESOS: 全株式制度の合計で**発行済株式の15%が上限**(SGX上場規則準拠)。初回は採用組40人に1,328万株=**1.0%**を3年ベスティングで付与予定。②PSPは新株発行のほか「既存株式の移転」でも充当可能で、Share Purchase Mandate(自己株買い)で取得した株式を使える。③新規買収の株式交換 | 供給は**希薄化(上限15%)か自己株買いの資金力**に依存。採用組1人当たり約33万株(IPO価格でS$25万)に対し、売却医師1人当たり平均約700万株(S$5.3百万)で**15〜20倍の差**【算出】 |
| (C)承継の動機づけ | **MP2条項**: Swap Sharesの半分は「自分が採用した新規専門医の売上目標」達成で解除、期限8〜10年。未達なら市場売却・返還。目論見書は「売却医師は新規専門医の採用に動機づけられる」と明記 | **4社で唯一の承継強制装置**。推定66歳の医師でもMP2期限は74〜76歳に当たり、引退前に後継の売上を立てる必要がある |
| (D)若手の経済 | 基本給および/または所属クリニック群の業績連動変動給。公式サイトは「民間開業の財務的障壁を下げる」「共有資源・紹介網・保険者パネル」を訴求。初年度売上は既存医の48% | 若手の経済はキャッシュ給与と立ち上げ支援が中心で、持分は補助的 |

**構造的な緊張**【確認→分析】: MP2は「後輩の売上が先輩の株式を解除する」設計である。後輩(Recruited)は自分の売上でクリニック群の業績に貢献し、変動給と1.0%のPSPを受け取るが、解除される株式の価値(先輩1人当たりS$2〜3百万相当)は先輩に帰属する。Foley & Lardner(2025年1月)は米国のPE案件について「高齢医師は最も高い報酬を得ており、売却対価とロールオーバー持分のより大きな割合を享受する可能性が高い。さらに重要なのは、高齢医師は2回目の出口とロールオーバー持分の売却を超えて診療に残る可能性が低いのに対し、若手医師はキャリアの大半をPEや他の金融投資家の下で働くことになり得る」と記しており【確認】、同型の緊張である。PSP枠の拡大か、売却医師がSwap Sharesを後輩に分け与える「Employee Specialists」経路(上場時に10人へ実施済み)の制度化が緩衝材になる。

**自己株買い経路の現実性**【算出/分析】: 上場後の発行済株式は約13.3億株(4億7,710万株÷35.9%)。15%上限は約2億株に相当し、初回PSP(1,330万株)の約15倍の余地がある。ただし自己株買いでSwap Sharesを吸収するには、売却医師1人分(約700万株)でIPO価格換算S$5.3百万の現金が要り、FY2025の調整後PAT(S$51.4百万)の約10%に当たる。年間数人の引退なら対応可能だが、産婦人科(70歳以上6人)のような**同時期の集団引退には資金的に追いつかない**。

**希薄化の方向**【分析】: 米国PE案件では売却医師がロールオーバー持分の希薄化防止(preemptive rights)を求めるのが通例だが(Morgan Lewis、§4.6)、上場会社Foundationの売却医師は一般株主であり、PSP/ESOSの新株発行で他の株主と同率で希薄化する。つまりFoundationでは「若手への持分供給」のコストを**SeaTown・公開株主・売却医師が按分して負担する**構造であり、PE型のように売却医師だけが保護されるわけではない。

### 4.3 Tamarind Health(TalkMed)【A: Composite Document・65EP】

| 装置 | 設計の有無と内容 | 評価 |
|---|---|---|
| (A)回収 | **あり**。Leaver(雇用・契約の終了または終了通知)となった創業医のTamarind株は「Tamarindおよび/または**その地位を引き継ぐ者**」へ全部まで強制譲渡させ得る。ベスティング・ビークルB株(対価の40.3%)は時間ベスティング(2031年まで)+追加条件で、未確定分の帰趨は非開示 | **後継医師への移転を明文化した唯一の例**。ただし「Tamarindの裁量(may require)」であり、自動ではない |
| (B)供給 | 回収した持分の後継者への移転。買収時の新株交付(TalkMed取引で医師株主は40.3%→30.5%に希薄化) | 新たな著名医師には買収ごとに供給されるが、**PCC・OncoCareの非創業医(20人超)への持分供給は開示なし** |
| (C)承継の動機づけ | 「腫瘍医のサブスペシャリティ化・キャリア進展機会」を統合目的に掲げる。契約上の後継採用条件は開示なし | 動機づけは**言明レベル** |
| (D)若手の経済 | 雇用契約(算定式非開示)。旧TalkMedのPSP(即時〜10年ベスティング)は非公開化で加速ベスティング・終了 | 上場時にあった従業員株式制度が消え、非上場株は流動性がない |

**切迫度**【推定/分析】: 創業医3名が65〜69歳で、ベスティング完了(2031年)時に70〜74歳。TalkMedの取引文書が「Founder Relevant Event(創業医の死亡・就業不能)」を定義している事実(姉妹文書)は、承継リスクが契約交渉の主題だったことを示す。Leaver条項は「出口」を整えたが、PCCの非創業医9人を**次の株主**に育てる経路は見えない。Nixon Peabodyが米国について指摘する「後から加わった医師は異なる株式クラス・取得原価・ベスティングを持ち、次の再編でその差が保存されない可能性がある」問題は、OncoCare創業医(2023年参加)とTalkMed創業医(2025年参加)の間にも潜在する【分析】。

### 4.4 HMI Medical【非公開】

- 条件が全て非開示のため(A)〜(C)は評価不能。公開情報から言えるのは、(i)過半数取得で創業医が少数持分を保持し医療経営を続ける型、(ii)眼科を中心に推定年齢の中央値58歳と最も高齢、(iii)Eagle Eye 17→21人、Harley Streetの32歳在籍など若手採用は進んでいる、の3点【確認/推定】。
- 米国の類例(§4.6)に照らせば、PE系の過半数保有では残余持分に買戻し(コール)条項が付くのが通例であり、回収経路はある可能性が高いが、それが若手に再配分されるかは別問題である【分析】。

### 4.5 OUE Healthcare / O2・Healthway【A: OUE公告・年次報告】

| 装置 | 設計の有無と内容 | 評価 |
|---|---|---|
| (A)回収 | 開示なし。創業医の40%は個人持株会社名義 | 【非公開】 |
| (B)供給 | 開示なし。新規医師が持分を得るには創業医の持株会社に加わるか、OUE側が持分を譲る必要がある | 【非公開】 |
| (C)承継の動機づけ | アーンアウト(成長目標、8年以内)は**2024年に目標達成で全額S$9.3百万を支払済み**。以後の成長連動は持分配当のみ | 承継を促す契約装置は**消費済み** |
| (D)若手の経済 | 傘下法人は税引後利益の90%を四半期配当(2024年計S$7.6百万) | 高配当は持分を持つ創業医に有利で、持分のない新規医師には届かない |

**切迫度**【推定】: 創業医は45〜50歳で、承継は10〜15年先。したがって現時点の弱点は「装置がない」ことではなく、「装置を作る時間はあるが、90%配当で**法人に資本が残らない**ため、将来の買戻し資金を内部に蓄積しにくい」ことである。Medical Economicsが米国の医師グループに勧める「買戻しは個人間ではなく診療法人を通じて行い、法人に資金を持たせる」設計(§4.6)の対極にある【分析】。

### 4.6 米国の参照モデル

| モデル | 持分の循環メカニズム | 区分 | 示唆 |
|---|---|---|---|
| **伝統的パートナーシップ(買入れ・買戻し契約)** | Medical Economics(2012): 「買入れ・買戻し契約は、どの事業でも承継計画の礎石であり、パートナーの出入りが多い医師所有の診療では特にそうである」。「若手医師は医学部時代の多額の債務のため高額な買入れを賄えず、診療法人は収益性の低下で高額な買戻しを賄えない」。対策として①初期出資額を**純資産(売掛金を除く)**に紐づけて買入れ負担を下げる、②**全ての持分の購入・償還を診療法人を通じて行い**、法人に資金を持たせる、③新規医師の報酬を先輩医師の給与の一定割合から段階的に引き上げ、その差額で買入れを賄う。AAFP FPM(2004、Bernick): 退職条件を定める最良の時期は「新株主が持分を買い入れるとき」で、そのとき要求は「自分に有利な取引を狙ったものではなく正当な承継計画と見られる」。標準的な買戻し契約は「株主が離脱すれば他の株主がその株式を買う」と定めるため、後継の若手が引退6カ月前に辞めると「後継者を失い、望まない買戻し義務を負う」リスクがあり、半引退期間は「通常4〜5年以内、延長は若手メンバーの裁量」 | **A** | **持分は構造的に循環する**。設計上の論点は循環の有無ではなく、若手の買入れ負担と法人の買戻し資金 |
| **Permanente Medical Group(医師所有の専門職法人)** | 「医師主導・自己統治」の多職種グループ。採用医師は約3年の勤務後に株主(shareholder)資格。カリフォルニア州の専門職法人規則では有資格者のみが株式を保有でき、退職時に償還 | B(採用資料・州法解説) | **雇用と持分が一体**。離職=持分の返還 |
| **ASCセーフハーバー(42 CFR 1001.952(r))** | 条文: 「投資持分を提供する条件は、当該投資家から事業体への過去または将来の紹介量・提供サービス量・その他の取引量と関連してはならない」「**各外科医投資家の前年度の診療収入の3分の1以上が手技の実施から得られていなければならない**」「事業体や投資家は、投資持分の取得資金を投資家に貸し付けたり保証したりしてはならない」「投資家への支払いは出資額に直接比例しなければならない」。多科ASCでは加えて手技の3分の1以上を当該ASCで実施することを要求。OIG FAQ: 「この基準を満たす医師は**ASCを自分の診療所の延長として使う蓋然性が高い**ため採用した」。Tenet 10-K(FY2024): USPIは「医師および/または医療システムとのジョイントベンチャーの組成を通じて施設を取得・開発」し、「投資先のパートナーシップ契約には、特定の事由が生じた場合に**非支配持分の一部または全部の買取りを当社に義務づける**条項がある」(償還可能非支配持分は2024年末で27.27億ドル) | **A** | **診療を続ける医師だけが持分を持てる**ため、引退で持分は必然的に回収・再シンジケートされる。買取り義務は運営会社の負債として計上される |
| **PE主導MSOロールアップ** | Morgan Lewis(2023、Thomson Reuters Health Law Handbook): ロールオーバーは「20〜40%の範囲が典型」で、目的は「医師に『身銭を切らせて』関心を持たせ、**早期引退や他の診療への移籍のリスクを減らす**こと」。「買い手は、売り手の雇用・コンサルティング関係が**理由を問わず終了した場合に発動する買戻し権**を求めることが多く、売り手は『ロールオーバー持分は対価の一部であり雇用上のインセンティブではない』として抵抗する」。売り手は希薄化防止のため新規発行への優先引受権を求める。譲渡は原則禁止、プット権は買い手が嫌う。Nixon Peabody(2026年3月): Good Leaver(所定年齢での退職・死亡・障害・会社都合解雇)は確定分を保持し公正価値で買戻されるが、「少数持分・流動性ディスカウント、評価上限、公正価値を下回る算式」が付くこともあり、「公正価値での買戻しは現金ではなく**将来の出口時にのみ支払われる約束手形**で行われることがある」。Bad Leaver(自発退職・懲戒・競業違反)は「未確定分を全て没収し、確定分は取得原価で買戻し」。2回目のロールでは「ベスティングがゼロから再開することがある」。Foley(2025年1月): 大型案件ではロールオーバーが「再編後の価値の40%に達することがある」。高齢医師と若手医師の非対称(§4.2で引用) | **A** | 回収はスポンサーへ。**新規医師への再配分は契約次第**で、保証されない。高齢の売却医師に有利で若手に不利な配分が構造的に生じる |
| **USAP(麻酔、Welsh Carson)** | 麻酔科医への持分提供を事業モデルの中核とし、医師が過半を保有。スポンサーWelsh Carsonの持分は設立時50.2%から2017年に約23%へ低下。採用時点で「2年でフルパートナー」の求人 | B(FTC訴状の報道・法律事務所解説・求人) | 若手に持分を渡し続けるには**スポンサーの希薄化受容**が必要 |
| **OneOncology / US Oncology Network** | OneOncology: TPG(その後Cencora)が過半、提携診療・医師・経営陣が少数持分を保持。US Oncology: 診療法人は医師所有のまま、McKessonは長期管理契約(CSA) | B | 医師所有を残す設計は承継を**各診療法人の内部問題**に残す |
| **Mayo Clinic(給与制)** | 40年以上、ベンチマークと標準化した昇給ステップによる給与のみ。賞与・インセンティブなし | B | 持分なしでも強いブランドと給与設計で定着させる対極モデル |

**帰結に関する査読研究**【A】
- **JAMA Health Forum 2025(Berquist・Klarnet・Dafny)**【A: PMC収録全文、HBS Working Knowledge 2025年8月26日】: 2016〜18年にPE所有者が売却(出口)した70診療の医師405人と対照810人を比較。売却2年後に同じ診療に残ったのは**44%(対照60%)**、他の診療へ移ったのは**43%(対照26%)**、引退は両群とも14%。残留率の差は16.5ポイント(相対27.5%低下)。医師は120人超の大規模グループへ移る確率が10ポイント高かった。Dafny教授は機序として「**初回投資家が残留のために提供した甘味料(sweeteners)が終わる**」こと、売却後の診療は「資産が少なく負債が多く、自律性と士気を下げる利益押し上げ活動に医師を駆り立てる」可能性を挙げる。
- **Health Affairs 2023(Bruch他)**【B】: 皮膚科・眼科・消化器のPE買収213診療と対照995診療で、臨床家の入替比率(入職÷退職)はPE 1.75対対照1.37と高く、医師からAPP(診療看護師等)への構成シフトが進んだ。

【分析】米国の教訓を一文にすれば、「**持分は、診療を続ける者が持ち、辞める者が返し、入る者が受け取る**」という循環を契約で強制しない限り、売却した世代に固着する。伝統的パートナーシップとASCセーフハーバーは三要素を全て備える。PEロールアップはこの循環のうち「返す」をスポンサー向けに設計したが「受け取る」を保証せず、その結果が出口後の離職率上昇として観測されている。

### 4.7 総合スコアカード【分析】

| 装置 | Foundation | Tamarind | HMI | OUE/O2 |
|---|---|---|---|---|
| (A)離脱時の持分回収 | ✗ 解除後は回収なし(解除前はShortfall) | **○ Leaver強制譲渡(後継者へ可)** | 【非公開】 | ✗ 開示なし |
| (B)新規医師への供給経路 | △ PSP/ESOS 15%枠(初回1.0%)、自己株買い、買収時交換 | △ 買収時の新株(既存医師は希薄化)。非創業医は不明 | 【非公開】 | ✗ 開示なし |
| (C)承継の動機づけ | **○ MP2(後継採用連動、8〜10年)** | △ 言明のみ | 【非公開】 | ✗ アーンアウト消費済み |
| (D)若手の経済 | ○ 給与+変動給+立ち上げ支援 | △ 雇用契約、非上場株は非流動 | 【非公開】 | △ 90%配当は持分保有者のみ |
| 人口動態の切迫度 | 高(55歳以上42%、産婦人科66歳) | 高(創業医65〜69歳) | **最高**(中央値58歳) | 低(中央値48歳) |
| 米国類型 | USAP型(上場株で若手に配る余地)だが回収なし | PE MSO型(Leaver回収)+医師拒否権 | PE過半数保有型 | 伝統的JV型(回収・買入れ設計なし) |

---

## ⑤ 結論: 「著名医師が辞めても株式を売却しない」問題への答え

1. **Foundationでは、ご懸念の問題は現実に起こり得る**【確認→分析】。モラトリアム解除後のSwap Sharesに売却義務はなく、引退した医師が35.9%の一部を保有し続けることを止める条項はない。新規医師への持分供給は(i)全制度合計15%の新株発行枠、(ii)自己株買いによる既存株式の充当、(iii)買収時の株式交換に限られ、いずれも**希薄化か現金**を要する。一方、同社のMP2条項は「後継を採用しなければ株式が市場売却され不足額を返す」という承継強制装置であり、**「引退前に後継を連れてくる」動機は4社で最も強い**。問題は「持分が後継に渡らない」ことであり、「後継が採用されない」ことではない。
2. **Tamarindは逆で、「持分は後継に渡せる」が「後継を育てる動機」が契約化されていない**。Leaver条項で創業医の持分をその地位を引き継ぐ者に移せる一方、PCC・OncoCareの非創業医への配分や、創業医のB株未確定分の扱いは非開示。創業医が65〜69歳である以上、この条項は5年以内に実際に試される可能性が高い。
3. **HMIは最も早く承継に直面するが設計は見えず、OUEは設計がないが時間がある**。
4. **IHHへの示唆**【分析】。IHHが専門医JV・リテンションJVを設計する場合、4社の弱点を埋める最小構成は次の3点である。(a)**退職・離脱時の定式価格(例: PAT倍率または純資産)による強制買戻し**を法人経由で行い、分割払いで資金負担を平準化する(Medical Economics型・ASCセーフハーバー型)。(b)買戻した持分を**後継者向けプールとして留保**し、公的部門から移籍する40〜50歳の中堅に、勤務年数(例: Permanente型の3年)と業績で段階的に配分する。(c)創業医の対価の一部を**後継採用連動(MP2型)**で解除し、「後継の売上が先輩の株を解除する」非対称を、後継にも同じ株式を一部割り当てることで緩和する。SMC倫理規程上、紹介量連動の対価は不可であるため、条件は「売上・PAT・採用人数」等の法人業績指標に限定する必要がある(米国ASCセーフハーバーの「投資条件は紹介量と無関係」と同じ発想)。

---

## ⑥ 未確認事項・制約

- Foundationの個別SSMAにおけるMP1/MP2目標値、Employee Specialistsへの割当条件、Shareholder Specialistsの個人別年齢(目論見書は平均のみ)。
- TamarindのB株未確定分のLeaver時の扱い、非創業医への株式・報酬制度、OncoCare創業医の年齢。Tamarind自社サイト(tamarindhealth.com)は改訂時点でもポリシー拒否で取得できなかった。
- HMI系5グループの医師持分比率・買戻し条項、Eagle Eye以外の年齢構成。Eagle Eye公式サイトは学位年を掲載していない。
- Healthway傘下専門医(Nobel・Urohealth・TEN Surgery等)の持分・年齢。
- 米国資料のうちPermanente公式(permanente.org)、FTC訴状原文、Health Affairs本文、Becker's、The Edge Singapore記事は改訂時点でも取得できず(ポリシー拒否またはサイト側のボット遮断)、B区分のまま。
- 年齢推計は卒業年ベースであり、個人単位の年齢を断定するものではない。

---

## ⑦ 主要出典

### 一次データ(A)
- Foundation Healthcare公式サイト 専門医一覧・各プロフィール(2026年10月13日取得): https://www.foundationhealthcare.sg/specialists/ (112人、/specialists/<slug>/)。採用ページ: https://www.foundationhealthcare.sg/become-our-partner/join-our-specialist-network/
- [Foundation Healthcare最終目論見書(2026年7月1日)](https://links.sgx.com/FileOpen/Foundation_Healthcare_Holdings_Limited_-_Final_Prospectus_dated_1_July_2026.ashx?App=IPO&FileID=6749) — Our Medical Specialists(pp.156-160)、Risk Factors(pp.48-49)、Management(pp.195-197: PSP/ESOS 15%上限、既存株式の充当)、Share Capital and Shareholders(pp.231-235)、Appendix C(C-16〜C-17: 公的部門の定年引上げと民間移籍、平均年齢約52歳)、Appendix D/E/F
- [SMC Annual Report 2025](https://file.go.gov.sg/smc-annual-report-2025.pdf) — Table 1-2(専門医7,634人、民間2,426人)、Table 2(新規専門医登録479人、民間35人)
- [TalkMed Composite Document(2025年6月30日)](https://links.sgx.com/1.0.0/corporate-announcements/55PEO68YLXWC6SCL/850256_TalkMed%20-%20Composite%20Document.pdf) — Tamarind議決権(取引前40.3%→取引後30.5%)、Leaver・強制譲渡、ベスティング・ビークル条項(pp.15-16, 29-31)
- [65 Equity Partners: Tamarind Healthポートフォリオ](https://www.65equitypartners.com/?p=1342) — 投資時期2023年12月・2025年9月、「創業医と提携して設立」
- [OUE Limited公告(2022年5月23日)](https://links.sgx.com/FileOpen/OUE_Proposed_Partnership_with_Group_of_Respiratory_and_Cardiothoracic_Medical_Practices_in_Singapore.ashx?App=Announcement&FileID=718242) — 創業医持株会社名、二層60/40、アーンアウト、臨床的独立性
- [OUEH Annual Report 2024](https://links.sgx.com/1.0.0/corporate-announcements/Z00PBE96GWAOOIT7/838171_OUEH%20Annual%20Report%202024.pdf)(Note 19: 90%分配方針)、[OUEH FY2025決算](https://links.sgx.com/1.0.0/corporate-announcements/ROEL1O4HUKFR445H/876304_OUEH%20Year%20Ended%202025%20Annoucement.pdf)(アーンアウト支払済)
- [HMI: Eagle Eye過半数取得(2022年1月)](https://www.hmimedical.com/news-resources/in-the-news/hmi-group-strengthens-specialist-offering-acquires-majority-stake-in-eagle-eye-centre)、[Eagle Eye医師一覧(21人)](https://eagleeyecentre.com.sg/doctors/)、[Harley Street Vascular](https://vascular.harleystreet.sg/about-us/)、[Solis Breast Care & Surgery Centre](https://www.solis.sg/)、[Apollo: PanAsia Health/HMIへの出資(2023年6月26日)](https://www.apollo.com/insights-news/pressreleases/2023/06/apollo-hybrid-value-funds-to-invest-in-panasia-health-s-health-management-international-2694401)
- 本リポジトリ: `data/ihh-sg-specialists-directory-2026-10.csv`、`data/sg-specialist-group-doctor-lists-2026-10.json`、`data/foundation-specialists-profiles-2026-10.csv`、ihh-sg-medical-suite-specialists.md
- 米国(A): [Berquist V, Klarnet L, Dafny L. Sale of Private Equity-Owned Physician Practices and Physician Turnover. JAMA Health Forum 2025;6(2):e245376(PMC11829224)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11829224)、[HBS Working Knowledge「What Happens When Private Equity Firms Sell Medical Practices」(2025年8月26日)](https://www.library.hbs.edu/working-knowledge/what-happens-when-private-equity-firms-sell-medical-practices)、[42 CFR 1001.952(r)(GovInfo、2024年版CFR)](https://www.govinfo.gov/content/pkg/CFR-2024-title42-vol5/pdf/CFR-2024-title42-vol5-sec1001-952.pdf)、[HHS OIG FAQ(ASCセーフハーバーの診療収入テスト)](https://oig.hhs.gov/faqs/general-questions-regarding-certain-fraud-and-abuse-authorities/)、[Tenet Healthcare Form 10-K FY2024(USPIのJV、Note 18 償還可能非支配持分)](https://www.sec.gov/Archives/edgar/data/70318/000007031825000009/thc-20241231.htm)、[Morgan Lewis「A 'Friendly' Guide to Private Equity Acquisitions of Physician Practices」Thomson Reuters Health Law Handbook Vol.35(2023)](https://www.morganlewis.com/-/media/files/publication/outside-publication/article/2023/a-friendly-guide-to-private-equity-acquisitions-of-physician-practices-thomson-reuters-health-law-handbook.pdf)、[Foley & Lardner(Roger D. Strode)「Physician Practice Private Equity Transactions: A Refresher」(2025年1月)](https://www.foley.com/insights/publications/2025/01/physician-practice-private-equity-transactions-refresher/)、[Nixon Peabody(Belostock・Grant)「The second exit: What happens to physician rollover equity when the platform sells」(2026年3月17日)](https://www.nixonpeabody.com/insights/articles/2026/03/17/the-second-exit-what-happens-to-physician-rollover-equity-when-the-platform-sells)、[Medical Economics「Buy-Sell Agreements: Critical for Any Practice」](https://www.medicaleconomics.com/view/buy-sell-agreements)、[AAFP Family Practice Management(Bernick)「Negotiating Your Semi-Retirement Package」(2004年11-12月)](https://www.aafp.org/pubs/fpm/issues/2004/1100/p51.pdf)

### 二次情報(B)
- [Bruch JD他, Health Affairs 2023;42(1):121-129 の要旨(Johns Hopkins HBHI)](https://hbhi.jhu.edu/node/357)、[NIHCM要約](https://nihcm.org/publications/private-equity-ownership-reshapes-workforce-composition-in-physician-practices)
- Permanente: [TPMG採用プロフィール(3年後の株主資格)](https://careers.asaging.org/profile/the-permanente-medical-group-inc-kaiser-permanente-northern-california/62994/)、[Permanente Federation: 8つの医師主導・自己統治グループ](https://permanente.org/?p=4823)
- USAP: [FTC v. U.S. Anesthesia Partners 訴状(2023年9月)の報道・解説(Welsh Carson持分50.2%→23%)](https://www.venable.com/insights/publications/2023/10/ftc-challenges-anesthesiology-acquisitions)、[USAP設立プレスリリース](https://www.usap.com/news-and-events/news/welsh-carson-anderson-stowe-and-healthcare-industry-veteran-announce-formation)
- [OneOncology: TPG・AmerisourceBergen買収(2023年4月)](https://www.businesswire.com/news/home/20230420005572/en)、[US Oncology Network: 医師所有モデル](https://www.oncpracticemanagement.com/issues/2016/november-2016-vol-6-no-11/physician-owned-community-based-oncology-practices-the-us-oncology-network-model)
- [Mayo Clinic News Network: 給与制モデル(2020)](https://newsnetwork.mayoclinic.org/discussion/structured-salary-only-compensation-plan-for-physicians-is-a-model-for-pay-equity-mayo-clinic-study-finds/)
- [Becker's: Senior physicians are cashing out — and leaving junior physicians with the debt](https://www.beckersasc.com/leadership/senior-physicians-are-cashing-out-and-leaving-junior-physicians-with-the-debt/)
- [HMI: Advanced Urology過半数取得(2024年10月)](https://www.manilatimes.net/2024/10/11/tmt-newswire/pr-newswire/hmi-medical-announces-partnership-with-advanced-urology-associates-to-expand-its-specialist-service-offerings/1983025)

### 姉妹文書(本リポジトリ)
- sg-four-specialist-groups-incentives-growth.md(4社のビジネスモデル・インセンティブ・成長戦略)
- sg-specialist-network-business-models.md、sg-specialist-group-typology.md、ihh-sg-medical-suite-specialists.md
