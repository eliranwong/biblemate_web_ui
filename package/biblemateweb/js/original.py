ORIGINAL_JS = """
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
    }
</script>
"""