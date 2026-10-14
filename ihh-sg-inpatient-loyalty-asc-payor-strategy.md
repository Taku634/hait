# IHH Singapore 戦略レポート: 「病床を使う症例」のロイヤルティ確保と専門医の病院外シフトの自社内取り込み — ご提示の見立ての検証とブラッシュアップ

**作成日**: 2026年10月14日
**位置づけ**: IHH Singapore戦略シリーズの統合文書。ご提示いただいた5つの見立て(①専門医グループの自社ASCシフトとIHH外施設利用は加速する、②病床を要する診療科・医師を戦略的に増やし入院インセンティブを付与する、③入院必要性の薄い科の認定医とJVでACC/Royal Squareへ能動的に出す、④病棟に残る専門科のグループを買収する、⑤資本提携によらない支払者交渉代行サービスとITシステム統一)を、過去レポート11本と一次データ(IHH 4病院の認定専門医1,295人)に加え、2026年8〜10月の新事実(IHH 2Q26決算、Foundation Healthcare 1H26決算説明会全文、Prudentialパネル施設一覧、Health Information法、CCCS・SMC・FTCの規制文書)で検証し、修正を加えたうえでIHHがとり得る戦略を再構成する。
**表記ルール**: 【確認】=出典原文で裏付けた事実、【算出】=一次データ・出典数値から本書が計算した値、【推定】=複数事実からの推計、【分析】=本書の解釈・提言、【未確認】=公開情報で確認できなかった事項。出典は「A=原文を取得して本文確認」「B=検索エンジン経由で要旨を確認(原文サイトがネットワーク制限で取得不可)」に区分し巻末に記載。

---

## 調査手順(Step-by-Step)

1. **過去レポートの再読**: `ihh-sg-growth-strategy.md`(成長戦略・付属A1〜A9)、`parkwayshenton-divestment-strategy.md`(調査アネックス第9章)、`ihh-sg-medical-suite-specialists.md`(認定医1,295人の一次データ)、`sg-specialist-group-typology.md`、`sg-four-specialist-groups-incentives-growth.md`、`sg-specialist-groups-succession-design.md`、`sg-specialist-network-business-models.md`、`sg-insurer-panel-accessibility.md`(⑩⑪補論含む)、`ihh-mitsui-specialist-network-acquisition.md`、`sg-asc-acc-market-report.md`、`us-out-of-hospital-strategy-cases-v2/v3.md`、`bor-decline-countermeasures.md`を通読し、5つの見立てに関係する既往の結論と出典を抽出した。
2. **一次データの再集計**: `data/ihh-sg-specialists-directory-2026-10.csv`(1,295人×26項目)を、本書が定義した「入院依存度」3区分(高・中・低)+随伴科に分類し、科別にグループ所属率・推定年齢・Thomson兼任率・Royal Square/Paragon所在・保険パネル接続率・Mount Elizabeth 2病院のみ認定の比率を算出した。
3. **英語Web調査(2026年10月14日時点)**: (a) Foundation Healthcare 1H26決算説明会スクリプト(SGX、2026年8月13日)全13ページ、(b) Prudential PRUPanel Connect参加施設一覧(2025年10月14日時点)、(c) IHH 2Q26決算報道、(d) Health Information Bill(2026年1月可決)の法律事務所解説、(e) CCCSのSMA料金ガイドライン決定(2007年・2010年)、(f) FTCの医療反トラスト政策声明撤回(2023年)、(g) SMC倫理規程(ECEG 2016)H3条文、(h) IHHのNEHR完全接続(2025年11月)・保険者協業(2026年7月)リリース、(i) Mount Alvernia新デイサージェリーセンター(2026年4月)等を取得・確認した。
4. **検証と修正**: 見立てごとに「支持/部分修正/再設計」を判定し、根拠と修正内容を明示した。
5. **戦略の再構成**: 修正後の見立てを4つの層(A: 病床を使う症例のロイヤルティ回復、B: 日帰り・外来の自社取り込み、C: 入院依存領域への選別的資本参加、D: 支払者対応・ITのサービス化)に再構成し、順序・KPI・リスク・DDギャップを整理した。

---

## ① Executive Summary

### 検証結果の要約

| # | ご提示の見立て | 判定 | 主な修正点【分析】 |
|---|---|---|---|
| ① | 専門医グループの持続可能性に関わらず、急性期病院→自社ASCへのシフトと、IHH認定医によるIHH外施設利用は加速する | **支持(確認)** | 加速の主因はグループの業績ではなく**保険者の施設単位の誘導**であり、グループが失速しても施設と保険者契約は残るため「持続可能性に関わらず」は正しい。ただしシフトの単位は「診療科」ではなく**「術式(acuity)」と「医師の症例ミックス」**である。最大の流出源は眼科や皮膚科ではなく、**入院も生む外科系(一般外科・整形・泌尿器)の日帰り部分**と、保険者のLOG(支払保証)が通る病院へ移る**その入院部分**である |
| ② | 病床を要する診療科(医師)を戦略的に増やし、可能なら入院させるインセンティブを患者または医師に付与する | **部分修正** | 「増やす」余地は小さい(IHHは外科系民間専門医の72〜96%を既に認定、民間新規専門医は年35人)。争点は頭数ではなく**各医師の入院症例のうちIHHに置かれる比率(ロイヤルティ)**と**後継者の確保**。医師への入院連動インセンティブはSMC倫理規程H3(紹介対価・現物給付の禁止)で不可、患者への値引き・特典はSMC規程と医療サービス法広告規則で不可。**合法的かつ規模の出る唯一の「患者インセンティブ」は保険商品設計(パネル・事前承認・eLOG・定額パッケージ)経由の自己負担低減**であり、②の実体は「支払者とのパネル・事前承認関係の回復」である |
| ③ | 自然減に任せず、入院必要性の薄い科の認定医のうち賛同者とJVを組成し、ACC設立またはRoyal Square活用で病院外へ能動的に出る | **支持(設計を修正)** | 方向は正しく、受け皿の容量競争は既に始まっている(Foundation FAC Novena 手術室4+内視鏡室2、Mount Alvernia新DSC 手術室4、HMI、Cura 手術室5、Novena Surgery 手術室3 vs. Royal Square 手術室2+内視鏡室4)。修正点は、(i) JVの相手に「入院必要性の薄い科」だけでなく**日帰り症例を多く持つ外科系の高頻度利用医**を含めること(持分で入院も結び付ける)、(ii) Royal Square 1拠点では不足で**2〜3拠点の追加**が要ること、(iii) 空く分譲スイート(MEMC 232戸・Novena 250戸超)はIHHの所有物ではなく、世代交代の受け皿設計(後継者認定・Annexe・持分の循環)とセットにすること |
| ④ | 病棟に残る専門科の専門医グループを買収してIHHとグループ双方の収益を増やす | **条件付き支持** | 対象は存在する(独立の入院依存科グループ: Asian Heart & Vascular 10人、Synergy Orthopaedic 9人、SportsIN 6人、OrthoSports 5人、Respiratory Medical Associates 5人等)。ただし、(i) Foundationは既にIHH認定の入院依存科医師58人(一般外科21・整形13・循環器11)を抱え、2H26に買収を再開する競合、(ii) **保険者の事前承認・LOGが病院単位で閉じている限り、医師を買っても入院はIHHに来ない**(Foundationは「hospital-agnostic」と明言)ため、④は層Aの支払者対応と施設持分とセットでのみ機能する、(iii) 100%買収より**少数持分・リテンションJV(カテ室・ハイブリッド手術室・後継採用)**を優先 |
| ⑤ | 資本提携に限らず、認定医の流出を防ぎIHH施設を使い続けてもらうために支払者との交渉代行サービスを提供し、そのためにITシステムを統一する | **方向は正しいが「交渉代行」は競争法上の再設計が必須** | 独立した競合関係にある1,000人超の専門医の料金を病院がまとめて交渉する行為は、CCCSがSMA料金ガイドラインを競争法第34条違反と判断した(2007年撤回・2010年決定)構図と同型のリスクを負う。合法で既に稼働している型は、(a) 保険者が料金表を設定し医師が個別に受諾する「医療機関主導の加入(Prudential HI-led、Thomson 100人・Raffles 90人超)」、(b) TPAとしての事務代行(iXchange、請求額上昇率を7〜10%→低一桁%へ)、(c) IHHが施設部分を契約し医師が個別に参加する定額パッケージ。⑤は「交渉代行」ではなく**「支払者対応業務のサービス化(加入経路・e-filing・事前承認・成果データ)」**として設計し直す。IT統一は、2027年初施行予定のHealth Information法(全ライセンス事業者にNEHR寄与を義務化、保険者のアクセス禁止)を**独立医師のクリニックEMR提供の契機**にするのが現実解。競合はFoundationのAVA(全私立・公立病院に導入済みと同社主張)である |

### ブラッシュアップ後の戦略の骨子【分析】

**IHH SGの課題は「入院が減ること」そのものではなく、「認定医1,295人の症例が、日帰り部分は他社ASCへ、入院部分は保険者のLOGが通る病院へ、IHHの管理外で再配分されていくこと」である。** 対応は4層で、順序が重要になる。

