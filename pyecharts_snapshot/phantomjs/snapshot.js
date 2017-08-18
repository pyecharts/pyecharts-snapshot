var page = require('webpage').create();
var system = require('system');

var file = system.args[1];
var snapshot = "" + 
"    function(){"+
"        var ele = document.querySelector('div[_echarts_instance_]');"+
"        var mychart = echarts.getInstanceByDom(ele);"+
"        return mychart.getDataURL({type:'png', excludeComponents: ['toolbox']});"+
"    }";

page.open(file, function(){
	window.setTimeout(function () {
		var content = page.evaluateJavaScript(snapshot);
		console.log(content);
        phantom.exit();
    }, 500);
});
