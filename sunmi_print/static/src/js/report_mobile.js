(function () {
'use strict';

$(document).ready(function () {
    //window.print();
    var afterPrint = function() {
        window.history.go(-1);
    };

    if (window.matchMedia) {
        var mediaQueryList = window.matchMedia('print');
        mediaQueryList.addListener(function(mql) {
            if (!mql.matches) {
                afterPrint();
            }
        });
    }
});

})();