1. **層A(0〜12か月)— 「病床を使う症例」のロイヤルティ回復**: Great Easternの事前承認停止(Mount Elizabeth 2病院、2025年6月〜、再開の報道なし)の解消と、Prudentialの医療機関主導パネルへのIHH病院の参加(現状はRoyal Squareのみ)を最優先する。認定医の54%(702人)はMount Elizabeth 2病院にしか認定を持たず、GE・Prudentialの誘導はこの層の入院に直接効く。手段は入院の定額パッケージ(循環器で開始済)、価格の再配置(Gleneagles・Parkway Eastを先にパネル施設化)、入院を支える病院側サービス(ホスピタリスト・ICU・麻酔)の提供である。
2. **層B(6〜24か月)— 日帰り・外来の自社取り込み**: Royal Squareを施設SPCとして高頻度利用医に持分30〜49%を時価で割り当て、Orchard・East・Napierに2〜3拠点を追加する。デカントの単位は術式で、相手は入院依存科の外科医を含める。全施設を6保険者のパネルに接続し、第三者医師の症例も受け入れる。
3. **層C(6〜36か月)— 入院依存領域への選別的資本参加**: 循環器(カテ室共同投資)、整形(脊椎・人工関節)、一般外科(肝胆膵・大腸)、脳神経外科、O&G(Thomsonとの争奪)で、独立グループへの少数持分・リテンションJVを優先。腫瘍と消化器は既往レポート(Icon、gutCARE/HC Surgical)の方針を維持。価格規律と承継条項(退任時買戻し・後継者プール・後継採用連動)を標準装備する。
4. **層D(0〜18か月)— 支払者対応・ITのサービス化**: iXchangeを「認定医向け支払者対応センター」(保険者別の加入経路、e-filing、事前承認、定額パッケージ運用、成果データ、国際PMI接続)へ拡張し、Prudential・HSBC Lifeの空白を埋める。C+(IHHの自社EMR)の外来モジュールまたは認定CMSを、Health Information法のNEHR義務への対応策として認定医に提供する。CCCS・SMCに抵触しない設計(保険者設定料金の個別受諾、固定事務手数料、紹介連動の分配なし)を前提にする。

---

## ② 前提のアップデート: 2026年8〜10月に判明した新事実

既往レポート(2026年8月31日〜10月13日)以降に確認できた事実を先に整理する。

| 領域 | 新事実 | 区分 |
|---|---|---|
| IHH 2Q26(2026年8月27日発表) | シンガポールの入院件数は前年比▲6%、入院単価+1%、病床稼働率は1Q安値から51%へ回復、EBITDAマージン29%。要因は「公的医療への構造的シフト」と中東情勢による医療渡航者減。「主要保険者と新パッケージを四半期中に投入」、SGは「2H26に回復軌道」と説明。戦略としては「支払者パートナーシップの強化、非伝統市場からの医療渡航、クォータナリー(高度医療)の維持、ネットワーク効果の最適化」を掲げる | B(The Star・Business Today)、A(Yahoo Finance SG) |
| Mount Elizabeth Hospital(Orchard) | 稼働率は2026年初の祝祭期に60%を下回り、4月に約70%へ回復。MEHはSG病床容量の42%を占め「ほぼ全てが待機的(elective)症例」 | B(The Star 2026年5月6日) |
| Foundation Healthcare 1H26(2026年8月13日説明会) | 売上S$129.2百万(+20.2%)、調整後EBITDA S$39.8百万(マージン37%→31%)、調整後PAT S$16.1百万(▲17.4%)、既存ベースの有機成長は「低〜中一桁%」。専門医108人・クリニック75・16領域、2H26に4人追加。**FAC Novena(2026年2月開業)は手術室4+内視鏡室2で「国内最大の独立型日帰り手術センター」、FAC Orchardは3〜6月に改装し7月に再開**。「2H26は主要保険者との提携により**Foundation以外の専門医からの症例**がFAC Novenaの稼働を押し上げる」。医師の92%が6社中3社以上のパネルに所属、**保険者3社と直接取決め(direct arrangement)があり所属医の加入経路が簡素化**。M&Aは2H26に再開、マレーシア・香港へ展開、ESOPを全医師に検討 | A(SGX掲載スクリプト) |
| 同上(Q&A、UBS質問への回答) | 「**我々はhospital-agnosticである。**医師は国内の複数の私立病院に入院させられ、患者の保険が特定施設への入院を促す場合、医師はその施設で手術・入院させられる。**保険者がLOGを特定病院に制限しても当社には重大な影響はない**」「保険会社が低コスト施設へ利用を誘導しようとしても、当社への影響は小さい。保険者は当社の医療センターがコストを管理できるため当社プラットフォームを好む」 | A(同上) |
| Prudential PRUPanel Connect(PPC)参加施設(2025年10月14日時点) | 私立病院はMount Alvernia・Raffles・Thomsonの3院のみ。**私立日帰り手術センターの区分に「Mount Elizabeth (Royal Square)」「Foundation Ambulatory Centre (Novena; Orchard)」「HMI Medical Centre」「Novena Surgery」「Novaptus」「Aptus (East/Paragon)」「Luma (Paragon/Royal Square)」「HC Surgical Specialists」**が並ぶ。IHHの4病院は病院区分に含まれない。eLOGは私立病院3院でS$30,000、日帰り手術センター・外来腫瘍センターでS$15,000 | A(Prudential公式) |
| Royal SquareのPPC接続 | 2026年8月1日付でPPCネットワークに追加。「IHH Healthcare Singapore傘下で初めてPPCに含まれる施設」 | A(IHH/Prudentialリリース 2026年8月17日) |
| Great Eastern | Mount Elizabeth 2病院への事前承認証明書(PAC)発行停止(2025年6月17日〜)について、2026年10月時点で再開・和解を報じる記事は見当たらない | B(検索結果に再開報道なし) |
| Mount Alvernia | 2026年4月、Thomson Roadキャンパスに新デイサージェリーセンター(**手術室4、需要に応じ段階開設**、回復5床、デイ病棟16床)を開設し、ICU/HDUを16室へ倍増 | B(Vatican News 2026年5月) |
| Health Information Bill | 2026年1月12日国会可決、**2027年初の施行をMOHが予定**。全ライセンス医療事業者に患者の主要情報(アレルギー・予防接種・診断・投薬・検査・画像・退院要約)のNEHRへの寄与を義務化。未接続が残る層として私立専門医クリニック・検査/画像ラボ・歯科を名指し。**雇用・保険目的でのアクセスは禁止** | A(Allen & Gledhill解説) |
| IHHのIT基盤 | 自社開発EMR「Cerebral Plus(C+)」が2025年6月までに4病院で稼働、2025年11月に4病院すべてがNEHRへ完全寄与(「私立医療グループで唯一」)。Parkway Shentonクリニックや独立専門医クリニックの接続については記載なし | A(IHHニュースルーム 2025年11月25日)、B(デジタル節目記事) |
| IHHと保険者(2026年7月10日) | AIA・Great Eastern・Income・Singlifeを「IPパートナー」とし、TPAのiXchangeが「IHHの病院・医師・保険者を接続」。iXchange管理プログラムの平均請求額上昇率を**従来の7〜10%から「極めて低い一桁%」へ抑制**。循環器で「期待費用とケアプロトコルを事前に定義した構造化治療パッケージ」を先行 | A(IHHニュースルーム) |
| 競争法(料金の共同交渉) | SMAは2007年4月1日に料金ガイドライン(GOF)を撤回(競争法第34条抵触のおそれ)。CCS(現CCCS)は2010年8月に「GOFは第34条に違反する」と正式決定。「**業界団体・職業団体による価格推奨は競争を害する**。価格の収斂点(focal points)を作り、独立した価格設定を制約する」。個々のクリニックが自院料金を表示することは「価格透明性に資し、CCSも奨励」 | A(CCS 2007年4月3日・2010年8月19日) |
| 米国の参照枠組み | FTCは2023年7月14日、1996年「医療分野の反トラスト執行方針声明」(メッセンジャーモデル等のセーフティゾーンを含む)とACO声明を撤回(DOJは同年2月に撤回)。「市場実態を反映しない」とし、以後は「一般原則に基づき事案ごとに評価」。臨床統合ネットワークの共同契約を容認した個別事例(Norman PHO、2013年2月)は存在する | A(FTCリリース)、B(Hall Render) |
| SMC倫理規程(ECEG 2016)H3 | 「紹介された患者について、いかなる供給源からも**無償の支払い・贈与・報酬を提供してfee splittingに参加してはならない**。同様に、他の医師・医療専門職・**医療施設へ患者を紹介することの対価として、キックバック、支払い、その他いかなる現物補償も求め、受け取ってはならない**」「紹介先の組織・会社・サービスに重要な利害を持つ場合は患者に開示」「患者に対し、重要な利害を持つ取引を強いる不当な影響力を行使してはならない」。医療広告では「無料・割引の検査や治療などの金銭的誘因を提供してはならない」「贈与その他の物的インセンティブで患者を誘ってはならない」 | A(ECEG 2016 pp.55・61〜62) |

