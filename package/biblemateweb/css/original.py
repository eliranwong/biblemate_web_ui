ORIGINAL_CSS = """
<style>
    /* Each verse acts as a container for word blocks */
    verse {
        display: block;
        margin-bottom: 20px;
        line-height: 1.3;
    }
    /* The interlinear word block container */
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
    /* Target all block elements inside .int to tighten their spacing */
    .int > *, .int > ref > * {
        line-height: 1.1;
        margin-top: 1px;
        margin-bottom: 1px;
    }
    /* Hover effects for interactive elements (even if JS isn't active here) */
    .int:hover {
        background-color: #f8fbff;
        border-color: #d6eaf8;
    }

    /* Transliteration Layers (Phonetic & SBL) - shared with Greek*/
    wsbl, wphono {
        direction: ltr;
        display: block;
        font-size: 0.8rem;
        color: #7f8c8d;
        font-style: italic;
    }
    /* Morphology Layer */
    wmorph {
        direction: ltr;
        display: block;
        font-family: monospace;
        font-size: 0.7rem;
        color: #27ae60;
        cursor: pointer;
    }
    wsn {
        direction: ltr;
        display: block;
        font-size: 0.7rem;
        color: #8e44ad;
        cursor: pointer;
    }
    /* Gloss (Literal Meaning) Layer */
    wgloss {
        direction: ltr;
        display: block;
        font-size: 0.85rem;
        color: #d35400;
    }
    /* Final Translation Layer */
    wtrans {
        direction: ltr;
        display: block;
        margin-top: 4px;
        padding-top: 3px;
        border-top: 1px solid #f0f0f0;
        font-size: 0.95rem;
        font-weight: bold;
        color: #2980b9;
        min-height: 1.2em; /* Ensures empty translations don't collapse the block */
    }

    /* UBA css */
    external {
        font-size: 80%;
    }
    red, z {
        color: red;
    }
    blu {
        color: blue;
        font-size: 80%;
    }
    points {
        color: gray;
        font-weight: bold;
        font-size: 80%;
    }
    bb {
        color: brown;
        font-weight: bold;
    }
    hp {
        color: brown;
        font-weight: bold;
        font-size: 80%;
    }
    highlight {
        font-style: italic;
    }
    transliteration {
        color: gray;
    }
    div.section, div.point {
        display: block;
        border: 1px solid green;
        border-radius: 5px;
        padding: 2px 5px;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    div.remarks {
        display: block;
        border: 1px solid gray;
        border-radius: 5px;
        padding: 2px 5px;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    div.bhs, div.hebch {
        direction: rtl;
    }
    div.info {
        margin-left: 5%;
        margin-right: 5%;
    }
    div.menu {
        margin-left: 2%;
        margin-right: 2%;
    }
    div.vword {
        border: 1px solid #F5B041;
        border-radius: 5px;
        padding: 2px 5px;
        margin-top: 3px;
        margin-bottom: 3px;
    }
    div.translation {
        border: 1px solid #9B59B6;
        border-radius: 5px;
        padding: 2px 5px;
        margin-top: 3px;
        margin-bottom: 3px;
    }
    div.ew {
        margin-left: 5%;
        margin-right: 5%;
        font-size: 110%;
        display: inline-block;
    }
    div.mr {
        margin-left: 100;
    }
    div.nav {
        margin-left: 5%;
        margin-right: 5%;
    }
    div.refList {
        display: inline;
    }
    /* css for linguistic annotations */
                
    div.bhp, div.bhw, div.w, div.int {
        display: inline-block;
        text-align: center;
    }
    div.int {
        vertical-align: text-top;
    }
    div.bhc {
        direction: rtl;
        border: 1px solid #9B59B6;
        border-radius: 5px;
        padding: 2px 5px;
        margin-top: 3px;
        margin-bottom: 3px;
    }
    div.bhp {
        border: 1px solid gray;
        border-radius: 5px;
        padding: 2px 5px;
        margin-top: 3px;
        margin-bottom: 3px;
    }
    div.bhw {
        border: 1px solid #F5B041;
        border-radius: 5px;
        padding: 2px 5px;
        margin-top: 3px;
        margin-bottom: 3px;
    }
    clid {
        color: #641E16;
        font-weight: bold;
    }
    mclid {
        color: #641E16;
        font-style: italic;
    }
    connector {
        color: #9B59B6;
    }
    ckind, ctyp, crela {
        color: #00008B;
        display: inline-block;
    }
    ptyp {
        text-decoration: underline;
        color: gray;
    }
    pfunction {
        color: #3498DB;
        font-size: 90%;
    }
    det {
        font-weight: bold;
    }
    undet {
        font-style: italic;
    }
    prela {
        display: none;
    }
    hbint, gntint, gloss {
        direction: ltr;
        vertical-align: super;
        display: inline-block;
        color: #D35400;
    }
    gntint, gloss {
        font-size: 90%;
    }
    cllevel {
        color: #9B59B6;
    }
    clinfo {
        color: #641E16;
        font-weight: bold;
    }
    subclinfo {
        color: #641E16;
        font-weight: bold;
        font-size: 80%;
    }
    funcinfo {
        color: #3498DB;
        font-size: 90%;
    }
    wordid {
        text-decoration: underline;
        font-size: 80%;
        color: gray;
    }
    cit, clt, cst, cbhs, cbsb, cleb {
        display: block;
    }
    clt, cbsb {
        color: #3498DB;
    }
    cst, cleb {
        color: #00008B;
    }
    cbsb, cleb {
        direction: ltr;
    }
    div.cltrans {
        margin-left: 10px;
        margin-right: 10px;
        display: block;
        border: 1px solid #00008B;
        border-radius: 5px;
        padding: 2px 5px;
        margin-top: 3px;
        margin-bottom: 3px;
    }
    div.wrap {
        display: inline-block;
    }
    cl {
        display: table;
    }
    div.c {
        vertical-align: top;
        text-align: left;
        border: 1px solid #9B59B6;
        border-radius: 5px;
        padding: 2px 5px;
        margin-top: 3px;
        margin-bottom: 3px;
    }
    div.p {
        display: inline-block;
        vertical-align: top;
        text-align: left;
        border: 1px solid gray;
        border-radius: 5px;
        padding: 2px 5px;
        margin-top: 3px;
        margin-bottom: 3px;
    }
    div.w, div.int {
        border: 1px solid #F5B041;
        border-radius: 5px;
        padding: 2px 5px;
        margin-top: 3px;
        margin-bottom: 3px;
    }

    /* css for clause segmentation */

    div.bhsa {
        direction: rtl;
        border-right: 5px solid #F5B041;
        margin-left: 5%;
        margin-right: 5%;
        padding: 5px 10px 5px 10px;
    }
    div.e {
        border-left: 5px solid #F5B041;
        margin-left: 5%;
        margin-right: 5%;
        padding: 5px 10px 5px 10px;
    }
</style>
"""