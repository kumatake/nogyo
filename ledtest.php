<<html>
<head>
	<title>LEDpython呼び出しテスト</title>
</head>
<body>

	<?php
		function test(){
			echo "ひゃっひょう";
		}

	?>
	
	<input name="start" type="button" value="LED点灯！" onclick="<?php test() ?>">
</body>
</html>>