**含意**【分析】: 既往レポートの前提(保険者の施設単位の誘導、Royal Squareが唯一のPrudential経路、Foundationの自社施設化)は、2026年10月時点でいずれも**強化**された。特にFoundationの「hospital-agnostic」発言と「第三者医師の症例を保険者経由でFACへ」という計画は、ご提示の見立て①を当事者が公式に裏書きしたに等しい。

---

## ③ 見立て①の検証: 専門医グループによる急性期病院→自社ASCシフトとIHH外施設利用は加速するか

### 3-1. 判定: 支持(確認)。ただし「何が、どの単位で動くか」を精緻化する

**支持する根拠**

1. **保険者が施設単位で受け皿を指定し、IHH病院が外れている**【確認】。PrudentialのPPCは医師×施設の組合せでパネルを定義し(`sg-insurer-panel-accessibility.md` ⑩)、私立病院の提携先はMount Alvernia・Raffles・Thomson、日帰り手術センターの提携先にはFAC Novena/Orchard・HMI・Novena Surgery・Aptus・Luma・HC Surgicalが並ぶ。IHH系はRoyal Squareだけである。Great EasternはMount Elizabeth 2病院のPACを止めたまま、日帰り手術センターへの事前承認は継続している(`sg-asc-acc-market-report.md`)。2026年4月以降の新ライダーは自己負担上限(S$6,000)を「パネル医または事前承認」の請求にのみ適用する(MOH 2025年11月26日)。
2. **グループ側がシフトを事業モデルとして明言した**【確認】。Foundation 1H26説明会: 「医療センターは、適切な低acuity手技を高コストの病院環境から低コストの外来医療センターへ移す(right-siting)」「2H26は主要保険者との提携により、Foundation以外の専門医からの症例がFAC Novenaの稼働を押し上げる」「医療センターは自社専門医と**第三者専門医**(保険者パートナーからの紹介を含む)の手技量で稼働が上がる長期資産」。さらに「保険者がLOGを特定病院に制限しても当社には重大な影響はない」。これは、IHHの館内に診療所を持つFoundation所属医(IHH認定医89人、`ihh-sg-medical-suite-specialists.md`)が、GE加入者をMount Elizabethではなく他院に入院させることを公の場で説明したものである。
3. **受け皿の容量が急増している**【確認】。FAC Novena(手術室4+内視鏡室2、1日36〜40件〔B〕)、FAC Orchard(1日14〜16件〔B〕、2026年7月再開)、Mount Alvernia新DSC(手術室4、2026年4月)、HMI Medical Centre、Cura(手術室5)、Novena Surgery(手術室3)、Luma(Royal Square)。Frost & Sullivanは民間独立型日帰り手術センターが2025年の9施設から2030年に40施設へ増えると予測する(`sg-specialist-group-typology.md`)。対するIHHのRoyal Squareは手術室2+内視鏡室4である。
4. **IHH認定医は既に「多病院型」である**【算出】。1,295人のうち243〜249人(19%)はThomsonの専門医名簿にも掲載され、科別では一般外科33%、O&G 47%、整形26%、泌尿器28%、麻酔32%、手外科44%がThomsonと兼任する。認定を持つIHH病院にクリニックがない医師は199人(15%)おり、入院先は患者の保険と希望で選ばれている(`sg-insurer-panel-accessibility.md` ⑩-3)。
5. **「持続可能性に関わらず」は正しい**【分析】。Foundationの調整後EBITDAマージンは37%→31%へ低下し、既存ベースの有機成長は低〜中一桁%にとどまる(1H26)。しかしシフトの駆動力はグループの収益ではなく、(a) 保険者の商品設計(2026年4月ライダー、PPCの施設単位)、(b) 既にHCSAライセンスを取得した施設の存在、(c) 医師が自ら施設を共同所有する動機(Novena Surgeryは2008年から医師シンジケートで存続、`sg-asc-acc-market-report.md`)にある。グループが失速しても、施設は別の資本に再シンジケートされる(Novena Surgery→Alfa Medicus→ICG出資、`sg-specialist-group-typology.md` ⑥)。AAMGのように消滅したグループでさえ、放射線腫瘍部門は医師個人に売り戻されて存続した(同⑦-3)。

**精緻化すべき点**【分析】

- **シフトの単位は「診療科」ではなく「術式」と「医師の症例ミックス」である。** Foundation自身が「追加する専門領域は手術系が中心。あらゆる外科医は手術室を必要とし、多くは術前画像を、ほとんどは麻酔医を必要とする」と述べ、同社のIHH認定医は一般外科21・整形13・循環器11・ENT 8・手外科6が中心である。つまり**自社ASCへ移るのは、入院も生む外科医の「日帰り部分」であり、同じ外科医の「入院部分」は保険者のLOGが通る病院へ移る**。眼科・皮膚科のような「入院必要性の薄い科」の離脱は施設料への影響が相対的に小さく、IHHにとっての本当の損失は、一般外科147人・整形144人・泌尿器43人といった入院依存科の外科医がIHHの手術室と病床から段階的に離れることにある。
- **Foundationの「日帰り化は入院件数を減らさない」は医師側の真実であり、IHH側の真実ではない。** 症例が日帰りか入院かは臨床で決まる(Foundation CCO)。しかしIHHにとっては、(a) 日帰り症例の施設料がIHHの手術室・内視鏡室からFACへ移り、(b) hospital-agnosticな医師の入院症例がLOGの通る病院へ移る、という二重の流出になる。

### 3-2. IHHの暴露度を一次データで測る

| 指標 | 値 | 含意【分析】 |
|---|---|---|
| Mount Elizabeth Orchard/Novenaにしか認定を持たない医師 | **702人(54%)** 【算出】 | GEの事前承認停止・Prudentialの非提携は、この層の入院症例に直接効く。Gleneagles・Parkway Eastの認定も持つ医師は迂回できるが、54%は迂回路がIHH内にない |
| 同、独立(非グループ)の入院依存度「高」の医師 | 321人/571人(56%)【算出】 | 層A(支払者対応)の最優先対象 |
| Thomson名簿にも掲載 | 243〜249人(19%) | 入院の代替先として既に稼働 |
| 独立医の平均パネル数 / グループ医 | 2.6社 / 4.4社。入院依存「高」では2.95社 / 4.80社、GE接続率41% / 83%、Prudential 76% / 95%【算出】 | 独立医ほどパネル外に置かれ、グループに入るとパネルが増える。グループ化の最大の価値提案が「支払者接続」であることの定量的裏付け |

---

## ④ 見立て②の検証: 病床を要する診療科・医師を戦略的に増やし、入院インセンティブを付与できるか

### 4-1. 一次データ: 認定医1,295人を入院依存度で分ける

本書は専門科を、主要な収益手技が入院を要するか(高)、入院と外来が混在するか(中)、主に外来・日帰りで完結するか(低)、他科に随伴するか(随伴)で分類した【分析】。分類は術式ベースの近似であり、同じ科でも医師の症例ミックスは異なる。

| 区分 | 科(人数) | 合計 | 比率 |
|---|---|---|---|
| **高** | 一般外科147、整形144、O&G 95、循環器79、腫瘍内科48、泌尿器43、集中治療33、脳神経外科23、心臓胸部外科19、神経内科19、血液12、小児外科4 | **666** | 51% |
| **中** | 小児科46、呼吸器21、腎臓20、感染症10、内科4、老年2、緩和1 | **104** | 8% |
| **低** | 眼科98、消化器68、ENT 65、皮膚科37、形成外科32、内分泌25、口腔外科23、精神科22、手外科18、リウマチ13、放射線腫瘍9、歯科系27、スポーツ医学2、核医学3、リハ1 | **443** | 34% |
| **随伴** | 麻酔科50、画像診断31、病理1 | **82** | 6% |

**科別の特徴(n≥10、独立医の比率・年齢・兼任・パネル)**【算出】

