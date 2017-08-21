var page = require('webpage').create();
var system = require('system');

var file = system.args[1];
var file_type = system.args[2];

var snapshot = "" + 
"    function(){"+
"        var ele = document.querySelector('div[_echarts_instance_]');"+
"        var mychart = echarts.getInstanceByDom(ele);"+
"        return mychart.getDataURL({type:'"+file_type+"', excludeComponents: ['toolbox']});"+
"    }";

page.open(file, function(){
	window.setTimeout(function () {
		var content = page.evaluateJavaScript(snapshot);
		console.log(content);
        phantom.exit();
    }, 500);
});
