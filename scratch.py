<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Title here</title>
	</head>
	<body>
		<h1>Welcome to our site, {{ name }}</h1>
		<p>
			It's so good of you to join us.
		</p>
		{% for item in list %}
			{% if item['success'] == True %}
				<h3 class="{{ item['style'] }}">Hello!</h3>
			{% else %}
				<p class="not-hello">{{ item }}</p>
			{% endif %}
		{% endfor %}

	</body>
</html>