| 科 | n | 区分 | グループ所属 | 卒後35年超(年齢判明数) | Thomson兼任 | IHH外のみで診療 | Prudential接続 | GE接続 |
|---|---|---|---|---|---|---|---|---|
| 一般外科 | 147 | 高 | 22% | 21%(91) | 33% | 8 | 94% | 57% |
| 整形外科 | 144 | 高 | 27% | 23%(92) | 26% | 4 | 96% | 63% |
| 眼科 | 98 | 低 | 39% | 18%(44) | 7% | 17 | 81% | 58% |
| O&G | 95 | 高 | 9% | 24%(42) | **47%** | 10 | 60% | 17% |
| 循環器 | 79 | 高 | 37% | 30%(47) | 10% | 3 | 86% | 58% |
| 消化器 | 68 | 低 | 22% | 32%(41) | 21% | 3 | 81% | 69% |
| ENT | 65 | 低 | 28% | 24%(42) | 12% | 3 | 88% | 35% |
| 麻酔科 | 50 | 随伴 | 12% | 50%(8) | 32% | 4 | 30% | 28% |
| 腫瘍内科 | 48 | 高 | **90%** | 21%(19) | 15% | 2 | 96% | 85% |
| 小児科 | 46 | 中 | 7% | 43%(28) | 22% | 6 | 43% | 30% |
| 泌尿器 | 43 | 高 | 47% | 30%(23) | 28% | 1 | 88% | 74% |
| 皮膚科 | 37 | 低 | 0% | 12%(17) | 3% | 7 | 68% | 16% |
| 集中治療 | 33 | 高 | 18% | 33%(9) | 21% | 2 | 27% | 18% |
| 形成外科 | 32 | 低 | 0% | 18%(11) | 28% | 6 | 72% | 34% |
| 内分泌 | 25 | 低 | 8% | 46%(13) | 0% | 0 | 56% | 24% |
| 脳神経外科 | 23 | 高 | 13% | 20%(15) | 4% | 0 | 78% | 57% |
| 呼吸器 | 21 | 中 | 19% | 33%(12) | 5% | 0 | 86% | 71% |
| 腎臓 | 20 | 中 | 0% | 36%(11) | 0% | 3 | 80% | 40% |
| 心臓胸部外科 | 19 | 高 | 5% | 33%(9) | 0% | 0 | 68% | 32% |
| 神経内科 | 19 | 高 | 5% | 20%(10) | 11% | 0 | 84% | 37% |
| 手外科 | 18 | 低 | 39% | 8%(12) | 44% | 0 | 100% | 83% |

**読み取り**【分析】
- 認定医の半数(666人)は入院依存度の高い科に属し、IHHの入院の実体は**独立外科医の待機手術**である(MEHは「ほぼ全てが待機的症例」〔B〕)。この層のグループ所属率は腫瘍内科を除けば9〜47%で、独立医が多数派である。
- **O&GはThomson兼任47%・GE接続17%**と、入院依存科の中で最も「IHHに固定されていない」科である。分娩は病床必須だが、Thomson・Mount Alverniaとの争奪戦が既に起きている。
- 入院依存科の独立医571人の内訳は、単独開業349人、2〜4人の共同診療144人、5人以上のグループ78人である【算出】。「買収できるグループ」は少数で、大半は個人である。

### 4-2. 「増やす」余地は小さい — 争点はロイヤルティと承継

- IHHは民間専門医の脳神経外科96%、消化器93%、心臓胸部外科90%、整形89%、腫瘍内科84%、泌尿器77%、一般外科72%、循環器72%を既に認定している(`ihh-sg-medical-suite-specialists.md`)。
- 民間部門への新規専門医登録は2025年に35人(SMC年次報告2025)。供給は公的部門からの中堅移籍(定年64歳・再雇用69歳)に依存する(`sg-specialist-groups-succession-design.md`)。
- 認定医の26〜28%は卒後35年超(推定60代以上)で、入院依存科の独立医でも28%に達する【算出】。

**したがって②の「増やす」は、(a) 各認定医の入院症例のうちIHHに置かれる比率を上げる(ロイヤルティ)、(b) 引退する入院依存科医師の症例とスイートを、IHHに整合した後継者に引き継がせる(承継)、(c) 公的部門を退く上級コンサルタントを病床依存のサブスペシャリティ(心臓外科・脳外科・脊椎・肝胆膵・移植・複雑がん外科)で選択的に迎える、の3つに読み替えるべきである**【分析】。(c)ではIHHが直接配分できるスイート(Gleneagles Annexeの賃貸区画120人分、病院保有区画)と立上げ支援が武器になる。Foundationは「新規専門医は初年度平均S$1.3百万、5年超の既存医はS$2.7百万」の立上げ曲線を開示しており、立上げ期の支援(事務・パネル・紹介網)が採用の決め手になっていると説明する(1H26説明会)。

### 4-3. 「入院させるインセンティブ」の法的な境界

| 対象 | 禁止されるもの【確認】 | 許容されるもの【分析】 |
|---|---|---|
| 医師 | ECEG H3: 医療施設への紹介の対価としての「キックバック、支払い、その他いかなる現物補償」の受領。症例数連動の分配(fee splitting)。SMAは利益保証も倫理と相容れないと表明(2023年、`ihh-mitsui-specialist-network-acquisition.md`) | 施設SPCへの**時価での持分参加**(配当は持分比例、患者への開示義務あり)、正当な役務契約(臨床統治・教育・治験)、手術枠・ICU・ホスピタリスト・麻酔など**入院を支える病院側サービスの提供**、Annexeスイートの市場賃料でのリース、後継者の共同採用 |
| 患者 | ECEG広告規定: 「無料・割引の検査や治療などの金銭的誘因」「贈与その他の物的インセンティブ」の提供禁止。医療サービス法(HCSA)広告規則: 割引・バウチャー・マイル等は「勧誘効果」があるとしてMOHが不可と回答(規則5(1)(g)を引用)〔B〕 | **保険商品設計を通じた自己負担の低減**(パネル医+事前承認で自己負担上限適用、eLOG、定額パッケージ)、料金の事前確定(MOHが奨励する価格透明性) |

**結論**【分析】: 患者に対する合法で規模の出る「入院インセンティブ」は、**IHH病院がパネル・事前承認の対象施設であること**そのものである。GE加入者がMount ElizabethでPACを得られず、Prudential加入者がIHH病院でパネル給付を受けられない状態は、競合病院に対する「負のインセンティブ」として既に働いている。②の実体は「支払者とのパネル・事前承認関係の回復」であり、これが本書の層Aである。

---

## ⑤ 見立て③の検証: 能動的にJVを組成しACC/Royal Squareへ出すべきか

### 5-1. 判定: 支持。能動的に動くべき理由

1. **容量競争が始まっている**。FAC Novena(手術室4+内視鏡室2)・FAC Orchard・Mount Alvernia新DSC(手術室4)・HMI・Cura(手術室5)・Novena Surgery(手術室3)に対し、Royal Squareは手術室2+内視鏡室4である。Foundationは「医療センターは最優先の成長の柱」「3市場で拠点拡大を機会的に検討」と述べ、Mount Alverniaは手術室を需要に応じて段階開設する。
2. **Prudentialのパネルは施設単位**であり、IHHの各ASCが個別にPPC施設になる必要がある。Royal Squareは2026年8月に入った。
3. **Hirslanden原則(テナントと競合する資産を持たない)は、テナント自身をJVパートナーにすれば満たされる**(`ihh-sg-growth-strategy.md` A9)。
4. **自然減に任せると、受け皿は他社になる**。Foundationは「2H26に第三者専門医の症例を保険者経由でFACへ」と明言した。IHH認定医の日帰り症例がFACへ流れ始めてから自社ASCを増やしても、医師の行動様式(どの施設に慣れるか、どこで持分を持つか)は固定されている。

### 5-2. 設計の修正点

**(i) デカントの単位は術式、JVの相手は「入院依存科の高頻度利用医」を含める**【分析】
- 既往レポートが示したとおり、配置はacuityで決め、同じ医師でも日帰り手技はASC、入院手術は病院に分散させる(`ihh-mitsui-specialist-network-acquisition.md` ⑤)。
- JVの持分は、ASCを高頻度に使う医師に割り当てる。その多くは一般外科・整形・泌尿器・消化器・眼科・ENT・手外科であり、「入院必要性の薄い科」に限定しない。**入院依存科の外科医がIHHのASCに持分を持てば、その医師の入院もIHHに置かれやすくなる**。米国のASCセーフハーバー(42 CFR 1001.952(r))が「各外科医投資家の診療収入の3分の1以上が手技から得られ、投資条件は紹介量と無関係」と定めるのは、まさに「施設を自分の診療の延長として使う医師」を株主に選ぶためである(`sg-specialist-groups-succession-design.md` ④-6)。
- Royal Squareに既に診療所を置くIHH認定医22人(眼科5、小児3、一般外科3、消化器2、形成2、整形1、O&G 1、循環器1、ENT 1、泌尿器1、精神科1、内分泌1、うちグループ所属はHMIのEagle Eye 1人・Royal Healthcare 1人のみ)は、第1号シンジケートの自然な候補である【算出】。

**(ii) Royal Square 1拠点では不足。2〜3拠点を追加する**【分析】
- 候補立地はOrchard(MEH・Paragon: IHH認定医64人がParagonに診療所、眼科13・一般外科8・皮膚7・O&G 7・形成5)、East(Parkway East、Aptus Eastが先行)、Napier(Gleneagles Annexe)。
- Royal Square(Hoi Hup–Sunway JV、2013年6月起算の99年リース、医療スイート171戸〔B〕)にはLuma(Tamarind)・Eagle Eye(HMI)・Royal Healthcare(双日)も入居しており、IHHは一テナントにすぎない。追加フロアのリースで拡張できるが、建物の支配権はない。
- 投資規模はFoundationの開示が参考になる: FAC Novena(手術室4)の設備投資S$2.5百万、画像センターS$5.4百万(`sg-specialist-group-typology.md`)。ASCは不動産を持たなければ軽資本である。

