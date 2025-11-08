from nicegui import ui

def original_oib(q: str | None = None):

    # Your provided HTML snippet
    content = """<verse><vid id="v19.117.1" onclick="luV(1)">1</vid> <br><div class="int"><wform><heb id="wh331049" class="ch70320 GE70639 H1984" onclick="luW(1,'331049','70320','70639','verb.piel.impv.p2.m.pl','H1984')" onmouseover="hl1('h331049','h70320','E70639')" onmouseout="hl0('h331049','h70320','E70639')" ondblclick="searchWord(1,331049)">הַֽלְל֣וּ</heb></wform><br><wsbl>halû</wsbl><br><wphono>hˈallˈû</wphono><br><ref onclick="lex('E70639')" ondblclick="searchLexicalEntry('E70639')"><wlex><heb>הלל</heb></wlex></ref><br><ref onclick="etcbcmorph('verb.piel.impv.p2.m.pl')"><wmorph>verb.piel.impv.p2.m.pl</wmorph></ref><br><ref onclick="bdbid('H1984')"><wsn>H1984</wsn></ref><br><wgloss>[you]+ praise</wgloss><br><wtrans>Praise</wtrans></div><heb> </heb><div class="int"><wform><heb id="wh331050" class="ch70320 GE70005 H853" onclick="luW(1,'331050','70320','70005','prep','H853')" onmouseover="hl1('h331050','h70320','E70005')" onmouseout="hl0('h331050','h70320','E70005')" ondblclick="searchWord(1,331050)">אֶת</heb><heb>־</heb></wform><br><wsbl>ʾet</wsbl><br><wphono>ʔeṯ-</wphono><br><ref onclick="lex('E70005')" ondblclick="searchLexicalEntry('E70005')"><wlex><heb>אֵת</heb></wlex></ref><br><ref onclick="etcbcmorph('prep')"><wmorph>prep</wmorph></ref><br><ref onclick="bdbid('H853')"><wsn>H853</wsn></ref><br><wgloss>[object marker]</wgloss><br><wtrans></wtrans></div><div class="int"><wform><heb id="wh331051" class="ch70320 GE70113 H3068" onclick="luW(1,'331051','70320','70113','nmpr.m.sg.a','H3068')" onmouseover="hl1('h331051','h70320','E70113')" onmouseout="hl0('h331051','h70320','E70113')" ondblclick="searchWord(1,331051)">יְ֭הוָה</heb></wform><br><wsbl>[yhwāh]</wsbl><br><wphono>[ˈyhwāh]</wphono><br><ref onclick="lex('E70113')" ondblclick="searchLexicalEntry('E70113')"><wlex><heb>יְהוָה</heb></wlex></ref><br><ref onclick="etcbcmorph('nmpr.m.sg.a')"><wmorph>nmpr.m.sg.a</wmorph></ref><br><ref onclick="bdbid('H3068')"><wsn>H3068</wsn></ref><br><wgloss>YHWH</wgloss><br><wtrans>the LORD,</wtrans></div><heb> </heb><div class="int"><wform><heb id="wh331052" class="ch70321 GE70078 H3605" onclick="luW(1,'331052','70321','70078','subs.m.sg.c','H3605')" onmouseover="hl1('h331052','h70321','E70078')" onmouseout="hl0('h331052','h70321','E70078')" ondblclick="searchWord(1,331052)">כָּל</heb><heb>־</heb></wform><br><wsbl>kol</wsbl><br><wphono>kol-</wphono><br><ref onclick="lex('E70078')" ondblclick="searchLexicalEntry('E70078')"><wlex><heb>כֹּל</heb></wlex></ref><br><ref onclick="etcbcmorph('subs.m.sg.c')"><wmorph>subs.m.sg.c</wmorph></ref><br><ref onclick="bdbid('H3605')"><wsn>H3605</wsn></ref><br><wgloss>whole</wgloss><br><wtrans>all you</wtrans></div><div class="int"><wform><heb id="wh331053" class="ch70321 GE70500 H1471" onclick="luW(1,'331053','70321','70500','subs.m.pl.a','H1471')" onmouseover="hl1('h331053','h70321','E70500')" onmouseout="hl0('h331053','h70321','E70078')" ondblclick="searchWord(1,331053)">גֹּויִ֑ם</heb></wform><br><wsbl>gôyim</wsbl><br><wphono>gôyˈim</wphono><br><ref onclick="lex('E70500')" ondblclick="searchLexicalEntry('E70500')"><wlex><heb>גֹּוי</heb></wlex></ref><br><ref onclick="etcbcmorph('subs.m.pl.a')"><wmorph>subs.m.pl.a</wmorph></ref><br><ref onclick="bdbid('H1471')"><wsn>H1471</wsn></ref><br<wgloss>people</wgloss><br><wtrans>nations!</wtrans></div><heb> </heb><div class="int"><wform><heb id="wh331054" class="ch70322 GE76864 H7623" onclick="luW(1,'331054','70322','76864','verb.piel.impv.p2.m.pl.prs.p3.m.sg','H7623')" onmouseover="hl1('h331054','h70322','E76864')" onmouseout="hl0('h331054','h70322','E76864')" ondblclick="searchWord(1,331054)">שַׁ֝בְּח֗וּהוּ</heb></wform><br><wsbl>šabĕḥûhû</wsbl><br><wphono>ˈšabbᵊḥˈûhû</wphono><br><ref onclick="lex('E76864')" ondblclick="searchLexicalEntry('E76864')"><wlex><heb>שׁבח</heb></wlex></ref><br><ref onclick="etcbcmorph('verb.piel.impv.p2.m.pl.prs.p3.m.sg')"><wmorph>verb.piel.impv.p2.m.pl.prs.p3.m.sg</wmorph></ref><br><ref onclick="bdbid('H7623')"><wsn>H7623</wsn></ref><br><wgloss>[you]+ praise +[him]</wgloss><br><wtrans>Extol Him,</wtrans></div><heb> </heb><div class="int"><wform><heb id="wh331055" class="ch70323 GE70078 H3605" onclick="luW(1,'331055','70323','70078','subs.m.sg.c','H3605')" onmouseover="hl1('h331055','h70323','E70078')" onmouseout="hl0('h331055','h70323','E70078')" ondblclick="searchWord(1,331055)">כָּל</heb><heb>־</heb></wform><br><wsbl>kol</wsbl><br><wphono>kol-</wphono><br><ref onclick="lex('E70078')" ondblclick="searchLexicalEntry('E70078')"><wlex><heb>כֹּל</heb></wlex></ref><br><ref onclick="etcbcmorph('subs.m.sg.c')"><wmorph>subs.m.sg.c</wmorph></ref><br><ref onclick="bdbid('H3605')"><wsn>H3605</wsn></ref><br><wgloss>whole</wgloss><br><wtrans>all you</wtrans></div><div class="int"><wform><heb id="wh331056" class="ch70323 GE70006 H9009" onclick="luW(1,'331056','70323','70006','art','H9009')" onmouseover="hl1('h331056','h70323','E70006')" onmouseout="hl0('h331056','h70323','E70006')" ondblclick="searchWord(1,331056)">הָ</heb><heb></heb></wform><br><wsbl>hā</wsbl><br><wphono>hā</wphono><br><ref onclick="lex('E70006')" ondblclick="searchLexicalEntry('E70006')"><wlex><heb>הַ</heb></wlex></ref><br><ref onclick="etcbcmorph('art')"><wmorph>art</wmorph></ref><br><ref onclick="bdbid('H9009')"><wsn>H9009</wsn></ref><br><wgloss>the</wgloss><br><wtrans></wtrans></div><div class="int"><wform><heb id="wh331057" class="ch70323 GE71088 H523" onclick="luW(1,'331057','70323','71088','subs.f.pl.a','H523')" onmouseover="hl1('h331057','h70323','E71088')" onmouseout="hl0('h331057','h70323','E71088')" ondblclick="searchWord(1,331057)">אֻמִּֽים</heb><heb>׃</heb></wform><br><wsbl>ʾumîm</wsbl><br><wphono>ʔummˈîm</wphono><br><ref onclick="lex('E71088')" ondblclick="searchLexicalEntry('E71088')"><wlex><heb>אֻמָּה</heb></wlex></ref><br><ref onclick="etcbcmorph('subs.f.pl.a')"><wmorph>subs.f.pl.a</wmorph></ref><br><ref onclick="bdbid('H523')"><wsn>H523</wsn></ref><br><wgloss>clan</wgloss><br><wtrans>peoples!</wtrans></div><heb> </heb><br></verse> <verse><vid id="v19.117.2" onclick="luV(2)">2</vid> <br><div class="int"><wform><heb id="wh331058" class="ch70324 GE70023 H3588" onclick="luW(2,'331058','70324','70023','conj','H3588')" onmouseover="hl1('h331058','h70324','E70023')" onmouseout="hl0('h331058','h70324','E70023')" ondblclick="searchWord(1,331058)">כִּ֥י</heb></wform><br><wsbl>kî</wsbl><br><wphono>kˌî</wphono><br><ref onclick="lex('E70023')" ondblclick="searchLexicalEntry('E70023')"><wlex><heb>כִּי</heb></wlex></ref><br><ref onclick="etcbcmorph('conj')"><wmorph>conj</wmorph></ref><br><ref onclick="bdbid('H3588')"><wsn>H3588</wsn></ref><br><wgloss>that</wgloss><br><wtrans>For</wtrans></div><heb> </heb><div class="int"><wform><heb id="wh331059" class="ch70324 GE70414 H1396" onclick="luW(2,'331059','70324','70414','verb.qal.perf.p3.m.sg','H1396')" onmouseover="hl1('h331059','h70324','E70414')" onmouseout="hl0('h331059','h70324','E70414')" ondblclick="searchWord(1,331059)">גָ֘בַ֤ר</heb></wform><br><wsbl>gābar</wsbl><br><wphono>ḡˈāvˈar</wphono><br><ref onclick="lex('E70414')" ondblclick="searchLexicalEntry('E70414')"><wlex><heb>גבר</heb></wlex></ref><br><ref onclick="etcbcmorph('verb.qal.perf.p3.m.sg')"><wmorph>verb.qal.perf.p3.m.sg</wmorph></ref><br><ref onclick="bdbid('H1396')"><wsn>H1396</wsn></ref><br><wgloss>[he]+ be superior</wgloss><br><wtrans>great is</wtrans></div><heb> </heb><div class="int"><wform><heb id="wh331060" class="ch70324 GE70014 H5921" onclick="luW(2,'331060','70324','70014','prep.prs.p1.u.pl','H5921')" onmouseover="hl1('h331060','h70324','E70014')" onmouseout="hl0('h331060','h70324','E70014')" ondblclick="searchWord(1,331060)">עָלֵ֨ינוּ</heb><heb>׀</heb></wform><br><wsbl>ʿālêynû</wsbl><br><wphono>ʕālˌênû</wphono><br><ref onclick="lex('E70014')" ondblclick="searchLexicalEntry('E70014')"><wlex><heb>עַל</heb></wlex></ref><br><ref onclick="etcbcmorph('prep.prs.p1.u.pl')"><wmorph>prep.prs.p1.u.pl</wmorph></ref><br><ref onclick="bdbid('H5921')"><wsn>H5921</wsn></ref><br><wgloss>upon +[us]</wgloss><br><wtrans>to us,</wtrans></div><heb> </heb><div class="int"><wform><heb id="wh331061" class="ch70324 GE70897 H2617" onclick="luW(2,'331061','70324','70897','subs.m.sg.a.prs.p3.m.sg','H2617')" onmouseover="hl1('h331061','h70324','E70897')" onmouseout="hl0('h331061','h70324','E70897')" ondblclick="searchWord(1,331061)">חַסְדֹּ֗ו</heb></wform><br><wsbl>ḥasdô</wsbl><br><wphono>ḥasdˈô</wphono><br><ref onclick="lex('E70897')" ondblclick="searchLexicalEntry('E70897')"><wlex><heb>חֶסֶד</heb></wlex></ref><br><ref onclick="etcbcmorph('subs.m.sg.a.prs.p3.m.sg')"><wmorph>subs.m.sg.a.prs.p3.m.sg</wmorph></ref><br><ref onclick="bdbid('H2617')"><wsn>H2617</wsn></ref><br><wgloss>+[his] loyalty</wgloss><br><wtrans>His loving devotion</wtrans></div><heb> </heb><div class="int"><wform><heb id="wh331062" class="ch70325 GE70008 H9000" onclick="luW(2,'331062','70325','70008','conj','H9000')" onmouseover="hl1('h331062','h70325','E70008')" onmouseout="hl0('h331062','h70325','E70008')" ondblclick="searchWord(1,331062)">וֶֽ</heb><heb></heb></wform><br><wsbl>we</wsbl><br><wphono>wˈe</wphono><br><ref onclick="lex('E70008')" ondblclick="searchLexicalEntry('E70008')"><wlex><heb>וְ</heb></wlex></ref><br><ref onclick="etcbcmorph('conj')"><wmorph>conj</wmorph></ref><br><ref onclick="bdbid('H9000')"><wsn>H9000</wsn></ref><br><wgloss>and</wgloss><br><wtrans>and</wtrans></div><div class="int"><wform><heb id="wh331063" class="ch70325 GE71035 H571" onclick="luW(2,'331063','70325','71035','subs.f.sg.c','H571')" onmouseover="hl1('h331063','h70325','E71035')" onmouseout="hl0('h331063','h70325','E71035')" ondblclick="searchWord(1,331063)">אֱמֶת</heb><heb>־</heb></wform><br><wsbl>ʾĕmet</wsbl><br><wphono>ʔᵉmeṯ-</wphono><br><ref onclick="lex('E71035')" ondblclick="searchLexicalEntry('E71035')"><wlex><heb>אֶמֶת</heb></wlex></ref><br><ref onclick="etcbcmorph('subs.f.sg.c')"><wmorph>subs.f.sg.c</wmorph></ref><br><ref onclick="bdbid('H571')"><wsn>H571</wsn></ref><br><wgloss>trustworthiness</wgloss><br><wtrans>the faithfulness</wtrans></div><div class="int"><wform><heb id="wh331064" class="ch70325 GE70113 H3068" onclick="luW(2,'331064','70325','70113','nmpr.m.sg.a','H3068')" onmouseover="hl1('h331064','h70325','E70113')" onmouseout="hl0('h331064','h70325','E70113')" ondblclick="searchWord(1,331064)">יְהוָ֥ה</heb></wform><br><wsbl>[yĕhwāh]</wsbl><br><wphono>[yᵊhwˌāh]</wphono><br><ref onclick="lex('E70113')" ondblclick="searchLexicalEntry('E70113')"><wlex><heb>יְהוָה</heb></wlex></ref><br><ref onclick="etcbcmorph('nmpr.m.sg.a')"><wmorph>nmpr.m.sg.a</wmorph></ref><br><ref onclick="bdbid('H3068')"><wsn>H3068</wsn></ref><br><wgloss>YHWH</wgloss><br><wtrans>of the LORD</wtrans></div><heb> </heb><div class="int"><wform><heb id="wh331065" class="ch70325 GE70028 H9005" onclick="luW(2,'331065','70325','70028','prep','H9005')" onmouseover="hl1('h331065','h70325','E70028')" onmouseout="hl0('h331065','h70325','E70028')" ondblclick="searchWord(1,331065)">לְ</heb><heb></heb></wform><br<wsbl>lĕ</wsbl><br><wphono>lᵊ</wphono><br><ref onclick="lex('E70028')" ondblclick="searchLexicalEntry('E70028')"><wlex><heb>לְ</heb></wlex></ref><br><ref onclick="etcbcmorph('prep')"><wmorph>prep</wmorph></ref><br><ref onclick="bdbid('H9005')"><wsn>H9005</wsn></ref><br><wgloss>to</wgloss><br><wtrans></wtrans></div><div class="int"><wform><heb id="wh331066" class="ch70325 GE70253 H5769" onclick="luW(2,'331066','70325','70253','subs.m.sg.a','H5769')" onmouseover="hl1('h331066','h70325','E70253')" onmouseout="hl0('h331066','h70325','E70253')" ondblclick="searchWord(1,331066)">עֹולָ֗ם</heb></wform><br><wsbl>ʿôlām</wsbl><br><wphono>ʕôlˈām</wphono><br><ref onclick="lex('E70253')" ondblclick="searchLexicalEntry('E70253')"><wlex><heb>עֹולָם</heb></wlex></ref><br><ref onclick="etcbcmorph('subs.m.sg.a')"><wmorph>subs.m.sg.a</wmorph></ref><br><ref onclick="bdbid('H5769')"><wsn>H5769</wsn></ref><br><wgloss>eternity</wgloss><br><wtrans>endures forever.</wtrans></div><heb> </heb><div class="int"><wform><heb id="wh331067" class="ch70326 GE70639 H1984" onclick="luW(2,'331067','70326','70639','verb.piel.impv.p2.m.pl','H1984')" onmouseover="hl1('h331067','h70326','E70639')" onmouseout="hl0('h331067','h70326','E70639')" ondblclick="searchWord(1,331067)">הַֽלְלוּ</heb><heb>־</heb></wform><br><wsbl>halû</wsbl><br><wphono>hˈallû-</wphono><br><ref onclick="lex('E70639')" ondblclick="searchLexicalEntry('E70639')"><wlex><heb>הלל</heb></wlex></ref><br><ref onclick="etcbcmorph('verb.piel.impv.p2.m.pl')"><wmorph>verb.piel.impv.p2.m.pl</wmorph></ref><br><ref onclick="bdbid('H1984')"><wsn>H1984</wsn></ref><br><wgloss>[you]+ praise</wgloss><br><wtrans>Hallelujah!</wtrans></div><div class="int"><wform><heb id="wh331068" class="ch70326 GE72038 H3050" onclick="luW(2,'331068','70326','72038','nmpr.m.sg.a','H3050')" onmouseover="hl1('h331068','h70326','E72038')" onmouseout="hl0('h331068','h70326','E72038')" ondblclick="searchWord(1,331068)">יָֽהּ</heb><heb>׃</heb></wform><br><wsbl>yāh</wsbl><br><wphono>yˈāh</wphono><br><ref onclick="lex('E72038')" ondblclick="searchLexicalEntry('E72038')"><wlex><heb>יָהּ</heb></wlex></ref><br><ref onclick="etcbcmorph('nmpr.m.sg.a')"><wmorph>nmpr.m.sg.a</wmorph></ref><br><ref onclick="bdbid('H3050')"><wsn>H3050</wsn></ref><br><wgloss>the Lord</wgloss><br><wtrans></wtrans></div><heb> </heb><br></verse>"""

    # Fix known issues
    content = content.replace("<br<", "<br><")

    # Inject JS for interactive highlighting
    ui.add_head_html("""
    <script>
        // MOCK W3.JS (Polyfill to avoid external dependency)
        var w3 = {
            addStyle: function(selector, prop, value) {
                document.querySelectorAll(selector).forEach(function(el) {
                     el.style.setProperty(prop, value);
                });
            }
        };

        // Variable used in original script for host interoperability

        function hl0(id, cl, sn) {
            if (cl != '') {
                w3.addStyle('.c'+cl,'background-color','');
            }
            if (sn != '') {
                w3.addStyle('.G'+sn,'background-color','');
            }
            if (id != '') {
                var focalElement = document.getElementById('w'+id);
                if (focalElement != null) {
                    focalElement.style.background='';
                }
            }
        }

        function hl1(id, cl, sn) {
            if (cl != '') {
                w3.addStyle('.c'+cl,'background-color','PAPAYAWHIP');
            }
            if (sn != '') {
                w3.addStyle('.G'+sn,'background-color','#E7EDFF');
            }
            if (id != '') {
                var focalElement = document.getElementById('w'+id);
                if (focalElement != null) {
                    focalElement.style.background='#C9CFFF';
                }
            }
            // Optional: Updates document title for host-app callbacks.
            // Uncomment if you are using a wrapper that listens to title changes.
            // if ((id != '') && (id.startsWith("l") != true)) {
            //     document.title = "_instantWord:::"+activeB+":::"+id;
            // }
        }

        // --- Placeholders for other onclick events to prevent console errors ---
        function luV(id) { console.log("Verse clicked:", id); }
        function luW(v, id, cl, sn, morph, strongs) { console.log("Word clicked:", id); }
        function lex(id) { console.log("Lexicon clicked:", id); }
        function searchLexicalEntry(id) { console.log("Search Lexicon:", id); }
        function etcbcmorph(morph) { console.log("Morphology clicked:", morph); }
        function bdbid(id) { console.log("BDB ID clicked:", id); }
        function searchWord(v, id) { console.log("Search word:", id); }
    </script>
    """)

    # Inject CSS to handle the custom tags and interlinear layout
    ui.add_head_html("""
    <style>
        /* Main container */
        .bible-text {
            direction: rtl;
            font-family: sans-serif;
            padding: 20px;
            background-color: #fafafa;
        }
        /* Verse container */
        verse {
            display: block;
            margin-bottom: 20px;
            line-height: 1.3;
        }
        /* Verse ID */
        vid {
            color: navy;
            font-weight: bold;
            font-size: 0.9rem;
            margin-left: 10px;
            cursor: pointer; /* pointer */
        }
        /* Interlinear word block */
        .int {
            display: inline-block;
            vertical-align: top;
            text-align: center;
            margin: 0 4px 10px 4px;
            padding: 4px 8px;
            background: white;
            border-radius: 6px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            border: 1px solid #eee;
            transition: background-color 0.2s; /* Smooth highlight transition */
        }
        .int > *, .int > ref > * {
            line-height: 1.1;
            margin-top: 1px;
            margin-bottom: 1px;
        }
        /* Hebrew Word */
        wform, heb {
            font-family: 'SBL Hebrew', 'Ezra SIL', serif;
            font-size: 1.6rem;
            color: #2c3e50;
            direction: rtl;
            display: inline-block;
            line-height: 1.2em;
            margin-top: 0;
            margin-bottom: -2px;
            cursor: pointer; /* pointer */
        }
        /* Transliterations */
        wsbl, wphono {
            display: block;
            font-size: 0.8rem;
            color: #7f8c8d;
            font-style: italic;
        }
        /* Morphology */
        wmorph {
            display: block;
            font-family: monospace;
            font-size: 0.7rem;
            color: #27ae60;
            cursor: pointer; /* pointer */
        }
        /* Lexical & Strongs */
        wlex {
            display: block;
            font-family: 'SBL Hebrew', serif;
            font-size: 1rem;
            color: #555;
            cursor: pointer; /* pointer */
        }
        wsn {
            display: block;
            font-size: 0.7rem;
            color: #8e44ad;
            cursor: pointer; /* pointer */
        }
        /* Gloss */
        wgloss {
            direction: ltr;
            display: block;
            font-size: 0.85rem;
            color: #d35400;
        }
        /* Translation */
        wtrans {
            direction: ltr;
            display: block;
            margin-top: 4px;
            padding-top: 3px;
            border-top: 1px solid #f0f0f0;
            font-size: 0.95rem;
            font-weight: bold;
            color: #2980b9;
            min-height: 1.2em;
        }
    </style>
    """)

    # Header
    ui.label('Original Interlinear Bible (OIB) - Psalm 117').classes('text-2xl font-bold q-mb-md text-center w-full')

    # Render the HTML
    ui.html(f'<div class="bible-text">{content}</div>', sanitize=False).classes('w-full')

original_oib()
ui.run(port=9999)