**(iii) 空く分譲スイートは、IHHの所有物ではない**【確認・分析】
- MEMCは分譲232戸、Novena Specialist Centreは250戸超の医師スイートで、第1期100戸は2週間で完売した(`ihh-sg-medical-suite-specialists.md` ③)。Gleneagles Medical Centreの売り出し例はS$15,000 psf超である。
- 入院必要性の薄い医師がACCへ移っても、その分譲スイートの売却・賃貸は所有者(医師)の判断であり、IHHは買い手を指定できない。ただし、(a) 認定(accreditation)の付与、(b) Annexe・病院保有区画の賃貸、(c) 後継者の共同採用、(d) 施設SPCの持分の循環(退任時の定式価格買戻し・後継者プール、`sg-specialist-groups-succession-design.md` ⑤)を通じて、スイートの次の入居者を入院依存科へ誘導できる。
- 副作用として、スイートの需要減は分譲価格を下げ、現所有者(入院依存科の医師を含む)の資産価値を毀損し得る。他方で後継者の参入コストは下がる。ACC側に外来診察室を併設し、低依存科の医師が診療所ごと移転できる設計にすれば、スイートの流動化が進む。

**(iv) 持分設計の標準装備**【分析、既往レポートの統合】
- 施設ごとにSPC、IHH 51〜70%/施術医30〜49%、割当は時価(FMV)、ベスティング、譲渡制限、退任・引退時の定式価格(PAT倍率または純資産)による法人経由の強制買戻し、後継者向け留保プール、後継採用連動(Foundation MP2型)。分配は持分比例のみ(症例数連動は不可)。患者への利害開示。
- 施設は全6保険者のパネルへ接続(Prudentialは施設単位、HSBC Life・Singlifeはe-filing設備が加入要件)。第三者医師の利用も受け入れ、稼働を優先する(Foundationと同じ論理)。

**(v) 対象医師の目安**【算出・分析】
- 低依存443人のうちASCを必要とするのは眼科98・消化器68・ENT 65・形成32・手外科18・口腔外科23(皮膚・精神・内分泌・リウマチは診察室のみ)。
- これに一般外科147・整形144・泌尿器43・O&G 95(婦人科日帰り)の日帰り部分が加わる。
- ロイヤルティ上の優先順位は、**Mount Elizabeth 2病院のみ認定(702人)かつThomson兼任(249人)**の重なる層である。

---

## ⑥ 見立て④の検証: 病棟に残る専門科のグループを買収すべきか

### 6-1. 判定: 条件付き支持

**対象は存在する**【算出】。企業資本が入っていない5人以上の共同診療グループで、入院依存度「高」に属するもの:

| グループ(診療所名の正規化) | IHH認定医数 | 科 | 拠点 | 備考 |
|---|---|---|---|---|
| Asian Heart & Vascular Centre | 10 | 循環器 | MEMC(10階・17階)、Novena、Parkway East〔B〕 | 国内有数の独立循環器グループ。カテ室は病院に依存 |
| Synergy Orthopaedic Group | 9 | 整形 | — | |
| SportsIN Orthopaedic | 6 | 整形(+麻酔1) | — | |
| OrthoSports | 5 | 整形 | — | |
| FeM Surgery(Novena/Gleneagles/Orchard) | 7 | 一般外科・脳神経外科ほか | 3キャンパス | 共用診療所型 |
| Respiratory Medical Associates | 5 | 呼吸器(+集中治療3) | — | 区分「中」 |
| Integrative Critical Care Anaesthesia & Pain Services | 14 | 集中治療10・麻酔5 | — | 随伴・ICU。病院運営に不可欠 |
| Kinder Clinic | 8 | 小児科 | — | 区分「中」 |
| (参考)Island Orthopaedic 7、TEN Surgery Group 5 | — | 整形・一般外科 | — | Healthway Medical Group傘下と既往レポートで確認(`sg-four-specialist-groups-incentives-growth.md`)。本CSVのグループ判定では未捕捉のため、独立とは扱わない |

**条件**【分析】

1. **買収は保険者の誘導を解かない**。Foundationは「hospital-agnostic」であり、保険者が特定病院へのLOGを制限すれば他院に入院させると明言した。IHHが入院依存科のグループを買っても、Mount ElizabethがGEのPAC対象外・Prudentialの非提携のままなら、買った医師の患者は保険者の都合で他院へ行く。**④は層A(支払者対応)と層B(施設持分)が先行して初めて機能する**。
2. **競合は買収を再開する**。Foundationは1H26にM&Aを一時停止したが「複数の候補と高度な協議中、2H26に完了見込み」とし、上場株という対価通貨、国内買収予算S$55百万、全医師向けESOPを持つ。既にIHH認定の入院依存科医師58人(一般外科21・整形13・循環器11)を抱える。
3. **SMC規程の制約**。紹介連動の対価は不可。整合は施設SPC・カテ室/ハイブリッド手術室の共同投資・正当な役務で設計する(`ihh-mitsui-specialist-network-acquisition.md` ③-1)。
4. **100%買収より少数持分・リテンションJVを優先**。場所貸しモデルの病院は医師グループ経営を中核能力に持たず(豪Ramsayの心理クリニック撤退、`parkwayshenton-divestment-strategy.md` 9-2)、創業医の持分と臨床統治を残した案件(HCA UK×LOC、USPI、Sarah Cannon)が雇用転換型に勝る。循環器では「カテ室・EP室・ハイブリッド手術室の共同投資+優先枠+後継育成」のリテンションJV、整形・脳神経外科では「脊椎・人工関節の病院内センター+日帰りはASC」の二層配置が整合する。
5. **承継条項を標準装備**。退任時の定式価格買戻し(法人経由・分割払い)、後継者向け留保プール、後継採用連動(MP2型)。4大グループのいずれも完成形を持たない弱点を埋める(`sg-specialist-groups-succession-design.md` ⑤)。
6. **価格規律**。FoundationのPF調整後EBITDA S$99.1百万(2025年)に対し上場時の時価総額は約S$10億(S$0.76×約13.3億株〔算出〕)で約10倍、HC Surgicalは5〜6倍(`ihh-sg-growth-strategy.md` A5)。入院依存科の小規模グループに、プラットフォームの倍率を払う理由はない。
7. **O&Gは別の論理**。Thomson兼任47%・GE接続17%の科であり、分娩はMount Elizabeth Novena・Orchard・Parkway Eastの病床を使う。買収よりも、産科パッケージの保険者接続と新生児・小児の病院側体制(KKH/Thomsonとの差別化)が先である。
8. **腫瘍・消化器は既往の方針を維持**。Icon(段階出資)、gutCARE JV/HC Surgical(Royal Square内視鏡)の優先順位は変えない(`ihh-sg-growth-strategy.md` ④、`parkwayshenton-divestment-strategy.md` 6)。

---

## ⑦ 見立て⑤の検証: 支払者交渉代行サービスとITシステム統一は成立するか

### 7-1. 判定: 方向は正しいが、「交渉代行」は競争法上の再設計が必須

**法的な制約**【確認】
- シンガポール: SMAの料金ガイドラインは2007年に競争法第34条抵触のおそれで撤回され、CCSは2010年に「第34条に違反する」と決定した。CCSの理由は「業界団体・職業団体による価格推奨は競争を害する。価格の収斂点を作り、独立した価格設定を制約する」である。CCCSの事業者間協力ガイダンス(2022年)も、共同販売(joint commercialisation)と業界団体の決定を第34条の対象と明記する〔B〕。
- 病院が、互いに競合する独立専門医1,000人超を代理して保険者と**料金を**交渉する行為は、医師間の価格の収斂点を病院が作る構図になり、第34条の「価格の固定」または「ハブ・アンド・スポーク型」の調整と評価されるリスクがある【分析】。MOHがパネルを「一般に反競争的ではない」と整理した根拠は、保険者が各医師と**個別に**料金・条件を合意し、医師が個別に受諾を判断できる点にあった(MOH 2024年7月2日、`sg-insurer-panel-accessibility.md` ⑥)。
- 米国: 独立医師の共同契約は「財務統合」「臨床統合」「メッセンジャーモデル」のいずれかで許容されてきたが、FTC・DOJは1996年の政策声明を2023年に撤回し、以後は事案ごとの評価に移った。臨床統合ネットワークの共同契約を容認した個別事例(Norman PHO、2013年)は残る。

**合法で、既にシンガポールで稼働している型**【確認】

| 型 | 実例 | 料金決定の主体 |
|---|---|---|
| 医療機関主導の加入(HI-led empanelment) | Prudential PPC: Thomson(2025年4月、約100人を一括追加)、Raffles(AIA、2025年1月、90人超)。Foundation「保険者3社と直接取決め、所属医の加入経路を簡素化」 | 保険者が料金表を設定、医師が個別に受諾 |
| TPAとしての事務代行 | iXchange(IHH): AIA・GE・Income・Singlifeと提携、資格確認・事前承認・請求・モニタリング。管理プログラムの請求額上昇率を7〜10%→低一桁%へ | 同上。TPA手数料はECEG H3により「実際の事務作業を反映した固定額」に限られ、医師の報酬比例は不可 |
| 定額・完結型パッケージ | IHHの循環器構造化パッケージ、Royal Square×PPC、固定価格パッケージ(料金改定を年2〜3%にキャップ) | IHHが施設部分を契約、医師は公表料金で個別参加 |
| 財務統合JV | 医師が契約主体(施設SPC等)の持分を持ち、リスクを共有する形 | 統合体として契約。CCCSへの事前相談・第34条の適用除外(純経済的便益)の検討を要する【分析】 |

**再設計後の⑤: 「支払者対応業務のサービス化(Payor Operations as a Service)」**【分析】

1. **保険者別の加入経路の提供**: Prudential(施設単位のHI-led)はIHHの各ASC・病院がPPC施設になることで開く。HSBC Life(Fullerton TPA経由)、Singlife(iXchange経由)、GE・AIA・Incomeは医師単位。IHHは申請・資格・請求パターンの整備・待機リスト対応を代行する(交渉ではなく、要件充足の支援)。SMA調査では「申請したが不成功または待機リスト」が保険者別に10〜34%、「患者の1/4超がパネル外のため他院へ流出」が53%であり(`sg-insurer-panel-accessibility.md` ⑥)、独立医の最大の痛点である。
2. **e-filing・事前承認・eLOGの運用**: HSBC Life・Singlifeはe-filing設備を加入要件とし、PrudentialはHIの事務所経由のe-fileを求める。
3. **定額パッケージの運用と料金ベンチマーク遵守の支援**: MOH料金ベンチマークの範囲内での料金設定支援(個別クリニックの料金表示はCCCSが奨励)。保険者が「パネル料金レンジを大幅に上回る医師の除外」を容認する環境(MOH 2025年10月)で、遵守支援は除外リスクの低減になる。
4. **成果データ**: Incomeは「臨床アウトカムの提出」を評価項目とし、Foundationは2027年前半からPROM/PREMを収集する。独立医が単独で用意できないデータ基盤を提供する。
5. **国際PMI・法人チャネル**: iXchangeの法人2,000社超、国際患者オフィス。
6. **価格と費用負担**: 医師から徴収する場合は固定の事務手数料(ECEG H3)。施設所有者としてIHHが負担し、施設利用と持分で回収する設計も可能。
7. **競合**: FoundationのAVAは「全私立・公立病院に導入済み」と同社が主張し、GEと提携して「保険者が電子契約で医師をパネルに自動追加」する機能を持ち、「地域の私立病院運営者と病院入院モジュールのUATを完了」した(1H26説明会)。IHH自身の院内ワークフローにAVAが入っている可能性があり、**自前(iXchange+C+)で行くか、AVAと競合/提携するかの判断が先決**である【未確認: IHH病院でのAVA利用の有無】。HMIのMHC、FullertonのTPA(HSBC Life)も同じ機能を持つ。

### 7-2. ITシステム統一の現実解: Health Information法を契機にしたクリニックEMRの提供

- **制度の追い風**【確認】: Health Information Billは2026年1月12日に可決され、MOHは2027年初の施行を予定する。全ライセンス医療事業者に主要情報のNEHR寄与を義務化し、私立専門医クリニックは未接続が残る層として名指しされた。保険・雇用目的のアクセスは禁止される。
- **IHHの資産**【確認】: 自社EMR「C+」が4病院で稼働し、4病院すべてがNEHRへ完全寄与済み(私立グループで唯一)。
- **設計**【分析】: 「統一」を強制するのではなく、(a) C+の外来・クリニックモジュール(または認定されたクリニック管理システム)を、NEHR義務への対応策として認定医に提供し、(b) e-filing・事前承認・パッケージ運用・PROM収集を同じ基盤に載せ、(c) 病院のC+と患者単位で接続する。医師にとっての価値は「2027年の法令対応+支払者対応の省力化」であり、IHHにとっての価値は「症例の可視化(どの医師のどの症例がどこへ行ったか)と定額商品の原価データ」である。
- **留意**: 保険者のNEHRアクセスは禁止されるため、支払者向けデータは患者同意に基づく別経路(PDPA)で設計する。Parkway Shentonクリニックの接続状況は未確認であり、GP側の接続も同じ基盤で進める。

---

## ⑧ ブラッシュアップ後の戦略: 4層の再構成

### 層A(0〜12か月): 「病床を使う症例」のロイヤルティ回復 — 支払者との関係修復が全ての前提

| 施策 | 内容 | 根拠 |
|---|---|---|
| A1. Great EasternのPAC再開 | Mount Elizabeth 2病院の標準的入院術式について、GEが指摘した「他院比20〜30%高い」請求を定額パッケージで埋め、PACの再開を交渉する。GE接続医は597人(46%)、入院依存科の独立医では41%にとどまる | GE停止の理由は病院料金(医師料金はベンチマーク連動で横並び)〔ST 2025年6月〕。IHHは既にiXchange管理プログラムで請求額上昇を低一桁%に抑制した実績を持つ |
| A2. PrudentialのHI-led参加 | Gleneagles・Parkway Eastを先にPPC提携病院とし(価格競争力のある施設から)、次にMount Elizabeth Novena。Prudential接続医は941人(73%)と最多だが、IHH病院では「非パネル扱い」になる | PPCの私立病院はAlvernia・Raffles・Thomsonの3院。Thomsonは一括で約100人を追加した前例 |
| A3. 入院の定額・完結型パッケージの拡充 | 循環器で開始済の構造化パッケージを、整形(人工関節・脊椎)、一般外科(大腸・ヘルニア・胆嚢)、泌尿器、産科へ拡大。料金改定キャップ(年2〜3%)を維持 | IHH 2Q26「主要保険者と新パッケージ投入」。CUHK Medical Centreの教訓(定額だけでは稼働は上がらず、誘導経路とセットが必要、`bor-decline-countermeasures.md` ⑤) |
| A4. 入院を支える病院側サービス | ホスピタリスト/集中治療・麻酔・術後管理の病院提供体制を整え、独立外科医が「入院を自院に置く」負担を下げる。ICU/HDUはMount Alverniaが16室へ倍増 | Integrative Critical Care(ICU 10人・麻酔5人)等の院内グループは資産。シンガポールの公立ではGIMホスピタリストが制度化〔B〕 |
| A5. 後継者の選択的受入れ | 公的部門を退く上級コンサルタントを、心臓外科・脳外科・脊椎・肝胆膵・移植・複雑がん外科でAnnexe・病院保有スイート+立上げ支援+パネル加入支援(層D)の組合せで迎える | 民間新規専門医35人/年、認定医の26〜28%が卒後35年超。Foundationは「採用組」40人を同じ論理で獲得 |
| A6. 手術枠・資源配分の公開ルール | OT・ICU・ハイブリッド手術室の配分を公開・一律化し、特定グループ優遇と見られない運用にする | テナント離反リスクの管理(`ihh-mitsui-specialist-network-acquisition.md` ④) |

### 層B(6〜24か月): 日帰り・外来の自社取り込み — 面で押さえる

| 施策 | 内容 |
|---|---|
| B1. Royal Squareの施設SPC化 | 高頻度利用医(現入居22人+Novenaの一般外科・整形・消化器・眼科・ENT)へ時価で30〜49%を割当。ベスティング・買戻し・後継者プール・持分比例分配・利害開示 |
| B2. 追加ASC/ACC 2〜3拠点 | Orchard(Paragon周辺の認定医64人を含む)、East、Napier。各拠点は手術室4+内視鏡室2〜4を標準とし、外来診察室を併設して低依存科の診療所移転を受け入れる。設備投資はFACの実績(S$2.5百万/手術室4)が参考 |
| B3. 術式単位のデカント・プロトコル | 内視鏡・白内障・ヘルニア・関節鏡・手外科・ENT・婦人科日帰り・乳腺の一部を標準でASCへ。病院は入院を要する症例と高acuityに集中(MEHの改装完了を活かす) |
| B4. 全保険者パネル接続と第三者医師の受入れ | 各施設をPPC施設にし、HSBC Life・Singlifeのe-filing要件を満たす。IHH認定医以外も受け入れ稼働を優先 |
| B5. 消化器・眼科の資本提携 | 既往方針(gutCARE JV/HC Surgical、中堅眼科グループ)をB1〜B2の施設に接続 |

### 層C(6〜36か月): 入院依存領域への選別的資本参加

| 領域 | 構造 | 候補(独立グループ、`data/`より) |
|---|---|---|
| 循環器 | カテ室・EP室・ハイブリッド手術室の共同投資+優先枠+後継育成の**リテンションJV**。買収可能なスケール資産は消滅(Novena Heart→Tamarind、Harley Street→HMI) | Asian Heart & Vascular(10人)、Orchard Heart Specialist(4人)、The Heart Specialist(4人) |
| 整形・脊椎 | 病院内の脊椎・人工関節センター(入院)+ASC持分(日帰り)の二層。少数持分 | Synergy Orthopaedic(9)、SportsIN(6)、OrthoSports(5)、Orthopaedics International(12、独立系) |
| 一般外科(肝胆膵・大腸・上部消化管) | 内視鏡(Royal Square)→大腸外科→腫瘍内科の連鎖の中核。少数持分またはSPC持分 | FeM Surgery(7)、The Gastroenterology Group(5、消化器15)ほか |
| 脳神経外科・心臓胸部外科 | 民間専門医の90〜96%を既に認定。買収より後継者受入れ(A5)と設備投資 | — |
| O&G | 産科パッケージの保険者接続、新生児・小児体制、Thomson兼任47%への対抗。資本取引は慎重 | FeM Surgery、Kinder(小児8) |
| 腫瘍 | 既往方針(Icon施設内JV→SG/ASEANカーブアウト共同保有、PCC契約精査) | — |
| 共通条件 | 時価、ベスティング、退任時の定式価格買戻し(法人経由・分割)、後継者プール、後継採用連動、紹介連動分配なし、CCCS審査の見通し、プラットフォーム倍率を払わない | — |

### 層D(0〜18か月): 支払者対応・ITのサービス化

| 施策 | 内容 |
|---|---|
| D1. iXchange 2.0 | 認定医向け「支払者対応センター」: 保険者別加入経路、申請・待機リスト対応、e-filing、事前承認、eLOG、パッケージ運用、ベンチマーク遵守支援、CCRP(請求紛争)対応、国際PMI。手数料は固定事務手数料(ECEG H3)。**料金の共同交渉は行わない** |
| D2. Prudential・HSBC Lifeの空白を埋める | PrudentialはA2・B4(施設単位)、HSBC LifeはFullerton TPAとの接続または直接協議 |
| D3. C+外来モジュール/認定CMSの提供 | 2027年初施行予定のHealth Information法のNEHR義務への対応策として認定医に提供。病院C+と患者単位で接続、PROM/PREM収集、支払者向けデータは患者同意に基づく別経路 |
| D4. CCCS・SMCの事前整理 | 財務統合JV(層B/C)の契約形態とD1の役務範囲について、CCCSの事業者間協力ガイダンスに沿った内部審査と必要に応じた相談。SMC規程H3(紹介対価禁止・利害開示)の運用ルールを文書化 |
| D5. AVAとの関係整理 | IHH病院内でのAVA利用状況の確認、提携か自前かの判断 |

### 実行順序と相互依存【分析】

```
層A(支払者修復)  ──先行──▶  層C(入院依存科への資本参加)が機能する前提
      │
      └──並行──▶  層D(加入経路・e-filing・EMR) ──▶ 層B(ASC面展開)の各施設をパネル施設化
                                                    │
                                                    └──▶ 層Cの医師にSPC持分で入院も結び付ける
```

- 層Aなしに層Cを進めると、「保険者に誘導されて他院に入院する医師」を買うことになる(Foundationの「hospital-agnostic」)。
- 層Dなしに層Bを進めると、ASCは建っても加入経路(特にPrudentialの施設単位)が開かず、稼働が上がらない(CUHKMC型の失敗)。
- 層Bなしに層Aだけを進めると、日帰り部分は他社ASCへ流れ続け、病院の手術室・内視鏡室の稼働は戻らない。

### KPI【分析】

| KPI | 定義 | 現状の参照値 |
|---|---|---|
| 入院ロイヤルティ | 認定医ごとの入院症例のうちIHH 4病院に置かれた比率(iXchange・C+・請求データで推計) | 【未確認】(社内データ) |
| パネル・事前承認カバレッジ | 認定医のうち、主要6保険者でIHH病院・ASCがパネル/事前承認対象となる症例の比率 | Prudential: 病院0院・ASC 1施設。GE: Mount Elizabeth 2病院PAC停止 |
| 日帰り症例のグループ内捕捉率 | 認定医の日帰り手技のうちIHH施設(病院+ASC)で実施された比率 | 【未確認】 |
| ASC稼働と第三者比率 | 手術室・内視鏡室の稼働率、非認定医の症例比率 | Royal Square: 手術室2+内視鏡室4 |
| 請求額上昇率 | iXchange管理プログラムと全体の平均請求額の前年比 | 管理プログラムは低一桁%(2026年7月) |
| スイートの世代交代 | Mount Elizabeth/Novena/Gleneaglesのスイートで入院依存科の後継者へ引き継がれた件数 | 卒後35年超が26〜28% |
| 承継装置の実装率 | SPC・JVのうち買戻し・後継者プール・後継採用連動を備える比率 | — |
| 単価ではなく回転 | 症例数×回転×原価。入院単価は保険者とベンチマークが抑える前提(既往レポートと同じ) | SG入院単価1Q26 ▲3%→2Q26 +1% |

### 主要リスク【分析】

1. **保険者が応じない**: GEが価格再配置に応じず、PrudentialがIHH病院のHI-led参加を認めない場合、層Aは定額パッケージとGleneagles/Parkway Eastの先行に限定される。MOHのMHICパネル作業部会(2025年10月設置)の帰趨が制度面の変数。
2. **競争法**: 層D1が「交渉代行」に踏み込めばCCCSの審査対象。層B/Cの財務統合JVも、同一科で多数の医師を束ねる場合は第34条の検討を要する。
3. **SMC規程**: 持分付与・役務契約が「紹介誘因」と見られない運用(時価、開示、症例連動の排除)の徹底。
4. **テナント政治**: 特定グループへの持分付与・買収が他テナントの離反を招く。公開・一律の配分ルール(A6)と、新規キャパシティへの配置で緩和。
5. **Foundation・HMIとの買収競争**: 2H26にFoundationが買収を再開。IHHは「場所と保険者接続」を差別化軸にし、倍率競争に入らない。
6. **資本と組織**: ASC 2〜3拠点、SPC、クリニックEMRの同時進行は経営資源を要する。Mount Elizabeth病院CEOとParkway Shenton CEOの兼務(Yong Yih Ming氏)を解消し、アウト・オブ・ホスピタルの専任体制を置くことは既往レポートの提言と同じ。
7. **公立の価格の錨**: SGH Elective Care Centre(2027年、300床)等の公立外来手術能力は私立ASCの価格上限を規定し続ける。
8. **規制の変化**: 完全な人頭払い、料金ベンチマークの適用拡大、パネル入れ替え規制の導入可能性。

---

## ⑨ 未確認事項・DDギャップ

- 認定医ごとの入院症例の施設別配分(ロイヤルティ)の実測値。社内の請求・入院データでしか検証できない。
- Great Eastern PACの現状(再開の有無、協議の条件)。公開情報では2025年6月の停止以降の更新が確認できない。
- Prudential PPCの2026年版施設一覧(Prudential公式の掲載は2025年10月14日時点)。
- IHH病院内でのFoundation AVAの利用有無と範囲。
- Royal SquareにおけるIHHのリース条件・拡張余地、追加ASC候補物件のHCSAライセンス要件への適合。
- Parkway Shentonクリニックおよび独立専門医クリニックのNEHR接続状況、C+の外来モジュールの開発状況。
- 独立グループ(Asian Heart & Vascular、Synergy Orthopaedic等)の医師の年齢・持分意向・既存の保険者契約。Island Orthopaedic・TEN Surgery GroupはHealthway傘下と既往レポートで確認しており、本CSVのグループ判定は下限値である。
- IHH 2Q26の決算資料原本(Bursa/SGX掲載)はネットワーク制限で取得できず、SG数値は報道(B)に依拠した。

---

## ⑩ 出典

### A = 原文を取得して本文確認

1. Foundation Healthcare Holdings「1H26 Earnings Call Script」(SGX、2026年8月13日) — https://links.sgx.com/1.0.0/corporate-announcements/W24OZ7ZOF8FK4CPV/901088_FHH%201H26%20Earnings%20Call%20Script.pdf (同内容: https://www.foundationhealthcare.sg/wp-content/uploads/2026/08/FHH-QA-Transcript-Earnings-Call-13082026.pdf) — FAC Novena(手術室4+内視鏡室2、2026年2月)、FAC Orchard(7月再開)、第三者専門医の症例、hospital-agnostic、保険者3社との直接取決め、92%が3社以上のパネル、1H26財務、M&A再開、ESOP、専門医の立上げ曲線
2. Prudential Singapore「PRUPanel Connect — Participating Healthcare Institutions」(2025年10月14日時点) — https://www.prudential.com.sg/ppc — 私立病院3院、日帰り手術センター一覧(Mount Elizabeth (Royal Square)、Foundation Ambulatory Centre (Novena; Orchard)、HMI Medical Centre、Novena Surgery、Aptus、Luma、HC Surgical)、eLOG限度額
3. IHH Healthcare/Prudential「IHH Healthcare and Prudential Partner to Offer Policyholders More Day Surgery Care Options at Mount Elizabeth Royal Square」(2026年8月17日) — https://www.media-outreach.com/news/singapore/2026/08/17/481308/ihh-healthcare-and-prudential-partner-to-offer-policyholders-more-day-surgery-care-options-at-mount-elizabeth-royal-square/
4. IHH Healthcare「Mount Elizabeth Royal Square: Specialised Day Care, All in a Day」(2025年11月4日) — https://www.ihhhealthcare.com/newsroom/care-in-action/mount-elizabeth-royal-square-specialised-day-care-all-in-a-day — 手術室2・内視鏡室4、Novena病院から徒歩5分、out-of-hospital戦略
5. IHH Healthcare「IHH Singapore Collaborates with Insurers to Improve Affordability of Private Hospital Care」(2026年7月10日) — https://www.ihhhealthcare.com/newsroom/care-in-action/ihh-singapore-collaborates-with-insurers-to-improve-affordability-of-private-hospital-care — AIA・GE・Income・Singlife、iXchange、請求額上昇率7〜10%→低一桁%、循環器パッケージ
6. IHH Healthcare「Proudly the First: IHH Healthcare Singapore Achieves Full NEHR Participation」(2025年11月25日) — https://www.ihhhealthcare.com/newsroom/care-in-action/proudly-the-first-ihh-healthcare-singapore-achieves-full-nehr-participation
7. The Edge Singapore/Yahoo Finance SG「IHH Healthcare's 2QFY2026 patmi up 29% y-o-y」(2026年8月27日) — https://sg.finance.yahoo.com/news/ihh-healthcares-2qfy2026-patmi-29-063443927.html — SG戦略4項目
8. Competition Commission of Singapore「CCS Decides against Singapore Medical Association ("SMA") Guidelines on Fees」(2010年8月19日) — https://www.ccs.gov.sg/media-and-consultation/newsroom/media-releases/ccs-decides-against-singapore-medical-association-sma-guidelines-on-fees
9. Competition Commission of Singapore「Press Statement Issued in Relation to SMA's Withdrawal of Fee Guidelines」(2007年4月3日) — https://www.ccs.gov.sg/media-and-events/newsroom/announcements-and-media-releases/press-statement-issued-in-relation-to-sma-s-withdrawal-of-fee-guidelines/
10. Federal Trade Commission「Federal Trade Commission Withdraws Health Care Enforcement Policy Statements」(2023年7月14日) — https://www.ftc.gov/news-events/news/press-releases/2023/07/federal-trade-commission-withdraws-health-care-enforcement-policy-statements
11. Allen & Gledhill「Health Information Bill passed to establish framework for the safe collection and sharing of health information」(2026年) — https://www.allenandgledhill.com/sg/publication/articles/32164/health-information-bill-passed-to-establish-framework-for-the-safe-collection-and-sharing-of-health-information — 2026年1月12日可決、2027年初施行予定、全ライセンス事業者のNEHR寄与義務、保険・雇用目的のアクセス禁止
12. Singapore Medical Council「2016 Ethical Code and Ethical Guidelines」(2017年1月施行) — https://isomer-user-content.by.gov.sg/77/775548fb-11df-4393-89c5-33717769ccf6/2016-smc-ethical-code-and-ethical-guidelines---(13sep16).pdf — H3 Financial conflicts of interest(pp.61〜62)、医療広告における金銭的誘因の禁止(p.55)
13. 本リポジトリ一次データ: `data/ihh-sg-specialists-directory-2026-10.csv`(IHH 4病院ディレクトリ1,295人、2026年10月8日取得)、`data/ihh-sg-specialists-summary-2026-10.json`。本書の【算出】は同CSVの再集計
14. 姉妹文書(本リポジトリ): `ihh-sg-growth-strategy.md`、`parkwayshenton-divestment-strategy.md`、`ihh-sg-medical-suite-specialists.md`、`sg-specialist-group-typology.md`、`sg-four-specialist-groups-incentives-growth.md`、`sg-specialist-groups-succession-design.md`、`sg-specialist-network-business-models.md`、`sg-insurer-panel-accessibility.md`、`ihh-mitsui-specialist-network-acquisition.md`、`sg-asc-acc-market-report.md`、`us-out-of-hospital-strategy-cases-v2.md`/`-v3.md`、`bor-decline-countermeasures.md`(各文書の出典一覧を参照。MOH IPライダー新要件、MOHパネル統計、LIA比較表、SMA調査、Foundation目論見書、TalkMed Composite Document、SMC年次報告2025等は姉妹文書で原文確認済み)

### B = 検索エンジン経由で要旨を確認(原文サイトがネットワーク制限で取得不可)

15. The Star「IHH Healthcare remains confident on growth trajectory」(2026年8月27日) — https://www.thestar.com.my/business/business-news/2026/08/27/ihh-healthcare-remains-confident-on-growth-trajectory — SG入院▲6%、入院単価+1%、稼働率51%、マージン29%
16. Business Today「IHH Healthcare 2Q PATMI Increased 30% To RM675 Million On Higher Patient Volume」(2026年8月27日) — https://www.businesstoday.com.my/2026/08/27/ihh-healthcare-2q-patmi-increased-30-to-rm675-million-on-higher-patient-volume/ — 新パッケージ投入、2H26回復見通し
17. New Straits Times「IHH Healthcare Q2 net profit surges 29pct to RM573mil」(2026年8月) — https://www.nst.com.my/business/corporate/2026/08/1520122/ihh-healthcare-q2-net-profit-surges-29pct-rm573mil
18. The Star「Higher earnings likely for IHH Healthcare in 2H26」(2026年5月6日) — https://www.thestar.com.my/business/business-news/2026/05/06/higher-earnings-likely-for-ihh-healthcare-in-2h26 — MEH稼働率60%未満→約70%(2026年4月)、SG病床容量の42%、ほぼ全て待機的症例
19. Kenanga「IHH Healthcare 1Q26 Results Note」(2026年5月28日) — https://www.kenanga.com.my/wp-content/uploads/2026/05/IHH-260528-1Q26-RN-Kenanga.pdf
20. Vatican News「Singapore Catholic non-profit hospital expands services」(2026年5月) — https://www.vaticannews.va/en/church/news/2026-05/singapore-catholic-non-profit-hospital-expands-services.html — Mount Alvernia新DSC(手術室4、段階開設、回復5床、デイ病棟16床)、ICU/HDU 16室
21. Growbeansprout「Foundation Healthcare Initiation Report」(2026年) — https://cdn.growbeansprout.com/strapi-uploads/Foundation_Healthcare_Initiation_Report_983e54796a.pdf — FAC Novena 1日36〜40件、FAC Orchard 1日14〜16件
22. CodeBlue「Prudential Partners Thomson Medical Centre To Offer More Health Care Options For Customers」(2025年4月) — https://codeblue.galencentre.org/2025/04/prudential-partners-thomson-medical-centre-to-offer-more-health-care-options-for-customers/ — 約100人の専門医を一括追加、パネル1,700人超
23. Yahoo News SG/The Straits Times「Insurer Great Eastern pauses pre-authorisation certificates for Mount Elizabeth admissions」(2025年6月) — https://sg.news.yahoo.com/insurer-great-eastern-pauses-pre-151000701.html
24. MOH(ask.gov.sg)「医療サービス法広告規則FAQ: 割引・バウチャー・マイル等」 — https://ask.gov.sg/moh/questions/clu6lx3rj009c314r1k2f7gjh (関連FAQ PDF https://www.moh.gov.sg/docs/librariesprovider8/resources/12-10-2023-advert-regs-faqs-(1).pdf は取得時404) — 割引の言及・バウチャー・ポイントは「勧誘効果」があり規則5(1)(g)に抵触し得る
25. Hall Render「FTC Approves Norman PHO Clinical Integration Program」(2013年2月20日) — https://hallrender.com/2013/02/20/ftc-approves-norman-pho-clinical-integration-program/ ／ FTC advisory opinion page — https://www.ftc.gov/node/46237
26. Allen & Gledhill「CCCS issues Business Collaboration Guidance Note」(2022年1月) — https://www.allenandgledhill.com/sg/publication/articles/20008/cccs-issues-business-collaboration-guidance-note-to-enable-businesses-to-collaborate-with-greater-confidence — 共同商業化・業界団体の決定が第34条の対象
27. Synapxe「Health Information Bill」(2026年1月12日) — https://www.synapxe.sg/news/national-programmes/health-information-bill
28. IHH Healthcare「IHH Singapore Hits New Digital and Imaging Milestones」 — https://www.ihhhealthcare.com/newsroom/care-in-action/ihh-singapore-hits-new-digital-and-imaging-milestones — 自社EMR「Cerebral Plus(C+)」が2025年6月までに4病院で稼働
29. The Edge Singapore(EdgeProp)「Three F&B strata units at Royal Square mall for sale」 — https://www.edgeprop.sg/amp/property-news/three-fb-strata-units-royal-square-mall-sale-198-mil — Hoi Hup–Sunway JV、2013年6月起算99年リース、医療スイート171戸
30. Mount Elizabeth専門医プロファイル(Asian Heart & Vascular Centreの拠点) — https://mountelizabeth.com.sg/patient-services/specialists/profile/goh-ping-ping ／ MEMC診療所一覧 — https://memc.com.sg/clinic/asian-heart-vascular-centre-level-10
31. The Hospitalist「Adoption of Hospitalist Care in Asia: Experiences From Singapore, Taiwan, Korea, and Japan」 — https://mdedge.com/content/adoption-hospitalist-care-asia-experiences-singapore-taiwan-korea-and-japan — シンガポール公立のGIMホスピタリストモデル

---

*本書の【分析】【推定】は上記出典と一次データからの筆者の整理であり、投資・契約判断には個別のデューデリジェンス(社内の入院配分データ、保険者との契約条件、CCCS・SMCに関する法的助言)を要する。*
